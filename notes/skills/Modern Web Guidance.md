---
type: note
created: 2026-07-05
source: https://developer.chrome.com/docs/modern-web-guidance?hl=ru
tags:
  - ai
  - claude-code
  - design
  - skills
moc: "[[AI]]"
---
# Modern Web Guidance

Источники:

- [Chrome for Developers — Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance?hl=ru)
- [GitHub — GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)

## Что это

**Modern Web Guidance** — набор skills/гайдов для AI coding agents, который добавляет в контекст агента современные практики веб-разработки: browser APIs, CSS/HTML/JS-фичи, performance, accessibility, compatibility и безопасные fallback-паттерны.

Поддерживается командами Google Chrome, Microsoft Edge и web dev community. На момент сохранения это preview release.

Главная идея: LLM часто тянет legacy-паттерны из обучающих данных. Modern Web Guidance подсовывает агенту свежие, экспертно отобранные и token-efficient рекомендации, чтобы он писал код на современной веб-платформе, а не городил лишний JS/библиотеки там, где уже есть нативные API.

## Зачем Данилу

Полезно для вайбкодинга, frontend-задач и AI-разработки в агентстве:

- улучшает качество кода, который генерируют Claude Code / Copilot / Antigravity / другие агенты;
- помогает не скатываться в устаревшие решения при разработке интерфейсов;
- даёт готовую базу для ревью AI-generated frontend-кода;
- полезно для внутренних стандартов: «делаем современно, доступно, быстро, без лишних зависимостей»;
- может лечь в чек-лист для frontend-проектов и mini apps.

## Что покрывает

Основные дисциплины из README:

| Блок | Что внутри |
|---|---|
| User Experience | View Transitions, entry/exit animations, parallax scroll, `scrollbar-color` |
| CSS Layout | Container queries, `subgrid`, `oklch`, `text-wrap`, line-height trimming |
| Performance | preloading, INP diagnostics, `scheduler.yield` |
| Forms & UI | CSS Anchor Positioning, Popover API, `<dialog>`, `:user-invalid`, auto-sizing fields |
| Accessibility | screen reader и keyboard operability, навигация, discoverability |
| Built-in AI | browser-native translation, summarization, language detection APIs |

В README заявлено 102 modern web features, включая CSS/Layout, HTML/DOM, JavaScript/API, security, performance и safe adoption patterns.

## Как работает

1. Агент активирует skill `modern-web-guidance` на релевантной web-задаче.
2. Агент запускает локальный semantic search:

```bash
npx modern-web-guidance@latest search "animate a dialog modal backdrop"
```

3. Затем забирает конкретный гайд:

```bash
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"
```

4. В контекст агента попадают точечные паттерны, gotchas, compatibility и fallback-рекомендации.

Важная деталь: CLI работает локально и приватно, без API keys и сетевых вызовов для поиска. `npx` используется, чтобы контент не устаревал.

## Установка

Рекомендованный вариант:

```bash
npx modern-web-guidance@latest install
```

Обновление:

```bash
npx modern-web-guidance@latest update
```

Vercel Skills CLI:

```bash
npx skills add GoogleChrome/modern-web-guidance
```

Claude Code plugin:

```text
/plugin marketplace add GoogleChrome/modern-web-guidance
/plugin install modern-web-guidance@googlechrome
/plugin  # Select GoogleChrome marketplace, press enter, enable AutoUpdate
/reload-plugins
```

Antigravity:

```bash
agy plugin install https://github.com/GoogleChrome/modern-web-guidance
```

## Примеры задач, где применять

### Новый UI

- accordion stats component с плавной анимацией открытия/закрытия;
- tab bar со sliding highlight через CSS Anchor Positioning;
- dashboard card с container queries.

### Модернизация legacy-кода

- заменить кастомные modal windows на `<dialog>`;
- мигрировать tooltips на Popover API + CSS Anchor Positioning.

### Безопасность

- passkey-based login через WebAuthn;
- starter CSP без поломки приложения;
- security audit сайта.

### Производительность

- preload страниц при hover по важным ссылкам;
- диагностика long tasks и INP;
- улучшение LCP.

## Принцип для работы с AI-агентами

Когда агент пишет frontend, ему нужно не просто «сделай компонент», а ограничение:

> Используй Modern Web Guidance: предпочитай современные нативные browser APIs, учитывай Baseline/browser compatibility, accessibility, performance и лёгкие fallback-паттерны. Не добавляй тяжёлые зависимости, если задачу решает веб-платформа.

Это снижает риск legacy-кода и лишнего JS.

## Связи

- [[Frontend design]] — рядом по UI/frontend-практикам.
- [[Claude Code]] — основной агентный сценарий применения.
- [[Claude How To]] — практическая работа с Claude Code.
- [[Vercel Find Skills]] — рядом по skills/agent workflow.
- [[Effective HTML skills]] — пересечение по web/platform-aware разработке.
- [[04 Sources/Курсы/AI-архитектор/00 - AI-архитектор|AI-архитектор]] — можно использовать как материал для frontend-блока.
