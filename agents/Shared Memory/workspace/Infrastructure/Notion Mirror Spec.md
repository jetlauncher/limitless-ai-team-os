# Notion Mirror Spec

Updated: 2026-04-26

## Purpose
Notion should mirror the agent infrastructure at an executive/dashboard level, while Obsidian remains the operating source of truth.

## Recommended Notion structure

### Page
**Agent Infrastructure OS**

Sections:
- Current status
- Agent registry
- Active infrastructure components
- Runbooks
- Credentials map with paths only, no secrets
- Recent changes
- Open issues

### Optional database: Agent Infrastructure Components

Suggested fields:
- Name — title
- Type — select: Agent, Gateway, Cron, Credential Reference, Runbook, Dashboard, Integration
- Owner — select: Kelly, Blaze, Signal, OpenClaw, Jet
- Status — select/status: Active, Paused, Needs Review, Broken, Deprecated
- Obsidian Path — rich text or URL
- Notion URL — URL
- Last Verified — date
- Notes — rich text

## Sync rule

- Detailed edits happen in Obsidian first.
- Kelly mirrors high-level status into Notion.
- Any Notion-only decision should be copied back into Obsidian before it becomes operational truth.
