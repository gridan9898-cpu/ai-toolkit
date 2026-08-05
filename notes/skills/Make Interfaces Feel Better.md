---
type: tool
created: 2026-07-02
status: seed
source:
  - "https://jakub.kr/skills/make-interfaces-feel-better"
  - "https://skills.sh/jakubkrehel/make-interfaces-feel-better/make-interfaces-feel-better"
moc: "[[AI]]"
tags:
  - ai
  - design
  - skills
  - vibe-coding
---
# Make Interfaces Feel Better

`make-interfaces-feel-better` — skill для AI-агентов про UI-polish: мелкие визуальные детали, из-за которых интерфейс ощущается качественнее.

Источник: https://jakub.kr/skills/make-interfaces-feel-better

Skills.sh: https://skills.sh/jakubkrehel/make-interfaces-feel-better/make-interfaces-feel-better

## Для чего

Использовать при создании или ревью интерфейсов, когда экран «нормальный, но что-то не так».

Подходит для:

- UI-компонентов;
- frontend-кода;
- анимаций;
- hover states;
- теней, бордеров, радиусов;
- типографики;
- micro-interactions;
- enter/exit animations;
- визуальной полировки.

## Триггеры

Фразы, которыми можно запускать skill у агента:

- `make it feel better`
- `feels off`
- `polish the UI`
- `improve visual details`
- `check optical alignment`
- `fix spacing, radius, shadows, typography`
- `add micro-interactions`
- `make this component feel more premium`

## На что обращает внимание

- **Typography** — размер, вес, line-height, контраст, tabular numbers.
- **Hover states** — не просто смена цвета, а ощущение интерактивности.
- **Optical alignment** — выравнивание глазами, не только по пикселям.
- **Concentric border radius** — согласованные радиусы вложенных элементов.
- **Shadows** — мягкая глубина без грязи.
- **Borders / outlines** — особенно для изображений и карточек.
- **Micro-interactions** — маленькие движения, которые помогают интерфейсу чувствоваться живым.
- **Enter/exit animations** — появление и исчезновение без резкости.

## Практическая ценность

Это не «сделай красиво» в целом. Это слой финальной доводки после того, как структура экрана уже понятна.

Хорошая схема:

```text
структура → дизайн-система → компонент → UI-polish через skill → ревью глазами
```

## Как просить агента

```text
Use the make-interfaces-feel-better skill.
Review this component for UI polish: typography, spacing, hover states, shadows, border radius, optical alignment, and micro-interactions.
Do not redesign the whole screen. Keep the structure. Improve only the details that make it feel more polished.
```

Русская версия:

```text
Используй принцип Make Interfaces Feel Better.
Проверь компонент на визуальную полировку: типографика, отступы, hover states, тени, радиусы, оптическое выравнивание и микроанимации.
Не переделывай экран целиком. Структуру оставь. Улучши только детали, из-за которых интерфейс будет ощущаться качественнее.
```

## Связи

- [[AI]] — MOC по AI и промптам.
- [[Frontend design]] — центральная заметка по дизайну в вайбкодинге.
- [[Open Design]] — смежный skill/подход для дизайна.
- [[Effective HTML skills]] — смежная тема frontend-качества.
