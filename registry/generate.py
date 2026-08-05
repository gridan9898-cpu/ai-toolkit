#!/usr/bin/env python3
"""Regenerate registry/registry.md from live Claude Code state on this machine.
No deps beyond stdlib. Run: python3 registry/generate.py
"""
import json
import os
from pathlib import Path
from datetime import date

HOME = Path.home()
CLAUDE_DIR = HOME / ".claude"
OUT = Path(__file__).parent / "registry.md"


def personal_skills():
    d = CLAUDE_DIR / "skills"
    if not d.is_dir():
        return []
    return sorted(p.name for p in d.iterdir() if p.is_dir())


def plugins():
    f = CLAUDE_DIR / "plugins" / "installed_plugins.json"
    if not f.is_file():
        return []
    data = json.loads(f.read_text())
    return sorted(data.get("plugins", {}).keys())


def mcp_servers():
    f = HOME / ".claude.json"
    if not f.is_file():
        return []
    data = json.loads(f.read_text())
    return sorted(data.get("mcpServers", {}).keys())


def main():
    lines = [
        "# Registry — installed skills / plugins / MCP",
        "",
        f"> Auto-generated {date.today().isoformat()} by `registry/generate.py`. "
        "Re-run after installing/removing anything. Source of truth is this machine's "
        "`~/.claude/`, not this file — regenerate, don't hand-edit.",
        "",
        "## Personal skills (`~/.claude/skills`)",
        "",
    ]
    lines += [f"- {s}" for s in personal_skills()] or ["- (none)"]
    lines += ["", "## Plugins (`~/.claude/plugins`)", ""]
    lines += [f"- {p}" for p in plugins()] or ["- (none)"]
    lines += ["", "## MCP servers (`~/.claude.json`)", ""]
    lines += [f"- {m}" for m in mcp_servers()] or ["- (none)"]
    lines.append("")
    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
