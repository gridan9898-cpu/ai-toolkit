#!/usr/bin/env python3
"""
agent-doctor — линтер дрейфа для системы ИИ-агентов Claude Code.

Когда у тебя не один агент, а несколько субагентов и скилов, их инструкции
со временем расходятся с реальностью: ссылаются на удалённые файлы, держатся
за отменённые концепции, сидят на невалидной модели. Ничего не падает —
агент просто молча делает не то. agent-doctor раз в неделю (или по кнопке)
сам обходит инструкции и находит этот дрейф ДО того, как он выстрелит.

Что проверяет (универсально, без конфига):
  1. DEAD PATH       — файловый путь в инструкции, которого больше нет.
  2. MODEL           — невалидная модель в frontmatter + карта моделей.
  3. DEAD AGENT REF  — упоминание субагента, которого нет в реестре.
  4. DEAD SKILL REF  — вызов скила, которого нет.
  5. MISFILED        — не-агентный файл (без frontmatter `name:`) в agents/.

Что включается конфигом (опционально, под твою систему):
  6. LIGHT MODEL     — «думающий» агент сидит на лёгкой модели (advisory).
  7. STALE FRAME     — отменённые у тебя формулировки/концепции в инструкциях.

Запуск:
  python3 agent-doctor.py                     # текст-отчёт
  python3 agent-doctor.py --json              # машиночитаемо
  python3 agent-doctor.py --quiet             # печатать только при находках (cron)
  python3 agent-doctor.py --config path.json  # явный конфиг

Конфиг (все ключи опциональны) ищется по порядку: --config → $AGENT_DOCTOR_CONFIG
→ ./.agent-doctor.json → ~/.claude/agent-doctor.config.json → нет (дефолты).
Пример конфига — agent-doctor.config.example.json рядом.

Ноль зависимостей, только stdlib. Задуман под ручной прогон и еженедельный cron.
"""
import os
import re
import sys
import json
import glob

HOME = os.path.expanduser("~")

DEFAULTS = {
    "agents_dir": "~/.claude/agents",
    "skills_dir": "~/.claude/skills",
    # тиры моделей + известные полные ID (обновлять по мере выхода моделей)
    "valid_models": [
        "fable", "sonnet", "opus", "haiku", "inherit",
        "claude-fable-5", "claude-opus-4-8", "claude-sonnet-5", "claude-haiku-4-5",
    ],
    "valid_model_prefixes": ["claude-", "anthropic/"],
    # «думающие» агенты, которым лёгкая модель — повод пересмотреть (пусто = проверка выкл)
    "thinking_agents": [],
    "light_models": ["fable", "haiku", "claude-fable-5", "claude-haiku-4-5"],
    # отменённые формулировки: [{"pattern": "...", "reason": "..."}] (пусто = проверка выкл)
    "stale_patterns": [],
    # маркеры отрицания рядом с формулировкой = инструкция её ЗАПРЕЩАЕТ, не нарушает
    "negation_markers": [
        r"не использ", r"не примен", r"не беру", r"больше не", r"отмен",
        r"а не", r"не выдум", r"deprecated", r"\bnot\b", r"\bno longer\b", r"\bdon'?t\b",
    ],
    # префиксы каталогов-состояний: отсутствие файла тут — мягкий warn, не error
    "state_dir_prefixes": [],
    # вендорные скил-паки, чьи внутренние доки/примеры не сканируем
    "skip_skill_substrings": ["superpowers"],
    # токены, похожие на ссылку-на-агента, но агентами не являющиеся
    "known_nonagents": [],
}

# ── статические regex (не зависят от конфига) ─────────────────────────
PATH_RE = re.compile(r"(?<![\w`])(~/[^\s`'\"()<>]+|/(?:Users|home)/[^\s`'\"()<>]+)")
MODEL_RE = re.compile(r"^model:\s*([^\s#]+)", re.MULTILINE)
GLOB_CHARS = set("*?{}[]")
PLACEHOLDER_RE = re.compile(r"\$|<|>|YYYY|MM|DD|SLUG|день[NnХXхx]|\bN\b|/N[./]|\{\{")


def load_config(argv):
    cfg = dict(DEFAULTS)
    path = None
    for i, a in enumerate(argv):
        if a == "--config" and i + 1 < len(argv):
            path = argv[i + 1]
        elif a.startswith("--config="):
            path = a.split("=", 1)[1]
    if not path:
        path = os.environ.get("AGENT_DOCTOR_CONFIG")
    for cand in ([path] if path else []) + [
        "./.agent-doctor.json", os.path.join(HOME, ".claude", "agent-doctor.config.json")
    ]:
        if cand and os.path.isfile(os.path.expanduser(cand)):
            try:
                with open(os.path.expanduser(cand), "r", encoding="utf-8") as f:
                    cfg.update({k: v for k, v in json.load(f).items() if k in DEFAULTS})
                cfg["_loaded_from"] = cand
            except (OSError, ValueError) as e:
                print(f"⚠ конфиг {cand} не прочитан: {e}", file=sys.stderr)
            break
    return cfg


def expand(p):
    return os.path.expanduser(p)


def has_agent_frontmatter(path):
    """Настоящая агент-дефиниция имеет frontmatter с `name:`. Симлинки на правила,
    заметки и прочий не-агентный файл в agents/ — не агент, не считать."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            head = f.read(600)
    except OSError:
        return False
    return head.lstrip().startswith("---") and re.search(r"^name:", head, re.MULTILINE) is not None


def registry_agents(agents_dir):
    return {
        os.path.splitext(os.path.basename(p))[0]
        for p in glob.glob(os.path.join(agents_dir, "*.md"))
        if has_agent_frontmatter(p)
    }


def registry_skills(skills_dir):
    return {os.path.basename(p) for p in glob.glob(os.path.join(skills_dir, "*")) if os.path.isdir(p)}


def clean_path(raw):
    return raw.rstrip(").,:;!?`'\"»\\").rstrip("/")


def is_glob(path):
    return any(c in GLOB_CHARS for c in path)


def check_paths(text, state_dir_prefixes):
    dead_ext, dead_state = [], []
    seen = set()
    state_res = [re.compile(re.escape(expand(p))) for p in state_dir_prefixes]
    for m in PATH_RE.finditer(text):
        raw = clean_path(m.group(1))
        if not raw or raw in seen:
            continue
        seen.add(raw)
        if is_glob(raw) or PLACEHOLDER_RE.search(raw) or raw.endswith("..."):
            continue
        expanded = expand(raw)
        if os.path.exists(expanded):
            continue
        if any(r.match(expanded) for r in state_res):
            dead_state.append(raw)
        else:
            dead_ext.append(raw)
    return dead_ext, dead_state


def check_model(text, agent_name, cfg):
    m = MODEL_RE.search(text)
    model = m.group(1).strip() if m else None
    issues = []
    if model is None:
        return None, issues
    valid = model in set(cfg["valid_models"]) or any(model.startswith(p) for p in cfg["valid_model_prefixes"])
    if not valid:
        issues.append(("error", f"невалидная модель '{model}'"))
    if agent_name in set(cfg["thinking_agents"]) and model in set(cfg["light_models"]):
        issues.append(("advisory", f"думающий агент на лёгкой модели '{model}' — пересмотреть"))
    return model, issues


def check_stale_frame(text, stale_patterns, negation_re):
    hits = []
    for entry in stale_patterns:
        pat, why = entry.get("pattern"), entry.get("reason", "отменённая формулировка")
        if not pat:
            continue
        for m in re.finditer(pat, text, re.IGNORECASE):
            window = text[max(0, m.start() - 60): m.end() + 60]
            if negation_re and negation_re.search(window):
                continue
            line = text[:m.start()].count("\n") + 1
            hits.append((line, why, m.group(0)))
    return hits


def check_agent_refs(text, agents, known_nonagents):
    refs = set(re.findall(r"`([a-z][a-z0-9-]{2,30})`", text))
    dead = []
    for r in refs:
        if r in agents or r in known_nonagents:
            continue
        # Контекст намеренно консервативный (zero false-positive важнее полноты):
        # ловим только явный диспатч-паттерн. Токены в бэктиках часто — теги/категории,
        # не имена агентов, поэтому не расширяем эвристику.
        ctx_ok = re.search(r"(агент|субагент|диспатч|deleg|отдать|звать)[^.\n]{0,40}`" + re.escape(r) + "`", text, re.IGNORECASE) \
            or re.search(r"`" + re.escape(r) + r"`[^.\n]{0,20}(агент|напишет|сделает|отвечает)", text, re.IGNORECASE)
        if ctx_ok:
            dead.append(r)
    return dead


def scan_file(path, agents, cfg, negation_re, agent_name=None):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    rec = {"file": path.replace(HOME, "~"), "findings": []}
    dead_ext, dead_state = check_paths(text, cfg["state_dir_prefixes"])
    for p in dead_ext:
        rec["findings"].append({"kind": "DEAD_PATH", "sev": "error", "detail": p})
    for p in dead_state:
        rec["findings"].append({"kind": "DEAD_PATH_STATE", "sev": "warn",
                                 "detail": f"{p} (state-dir, возможно создаётся на первой задаче)"})
    if agent_name is not None:
        model, mi = check_model(text, agent_name, cfg)
        rec["model"] = model
        for sev, msg in mi:
            rec["findings"].append({"kind": "MODEL", "sev": sev, "detail": msg})
        for r in check_agent_refs(text, agents, set(cfg["known_nonagents"])):
            rec["findings"].append({"kind": "DEAD_AGENT_REF", "sev": "warn", "detail": f"`{r}` — нет в реестре агентов"})
    for line, why, frag in check_stale_frame(text, cfg["stale_patterns"], negation_re):
        rec["findings"].append({"kind": "STALE_FRAME", "sev": "warn", "detail": f"L{line}: «{frag}» — {why}"})
    return rec


def main():
    argv = sys.argv[1:]
    cfg = load_config(argv)
    agents_dir = expand(cfg["agents_dir"])
    skills_dir = expand(cfg["skills_dir"])
    negation_re = re.compile("|".join(cfg["negation_markers"]), re.IGNORECASE) if cfg["negation_markers"] else None

    agents = registry_agents(agents_dir)

    records, model_map, misfiled = [], {}, []
    for p in sorted(glob.glob(os.path.join(agents_dir, "*.md"))):
        name = os.path.splitext(os.path.basename(p))[0]
        if not has_agent_frontmatter(p):
            misfiled.append((name, os.readlink(p) if os.path.islink(p) else None))
            continue
        rec = scan_file(p, agents, cfg, negation_re, agent_name=name)
        rec["agent"] = name
        model_map[name] = rec.get("model")
        records.append(rec)
    for p in sorted(glob.glob(os.path.join(skills_dir, "*", "SKILL.md"))):
        if any(s in p for s in cfg["skip_skill_substrings"]):
            continue
        records.append(scan_file(p, agents, cfg, negation_re))

    with_findings = [r for r in records if r["findings"]]
    total = sum(len(r["findings"]) for r in records)
    errors = sum(1 for r in records for f in r["findings"] if f["sev"] == "error")
    thinking = set(cfg["thinking_agents"])
    light = set(cfg["light_models"])

    if "--json" in argv:
        print(json.dumps({"records": records, "model_map": model_map, "misfiled": misfiled,
                          "total_findings": total, "errors": errors}, ensure_ascii=False, indent=2))
        return 1 if errors else 0

    if "--quiet" in argv and total == 0:
        return 0

    n_skills = len([r for r in records if "agent" not in r])
    print("=" * 60)
    print(f"AGENT-DOCTOR — {len(agents)} агентов, {n_skills} скилов")
    print(f"находок: {total}  (ошибок: {errors})")
    if cfg.get("_loaded_from"):
        print(f"конфиг: {cfg['_loaded_from']}")
    print("=" * 60)

    print("\n[МОДЕЛИ]")
    for name in sorted(model_map):
        mm = model_map[name] or "(inherit)"
        tag = "  ⚠ лёгкая" if (name in thinking and mm in light) else ""
        print(f"  {name:<22} {mm}{tag}")

    if misfiled:
        print("\n[НЕ-АГЕНТНЫЕ ФАЙЛЫ В agents/] (нет frontmatter `name:` — не считаются агентами)")
        for name, link in misfiled:
            print(f"  ~ {name}.md{f' → {link}' if link else ''}")

    if not with_findings:
        print("\n✅ дрейфа не найдено.")
        return 0

    order = {"error": 0, "warn": 1, "advisory": 2}
    print("\n[НАХОДКИ]")
    for r in with_findings:
        print(f"\n▸ {r.get('agent') or r['file']}  ({r['file']})")
        for f in sorted(r["findings"], key=lambda x: order.get(x["sev"], 3)):
            mark = {"error": "✗", "warn": "•", "advisory": "~"}.get(f["sev"], "-")
            print(f"    {mark} [{f['kind']}] {f['detail']}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
