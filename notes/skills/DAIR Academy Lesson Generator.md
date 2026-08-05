---
type: source
created: 2026-07-04
status: active
source: "Telegram video + text from Данил; https://github.com/dair-ai/dair-academy-plugins"
repo: "https://github.com/dair-ai/dair-academy-plugins/tree/main/plugins/lesson-generator"
moc: "[[AI]]"
tags:
  - ai
  - claude-code
  - learning
  - skills
---
# DAIR Academy Lesson Generator

Источник: Telegram-видео/пост от Данила + [dair-ai/dair-academy-plugins](https://github.com/dair-ai/dair-academy-plugins).  
Контекст из поста: Elvis Saravia выпустил skill `/lesson-generator` для обучения чему угодно с агентом.

## Что это

`lesson-generator` — plugin/skill из **DAIR Academy Plugins** для Claude Code. Он генерирует компактные интерактивные мини-курсы как браузерный HTML/CSS/JS-артефакт.

Типовой результат:

- `index.html` — оболочка курса: sidebar, lesson reader, flashcards, quizzes, review;
- `styles.css` — дизайн под чтение и обучение;
- `script.js` — данные курса, навигация, flashcards, quiz feedback.

По умолчанию делает **6–8 уроков**, если пользователь явно не просит один урок.

## Что умеет

- Генерировать уроки/курсы по любой теме.
- Делать структуру курса: описание, последовательность уроков, цели, ключевые концепты.
- Добавлять 2–4 learning objectives на урок.
- Добавлять 2–3 flashcards на урок.
- Добавлять 1–2 quiz / knowledge check на урок.
- Делать cumulative review / final quiz.
- Встраивать source links, если есть исходники или web-backed content.
- Представлять курс как self-contained browser artifact без backend/database.
- В связке с `/image-generator` добавлять изображения через Nano Banana Pro.

## Установка

Marketplace:

```text
/plugin marketplace add dair-ai/dair-academy-plugins
```

Установка plugin:

```text
/plugin install lesson-generator@dair-academy-plugins
```

Общий шаблон из DAIR Academy Plugins:

```text
/plugin install <plugin-name>@dair-academy-plugins
```

## Связка с image-generator

`image-generator` — соседний plugin из того же marketplace. Использует Gemini Nano Banana Pro / `gemini-3-pro-image-preview`.

Установка:

```text
/plugin install image-generator@dair-academy-plugins
```

Требуется `GEMINI_API_KEY`:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Возможности image-generator:

- text-to-image;
- image editing;
- multi-image composition;
- output 1K/2K/4K;
- aspect ratios от `1:1` до `21:9`;
- Google Search grounding;
- до 14 reference images;
- SynthID watermark на сгенерированных изображениях.

## Пример из видео

В DAIR.AI Academy Builder пользователь просит:

```text
Build me a mini course on dark matter. These lessons will be for a high-school student.
```

В интерфейсе подключены:

- `/frontend-design`
- `/lesson-generator`
- `/image-generator`
- web search

Результат: интерактивный курс про dark matter с разделами вроде:

- The Universe's Hidden Mystery
- How We Know It Exists
- Dark Matter vs Regular Matter
- How We Hunt for Dark Matter
- The Mystery Continues
- Knowledge Check

Через image-generator добавляются визуалы:

- `hero.png` — cosmic scene для первого урока;
- `galaxy-halo.png` — dark matter halo around a galaxy;
- `lensing.png` — gravitational lensing visualization.

## Как применять Данилу

Хороший инструмент для быстрого обучения и упаковки знаний:

1. **Изучение новой темы** — попросить mini-course на тему, которую надо быстро разложить.
2. **Обучение сотрудников/клиентов** — делать микро-курсы по процессам, CRM, AI-инструментам, регламентам.
3. **Личный бренд** — превращать сложную тему в интерактивный образовательный артефакт для аудитории.
4. **Внутренняя база агентства** — делать onboarding-уроки: amoCRM, интеграции, webhooks, QA, безопасность.
5. **Практика product thinking** — курс как маленький продукт: структура, прогресс, проверки понимания, визуалы.

## Сильная идея

Это не просто “сгенерировать текст урока”. Ценность в том, что агент сразу собирает **обучающий артефакт**:

```text
тема → структура → уроки → проверка знаний → визуалы → HTML-продукт
```

Для Данила это полезнее обычного конспекта, потому что результат можно открыть, показать, переиспользовать и доработать.

## Ограничения и риски

- Нужна проверка фактов, особенно если курс строится по web search.
- Сгенерированный курс может выглядеть убедительно, но быть поверхностным.
- Для коммерческого/клиентского обучения нужен human review.
- Изображения через Nano Banana требуют Gemini API key и могут иметь ограничения модели.
- Self-contained HTML удобен для прототипа, но не равен полноценной LMS.

## Практический prompt-шаблон

```text
Use /lesson-generator to build a compact 6-lesson interactive course on [topic] for [audience].
Goal: [what learner should be able to do].
Include: lesson objectives, short explanations, examples, flashcards, per-lesson quiz, final review.
If web search is used, add clickable source cards.
If /image-generator is available, add 2-3 relevant visuals.
Keep it concise and useful for repeated study.
```

## Связи

- [[Claude Code]] — среда, куда ставится plugin.
- [[Что такое skills]] — общий концепт agent skills.
- [[Vercel Find Skills]] — подход к поиску и установке skills под задачу.
- [[YouTube Fetcher to Markdown]] — похожий контур превращения контента в учебные материалы.
- [[AI-проекты из контактов и реальных болей]] — можно использовать для образовательных микро-продуктов.
- [[Как обучаться быстрее]] — связанная тема обучения через структуру и практику.
