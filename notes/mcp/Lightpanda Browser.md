---
type: note
created: 2026-07-31
source: https://github.com/lightpanda-io/browser
source_type: GitHub repository
status: captured
tags:
  - agents
  - ai
  - browser
  - automation
  - mcp
  - scraping
  - dev-tools
moc: "[[AI]]"
---
# Lightpanda Browser

Источник: [lightpanda-io/browser](https://github.com/lightpanda-io/browser) · проверен commit `392bb4c` от 31.07.2026 · лицензия **AGPL-3.0-only**.

## Что это

**Lightpanda** — headless-браузер на Zig, написанный с нуля для AI-агентов и автоматизации, а не fork Chromium/WebKit. Даёт CLI для fetch/render, CDP/WebSocket server для Puppeteer и других совместимых клиентов, нативные agent mode и MCP server.

По README автора, в сетевом benchmark на 933 реальных страницах Lightpanda показал peak memory 123 MB против 2 GB у Headless Chrome на 100 страницах и 5 s против 46 s на 100 страницах. Это **самоизмерение проекта**, не независимое доказательство; проверять на нужных сайтах.

## Возможности

- `lightpanda fetch` — рендер и dump HTML или Markdown; есть ожидания по selector/script/time и `--obey-robots`.
- `lightpanda serve` — CDP server на localhost для подключения automation-клиента без переписывания Puppeteer-кода.
- `lightpanda agent` — выполнение веб-задач через LLM или без LLM в REPL. Сессию можно сохранить в PandaScript (JavaScript с native browser primitives) и затем воспроизводить детерминированно без токенов/model runtime.
- MCP JSON-RPC 2.0: stdio или HTTP. HTTP-режим умеет изолированные browsing sessions с отдельными page/cookies/memory либо общую сессию для нескольких агентов.
- Поддержка Anthropic, OpenAI, Gemini, Vertex AI, Hugging Face и Ollama в agent mode.

## Зачем Данилу

- Лёгкий browser layer для агентских сценариев: извлечь Markdown/данные с разрешённого сайта, пройти веб-flow, собрать evidence для аналитики.
- Кандидат на многосессионный MCP-браузер: каждый агент может иметь отдельный cookies/page context, не перетирая состояние других.
- Связка «LLM прототипирует web-flow → PandaScript исполняет его без модели» полезна для дешёвого повторяемого мониторинга, если сценарий уже отлажен.

## Ограничения и решение по применению

- Это не Chromium: CDP/Puppeteer-совместимость нужно проверять на сложных SPA, login-flow и сайтах с нестандартным JS; не считать её drop-in без бенча.
- По README telemetry включена по умолчанию; до запуска выключить через `LIGHTPANDA_DISABLE_TELEMETRY=true` и сверить конкретный релиз/политику приватности.
- **AGPL-3.0-only:** для модификаций и сетевого сервиса последствия лицензии нужно отдельно оценить до клиентского/коммерческого self-hosted использования. Обычная локальная автоматизация не равна автоматическому разрешению на закрытый сервис вокруг изменённого кода.
- Соблюдать ToS, robots.txt, лимиты и правила данных целевого сайта; сначала искать API.
- Сейчас не устанавливать: в Hermes уже есть браузерные инструменты. Сначала сравнить Lightpanda с текущим контуром/Playwright на 2–3 реальных разрешённых сценариях по стабильности, памяти, скорости и изоляции сессий.

## Связи

- [[AI]]
- [[Playwright MCP]]
- [[Obscura]]
- [[jcode]]
- [[Browser to API skill]]
- [[Безопасность skills]]
- [[Аудит skills]]
