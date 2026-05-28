# Session Memory Workflow

Use this workflow whenever Kelly 2 or another agent finishes a meaningful work session with Jet.

## At session end or after meaningful progress

1. Write a short entry to the agent daily note:
   - `Agents/<Agent>/Daily/YYYY-MM-DD.md`
2. If the work affects other agents, add a handoff to:
   - `Agents/Shared Memory/Daily/YYYY-MM-DD.md`
3. If the session has durable value, create a session note:
   - `Agents/<Agent>/Sessions/YYYY-MM-DD - <topic>.md`
4. Promote only stable, reusable facts into:
   - `Agents/<Agent>/Memory/MEMORY.md`
   - or shared memory/protocol notes when relevant.

## What counts as durable

- Stable preferences from Jet
- Agent roles and routing rules
- Tool setup paths and verified integrations
- Repeatable workflows
- Decisions that future agents must respect

## What should stay out of durable memory

- One-off task progress
- Stale status updates
- PR numbers, issue numbers, commit SHAs
- Temporary file counts
- Raw logs
- Secrets

## Session note template

```markdown
# YYYY-MM-DD - Topic

## Context

## What changed

## Files / paths

## Decisions

## Handoff for other agents

## Follow-ups
```
