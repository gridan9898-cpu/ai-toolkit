---
type: note
created: 2026-07-31
source: https://github.com/Kappaemme-git/codex-mac-storage-cleanup
source_type: GitHub repository
status: captured
tags:
  - ai
  - skills
  - codex
  - macos
  - storage
  - safety
moc: "[[AI]]"
---
# Mac Storage Cleanup skill

Источник: [Kappaemme-git/codex-mac-storage-cleanup](https://github.com/Kappaemme-git/codex-mac-storage-cleanup) · проверен commit `66fec5d` от 26.05.2026 · npm-пакет `codex-mac-storage-cleanup` v1.0.0 · лицензия MIT.

## Что это

Skill для Codex, который сначала проводит **read-only аудит** macOS-хранилища, ранжирует кандидатов на очистку по риску и требует явного подтверждения перед изменением или удалением файлов.

В комплекте Python-скрипт `storage_audit.py`: он оценивает Trash, Downloads, user caches/logs, Xcode DerivedData/simulators, npm/pnpm/yarn/general/Cargo/Go caches, крупные файлы и типовые build-артефакты (`node_modules`, `dist`, `.next`, `target` и т.д.). По умолчанию исключает `.codex`, iCloud/Photos пути.

## Правильная логика из skill

1. Сначала аудит без изменений.
2. Показать абсолютные пути, размер, категорию и риск.
3. Получить подтверждение на **конкретный** список.
4. Личные/неоднозначные файлы перемещать в Trash; permanent delete — только для проверенных cache/log/generated artifacts.
5. После очистки сверить свободное место.

Это нормальный safety pattern для destructive-операций: отчёт → ограниченное согласование → минимальный набор действий → проверка результата.

## Важные ограничения

- Работает только на **macOS** и ориентирован на пути `~/Library`, Xcode и `/private/tmp`; на текущем Linux/Hermes не применим без отдельной адаптации.
- Installer из npm **безусловно удаляет** существующую папку `${CODEX_HOME:-~/.codex}/skills/mac-storage-cleanup`, затем копирует новую версию. Перед обновлением/установкой надо проверить, нет ли там локальных правок или другой одноимённой skill.
- На macOS пользовательский контекст Данила может отличаться от серверного; запускать audit только на целевом Mac и не переносить вывод между машинами как актуальный факт.
- Даже с read-only первым проходом нельзя считать cache автоматически безопасным: Docker volumes, local AI models, environments и Downloads требуют отдельного согласования.

## Зачем Данилу

Не как способ «почистить сервер» сейчас, а как готовый паттерн для безопасного storage-audit на Mac: когда macOS забивается Xcode, Docker, node/npm или экспортами. При реальной задаче лучше провести audit на его Mac, а не устанавливать skill вслепую.

## Связи

- [[AI]]
- [[Что такое skills]]
- [[Аудит skills]]
- [[Безопасность skills]]
- [[jcode]]
