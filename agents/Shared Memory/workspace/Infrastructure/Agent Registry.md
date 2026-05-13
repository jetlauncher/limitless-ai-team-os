# Agent Registry

Updated: 2026-05-12

| Agent | Profile / Surface | Primary responsibility | Obsidian workspace | Durable memory | Notes |
|---|---|---|---|---|---|
| Kelly | default Hermes / Telegram DM | Ops, automation, dashboards, config, troubleshooting | `Agents/Hermes/` | `Agents/Hermes/Memory/MEMORY.md` | Primary coordinator |
| Blaze | `blaze` / `@blazehermesaibot` | Content creation and creative production | `Agents/Blaze/` | `Agents/Blaze/Memory/MEMORY.md` | Owns content crons and assets |
| Signal | `signal` / `@signalhermesaibot` | AI research, search, trends, intelligence | `Agents/Signal/` | `Agents/Signal/Memory/MEMORY.md` | Feeds research into Blaze/Kelly |
| OpenClaw | local gateway/runtime | Tool runtime, model routing, channels, browser/gateway layer | `Agents/OpenClaw/` | `Agents/OpenClaw/memory.md` | Runtime infrastructure notes only |
| Codex | ChatGPT Codex desktop/local coding agent | Code, files, repo work, deployments, workspace operations, session logs | `Agents/Codex/` | `Agents/Codex/memory.md` | Bridges local Codex work into Shared Memory |

## Operating principle

Each agent gets:
- A profile-specific built-in memory layer.
- A human-readable Obsidian workspace.
- A shared memory path for cross-agent handoffs.
- No raw secrets in notes.
