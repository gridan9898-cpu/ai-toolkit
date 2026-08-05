---
type: note
created: 2026-06-21
updated: 2026-06-21
status: seed
source:
  - https://github.com/nexu-io/open-design
moc: "[[AI]]"
tags:
  - ai
  - design
  - skills
  - vibe-coding
---
# Open Design

**Open Design** — local-first open-source альтернатива Claude Design от Nexu Labs для agent-native дизайна.

Репозиторий: https://github.com/nexu-io/open-design

## Что делает

Превращает coding agents в дизайн-движок: агент читает skills, дизайн-системы и plugins из файловой структуры и генерирует визуальные артефакты.

Подходит для:

- web / desktop / mobile prototypes;
- лендингов и SaaS-экранов;
- live dashboards / artifacts;
- deck / презентаций;
- изображений, видео и HyperFrames motion graphics;
- HTML / PDF / PPTX / MP4 export.

## Что есть внутри

По присланному источнику:

- 71 шаблон интерфейсов в формате `DESIGN.md`;
- 19 встроенных skills;
- 5 готовых визуальных стилей;
- поддержка desktop/mobile форматов;
- интеграции с Claude Code, Codex, Cursor Agent, Gemini CLI, OpenCode, Qwen и другими.

По текущему README репозитория на 2026-06-21:

- 100+ skills;
- 150 brand-grade `DESIGN.md` systems;
- 261 ready-to-use plugins;
- sandboxed iframe preview;
- MCP/CLI-интеграции с Claude Code, Codex CLI, Cursor, OpenCode, Qwen, Copilot, Hermes, Kimi, Antigravity и другими CLI.

## Как связано с вайбкодингом

Ключевая идея: **дизайн становится отдельным файловым контуром проекта**, а не разовой фразой «сделай красиво».

Рабочая схема:

```text
brief → DESIGN.md / дизайн-система → skill/plugin → prototype → critique → handoff в coding agent
```

Open Design хорошо ложится в процесс из [[Frontend design]]:

1. Сначала сформировать направление и дизайн-систему.
2. Сделать 1–2 эталонных прототипа.
3. Проверить UI до продакшн-кода.
4. Только потом отдавать агенту задачу на реализацию компонентов.

## Интеграции

Из README:

- Claude Code — `od mcp install claude`;
- Codex CLI — `od mcp install codex`;
- Cursor — `od mcp install cursor`;
- GitHub Copilot / VS Code — `od mcp install copilot`;
- также заявлены OpenCode, Qwen, Hermes, Kimi, Antigravity и другие.

## Риски и проверка

Перед установкой:

- провести [[Аудит skills|аудит skills/plugins]];
- не ставить глобально без необходимости;
- проверить, какие файлы и MCP-интеграции меняет installer;
- отдельно смотреть, не уходит ли контекст проекта во внешний model router/AMR;
- начинать с локального тестового проекта, а не с рабочего репозитория.

## Практический вывод

Open Design стоит рассматривать как **дизайн-слой перед кодингом**: он полезен не тем, что «делает красиво», а тем, что формализует visual direction, `DESIGN.md`, прототипы и handoff для coding agent.

Связи: [[Frontend design]], [[Что такое skills]], [[Локальная установка skills]], [[Аудит skills]], [[Effective HTML skills]], [[Lottie skill]], [[Antigravity Awesome Skills]].
