# Agent Memory

Agent Memory is the durable context an agent uses to avoid asking the human the same questions repeatedly.

## Layers

1. Built-in Hermes memory — compact durable facts injected into future sessions.
2. Human-readable markdown memory — inspectable `Memory/MEMORY.md` per agent.
3. Daily notes — temporary operational context and handoffs.
4. Source archive — raw and processed inputs that should not be compressed too aggressively.
5. Concepts/MOCs — index layer that connects related notes.

## Good memory

- Stable preferences.
- Long-lived project conventions.
- Environment facts.
- Reusable lessons.

## Bad memory

- Temporary task progress.
- Raw transcripts.
- Secrets.
- Stale one-week facts.
- Unverified claims.
