# Agent Infrastructure OS

Updated: 2026-04-26
Owner: Jet + Kelly
Status: Active source of truth

## Decision
All agent infrastructure should be stored in two human-readable layers:

1. **Obsidian = operating source of truth**
   - Local, fast, inspectable, versionable markdown.
   - Stores durable architecture, routing, workflows, memory rules, handoffs, runbooks, and config maps.
   - Never stores raw secrets.

2. **Notion = executive/control-room mirror**
   - High-level index for Jet to review agent infrastructure, status, responsibilities, and links back to Obsidian paths.
   - Good for dashboards, project/task databases, and human review.
   - Never stores raw secrets.

## Folder map

```text
Agents/
├── Hermes/                    # Kelly: ops/general automation
│   ├── Memory/MEMORY.md
│   ├── Daily/
│   ├── Protocols/
│   └── Scratchpad/
├── Blaze/                     # content + creative production
│   ├── Memory/MEMORY.md
│   ├── Content/
│   ├── Daily/
│   ├── Protocols/
│   └── Scratchpad/
├── Signal/                    # AI research/search/intelligence
│   ├── Memory/MEMORY.md
│   ├── Intel/
│   ├── Daily/
│   ├── Protocols/
│   └── Scratchpad/
├── OpenClaw/                  # gateway/config/tool runtime notes
└── Shared Memory/
    ├── Infrastructure/
    │   ├── Agent Infrastructure OS.md
    │   ├── Agent Registry.md
    │   └── Notion Mirror Spec.md
    ├── Daily/
    └── Protocols/
```

## Agent roles

- **Kelly / Hermes** — ops, automation, dashboards, config, monitoring, troubleshooting, cross-agent coordination.
- **Blaze** — content creation, copywriting, carousel/video assets, creative production systems.
- **Signal** — AI research, search, trend intelligence, competitive/market monitoring.
- **OpenClaw** — gateway/runtime layer, local model routing, browser/tool/channel infrastructure.

## Routing rules

- General ops/config/automation → Kelly.
- Dedicated content generation → Blaze.
- Dedicated AI research/search → Signal.
- Tool/runtime/gateway issues → Kelly, with notes under `Agents/OpenClaw/` and `Agents/Shared Memory/Infrastructure/`.

## Secrets policy

- Do **not** put API keys, bot tokens, passwords, session cookies, or connection strings in Obsidian or Notion.
- Store only credential *locations* and ownership notes.
- Represent any secret value as `[REDACTED]` if referenced.
- Credential references currently known:
  - Notion API key file: `~/.config/notion/api_key`
  - OpenRouter API key file: `~/.config/openrouter/api_key`
  - OpenAI API key file: `~/.config/openai/api_key`
  - Blotato API key file: `~/.config/blotato/api_key`

## Sync model

- Obsidian holds detailed operational truth.
- Notion holds the current control-room page/database entry.
- Updates should be summarized in `Agents/Shared Memory/Daily/YYYY-MM-DD.md`.
- Durable facts get promoted to the correct `Memory/MEMORY.md` or shared infrastructure note.

## Immediate next upgrades

- Create a Notion database for agent infrastructure components if Jet wants a full dashboard.
- Add runbooks for: OpenClaw restart/repair, Telegram gateway profiles, Notion sync, content crons, revenue alerts.
- Add a lightweight weekly audit: profile health, crons, credentials present, gateway status, Notion/Obsidian sync status.
