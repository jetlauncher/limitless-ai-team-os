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
- Codex: `Agents/Codex/`
- Cowork: `Agents/Cowork/`

## Decision rule
- Agent-specific durable fact → that agent's `Memory/MEMORY.md` and/or profile memory.
- Cross-agent durable fact → `Agents/Shared Memory/`.
- Today's handoff → `Agents/Shared Memory/Daily/YYYY-MM-DD.md`.
- Repeatable process → relevant `Protocols/` folder.
- Temporary scratch → relevant `Scratchpad/`.

## Safety
Never put raw secrets, tokens, passwords, or private credentials in memory notes. Reference credential file paths instead.

## Jet directive — 2026-05-27
Jet explicitly asked Kelly 2 to use Obsidian to create and update memory and session records between Jet and all current/future agents so the system does not forget meaningful work.

Operational rules:
- Obsidian is the detailed, inspectable source of truth for agent memory, session summaries, handoffs, protocols, and infrastructure decisions.
- Built-in Hermes memory is only a compact index for stable facts and where to look.
- Meaningful Kelly 2 sessions should create/update `Agents/Hermes/Sessions/` or `Agents/Hermes/Daily/`.
- Cross-agent work should create/update `Agents/Shared Memory/Daily/` and, when durable, the relevant shared protocol note.
- Other agents should follow the same pattern in their own `Agents/<Agent>/` folder.
