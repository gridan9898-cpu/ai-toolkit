---
type: note
created: 2026-07-05
source: https://github.com/colbymchenry/codegraph
tags:
  - agents
  - ai
  - dev-tools
  - mcp
moc: "[[AI]]"
---
# CodeGraph

Источник: [GitHub — colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)  
Сайт/доки: [colbymchenry.github.io/codegraph](https://colbymchenry.github.io/codegraph/)  
Язык: TypeScript  
Лицензия: MIT

## Что это

**CodeGraph** — локальный pre-indexed knowledge graph для кодовой базы. Он строит граф символов, вызовов и зависимостей, а потом даёт AI-агенту точный контекст через MCP/CLI без долгого crawling по файлам.

Заявленная поддержка агентов: Claude Code, Codex, Gemini, Cursor, OpenCode, Antigravity, Kiro, Hermes Agent.

Ключевой тезис проекта: **surgical context, fewer tool calls, faster answers, 100% local**.

## Зачем Данилу

Полезно для AI-разработки и роли IT Lead:

- ускоряет понимание больших/чужих репозиториев;
- снижает количество `Read`/`grep`/поисковых проходов агента;
- помогает точнее оценивать impact изменений перед правками;
- может быть полезен для ревью legacy-проектов, CRM-интеграций, frontend/backend проектов;
- интересен как паттерн: не «дай агенту весь репозиторий», а **сначала локальный индекс → потом точечный контекст**.

## Как работает

1. Устанавливается CLI/MCP-сервер.
2. В проекте выполняется `codegraph init`.
3. Создаётся локальная `.codegraph/` база.
4. Агент получает доступ к `codegraph_explore` через MCP.
5. При изменениях файлов индекс auto-sync'ится через watcher.

Важно: индекс локальный, без API keys и внешних сервисов. Используется SQLite.

## Установка и базовый workflow

```bash
# глобальная установка
npm install -g @colbymchenry/codegraph

# настройка агентов
codegraph install

# в каждом проекте
codegraph init

# проверка состояния
codegraph status
```

Альтернативно из README:

```bash
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
```

Для удаления конфигов агентов:

```bash
codegraph uninstall
```

Для удаления индекса из проекта:

```bash
codegraph uninit
```

## MCP-интерфейс

В MCP по умолчанию выставлен один основной инструмент:

- `codegraph_explore` — возвращает entry points, связанные символы, source snippets и call paths одним запросом.

Другие инструменты существуют, но по умолчанию не показываются агенту, чтобы не перегружать выбор:

- `codegraph_node`
- `codegraph_search`
- `codegraph_callers`
- `codegraph_callees`
- `codegraph_impact`
- `codegraph_files`
- `codegraph_status`

Это важная продуктовая идея: **один сильный инструмент лучше меню из многих узких**, если цель — надёжно направить агента.

## CLI-команды, которые стоит помнить

```bash
codegraph explore <query>       # релевантный source + call paths
codegraph query <search>        # поиск символов
codegraph node <symbol|file>    # символ/source/callers или файл с line numbers
codegraph callers <symbol>      # кто вызывает символ
codegraph callees <symbol>      # что вызывает символ
codegraph impact <symbol>       # что затронет изменение символа
codegraph affected [files...]   # какие тесты затронуты изменениями
codegraph files                 # структура файлов
codegraph status                # статистика и состояние индекса
```

## Ключевые возможности

| Возможность | Смысл |
|---|---|
| Surgical Context | один запрос возвращает нужные символы, snippets и call paths |
| Full-text search | быстрый поиск по кодовой базе через FTS5 |
| Impact analysis | callers/callees/blast radius до изменения кода |
| Always fresh | watcher обновляет граф при изменениях файлов |
| 20+ языков | TS/JS, Python, Go, Rust, Java, C#, PHP, Ruby, C/C++, Swift, Kotlin, Dart, Vue, Svelte, Astro и др. |
| Framework-aware routes | понимает роуты Django, Flask, FastAPI, Express, NestJS, Laravel, Rails, Nuxt, SvelteKit, Astro и др. |
| RN/iOS bridging | связывает JS ↔ native границы в React Native / Expo / Swift / ObjC |

## Что особенно интересно

### Auto-sync без ручного `sync`

При запуске `codegraph serve --mcp` индекс поддерживается тремя слоями:

1. file watcher с debounce;
2. staleness banner, если агент запрашивает файл, который ещё не синхронизирован;
3. catch-up при подключении MCP-сервера.

То есть агенту явно сигналят, если индекс может быть чуть устаревшим.

### Impact-aware разработка

`codegraph impact` и `codegraph affected` можно использовать перед изменениями:

- что сломается, если поменять функцию/класс;
- какие тесты надо прогнать;
- какие routes/API flows затронуты.

Это прям полезный паттерн для более взрослой AI-разработки: сначала impact map, потом правка.

## Риски / ограничения

- Это внешний open-source инструмент: перед установкой в рабочую среду нужно отдельно проверить доверие, telemetry, permissions и то, какие файлы он пишет в конфиги агентов.
- В README указана anonymous telemetry; её надо явно проверить/отключить, если нужна строгая приватность.
- Как любой static analysis, не всё видит идеально: dynamic dispatch, reflection, DI containers и framework conventions могут ограничивать полноту графа.
- Для WSL/сетевых дисков есть нюансы с SQLite/WAL и lock'ами.

## Как применить

- Для большого проекта: перед сессией с Claude Code/Codex сделать `codegraph init`, затем просить агента сначала использовать `codegraph_explore`/impact analysis.
- Для ревью клиентского проекта: быстро получить карту зависимостей и риски изменений.
- Для агентства: добавить в стандарт «AI-разработка в чужом репозитории»: **index → explore → impact → edit → affected tests**.
- Для личного обучения: разобрать CodeGraph как пример инфраструктурного продукта для AI coding agents.

## Связи

- [[Claude Code]] — основной сценарий применения через MCP.
- Codex — возможный агентный сценарий применения.
- [[Что такое MCP]] — CodeGraph подключается как MCP-сервер.
- [[Awesome Codex Subagents]] — рядом по теме coding agents.
- [[AI Agents From Scratch]] — рядом по агентной инфраструктуре.
- [[Ruflo]] — соседний тяжёлый инфраструктурный инструмент: agent meta-harness со swarm-координацией.
- Hermes Agent — заявлена поддержка Hermes Agent.
- [[04 Sources/Курсы/AI-архитектор/00 - AI-архитектор|AI-архитектор]] — можно использовать как пример tooling для AI-разработки.
