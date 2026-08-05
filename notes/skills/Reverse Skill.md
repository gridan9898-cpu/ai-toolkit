---
type: note
created: 2026-07-06
status: seed
moc: "[[AI]]"
tags:
  - ai
  - security
  - skills
source: https://github.com/zhaoxuya520/reverse-skill
---
# Reverse Skill

## Source

- GitHub: [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)
- License: MIT
- Описание репозитория: cybersecurity skills router pack для AI coding clients.
- Поддержка клиентов по README: Claude Code, Kiro, Cursor, Cline, Windsurf, Codex CLI и др.
- Статус на момент сохранения: ~7.5k stars, ~1.2k forks, active repo.

## Что это

`reverse-skill` — пакет skill/router-правил для AI-агентов под задачи:

- reverse engineering;
- authorized penetration testing;
- security research;
- CTF;
- APK / ELF / JS / PCAP / binary analysis;
- bootstrap toolchain под нужный сценарий.

Заявленный workflow:

```text
User task → RULES.md → Skill Router → Scenario Skill → Tools / MCP / Scripts → Report + field journal
```

Идея: AI-агент по задаче выбирает подходящий playbook, проверяет доступные инструменты, поднимает недостающий toolchain и ведёт field journal, чтобы не повторять ошибки.

## Что внутри по смыслу

- `RULES.md` — главный файл поведения и маршрутизации.
- `README_AI.md` — инструкции именно для AI-агента.
- `skills/routing.md` — routing matrix по сценариям.
- `skills/tool-index.md` генерируется при setup и показывает доступность инструментов.
- `CTF-Sandbox-Orchestrator/` — набор skill-сценариев для CTF/sandbox-задач.
- Скрипты bootstrap для toolchain, включая Kali-oriented setup.
- Поддержка MCP/интеграций для security tools.

## Зачем Данилу

Полезно не как готовый «поставить и забыть», а как **референс архитектуры skill-router pack**:

1. Как организовать routing между сценариями.
2. Как разделять `RULES`, `SKILL.md`, `tool-index`, `field-journal`, scripts и references.
3. Как делать on-demand bootstrap инструментов вместо гигантского постоянного контекста.
4. Как проектировать self-evolving knowledge base / field journal для повторяемых агентских задач.
5. Как адаптировать идею для легальных внутренних задач: диагностика, аудит, документация, интеграции, CRM/DevOps-процессы.

## Важное ограничение

Это dual-use security tooling. Не ставить и не запускать автоматически.

Использовать только для:

- CTF;
- локальных лабораторий;
- анализа своих файлов/систем;
- явно авторизованного security research.

Для Данила ценность сейчас больше архитектурная: изучить структуру skill router, а не применять offensive workflow.

## Как применить безопасно

1. Не подключать глобально в Claude/Cursor/Hermes без отдельного решения.
2. Сначала изучить структуру файлов:
   - `RULES.md`
   - `README_AI.md`
   - `skills/routing.md`
   - несколько `SKILL.md` из `CTF-Sandbox-Orchestrator/`
3. Вытащить паттерны:
   - routing matrix;
   - tool availability index;
   - field journal;
   - scenario-specific skills;
   - bootstrap scripts.
4. Перенести паттерн на мирные задачи: например, `amoCRM-integration-skill-router`, `client-audit-router`, `knowledge-base-rag-router`.

## Риски

- Может содержать инструкции, которые конфликтуют с безопасным поведением агента: например, попытки подавлять safety/legal disclaimers.
- Глобальная установка такого router pack может расширить поверхность риска.
- Bootstrap scripts могут менять окружение и ставить heavy security tools.
- Перед использованием нужен ручной аудит файлов и команд.

## Связи

- [[Что такое skills]] — базовая концепция skills.
- [[Безопасность skills]] — риски установки и выполнения чужих skill packs.
- [[Claude Code Security Guidance]] — безопасная работа с coding agents.
- [[The Hitchhiker's Guide to Agentic AI]] — рядом по теме агентских систем.
