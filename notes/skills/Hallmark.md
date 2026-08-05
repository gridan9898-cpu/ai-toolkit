---
type: note
created: 2026-07-08
status: seed
source: "https://github.com/Nutlope/hallmark"
moc: "[[AI]]"
tags:
  - agents
  - ai
  - design
  - skills
  - vibe-coding
---
# Hallmark

**Hallmark** — «anti-AI-slop» design skill для AI coding agents (Claude Code, Cursor, Codex). Отказывается от типового AI-вида интерфейса: выбирает макроструктуру, применяет rule-set, прогоняет вывод через 57 slop-test gates + pre-emit self-critique перед выдачей.

Источник: [GitHub — Nutlope/hallmark](https://github.com/Nutlope/hallmark)  
Автор: Nutlope (Together AI)  
Демо: [usehallmark.com](https://usehallmark.com)  
Лицензия: MIT. ~3.6k звёзд на момент добавления.

## Что это

Тот же класс инструментов, что [[Impeccable]] и [[Taste Skill]] — убрать шаблонный «AI-вайб» из UI, который генерят coding agents. Отличие Hallmark — акцент на **уникальном визуальном отпечатке** каждой страницы и извлечении «design DNA» из чужих референсов.

## Четыре команды

| Команда | Что делает |
|---|---|
| `(default, build)` | Строит новый UI: выбирает макроструктуру, применяет rule-set, прогоняет slop-test |
| `hallmark audit <target>` | Оценивает существующий код на анти-паттерны, выдаёт punch list без правок |
| `hallmark redesign <target>` | Сохраняет копирайт/IA/бренд, но пересобирает со другой структурной «отпечаткой» |
| `hallmark study <screenshot\|URL>` | Извлекает design DNA (макроструктура, типографическая пара, цветовой якорь) из референса, опционально выдаёт портативный `design.md`. Отказывается от pixel-clone и платных шаблонов |

## Технические детали

- **20 тем** — переключение клавишей `T`.
- **57 проверок качества** (slop-test gates) + self-critique перед выдачей результата.
- Study-функция — способ вытащить «дизайн-ДНК» из понравившегося сайта/скриншота в переносимый `design.md`, а не скопировать 1:1.

## Установка

```bash
npx skills add nutlope/hallmark
```

Либо вручную скопировать `SKILL.md` и `references/`:

- Claude Code: `~/.claude/skills/hallmark/`
- Cursor: `.cursor/rules/hallmark.mdc`
- Codex: `~/.codex/skills/hallmark/`

Перед установкой — [[Аудит skills|аудит безопасности]], как и для остальных сторонних skills.

## Зачем Данилу

- Тот же кластер задач, что [[Impeccable]] и [[Taste Skill]]: лендинги, портфолио, UI-прототипы CRM/дашбордов для агентства.
- `study` полезен точечно: взять референс клиента/конкурента и вытащить design DNA вместо копирования один в один.
- `audit`/`redesign` — для полировки/переработки уже сгенерированного AI-интерфейса без потери контента.

## Связи

- [[Impeccable]] — соседний anti-slop инструмент с детекторами и командами `/impeccable`.
- [[Taste Skill]] — соседний anti-slop инструмент со стилевыми пресетами (dials).
- [[Frontend design]] — базовая логика: дизайн как отдельная фаза вайбкодинга.
- [[Make Interfaces Feel Better]] — финальная полировка интерфейсов.
- [[AI]] — MOC по AI-инструментам и вайбкодингу.
