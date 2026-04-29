# Agent Memory Routing

## Memory layers
1. Built-in profile memory: compact durable facts injected into that profile.
2. Agent-local Obsidian memory: human-readable workspace per agent.
3. Shared Obsidian memory: cross-agent handoffs and shared source-of-truth notes.
4. Session search: recall past task progress; do not duplicate temporary progress into durable memory.

## Agent-local folders
- Kelly/Hermes: `Agents/Hermes/`
- Blaze: `Agents/Blaze/`
- Signal: `Agents/Signal/`
- OpenClaw: `Agents/OpenClaw/`

## Decision rule
- Agent-specific durable fact → that agent's `Memory/MEMORY.md` and/or profile memory.
- Cross-agent durable fact → `Agents/Shared Memory/`.
- Today's handoff → `Agents/Shared Memory/Daily/YYYY-MM-DD.md`.
- Repeatable process → relevant `Protocols/` folder.
- Temporary scratch → relevant `Scratchpad/`.

## Safety
Never put raw secrets, tokens, passwords, or private credentials in memory notes. Reference credential file paths instead.
