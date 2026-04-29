# Hermes Operating System

This is the simplest way to work with Hermes inside the shared Obsidian vault.

## Where things go
- **Hermes local work** -> `Hermes/`
- **Stable shared context across agents** -> [[../OpenClaw/memory|OpenClaw/memory]]
- **Cross-agent day log** -> [[../Shared Memory/Daily/2026-04-21|Shared Memory/Daily/2026-04-21]]
- **Hermes day log** -> [[Daily/2026-04-21|Hermes Daily/2026-04-21]]

## Default workflow
1. Read shared context in [[../OpenClaw/memory|OpenClaw Memory]] if the task depends on previous work.
2. Use `Hermes/Scratchpad/` for quick rough notes.
3. Save Hermes-only working notes in `Hermes/Daily/`.
4. Save reusable methods in `Hermes/Protocols/`.
5. If another agent should know something, add a compact note to `Shared Memory/Daily/`.
6. If the information is durable and cross-agent, add it to [[../OpenClaw/memory|OpenClaw Memory]].

## Decision rule
- **Temporary** -> Scratchpad
- **Today only** -> Daily
- **Repeatable** -> Protocols
- **Shared durable context** -> OpenClaw Memory
- **Shared daily coordination** -> Shared Memory Daily
