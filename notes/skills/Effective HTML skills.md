---
type: tool
created: 2026-06-21
status: seed
source:
  - "https://github.com/plannotator/effective-html"
  - "telegram video: video_ed8094605c46.mp4"
moc: "[[AI]]"
tags:
  - design
  - dev-tools
  - skills
---
# Effective HTML skills

`effective-html` — набор готовых AI skills для генерации автономных, визуально сильных HTML-документов.

Репозиторий: https://github.com/plannotator/effective-html

## Что входит

| Skill | Для чего |
|---|---|
| `html` | Обычные self-contained HTML-страницы: отчёты, объяснения, сравнения, прототипы, презентационные страницы. |
| `html-diagram` | Полноэкранные архитектурные и системные диаграммы. Приоритет — качественный SVG, минимум лишнего текста. |
| `html-plan` | Визуально организованные HTML-страницы с планами. |

## Идея

Скиллы превращают разовые промпты для красивых HTML-артефактов в переиспользуемый инструмент. Вместо того чтобы каждый раз объяснять стиль, структуру, визуальную плотность и требования к HTML, модель подгружает готовую инструкцию и локальные референсы.

Главный фокус — не просто «сделать HTML», а получить самостоятельный визуальный артефакт:

- один HTML-файл;
- аккуратная визуальная композиция;
- высокая плотность смысла;
- тёмная тема;
- локальные референсы стиля;
- пригодность для шаринга или демонстрации.

## Установка

```bash
npx skills add plannotator/effective-html
```

Посмотреть доступные skills перед установкой:

```bash
npx skills add plannotator/effective-html --list
```

Установить конкретный skill:

```bash
npx skills add plannotator/effective-html --skill html-diagram
npx skills add plannotator/effective-html --skill html-plan
```

## Установка как plugin

### Claude Code

```bash
/plugin marketplace add plannotator/effective-html
/plugin install plannotator-effective-html@effective-html
```

### Codex

```bash
codex plugin marketplace add plannotator/effective-html
codex plugin add plannotator-effective-html@effective-html
```

## Когда использовать

- Нужно быстро собрать красивый HTML-отчёт или страницу для клиента.
- Нужно объяснить архитектуру, интеграции, stack или процесс через диаграмму.
- Нужно превратить план в визуальный документ, который проще читать и обсуждать.
- Нужно сделать самостоятельный артефакт, который можно открыть в браузере без внешней инфраструктуры.

## Практический вывод

Для нашей базы это полезно как референс по направлению [[Что такое skills]]: скиллы — это не только «инструкции для кода», но и упаковка визуального стиля, примеров и формата результата.

Особенно интересен `html-diagram`: его можно использовать для схем amoCRM-интеграций, клиентских процессов, AI-автоматизаций и архитектуры внутренних инструментов.

## Связанные заметки

- [[Что такое skills]]
- [[Локальная установка skills]]
- [[Аудит skills]]
- [[Безопасность skills]]
- [[Frontend design]]
