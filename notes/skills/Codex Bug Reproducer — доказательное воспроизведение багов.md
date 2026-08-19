---
type: skill
status: reference
created: 2026-08-03
source: https://github.com/Kappaemme-git/codex-bug-reproducer
tags:
  - ai
  - codex
  - debugging
  - testing
  - quality
---
# Codex Bug Reproducer — доказательное воспроизведение багов

[Codex Bug Reproducer](https://github.com/Kappaemme-git/codex-bug-reproducer) — MIT-skill для Codex, который ищет вероятные баги в кодовой базе или превращает известный баг-репорт в минимальное воспроизведение. Его ключевое правило: **подозрение не является багом, пока конкретный тест не упал по предсказанной причине**.

## Что делает

- читает код, контракты, тесты, вызовы, схемы и историю изменений в read-only режиме;
- находит и ранжирует кандидатов по достижимости, доказательствам ожидаемого поведения, воспроизводимости и impact;
- перед созданием теста показывает точный триггер, ожидаемый и предполагаемый фактический результат, место в коде и риск;
- создаёт узкий deterministic regression test только после разрешения;
- отделяет настоящий repro от ошибки setup-а или нерелевантного падения;
- после подтверждения изолирует root cause и отдельно запрашивает разрешение на production-patch;
- фиксирует red → green доказательство и генерирует Markdown + JSON evidence-отчёт.

## Два approval gate

| Этап | Что разрешено | Что запрещено без следующего согласия |
|---|---|---|
| До Gate 1 | читать код/конфиг/тесты/логи/git; безопасно запустить уже существующий targeted test | создавать файлы, ставить зависимости, менять код/конфиг, запускать миграции или formatter |
| Gate 1: тест кандидата | создать только заранее перечисленные reproduction files и выполнить конкретную команду | менять production code, добавлять «заодно» cleanup или другой фикс |
| Gate 2: фикс | изменить только перечисленные production files и прогнать согласованный набор проверок | расширять scope при изменении файлов, API, зависимостей или подхода без нового согласия |

Это полезная защита от типичной херни: агент увидел странный участок кода, объявил его багом и сразу «починил» поведение, которое могло быть намеренным.

## Режимы

- **`hunt-and-prove`** — по умолчанию: искать кандидаты и доказывать сильнейшие;
- **`reproduce-only`** — остановиться на минимальном падающем кейсе, не править production;
- **`prove-fix`** — для известного бага: reproduction → отдельное согласие → фикс → red/green;
- **`flaky`** — для timing/order/concurrency-зависимых падений; единичный случай не считать доказанным.

## На что skill смотрит при поиске

Приоритетные поверхности: границы и pagination, state/lifecycle, различие create/update validation, `0`/`false`/пустая строка, время/UTC/округление, identity и cache keys, async/error paths, idempotency/retry, access/tenant boundaries.

Кандидат остаётся в списке только если есть: достижимый путь, конкретный trigger, защищаемый контракт ожидаемого поведения, тест, отличающий ожидаемое от фактического, и именно ошибка поведения — не стилистический спор или новая feature request.

## Пример использования upstream

```text
Use $bug-reproducer to scan this codebase for likely bugs, rank the strongest candidates, and ask before creating tests or changing code.
```

Известный симптом:

```text
Use $bug-reproducer to investigate this bug: requesting page 1 skips the first results. Propose a minimal reproduction and wait for my approval before changing project files.
```

Только доказательство без фикса:

```text
Use $bug-reproducer in reproduce-only mode to find and prove likely bugs in this project. Do not change production code.
```

## Артефакты

После согласованных действий skill создаёт:

```text
outputs/bug-reproducer-evidence.json
outputs/bug-reproducer-report.md
```

В отчёте: исходный симптом, expected vs actual, минимальный repro, root cause, согласованные файлы, команды и red/green evidence, broader checks, ограничения и остаточные риски. Возможные статусы: `REPRODUCED`, `NOT_REPRODUCED`, `INCONCLUSIVE`, `FIX_PROVEN`, `STILL_FAILING`, `FIX_REGRESSION` и др.

## Применимость для Данила

Хороший паттерн для сложных агентных разработок и клиентских систем: сначала доказать баг через контракт и минимальный тест, затем согласованно менять код. Особенно нужен там, где опасны silent regression: CRM-автоматизации, интеграции API, расчёты, роли и доступы.

Но запускать «сканирование на баги» по любой базе без цели — легко потратить время на низкоприоритетные edge cases. Адекватный вход: конкретный симптом, дорогой участок, свежая регрессия или аудит перед релизом.

## Установка

Upstream предлагает:

```bash
npx --yes codex-bug-reproducer@latest
```

Это кладёт skill в `~/.codex/skills/bug-reproducer` и требует restart Codex. Для Hermes skill не установлен и совместимость не подтверждена: переносить можно методологию, но не считать Codex-конфиг готовым к использованию здесь.

## Связи

- [[Matt Pocock Skills]] — содержит соседний disciplined loop `diagnosing-bugs`.
- [[Open Code Review — AI code review CLI]] — другой слой контроля качества кода.
- [[30-minute security checklist for vibe coding]] — корректность не заменяет security-аудит.
- [[Спецификация]] — контракты и ожидаемое поведение должны быть явными до проверки бага.

## Источник

- GitHub: [Kappaemme-git/codex-bug-reproducer](https://github.com/Kappaemme-git/codex-bug-reproducer), README, SKILL.md и references, проверено 2026-08-03.
- Локально просмотренная ревизия: `52a7a22d463e36d491a4ba4eb31b58a5bd813cc8`.
