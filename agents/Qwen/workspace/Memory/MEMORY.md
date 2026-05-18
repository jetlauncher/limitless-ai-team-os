---
created: 2025-04-12
updated: 2026-05-18
agent: qwen
---

# Qwen — Durable Memory

## Todoist integration
- **Status:** NOT CONFIGURED — no API token at `~/.config/todoist/api_key`.
- Tasks are fetched by label: `qwen`, `ai`, `agent`, `delegate` OR prefix: `Qwen:`, `AI:`, `Agent:`.
- Setup note lives at `Outputs/todoist-setup-needed.md`.

## Workspace paths
- Local workspace: `~/Documents/Obsidian Vault/Agents/Qwen/`
- Daily notes: `Agents/Qwen/Daily/YYYY-MM-DD.md`
- Outputs: `Agents/Qwen/Outputs/`
- Queue (legacy/manual): `Agents/Qwen/Queue/`
- Protocols: `Agents/Qwen/Protocols/`
- Durable memory: `Agents/Qwen/Memory/MEMORY.md`
- Shared memory: `Agents/Shared Memory/Daily/YYYY-MM-DD.md`

## Safety boundaries
- No publishing, external messaging, deploying, or spending without explicit approval.
- No printing/logging secrets (API keys, tokens, passwords).

## X-Radar
- Runs via local Comet browser + Ollama qwen3.6:35b. No X API credits.
- Reports written to `Agents/Qwen/Outputs/X-Radar/`.
- Protocol: `Agents/Qwen/Protocols/x-radar-comet-qwen-workflow.md`.
