# ai-toolkit

Реестр и заметки по AI skills / MCP-серверам — вынесено из личного vault, чтобы не засорять базу знаний и искать в одном месте.

## Структура

- [`registry/registry.md`](registry/registry.md) — что реально установлено на машине (skills, plugins, MCP servers). Автогенерируется, не редактировать руками.
- `registry/generate.py` — пересобирает `registry.md` из `~/.claude/` (skills, plugins, `~/.claude.json` → mcpServers). Запуск: `python3 registry/generate.py`.
- `notes/skills/` — заметки-обзоры про skills: концепты, чужие подборки, конкретные skills на примете.
- `notes/mcp/` — то же для MCP.
- `notes/agents/` — субагенты: конфиги, README, готовые агенты под конкретные роли (`agent-doctor` — линтер конфигов агентов/skills).

## Обновить реестр

```bash
python3 registry/generate.py
git add registry/registry.md
git commit -m "registry: refresh"
```
