---
type: tool
created: 2026-06-21
status: seed
source:
  - "telegram video: video_b4dcf4dfb9c9.mp4"
  - "https://github.com/lybeen/skill-create-lottie"
moc: "[[AI]]"
tags:
  - design
  - dev-tools
  - skills
---
# Lottie skill

`create-lottie` — open-source AI skill для генерации Lottie-анимаций из обычного текстового описания.

Репозиторий: https://github.com/lybeen/skill-create-lottie

## Что делает

Пользователь описывает анимацию обычным языком, а skill генерирует готовый `.json` в формате Lottie.

Пример запроса:

```text
/create-lottie a red circle that bounces up and down
```

На выходе — валидный Lottie JSON, который можно проверить в Lottie player/editor и встроить в интерфейс.

## Возможности

| Блок | Что умеет |
|---|---|
| Формы | Прямоугольники, эллипсы, звёзды, полигоны, кастомные path. |
| Цвета | RGB/RGBA, opacity, fills, strokes, gradients. |
| Анимации | Position, rotation, scale, opacity, color changes, morphing. |
| Тайминг | Duration, frame rate, keyframes, easing. |
| Слои | Несколько layers, порядок наложения, visibility range. |
| Текст | Базовые text layers со стилями. |

## Технические параметры по умолчанию

- Формат файла: `.json`
- Lottie version: `5.12.2`
- Canvas: `512x512`
- Frame rate: `60 fps`
- Цвета: `[R, G, B, A]` в диапазоне `0–1`

## Примеры задач

```text
/create-lottie a green circle that moves from left to right over 3 seconds
```

```text
/create-lottie three colored dots fading in one after another, then all fading out together
```

```text
/create-lottie a checkmark that draws itself in from the bottom, green color, 1.5 seconds
```

## Где полезно

- UI-анимации: loading, success, error, empty state.
- Быстрые motion-прототипы для лендингов и SaaS-интерфейсов.
- Генерация тестовых Lottie-ассетов без After Effects.
- Клиентские презентации: показать идею движения до полноценного дизайна.
- Микроанимации для продуктовых интерфейсов и автоматизаций.

## Ограничения

- Не заменяет полноценный motion design в сложных сценах.
- Сложные path morphing и advanced After Effects-фичи могут требовать ручной доработки.
- Нет audio support — это ограничение самого Lottie.
- Лучше начинать с простой анимации и усложнять итерациями.

## Практический вывод

Это хороший кандидат в копилку skills рядом с [[Effective HTML skills]]: `effective-html` закрывает визуальные HTML-артефакты, а `create-lottie` — лёгкие векторные анимации для интерфейсов.

Для рабочих задач можно использовать как быстрый способ сделать:

- анимированные статусы для дашбордов;
- success/error-анимации для клиентских форм;
- loading-анимации для AI-инструментов;
- простые визуальные эффекты для презентационных страниц.

Перед использованием в проде — прогонять JSON через LottieFiles Preview или другой Lottie player.

## Связанные заметки

- [[Что такое skills]]
- [[Локальная установка skills]]
- [[Effective HTML skills]]
- [[Frontend design]]
