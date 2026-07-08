# Self-Improving Agent Loop — Limitless AI Brain OS

All Limitless OS agents should use this loop whenever they receive durable knowledge, complete non-trivial work, ingest a source, learn a reusable workflow, or get corrected by Jet.

## Core loop

```text
Capture → Archive → Extract → Promote → Link → Review → Reuse
```

## When to run it

Run the loop for:

- YouTube/podcast links, Plaud transcripts, voice memos, Apple Notes, articles, or external references.
- Jet corrections, stable preferences, identity/context updates, new frameworks, and repeated workflows.
- Non-trivial builds, dashboards, automations, research sweeps, content packages, and deployment work.
- Anything another agent would need to know next week.

Do not run it for:

- trivial chat replies
- temporary task progress
- raw secrets/tokens/passwords/session cookies
- one-off facts that will be stale within a week

## Required write targets

1. **Raw/source material** → `~/Documents/Limitless OS/Agents/Shared Memory/Sources/`
2. **Processed extraction** → source-specific `Summaries/` or `Processed/`
3. **Agent-local durable context** → `~/Documents/Limitless OS/Agents/<Agent>/Memory/MEMORY.md`
4. **Agent-local work log** → `~/Documents/Limitless OS/Agents/<Agent>/Daily/YYYY-MM-DD.md`
5. **Cross-agent handoff** → `~/Documents/Limitless OS/Agents/Shared Memory/Daily/YYYY-MM-DD.md`
6. **Concept/MOC links** → `~/Documents/Limitless OS/Agents/Shared Memory/AI Brain OS/Concepts/` or relevant `Shared Memory` project files
7. **Uncertain/sensitive changes** → Review Queue, not durable memory

## Promotion rules

Promote only durable knowledge:

- stable Jet preferences and corrections
- project conventions
- reusable procedures and lessons
- important people/projects/companies/frameworks
- source-backed strategic insights

Keep out of durable memory:

- secrets, tokens, credentials, private session data
- raw transcripts or long dumps
- temporary TODO state and ephemeral task progress
- unverified claims unless clearly marked `Needs review`

## Review gates

Human approval is required before deleting/renaming source material, posting publicly, emailing/messaging externally, making purchases, changing credentials, changing billing, or promoting sensitive strategic claims as settled truth.

## Canonical package

The operating package lives at:

`~/Documents/Limitless OS/Agents/Shared Memory/AI Brain OS/`

Start with `README.md`, then use the templates, prompts, protocols, and concepts there.
