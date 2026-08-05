---
type: source
created: 2026-07-04
status: active
source: "https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md"
repo: "https://github.com/vercel-labs/skills"
moc: "[[AI]]"
tags:
  - ai
  - claude-code
  - codex
  - skills
---
# Vercel Find Skills

Источник: [vercel-labs/skills — find-skills/SKILL.md](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md)

## Что это

`find-skills` — skill из репозитория **vercel-labs/skills**, который помогает агенту находить и устанавливать подходящие agent skills под задачу пользователя.

Описание из frontmatter: skill нужен, когда пользователь спрашивает «как сделать X», «найди skill для X», «есть ли skill, который…», хочет расширить возможности агента или ищет tools/templates/workflows.

Репозиторий: **vercel-labs/skills** — `The open agent skills tool - npx skills`.

На момент добавления:

- GitHub stars: **24,989**;
- updated: **2026-07-04T13:29:44Z**;
- browse skills: [skills.sh](https://skills.sh/).

## Зачем Данилу

Это не просто отдельный skill, а полезный **роутер-паттерн** для работы с экосистемой agent skills:

- не пытаться каждый раз писать workflow с нуля;
- сначала понять домен и конкретную задачу;
- проверить, есть ли уже готовый skill;
- оценить качество источника перед рекомендацией;
- установить skill только после осознанного выбора.

Для твоего фокуса **IT Lead / AI-автоматизация / Claude Code / Codex** это полезно как правило оператора: если задача повторяемая или специализированная, сначала искать installable skill, а не городить кастомный промпт.

## Как применять

Базовый поиск:

```bash
npx skills find <query>
```

Поиск с ограничением по владельцу:

```bash
npx skills find <query> --owner <owner>
```

Установка:

```bash
npx skills add <package>
```

Глобальная установка без подтверждений:

```bash
npx skills add <owner/repo@skill> -g -y
```

Проверка и обновление:

```bash
npx skills check
npx skills update
```

## Алгоритм из skill

1. Понять потребность:
   - домен: React, testing, design, deployment и т.д.;
   - конкретная задача: tests, animations, PR review, changelog;
   - насколько задача типовая и вероятно покрыта skill.
2. Сначала проверить leaderboard на [skills.sh](https://skills.sh/).
3. Если leaderboard не закрывает задачу — искать через CLI:
   - `npx skills find react performance`;
   - `npx skills find pr review`;
   - `npx skills find changelog`.
4. Перед рекомендацией проверять качество:
   - install count — лучше 1K+, осторожно с <100;
   - reputation источника — `vercel-labs`, `anthropics`, `microsoft` надёжнее неизвестных авторов;
   - GitHub stars — repo <100 stars считать слабым сигналом.
5. Дать пользователю варианты:
   - название skill;
   - что делает;
   - installs/source;
   - install command;
   - ссылку на skills.sh.
6. Если подходящего skill нет:
   - сказать прямо, что skill не найден;
   - помочь обычными возможностями агента;
   - предложить создать свой через `npx skills init`.

## Категории для поиска

| Категория | Примеры запросов |
|---|---|
| Web Development | `react`, `nextjs`, `typescript`, `css`, `tailwind` |
| Testing | `testing`, `jest`, `playwright`, `e2e` |
| DevOps | `deploy`, `docker`, `kubernetes`, `ci-cd` |
| Documentation | `docs`, `readme`, `changelog`, `api-docs` |
| Code Quality | `review`, `lint`, `refactor`, `best-practices` |
| Design | `ui`, `ux`, `design-system`, `accessibility` |
| Productivity | `workflow`, `automation`, `git` |

## Практический вывод

Нормальный workflow для агента:

```text
запрос пользователя → понять домен/задачу → skills.sh → npx skills find → quality check → предложить 2–3 варианта → установить только выбранное
```

Главная ценность — не сама команда `find`, а дисциплина: **не ставить и не советовать skills вслепую**. Сначала проверить популярность, источник и repo-quality, потом уже предлагать установку.

## Связи

- [[Matt Pocock Skills]]
- [[Antigravity Awesome Skills]]
- [[Claude How To]]
- [[Claude Code Prompt Library]]
- [[Что такое skills]]
