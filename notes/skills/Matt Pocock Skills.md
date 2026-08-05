---
type: source
created: 2026-07-03
status: active
source: "https://github.com/mattpocock/skills"
moc: "[[AI]]"
tags:
  - ai
  - claude-code
  - skills
  - templates
---
# Matt Pocock Skills

Источник: [mattpocock/skills](https://github.com/mattpocock/skills)

## Что это

Набор агентских **skills для Claude Code / Codex / coding agents** от Matt Pocock. Позиционирование автора: «real engineering, not vibe coding» — маленькие, адаптируемые и компонуемые навыки, которые не забирают контроль над процессом.

Описание репозитория: **Skills for Real Engineers. Straight from my .claude directory.**  
Лицензия: **MIT**  
Обновлено на GitHub: **2026-07-03T06:16:33Z**

## Зачем Данилу

Это хорошая библиотека паттернов для перехода от хаотичного вайбкодинга к инженерному процессу с агентом:

- сначала выровнять задачу через интервью/grilling;
- зафиксировать доменный язык проекта в `CONTEXT.md` и ADR;
- резать планы на вертикальные issues;
- делать TDD и диагностику багов по циклу;
- регулярно улучшать архитектуру, чтобы агент не строил «ком грязи».

Для твоего фокуса **IT Lead / amoCRM / AI-интеграции** особенно полезны: `grill-with-docs`, `to-prd`, `to-issues`, `tdd`, `diagnosing-bugs`, `code-review`, `handoff`.

## Установка из README

```bash
npx skills@latest add mattpocock/skills
```

После установки автор рекомендует выбрать нужные skills и обязательно запустить:

```text
/setup-matt-pocock-skills
```

Он настраивает issue tracker, triage labels и место для создаваемых docs.

> Важно: я **не устанавливал** эти skills в Hermes/Claude. Это только заметка в базе знаний.

## Главные идеи

| Проблема | Решение из репозитория |
|---|---|
| Агент сделал не то | `grill-me` / `grill-with-docs`: агент сначала жёстко интервьюирует по задаче |
| Агент многословный и плохо понимает домен | общий язык проекта: `CONTEXT.md`, glossary, ADR |
| Код не работает | feedback loops: типы, браузер, тесты; `tdd`, `diagnosing-bugs` |
| Кодовая база превращается в грязь | регулярный дизайн кода: `codebase-design`, `improve-codebase-architecture`, `code-review` |

## Skills из репозитория

### Engineering

- **[ask-matt](https://github.com/mattpocock/skills/blob/main/skills/engineering/ask-matt/SKILL.md)** — Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.
- **[grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)** — Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs inline.
- **[triage](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md)** — Move issues through a state machine of triage roles.
- **[improve-codebase-architecture](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md)** — Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md)** — Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo before using the other engineering skills.
- **[to-issues](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md)** — Break any plan, spec, or PRD into independently-grabbable issues using vertical slices.
- **[to-prd](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md)** — Turn the current conversation into a PRD and publish it to the issue tracker. No interview — just synthesizes what you've already discussed.
- **[prototype](https://github.com/mattpocock/skills/blob/main/skills/engineering/prototype/SKILL.md)** — Build a throwaway prototype to answer a design question — a runnable terminal app for state/logic questions, or several radically different UI variations toggleable from one route.
- **[diagnosing-bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md)** — Disciplined diagnosis loop for hard bugs and performance regressions: reproduce → minimise → hypothesise → instrument → fix → regression-test.
- **[research](https://github.com/mattpocock/skills/blob/main/skills/engineering/research/SKILL.md)** — Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent.
- **[tdd](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)** — Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **[domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)** — Actively build and sharpen a project's domain model — challenge terms against the glossary, stress-test with edge-case scenarios, and update `CONTEXT.md` and ADRs inline.
- **[codebase-design](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md)** — Shared discipline and vocabulary for designing deep modules: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface.
- **[code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md)** — Two-axis review of the diff since a fixed point: **Standards** (does it follow the repo's coding standards, plus a Fowler smell baseline?) and **Spec** (does it faithfully implement the originating issue/PRD?), run as parallel sub-agents so neither pollutes the other.

### Productivity

- **[grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)** — Get relentlessly interviewed about a plan or design until every branch of the decision tree is resolved.
- **[handoff](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md)** — Compact the current conversation into a handoff document so another agent can continue the work.
- **[teach](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md)** — Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
- **[writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md)** — Reference for writing and editing skills well: the vocabulary and principles that make a skill predictable.
- **[grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)** — Interview the user relentlessly about a plan or design until every branch of the decision tree is resolved. The reusable loop behind `grill-me` and `grill-with-docs`.

## Как применить у себя

1. Взять не весь набор, а 3–5 рабочих skills под текущий стек.
2. Начать с процесса: `grill-with-docs → to-prd → to-issues → tdd/code-review → handoff`.
3. Для рабочих интеграций завести проектный `CONTEXT.md`: термины amoCRM, сущности, воронки, webhooks, ограничения клиента.
4. Для сложных багов использовать не «почини», а цикл `reproduce → minimise → hypothesise → instrument → fix → regression-test`.
5. Раз в несколько дней/итераций прогонять архитектурный обзор, иначе агент быстро нарастит технический долг.

## Что можно украсть как принципы

- **Grilling before coding** — агент должен сначала добить неопределённость вопросами.
- **Vertical slices** — задачи должны быть независимо берущимися в работу.
- **Domain language** — меньше болтовни, больше точных терминов проекта.
- **Feedback loop first** — без тестов/типов/запуска агент слепой.
- **Design every day** — AI ускоряет не только разработку, но и энтропию.

## Связи

- [[AI]] — MOC по AI-инструментам и промптингу.
- [[Claude Code]] — базовая заметка по Claude Code.
- [[Что такое skills]] — общая концепция skills.
- [[Локальная установка skills]] — установка skills локально.
- [[Аудит skills]] — проверка качества и безопасности skills.
- [[Безопасность skills]] — риски сторонних skills.
- [[Claude Code Prompt Library]] — библиотека промптов Claude Code.
