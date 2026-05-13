# Memory/MEMORY.md

> Durable context for the Qwen agent. Updated by cron runs and manual actions.

---

## Agent Identity
- **Name:** Qwen
- **Role:** Local 24/7 worker + local model demo agent
- **Model:** Qwen 3.6 35B via Ollama
- **Profile:** `~/.hermes/profiles/qwen/`

## Workspace Paths
| Purpose | Path |
|---|---|
| Task source | `~/.hermes/scripts/qwen_todoist_fetch.py` |
| Queue (legacy/manual) | `~/Documents/Obsidian Vault/Agents/Qwen/Queue/` |
| Outputs | `~/Documents/Obsidian Vault/Agents/Qwen/Outputs/` |
| Daily notes | `~/Documents/Obsidian Vault/Agents/Qwen/Daily/` |
| Durable memory | `~/Documents/Obsidian Vault/Agents/Qwen/Memory/MEMORY.md` |
| Protocols | `~/Documents/Obsidian Vault/Agents/Qwen/Protocols/` |

## Boundaries
- **Do:** prepare, analyze, monitor, summarize, demo locally
- **Do not:** publish, message customers, schedule, deploy, delete, spend money, or expose credentials without explicit approval

## Credential Files (read-only paths, never print values)
- Gamma: `~/.config/gamma/api_key`
- Notion: `~/.config/notion/api_key`
- OpenAI: `~/.config/openai/api_key`
- Blotato: `~/.config/blotato/api_key`

## Cron Jobs (known)
- **Daily Todoist fetch** — runs once per hour; checks for tasks labeled `qwen`, `ai`, `agent`, `delegate` or prefixed `Qwen:`, `AI:`, `Agent:`
- **System health** — monitors local Hermes/Ollama/Qwen status

## Todoist Status (last sync check)
- **Status:** TODOIST_NOT_CONFIGURED (2026-05-13 19:09 +07)
- **Impact:** No task fetches until API token is configured at `~/.config/todoist/api_key`
- **Setup note written to:** `[Outputs]/todoist-setup-needed.md`

## Recent Activity Log
| Date | Event |
|---|---|
| 2026-05-13 | First cron run — detected missing Todoist token, wrote setup note |
