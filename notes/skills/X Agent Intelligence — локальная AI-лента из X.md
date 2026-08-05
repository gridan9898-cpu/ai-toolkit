---
type: source
status: reference
created: 2026-08-03
source: "Сообщение Данила + https://github.com/dair-ai/dair-academy-plugins"
repo: "https://github.com/dair-ai/dair-academy-plugins/tree/main/plugins/x-agent-intelligence"
tags:
  - ai
  - skills
  - mcp
  - x
  - intelligence-feed
---
# X Agent Intelligence — локальная AI-лента из X

Источник: сообщение Данила + [DAIR Academy Plugins / x-agent-intelligence](https://github.com/dair-ai/dair-academy-plugins/tree/main/plugins/x-agent-intelligence).

`x-agent-intelligence` — skill/plugin для сборки из **официального X MCP** локальной HTML-ленты по AI, агентам, исследованиям, релизам, статьям и проектам. Результат — self-contained `feed.html`: поиск, фильтры категорий, группировка по датам, авторы и аватары, ссылки на исходные посты, краткое «почему важно» и превью медиа при наличии.

## Что делает

1. Через X MCP получает посты выбранных аккаунтов за заданный период.
2. Отбрасывает ответы и репосты по умолчанию, дедуплицирует по ID.
3. Ранжирует не только по engagement, а по релевантности, качеству источника, свежести и разнообразию.
4. Делает краткие **фактические** заголовки и summary, оставляя ссылку на каждый первичный пост.
5. Рендерит один локально открываемый `feed.html`, без backend, build-step или внешних runtime-зависимостей.

Исходные тексты постов по умолчанию не обязательно сохраняются: авторы рекомендуют хранить ссылки и короткие summaries, а не републиковать целиком посты или скачивать чужие медиа без законного основания.

## Что требуется

- подключить официальный X API MCP: `https://api.x.com/mcp`;
- для read-only варианта достаточно app-only Bearer token в локальном secret/config, не в репозитории и не в HTML;
- альтернативно официальный bridge `xurl` с OAuth 2.0 PKCE; его `~/.xurl` содержит refresh-токены и считается секретом;
- установить plugin из DAIR Academy Plugins — upstream-инструкция ориентирована на Claude Code; skill описан как vendor-neutral, но фактическую совместимость с Hermes надо проверять после установки/подключения MCP.

Если X MCP не подключён, корректное поведение — остановиться и настроить доступ, **не подменять его скрейпингом и не выдумывать посты**.

## Установка и запуск (из upstream)

```text
/plugin marketplace add dair-ai/dair-academy-plugins
/plugin install x-agent-intelligence@dair-academy-plugins
```

Базовый запрос:

```text
Use the x-agent-intelligence skill to build a self-contained local feed from my X MCP connection; ask for my source handles if needed, save feed.html, and validate it.
```

Для русской формулировки из сообщения Данила:

```text
Используй skill x-agent-intelligence, чтобы создать автономную локальную ленту на основе моего подключения к X MCP; при необходимости запроси у меня хендлы источников, сохрани результат в feed.html и проверь его.
```

## Стартовый набор источников — не копировать весь

В assets есть публичный список, но он слишком широк для первой ленты. Для трека Данила разумнее начать с **8–12 аккаунтов** и раз в неделю вычищать шум. Кандидаты из списка upstream: `NousResearch`, `AnthropicAI`, `OpenAI`, `OpenAIDevs`, `GoogleDeepMind`, `huggingface`, `simonw`, `karpathy`, `swyx`, `bcherny`, `thdxr`, `ClaudeDevs`.

Нужно разделить источники по цели, иначе «AI-новости» снова превратятся в бесконечный поток:

| Контур | Что отслеживать |
|---|---|
| Практика и доход | агенты, AI-инфраструктура, кейсы внедрения, инструменты для разработки |
| Глубина | модели, исследования, evals, архитектурные решения |
| Рынок | запуски продуктов и паттерны спроса, а не весь инфошум |

## Регулярный запуск

Skill не содержит scheduler и не хранит credentials, state или оркестрацию. После первого валидного прогона обновление можно запускать по cron/Hermes раз в день; режим «каждые 4 часа» имеет смысл только если лента реально используется для быстрых решений. Иначе это будет регулярное производство шума.

## Вывод для Данила

Гипотеза хорошая как **контролируемый research-вход** для AI-трека и кейсов. До настройки нельзя заявлять, что она работает в Hermes: сначала нужен X MCP и тестовый запуск. Критерий ценности — за неделю лента должна дать хотя бы несколько применимых идей/сигналов, а не просто чтение.

## Связи

- [[DAIR Academy Lesson Generator]] — другой plugin из того же набора DAIR Academy Plugins.
- [[Что такое MCP]] — транспорт, через который skill получает данные X.
- [[Эпистемическая маршрутизация]] — первичные посты и summary нужно отделять от непроверенных заявлений.
- AI-архитектор и вайбкодинг — лента должна питать практику и кейсы, а не служить новостной зависимостью.

## Источник и проверка

- [README plugin](https://github.com/dair-ai/dair-academy-plugins/tree/main/plugins/x-agent-intelligence), [official X MCP docs](https://docs.x.com/tools/mcp), проверено 2026-08-03.
- Локально просмотрена ревизия DAIR Academy Plugins: `0abffdcb374644c77b2aabf02f694e15f85ebc16`; plugin version `1.4.0`.
