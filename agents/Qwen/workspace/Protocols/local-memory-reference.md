# Qwen Local Memory System — Reference Guide

This is a **local-only reference** for Qwen on this machine. Not synced externally.

## How memory works
- **Built-in Hermes profile memory**: Durable across sessions. Stores facts, preferences, corrections, and skills.
  - `hermes memory list` — list stored memories
  - `hermes memory add "what you want to remember"` — add
  - Skills stored in `~/.hermes/skills/`
- **Obsidian vault memory**: Human-readable, shareable between agents.
  - Durable memory: `Agents/Hermes/MEMORY.md` (Kelly) or equivalent per agent
  - Daily coordination: `Agents/Shared Memory/Daily/YYYY-MM-DD.md`
  - Agent workspaces: `Agents/Hermes/`, `Agents/Blaze/`, `Agents/Signal/`, etc.
- **Local files on this machine**: `~/Documents/Limitless OS/Agents/Qwen/`
  - `Memory/MEMORY.md` — this file
  - `Daily/YYYY-MM-DD.md` — daily operational notes
  - `Protocols/` — workflow documentation
  - `Outputs/` — generated reports and artifacts

## Never store secrets
- API keys, tokens, passwords, session strings, credentials → credential file paths only
