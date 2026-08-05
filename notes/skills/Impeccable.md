---
type: note
created: 2026-07-05
updated: 2026-07-05
status: seed
source: "https://github.com/pbakaus/impeccable"
moc: "[[AI]]"
tags:
  - agents
  - ai
  - design
  - skills
  - vibe-coding
---
# Impeccable

**Impeccable** — набор design guidance для AI coding agents: 1 skill, 23 команды, live browser iteration и 45 детерминированных правил для детекта типичных AI-generated frontend design анти-паттернов.

Источник: [GitHub — pbakaus/impeccable](https://github.com/pbakaus/impeccable)  
Документация: [impeccable.style](https://impeccable.style)  
npm: `impeccable`, версия на момент добавления — `3.2.0`, лицензия Apache-2.0.

## Что это

Инструмент вырос из [[Frontend design|frontend-design]] skill от Anthropic, но добавляет более полный рабочий контур для AI-дизайна:

- **setup flow**: `npx impeccable install` → `/impeccable init`;
- создаёт/использует `PRODUCT.md` и предлагает `DESIGN.md`, чтобы агент понимал аудиторию, бренд, voice, цвета, типографику, компоненты и анти-референсы;
- даёт команды для общей дизайн-лексики с агентом: `audit`, `polish`, `critique`, `distill`, `animate`, `bolder`, `quieter` и др.;
- включает **45 deterministic detector rules** без LLM/API key для проверки типичных AI-дизайн-штампов;
- поддерживает live browser iteration и browser extension.

## Зачем Данилу

Полезно для вайбкодинга, лендингов, CRM/UI-прототипов и личных AI-проектов, где главная проблема — не «сверстать», а убрать типичный AI-вайб:

- Inter everywhere;
- фиолетово-синие градиенты;
- cards in cards;
- серый текст на цветном фоне;
- rounded-square icon tile над каждым заголовком;
- визуальная «SaaS-шаблонность» без характера продукта.

Практическая ценность: сделать дизайн отдельной проверяемой фазой, а не надеяться, что coding agent сам «сделает красиво».

## Как применять

Базовый сценарий в проекте:

```bash
npx impeccable install
```

Потом внутри AI coding tool:

```text
/impeccable init
/impeccable audit
/impeccable polish
/impeccable critique
/impeccable distill
```

Фокусные команды:

```text
/impeccable audit the header
/impeccable polish the checkout form
```

Если команда нужна часто, её можно закрепить:

```text
/impeccable pin audit
```

## Поддерживаемые инструменты

- Cursor
- Claude Code
- GitHub Copilot
- Gemini CLI
- Codex CLI
- OpenCode
- Pi
- Kiro
- Trae
- Rovo Dev
- Qoder

Для Codex CLI используются skills, не `/prompts:` commands. Repo-local installs живут в `.agents/skills/`, user-wide installs — в `~/.agents/skills/`.

## Важное по `.impeccable`

Impeccable пишет рабочие файлы в `.impeccable/`: скриншоты, live-mode state, cache, local config. Большая часть — ephemeral и не должна попадать в git.

Shared artifacts, которые могут быть полезны в репозитории:

- `.impeccable/config.json`
- `.impeccable/live/config.json`
- `.impeccable/design.json`
- `.impeccable/critique/*.md`

Перед коммитом проекта с Impeccable надо отдельно проверить `.gitignore`.

## Где использовать первым

1. Маленький лендинг / product page для портфолио.
2. UI-прототип CRM/дашборда для агентства.
3. Финальная полировка интерфейса после генерации в Claude/Codex.
4. Аудит чужого AI-generated frontend перед публикацией.

## Связи

- [[Frontend design]] — базовая логика: дизайн как отдельная фаза.
- [[Taste Skill]] — соседний anti-slop инструмент со стилевыми пресетами (dials).
- [[Hallmark]] — соседний anti-slop инструмент с 57 slop-test gates и извлечением design DNA.
- [[Make Interfaces Feel Better]] — ручная/агентная полировка интерфейсов.
- [[Modern Web Guidance]] — современные web/UI-практики.
- [[designmd.supply]] — хранение дизайн-систем и бренд-гайдов в Markdown.
- [[AI]] — MOC по AI-инструментам и вайбкодингу.
