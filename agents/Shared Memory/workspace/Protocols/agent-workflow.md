# Agent Workflow

Use this rule set to keep the Obsidian system simple.

## Memory layers
- `Agents/Hermes/` = Hermes local workspace
- `Agents/OpenClaw/memory.md` = stable shared context across agents
- `Agents/Shared Memory/Daily/YYYY-MM-DD.md` = daily cross-agent coordination
- `Agents/Codex/` = ChatGPT Codex local workspace and session memory
- `Agents/Cowork/` = Claude Cowork desktop workspace and session memory

## What belongs where
### OpenClaw Memory
Put:
- durable preferences
- stable operating rules
- business context likely to matter again
- shared conventions between agents

### Shared Memory Daily
Put:
- what changed today
- handoffs
- decisions another agent may need today or soon
- active blockers and next actions

### Agent-local folders
Put:
- rough work
- drafts
- agent-specific protocols
- notes not yet ready for shared memory

## Principle
Write once in the smallest useful place. Promote upward only when the information becomes shared or durable.
