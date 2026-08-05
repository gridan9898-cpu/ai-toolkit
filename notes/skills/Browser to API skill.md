---
type: source
created: 2026-07-04
status: active
source: "https://www.skills.sh/browserbase/skills/browser-to-api"
repo: "https://github.com/browserbase/skills/tree/main/skills/browser-to-api"
moc: "[[AI]]"
tags:
  - ai
  - dev-tools
  - llm
  - skills
  - templates
---
# Browser to API skill

Источник: [skills.sh — browserbase/browser-to-api](https://www.skills.sh/browserbase/skills/browser-to-api)  
GitHub: [browserbase/skills — skills/browser-to-api](https://github.com/browserbase/skills/tree/main/skills/browser-to-api)

## Что это

`browser-to-api` — skill для **replay-driven API discovery**: берёт уже записанный `browser-trace`, сопоставляет CDP request/response события, шаблонизирует URL, выводит JSON-схемы по примерам и собирает **OpenAPI 3.1** + HTML-отчёт.

Важно: сам трафик skill **не снимает**. Он работает офлайн поверх результата sibling-skill `browser-trace`:

```text
browser-trace  → .o11y/<run>/cdp/network/{requests,responses}.jsonl
browser-to-api → .o11y/<run>/api-spec/index.html + openapi.yaml + client.mjs
```

## Зачем Данилу

Полезен для задач IT Lead / AI-автоматизации, когда нужно быстро разобраться с чужим веб-сервисом без нормальной документации:

- восстановить API сайта/кабинета по браузерному сценарию;
- получить OpenAPI-спеку для интеграции, клиента или SDK;
- понять, какие XHR/fetch endpoints дергает фронт;
- сделать отчёт по покрытию: какие пользовательские flows ещё надо пройти, чтобы расширить спеки.

Практический кейс: если клиентский сервис не даёт API-доки, можно пройти ключевые сценарии в браузере, снять trace и получить рабочую карту endpoints вместо ручного копания в DevTools.

## Как применять

Установка:

```bash
npx skills add https://github.com/browserbase/skills --skill browser-to-api
```

Базовый pipeline:

```bash
# 1. Сначала снять трафик через browser-trace
# желательно включить browse network on, чтобы сохранить response bodies

# 2. Сгенерировать спецификацию
node scripts/discover.mjs --run .o11y/my-site

# 3. Открыть главный артефакт
open .o11y/my-site/api-spec/index.html
```

Ключевые выходные файлы:

| Файл | Зачем |
|---|---|
| `index.html` | главный self-contained HTML-отчёт |
| `openapi.yaml/json` | машинно-читаемая OpenAPI 3.1 спецификация |
| `client.mjs` | zero-dep fetch client по найденным операциям |
| `report.md` | markdown summary + curl-примеры |
| `confidence.json` | уверенность по endpoints и флаги нормализации |
| `samples/*.json` | редактированные request/response примеры |

## Сильные стороны

- Автоматически режет шум: analytics, tracking, bot-defense, cookie/session plumbing, HTML page renders.
- Умеет раскладывать GraphQL / JSON-RPC / multiplexed endpoints по `operationName`, `method`, `action`, `opname`, `op`.
- Может строить response-body schemas, если вместе с `browser-trace` были сохранены body samples через `browse network on`.
- Даёт не только spec, но и человекочитаемый отчёт + примеры запросов.

## Ограничения и риски

- Покрытие ограничено только теми flows, которые реально прошли в браузере.
- Схемы индуктивные: выводятся по примерам, это не контракт сервера.
- Auth только наблюдается (`x-observed-auth`), полноценную security scheme skill не гарантирует.
- Path templating эвристический; спорные URL надо смотреть в `confidence.json`.
- Redaction best-effort: дефолтно режет типовые секреты, но кастомные токены/ключи надо добавлять через `--redact`.
- На skills.sh у skill были аудиты: Gen Agent Trust Hub — pass, Socket — pass, Snyk — fail. Перед реальным использованием в проекте стоит посмотреть причину Snyk fail.

## Лучшие практики

1. Проходить в браузере именно те сценарии, которые надо документировать.
2. Для шумных сайтов ограничивать origin через `--origins`.
3. Сначала смотреть `report.md` / `index.html`, а не сразу верить OpenAPI.
4. Если нужен более уверенный spec — ставить `--min-samples 2+`.
5. Если важны response schemas — обязательно сочетать с `browse network on`.

## Связи

- [[Vercel Find Skills]] — общий подход: сначала искать готовые skills, потом ставить осознанно.
- [[Что такое skills]] — концепт agent skills.
- [[Реверс-инжиниринг]] — практический сценарий восстановления API.
- [[AI Vibe Coding Cookbook]] — может пригодиться как инструмент для вайбкодинг-интеграций.
