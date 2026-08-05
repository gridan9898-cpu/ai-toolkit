---
type: note
created: 2026-07-05
source: https://github.com/rohitg00/agentmemory
tags:
  - agents
  - ai
  - claude-code
  - codex
  - dev-tools
  - knowledge-base
  - mcp
moc: "[[AI]]"
---
# AgentMemory

Источник: [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)  
Сайт: [agent-memory.dev](https://agent-memory.dev)  
Связи: [[Claude Code]], [[CodeGraph]], [[AI Agents From Scratch]], [[AI Engineering from Scratch]], [[Structured Summary для длинных сессий]], [[Субагенты]]

## Что это

**AgentMemory** — persistent memory layer для AI coding agents. Идея простая: агент должен помнить проект, решения, ошибки, паттерны и прошлые сессии, чтобы не заставлять человека каждый раз заново объяснять контекст.

Проект заявляет поддержку Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, pi, OpenCode и любых MCP-клиентов.

## Как работает

AgentMemory подключается к агентам через hooks / MCP / plugins и собирает контекст автоматически:

- старт сессии и project path;
- user prompts после privacy filtering;
- tool use: какие файлы читались/менялись, какие команды запускались;
- ошибки инструментов;
- subagent lifecycle;
- summary на завершении сессии;
- reinjection памяти перед compaction.

По README внутри используются несколько типов памяти:

| Тип | Что хранит | Аналогия |
|---|---|---|
| Working | raw observations из tool use | short-term memory |
| Episodic | compressed summaries сессий | «что произошло» |
| Semantic | факты и паттерны | «что я знаю» |
| Procedural | workflows и decision patterns | «как делать» |

Поиск: BM25 + vector + knowledge graph + RRF fusion. Есть memory evolution: versioning, supersession, relationship graphs, auto-forgetting, TTL, contradiction detection, importance eviction.

## Зачем Данилу

- **Для больших AI-сессий:** меньше потерь контекста после compaction/new session.
- **Для coding agents:** память о структуре проекта, повторяющихся ошибках, командах, паттернах и архитектурных решениях.
- **Для агентства:** можно изучать как пример memory-инфраструктуры для внутренних AI-операторов.
- **Для Hermes/Codex/Claude Code:** полезный референс, как строить слой памяти поверх hooks, summaries, retrieval и MCP.

## Практическое применение

Не ставить сразу в рабочий контур без проверки. Нормальный тестовый сценарий:

1. поднять в отдельном sandbox-проекте;
2. подключить к одному агенту, не ко всей системе;
3. проверить privacy filtering на секретах и клиентских данных;
4. оценить качество recall: вспоминает ли реально полезное, а не шум;
5. посмотреть, насколько память раздувается и как работает forgetting;
6. только потом думать об интеграции в рабочий workflow.

## Риски

- Автоматический capture может собрать лишнее, если плохо настроены privacy filters.
- Память агента легко превращается в мусор, если нет decay/importance/contradiction handling.
- Для клиентских проектов нужен строгий threat model: что хранится, где лежит база, кто имеет доступ, как удалить данные.
- Memory layer не заменяет нормальную документацию проекта и явные решения в `DECISIONS.md` / спецификациях.

## Мой вывод

Сильный ресурс как **референс архитектуры памяти для AI-агентов**. Для Данила ценность не в «срочно поставить», а в идеях: hooks → capture → summarize → retrieve → inject → forget.

Это можно использовать как модель для развития собственной системы памяти в Hermes/рабочих AI-операторах: меньше повторных объяснений, больше устойчивого проектного контекста, но с жёсткой гигиеной приватности и шума.
