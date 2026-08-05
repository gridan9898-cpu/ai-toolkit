---
type: note
created: 2026-07-05
updated: 2026-07-05
status: seed
source: "https://github.com/Leonxlnx/taste-skill"
moc: "[[AI]]"
tags:
  - agents
  - ai
  - design
  - skills
  - vibe-coding
---
# Taste Skill

**Taste Skill** — «anti-slop» frontend-фреймворк в виде portable **Agent Skills** для AI coding agents. Улучшает интерфейсы, которые генерит AI: сильнее layout, типографика, motion и spacing вместо шаблонного «boilerplate-looking UI».

Источник: [GitHub — Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)  
Сайт: [tasteskill.dev](https://tasteskill.dev)  
Лицензия: MIT.

## Что это

Набор SKILL.md-файлов, которые агент подхватывает автоматически (Codex, Cursor, Claude Code и др.). Философия: правила описывают **design intent**, а не конкретный фреймворк, поэтому работает с React/Vue/Svelte.

Две категории skills:

- **implementation skills** — выдают код;
- **image-generation skills** — выдают только референс-картинки (web/mobile/brand kits) для дальнейшей реализации.

Отличие от других AI-дизайн-скиллов (по словам автора): много специализированных вариантов, регулируемые «dials» в ключевых скиллах и anti-repetition правила, основанные на отдельном research.

## Набор скиллов

| Skill | Install name | Для чего |
|---|---|---|
| taste-skill | `design-taste-frontend` | базовый: агрессивный anti-slop, вариативный layout, GSAP-motion |
| image-to-code-skill | `image-to-code` | image-first: сгенерить референсы → проанализировать → сверстать под них |
| redesign-skill | `redesign-existing-projects` | аудит и починка существующего UI (layout, spacing, иерархия) |
| soft-skill | `high-end-visual-design` | premium/«дорогой» UI: мягкий контраст, whitespace, spring motion |
| output-skill | `full-output-enforcement` | заставляет модель дописывать до конца, без placeholder-заглушек |
| minimalist-skill | `minimalist-ui` | editorial UI в духе Notion/Linear |
| brutalist-skill | `industrial-brutalist-ui` | Swiss type, жёсткий контраст, экспериментальный layout |
| stitch-skill | `stitch-design-taste` | правила под Google Stitch + опциональный экспорт `DESIGN.md` |

Каждый скилл делает одну задачу — брать нужно точечно, не все сразу.

## Настройки (dials в taste-skill)

Числа 1–10 в начале файла:

- **DESIGN_VARIANCE** — экспериментальность layout (ниже: центрированный/чистый · выше: асимметрия/модерн);
- **MOTION_INTENSITY** — глубина анимаций (ниже: hover · выше: scroll/magnetic);
- **VISUAL_DENSITY** — плотность инфы на экране (ниже: воздух · выше: плотные дашборды).

## Зачем Данилу

Тот же класс задач, что и [[Impeccable]] / [[Frontend design]] — убрать «AI-slop» из интерфейсов, но акцент на **стилевых пресетах под нужный характер продукта** (premium / minimalist / brutalist) и на image-first пайплайне.

Полезно для:

- лендингов и портфолио;
- UI-прототипов CRM/дашбордов агентства (`VISUAL_DENSITY` под дашборды);
- редизайна уже собранного UI (`redesign-skill`);
- связки «референс-картинка → верстка» через `image-to-code`.

## Как ставить

Все скиллы ставятся через один CLI:

```bash
npx skills add https://github.com/Leonxlnx/taste-skill
```

Один конкретный скилл — по install name:

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Также можно просто скопировать `SKILL.md` в проект или вставить в разговор с Codex/ChatGPT.

## Практический выбор скилла

- «сделай красиво / современно» → `design-taste-frontend`;
- «дорого и спокойно» → `high-end-visual-design`;
- «строго и editorial» → `minimalist-ui`;
- «почини существующий UI» → `redesign-existing-projects`;
- «сначала картинка, потом код» → `image-to-code`.

## Связи

- [[Impeccable]] — соседний anti-slop инструмент, но с детектором и командами `/impeccable`.
- [[Hallmark]] — соседний anti-slop инструмент с 57 slop-test gates и извлечением design DNA.
- [[Frontend design]] — базовая логика: дизайн как отдельная фаза вайбкодинга.
- [[Make Interfaces Feel Better]] — финальная полировка интерфейсов.
- [[Modern Web Guidance]] — современные web/UI-практики.
- [[AI]] — MOC по AI-инструментам и вайбкодингу.
