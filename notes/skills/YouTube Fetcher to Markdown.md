---
type: tool
created: 2026-07-02
status: seed
source:
  - "https://github.com/JimmySadek/youtube-fetcher-to-markdown"
moc: "[[AI]]"
tags:
  - ai
  - knowledge-base
  - skills
  - telegram
---
# YouTube Fetcher to Markdown

`youtube-fetcher-to-markdown` — Claude Code / agent skill: превращает YouTube-видео в структурированную Markdown-заметку.

Источник: https://github.com/JimmySadek/youtube-fetcher-to-markdown

## Что делает

На вход получает YouTube URL или video ID. На выходе создаёт `.md` файл с:

- YAML frontmatter;
- названием видео;
- каналом;
- ссылкой;
- video ID;
- датой выгрузки;
- языком субтитров;
- типом captions: manual / auto-generated;
- длительностью;
- датой публикации;
- описанием видео;
- chapters, если доступны;
- полным transcript.

Файл по умолчанию сохраняется в:

```text
~/yt_transcripts/YYYY-MM-DD_video-title_[VIDEO_ID].md
```

## Зависимости

Обязательные:

```bash
pip install youtube-transcript-api requests
```

Рекомендуемая:

```bash
pip install yt-dlp
```

`yt-dlp` нужен для нормальной меты: description, chapters, duration, upload date.

## Ограничения

- Работает только если у видео есть captions: ручные или auto-generated.
- Если captions отключены, нужен Whisper/ASR.
- Private / age-restricted видео могут не доставаться.
- Качество transcript зависит от языка и качества auto-captions.

## Польза для базы знаний

Сильный инструмент для вытаскивания знаний из видео без ручного конспектирования.

Сценарии:

- YouTube → transcript → summary → evergreen note.
- Видео курса → структурированный конспект.
- Интервью/подкаст → тезисы и цитаты.
- Англоязычный эксперт → методология в Markdown.
- Материал для Telegram-поста или статьи.

## Как просить агента

```text
Use youtube-fetcher.
Fetch transcript from this YouTube URL, save it as Markdown, then make a structured summary with key ideas, timestamps, and useful quotes.
```

Русская версия:

```text
Достань transcript из этого YouTube-видео, сохрани в Markdown, затем сделай структурированную выжимку: ключевые идеи, таймкоды, цитаты и что можно добавить в базу знаний.
```

## Проверка установки для Hermes

Проверено 2026-07-02 в текущей среде Hermes:

- `python3` есть;
- `npx` есть;
- `yt-dlp` установлен: `/home/adam/.local/bin/yt-dlp`;
- Python-зависимости уже есть:
  - `youtube_transcript_api`;
  - `requests`;
- `fetch_transcript.py --check-deps` возвращает `All dependencies are installed.`

Вывод: **технически можно поставить как локальный Hermes skill**.

Но это не обязательно: сам скрипт уже можно использовать напрямую. Для аккуратной установки лучше положить skill в отдельную папку внутри Hermes skills и поправить `SKILL.md`, потому что оригинал ожидает путь:

```text
~/.config/skillshare/skills/youtube-fetcher/scripts/fetch_transcript.py
```

В Hermes путь будет другим, например:

```text
/home/adam/.hermes/skills/external/youtube-fetcher-to-markdown/scripts/fetch_transcript.py
```

## Рекомендованный вариант установки

Не ставить через `npx skills add` вслепую. Лучше:

1. Склонировать репозиторий в `~/.hermes/skills/external/youtube-fetcher-to-markdown/`.
2. Провести [[Аудит skills|аудит безопасности]].
3. Заменить в `SKILL.md` путь `~/.config/skillshare/...` на Hermes-путь.
4. Проверить командой:

```bash
python3 ~/.hermes/skills/external/youtube-fetcher-to-markdown/scripts/fetch_transcript.py --check-deps
```

5. Протестировать на одном коротком YouTube-видео.

## Аудит безопасности: быстрый вывод

Скрипт выглядит умеренно безопасно:

- не использует `shell=True`;
- вызывает `yt-dlp` через список аргументов;
- пишет файлы только в `~/yt_transcripts/` или в явно заданный `--output`;
- сетевые обращения ограничены YouTube / oEmbed / transcript API;
- нет `eval` / произвольного выполнения кода.

Риск: это всё равно сторонний репозиторий, поэтому перед постоянной установкой надо фиксировать конкретный commit и не автообновлять без повторного аудита.

## Связи

- [[AI]] — MOC по AI-инструментам и skills.
- [[Что такое skills]] — общая тема agent skills.
- [[Аудит skills]] — проверка сторонних skills перед установкой.
- [[Telegram-бот для summary YouTube-видео]] — смежная идея продукта.
