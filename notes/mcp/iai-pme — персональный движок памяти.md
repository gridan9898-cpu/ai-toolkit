---
type: tool
created: 2026-07-28
source: https://github.com/CodeAbra/iai-personal-memory-engine
repository: CodeAbra/iai-personal-memory-engine
license: MIT
status: watchlist
tags:
  - agents
  - ai
  - hermes
  - memory
  - mcp
  - privacy
moc: "[[AI]]"
---
# iai-pme — персональный движок памяти

Источник: [CodeAbra/iai-personal-memory-engine](https://github.com/CodeAbra/iai-personal-memory-engine)  
Связи: [[Что такое MCP]], [[AgentMemory]], [[AI]], [[Hermes-оператор]]

## Что это

`iai-pme` — локальный persistent-memory engine для AI-агентов через MCP-over-stdio. Он хранит эпизоды диалогов дословно, строит semantic/procedural layers, возвращает релевантные фрагменты и может консолидировать память в фоне.

Заявлены Linux/macOS, Python 3.11–3.12, Node 18+ и Rust. Основной storage — `~/.iai-mcp/`; база заявлена зашифрованной AES-256-GCM.

## Где применим

Сильный сценарий проекта — Claude Code и Codex CLI: hooks автоматически захватывают сессии и добавляют recall при старте. Для других MCP-клиентов доступны MCP tools, но автоматический capture/recall авторы пока не реализовали.

## Проверка для Hermes — 2026-07-28

Проверен исходный код `main` на commit `1cd1000…` и релиз `v2.6.1`.

- Hermes технически умеет подключать local stdio MCP, поэтому tools можно было бы добавить.
- Для Hermes автоматические hooks не заявлены. Значит ключевая функция iai-pme — фоновый полный capture и reinjection контекста — в текущем контуре не заработает без отдельной интеграции.
- В процессе захвата текст диалогов временно хранится в plaintext JSONL в `~/.iai-mcp/.deferred-captures/`; файлы создаются с правами `0600`.
- В коде не найден обычный telemetry/analytics HTTP-контур; на Linux daemon использует Unix socket. Это статическая проверка, не независимый security audit.
- Проект предусматривает вызовы `claude -p` для части synthesis/consolidation. Поэтому «полностью локальный» режим нужно отдельно подтверждать конфигурацией и отключением таких путей.
- Python dependency audit на дату проверки не показал известных CVE. Проект молодой, текущий commit не подписан; это не основание доверять ему как зрелому security-critical слою.

## Решение

**Не ставить в рабочий Hermes-контур сейчас.**

Причина: он дублирует уже существующую систему Hermes (`user/memory`, контекстные Markdown-файлы, `session_search`, Obsidian), при этом добавляет отдельную непрозрачную базу дословных диалогов, daemon и риск захвата чувствительных данных. Для Hermes не доступен его ключевой автоматический workflow.

## Если вернуться к тесту

Только при подтверждённой боли: текущие `session_search` + канонический контекст не находят нужные детали прошлых сессий.

Тестировать изолированно:

1. зафиксировать release `v2.6.1` (commit `6bf778…`), не ставить плавающий `main`;
2. отдельный venv и отдельный store без реальных чувствительных диалогов;
3. не устанавливать capture hooks;
4. разрешить Hermes только read-oriented инструменты (`memory_search`, `memory_recall`), не весь набор MCP tools;
5. отключить / проверить отсутствие вызовов `claude -p`;
6. сравнить recall с `session_search` и Obsidian по конкретным тестовым кейсам.
