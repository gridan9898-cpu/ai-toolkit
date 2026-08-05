---
type: tool
created: 2026-06-21
status: seed
source:
  - "https://github.com/sickn33/antigravity-awesome-skills"
moc: "[[AI]]"
tags:
  - claude-code
  - codex
  - dev-tools
  - skills
---
# Antigravity Awesome Skills

`antigravity-awesome-skills` — большая installable-библиотека agentic skills для AI coding assistants.

Репозиторий: https://github.com/sickn33/antigravity-awesome-skills

## Что это

Библиотека переиспользуемых `SKILL.md`-плейбуков для Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, GitHub Copilot и других AI-ассистентов.

Идея: вместо разрозненных промптов держать устанавливаемый каталог skills, bundles, workflows и plugin-safe distributions под повторяющиеся задачи.

На 2026-06-21 в README заявлено:

- 1,678+ skills;
- 41k+ GitHub stars;
- MIT license;
- npm installer;
- specialized plugin packs;
- workflows и bundles для разных ролей/задач.

## Установка

Полная установка библиотеки:

```bash
npx antigravity-awesome-skills
```

По умолчанию ставит skills в:

```text
~/.agents/skills
```

Проверка установки:

```bash
test -d ~/.agents/skills && echo "Skills installed in ~/.agents/skills"
```

## Установка под разные инструменты

| Tool | Команда |
|---|---|
| Claude Code | `npx antigravity-awesome-skills --claude` |
| Cursor | `npx antigravity-awesome-skills --cursor` |
| Codex CLI | `npx antigravity-awesome-skills --codex` |
| Gemini CLI | `npx antigravity-awesome-skills --gemini` |
| Antigravity IDE | `npx antigravity-awesome-skills --antigravity` |
| Antigravity CLI `agy` | `npx antigravity-awesome-skills --agy` |
| Kiro CLI | `npx antigravity-awesome-skills --kiro` |
| Custom path | `npx antigravity-awesome-skills --path ./my-skills` |

## Specialized plugins

README рекомендует не ставить всё подряд, если задача понятна. Лучше начинать с focused plugin pack под конкретный домен.

Примеры plugin packs:

| Plugin | Для чего |
|---|---|
| AAS Web App Builder | frontend/full-stack web apps |
| AAS Product Design Studio | UI, brand, portfolio, accessibility, visual work |
| AAS Security Engineer | authorized security testing, audit, hardening |
| AAS Secure App Builder | secure-by-default feature development |
| AAS Documents & Presentations | документы, конвертация, презентации |
| AAS Data Analytics | SQL, dashboards, product analytics, experiments |
| AAS Agent & MCP Builder | agentic apps, MCP tools, RAG, eval loops |
| AAS OSS Maintainer | PRs, releases, reviews, handoffs |
| AAS QA & Test Automation | тесты, browser automation, QA stabilization |
| AAS DevOps & Cloud | infrastructure, deployments, ops workflows |
| AAS API Platform Builder | API design, OpenAPI, auth, security, load tests |
| AAS SaaS Launch & Revenue | MVP, pricing, payments, analytics, SEO |
| AAS AI Product & Evaluation Ops | AI product metrics, evals, tracing, experiments |

## Как использовать

Пример первого запуска из README:

```text
Use @brainstorming to plan a SaaS MVP.
```

Для некоторых инструментов формат вызова отличается:

- Claude Code plugin flow: slash-команды или plugin marketplace;
- Cursor / Antigravity: `@skill-name`;
- Codex / Gemini CLI: текстом `Use skill-name ...`;
- Antigravity CLI `agy`: slash-команды типа `/brainstorming ...`.

## Когда полезно

- Нужна большая библиотека готовых рабочих паттернов для AI coding agents.
- Нужно быстро найти skill под задачу: coding, testing, security, DevOps, data, docs, product, growth.
- Нужно сравнить разные plugin packs и поставить не всё, а только доменный набор.
- Нужно собрать локальную skill-базу для Codex/Claude/Cursor/Antigravity.

## Риски и правило использования

Большой каталог skills — это не всегда плюс. Чем больше skills подключено без отбора, тем выше риск шума, лишнего контекста и непредсказуемых инструкций.

Правило: сначала ставить focused plugin pack под задачу, а полную библиотеку — только если реально нужен широкий локальный каталог.

Перед установкой в рабочую среду:

- проверить `SKILL.md` выбранного skill;
- смотреть разрешения/команды, которые skill предлагает запускать;
- не ставить весь каталог глобально без необходимости;
- для клиентских/боевых проектов использовать локальную установку и аудит.

## Практический вывод

Это не один skill, а каталог и installer для skill-экосистемы. Полезно держать как карту, откуда можно брать готовые skills и plugin packs под конкретные рабочие задачи.

Для наших задач особенно интересны:

- Web App Builder;
- Agent & MCP Builder;
- Data Analytics;
- QA & Test Automation;
- API Platform Builder;
- AI Product & Evaluation Ops;
- SaaS Launch & Revenue.

## Связанные заметки

- [[Что такое skills]]
- [[Локальная установка skills]]
- [[Аудит skills]]
- [[Безопасность skills]]
- [[Effective HTML skills]]
- [[Lottie skill]]
