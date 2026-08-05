---
type: note
created: 2026-07-04
source: https://github.com/microsoft/SkillOpt
tags:
  - agents
  - ai
  - claude-code
  - codex
  - knowledge-base
  - skills
moc: "[[AI]]"
---
# SkillOpt

Источник: [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)  
Связи: [[Claude Code]], [[Что такое skills]], [[Аудит skills]], [[Безопасность skills]], [[Субагенты]]

## Что это

**SkillOpt** — фреймворк Microsoft для оптимизации агентных skills без дообучения модели. Идея: skill-документ в Markdown рассматривается как «обучаемое состояние» агента, а веса LLM остаются замороженными.

Формула: **rollout → reflect → propose edit → validation gate → update skill**.

То есть система прогоняет задачи, смотрит ошибки/оценки, предлагает ограниченные правки skill-файла и принимает их только если они улучшают held-out validation score.

## Зачем это важно

Обычные skills часто:

- пишутся руками;
- генерируются разово сильной моделью;
- хаотично правятся после ошибок;
- не имеют нормальной проверки, стало ли лучше.

SkillOpt пытается сделать для skills то, что optimizer делает для весов модели: **итеративное улучшение с метриками, batch/epoch-подходом, learning-rate бюджетом и validation gate**.

Ключевой плюс: после оптимизации в продакшене используется компактный `best_skill.md`, без дополнительных inference-time model calls.

## Основные детали

- Артефакт: `best_skill.md`, обычно 300–2000 токенов.
- Target model выполняет задачи с текущим skill.
- Optimizer model анализирует trajectories/score и предлагает bounded edits: add/delete/replace.
- Candidate edit принимается только при улучшении validation score.
- Есть rejected-edit buffer, textual learning-rate budget, slow/meta update.
- Поддерживаются execution harnesses: direct chat, Codex CLI, Claude Code CLI.
- По README: проверялось на 6 benchmarks, 7 target models и 3 harnesses; заявлены сильные приросты к no-skill baseline.

## SkillOpt-Sleep

В версии `v0.2.0` появился **SkillOpt-Sleep** — ночной offline self-evolution engine для локальных coding agents:

- собирает прошлые сессии;
- майнит повторяющиеся паттерны;
- делает replay/dream rollouts;
- консолидирует validated skills через held-out gate;
- имеет plugin shells для Claude, Codex, Copilot, Devin, OpenClaw.

Это особенно интересно как направление: агент не просто исполняет задачи, а ночью улучшает собственные рабочие инструкции/skills на основе истории.

## Установка

```bash
pip install skillopt
```

Опциональные extras:

```bash
pip install skillopt[webui]    # Gradio dashboard
pip install skillopt[claude]   # Claude backend
pip install skillopt[alfworld] # ALFWorld benchmark
```

Из исходников:

```bash
git clone https://github.com/microsoft/SkillOpt.git
cd SkillOpt
pip install -e .
```

## WebUI

```bash
pip install -e ".[webui]"
python -m skillopt_webui.app
```

Флаги:

| Flag | Default | Что делает |
|---|---:|---|
| `--port` | `7860` | порт |
| `--host` | `0.0.0.0` | bind address |
| `--share` | off | публичная Gradio-ссылка |

## Как применить Данилу

1. **Оптимизация рабочих skills для Claude Code / Codex**  
   Не просто писать skill руками, а прогонять его на наборе типовых задач: CRM-интеграции, отчёты, API-клиенты, рефакторинг, audit checklist.

2. **Skill regression testing**  
   Любое изменение skill должно проходить небольшой validation set: стало ли качество лучше, не вырос ли хаос, не ухудшилась безопасность.

3. **Агентство / IT Lead контур**  
   Можно собрать benchmark из реальных повторяющихся задач агентства: amoCRM, интеграции, генерация ТЗ, проверка webhook/API, отчёты. SkillOpt-подход помогает превращать опыт в стабильные инструкции.

4. **Личный AI-оператор**  
   Идея SkillOpt-Sleep ложится на Hermes/Claude/Codex: регулярная консолидация выводов из сессий в улучшенные skills/правила, но только через проверку и без слепого автосохранения мусора.

## Ограничения и риски

- Это исследовательский/инженерный фреймворк, не «поставил и магия».
- Нужны качественные datasets/benchmarks, иначе оптимизация будет подгонкой под шум.
- Validation gate критичен: без него self-improvement легко превращается в деградацию инструкций.
- Для приватных данных надо отдельно продумать redaction и хранение transcripts.
- Автоматическое изменение skills без ревью опасно: можно незаметно закрепить плохие паттерны.

## Вывод

SkillOpt — важная штука не как готовая кнопка, а как **модель мышления для инженерии skills**: skills надо не просто писать, а тренировать, валидировать и версионировать как полноценный артефакт системы.

Для Данила самый полезный угол: взять подход SkillOpt для построения **benchmark-driven skills** под Claude Code/Codex/Hermes и постепенно улучшать рабочие инструкции на реальных задачах агентства.
