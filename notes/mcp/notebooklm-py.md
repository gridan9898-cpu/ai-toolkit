---
type: source
created: 2026-07-08
topic: ai-tools
status: captured
source: https://github.com/teng-lin/notebooklm-py
tags:
  - agents
  - ai
  - cli
  - mcp
  - notebooklm
  - python
moc: "[[AI]]"
---
# notebooklm-py

## Source

- GitHub: https://github.com/teng-lin/notebooklm-py
- Package: unofficial Python API / CLI / MCP / agent skill for Google NotebookLM.
- License: MIT.
- Repo signal on 2026-07-08: ~17.3k stars, ~2.4k forks, active updates.

## Что это

`notebooklm-py` даёт программный доступ к NotebookLM:

- Python API;
- CLI `notebooklm`;
- MCP server;
- REST server;
- agent integration / skill for Claude Code, Codex, OpenClaw-like agents.

Покрывает основные сущности NotebookLM: notebooks, sources, chat, notes, labels, research, sharing, генерацию артефактов.

## Зачем Данилу

Полезно как инструмент для AI-оператора и личной базы знаний:

1. **Research offload** — загружать пачку документов/URL/YouTube/PDF в NotebookLM и получать ответы с цитатами, не жечь токены агента на длинное чтение.
2. **Сборка source digest** — автоматизировать импорт источников и вытаскивать summary/FAQ/study guide/briefing doc.
3. **Конвейер базы знаний** — агент может создавать notebook под тему, добавлять источники, задавать вопросы, сохранять заметки и выгружать структурированный результат в Obsidian/Hermes.
4. **Контент-артефакты** — генерировать audio overview, video overview, slide deck, infographic, quiz/flashcards/report из корпуса материалов.
5. **MCP/CLI слой** — можно подключать к агентам как инструмент, а не вручную прыгать по UI NotebookLM.

## Как применить

### Рабочий auth-flow: macOS → Hermes-хост без Xvfb

Проверенный сценарий для headless Hermes-хоста: авторизация происходит **локально на macOS**, а сервер получает только готовый auth state.

1. На macOS авторизоваться через `notebooklm-py`:
   - `notebooklm login --browser-cookies auto`, если Chrome уже авторизован в нужном Google-аккаунте;
   - иначе — интерактивный `notebooklm login` в локальном браузере.
2. Напрямую через `scp` перенести на сервер **только** файл `storage_state.json` в `~/.notebooklm/profiles/default/`.
3. На Hermes-хосте агент выставляет права `600` на этот файл и проверяет сессию: `notebooklm auth check --test`.

Не сохранять в заметках, чатах или репозиториях содержимое auth state, cookies, токены и команды с конкретными IP/хостами. По умолчанию агент **не пытается запускать графический login на сервере** и не требует Xvfb.

### Минимальный тестовый сценарий

```bash
uv tool install "notebooklm-py[browser]"
# Локальная macOS-авторизация; затем storage_state.json переносится на сервер отдельно.
notebooklm login --browser-cookies auto

# На Hermes-хосте, после безопасного переноса файла:
chmod 600 ~/.notebooklm/profiles/default/storage_state.json
notebooklm auth check --test
```

Дальше MVP-пайплайн:

1. Создать notebook под тему.
2. Добавить 5–20 источников: URL/PDF/YouTube/Markdown.
3. Попросить NotebookLM собрать:
   - главные тезисы;
   - спорные места;
   - практические применения;
   - вопросы для дальнейшего исследования;
   - цитаты/ссылки на источники.
4. Экспортировать результат в Obsidian как source digest.
5. Агент делает финальную упаковку: связи, задачи, решения, применимость к Данилу.

## Ограничения и риски

- Это **неофициальный API**: Google может поменять внутренние endpoints/UI, возможен breakage.
- Нужен auth state Google; не хранить его содержимое, cookies, токены или credentials в заметках, промптах и репозиториях.
- NotebookLM остаётся внешним сервисом: приватные/чувствительные материалы грузить осознанно.
- Для headless Hermes-хоста использовать перенос одного `storage_state.json` после локального login на macOS; графический login на сервере по умолчанию не запускать.
- Не ставить как Hermes skill без отдельного решения: сначала проверить локальный CLI/MCP сценарий.

## Быстрый вывод

Инструмент выглядит сильным для связки **NotebookLM как дешёвый слой синтеза + Hermes/агент как оператор и финальный редактор**. Приоритет применения: не «ещё одна игрушка», а конкретный pipeline для обработки курсов, YouTube, PDF и рабочих исследований в Obsidian.

## Связи

- [[AI]] — AI-инструменты и агентские workflow.
- Идея Hermes `ideas/ai-personal-knowledge-base.md` — может стать backend-слоем для анализа источников.
- [[Second Brain AI Assistant Course]] — близкая тема по личной базе знаний.
- [[Обучение]] — полезно для обработки учебных материалов.
