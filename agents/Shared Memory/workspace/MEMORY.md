# Shared Memory — Durable Routing Anchor

Created/verified by Kelly nightly build on 2026-07-04 at 02:02 Bangkok.

## Purpose
This is the stable cross-agent memory anchor for the Limitless OS agent workspace. It complements daily notes by holding durable routing rules, ownership conventions, and long-lived safety policies.

## Canonical workspace
- Active workspace: `/Users/ultrafriday/Documents/Limitless OS/Agents/`
- Frozen legacy mirror: `/Users/ultrafriday/Documents/Obsidian Vault/Agents/` — do not treat as current.

## Routing rules
- Kelly/Hermes: ops, orchestration, dashboards, configuration, revenue/system monitoring, and cross-agent coordination.
- Blaze: content, creative packaging, visual direction, and public-facing asset polish.
- Signal: AI research/search and source-backed research sweeps.
- Bolt: local builds, scripts, dashboards, prototypes, and implementation notes.
- Qwen: local worker for summaries, hygiene, private/local file processing, and low-risk prep; mark uncertain conclusions `Needs Kelly review`.
- Oracle: local-first idea surfacing from the knowledge network.
- Other specialist agents: keep role-specific durable notes in their own `Memory/MEMORY.md` and daily handoffs in Shared Memory daily notes.

## Where notes go
- Temporary scratch: `Agents/<Agent>/Scratchpad/`
- Today-only status: `Agents/<Agent>/Daily/YYYY-MM-DD.md`
- Durable agent-specific memory: `Agents/<Agent>/Memory/MEMORY.md`
- Cross-agent handoffs: `Agents/Shared Memory/Daily/YYYY-MM-DD.md`
- Reusable protocols: `Agents/Shared Memory/Protocols/`

## Safety policy
Never store raw API keys, bot tokens, passwords, private sessions, or connection strings here. Reference credential file paths only when operationally necessary.

## Review cadence
Kelly should review this file when routing rules change, when a new active profile is added, or when daily sync notes repeatedly mention the same blocker.
