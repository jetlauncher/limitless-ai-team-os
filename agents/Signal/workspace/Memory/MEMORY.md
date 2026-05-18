# Signal — Durable Memory

Use this file for durable, agent-specific memory that should remain useful across sessions.

## Stable identity
- Agent: Signal
- Role: Dedicated AI research/search agent: high-signal AI/business updates, source-grounded research, and founder/operator implications.
- Profile: Hermes profile ~/.hermes/profiles/signal, Telegram @signalhermesaibot

## Memory rules
- Store only stable facts, preferences, conventions, source-of-truth paths, and reusable context.
- Do not store secrets, raw API keys, passwords, or temporary task progress.
- Put temporary context in `Daily/` or `Scratchpad/`, not here.
- Promote repeated workflows into `Protocols/`.

## Durable notes
- Created/verified on 2026-04-26.
- Signal intel for Jet’s X/content engine should prioritize AI shifts that can become founder/operator implications in Jet’s YouTube-aligned voice: calm, practical, educational, premium, and relevant to Thai/SEA businesses.
- 2026-05-03: Jet designated Notion database `Work Output by Friday team` as the place to store Signal’s substantive work outputs, research notes, and deliverables when appropriate. URL: https://www.notion.so/3581290f50f44b7dbc8b93879ca31916. Database ID: `3581290f-50f4-4b7d-bc8b-93879ca31916`. Schema verified: `Name` title, `Agent` select, `Status` select, `Type` select, `Skool Category` select, `Date Created` created_time.
- 2026-05-03: Created cron job `28f1f5d64725` (`Signal daily Notion work wrap`) to create/update one Notion page titled `Signal Daily Wrap — YYYY-MM-DD` in the same database every day at 23:55 +07. Delivery is local to avoid noisy Telegram alerts; Notion remains the source-of-truth output.
- 2026-05-10: Signal substantive reports/briefs should use Signal Reports Database as the canonical report target when appropriate. Database ID: `353d076c-9ad3-81cd-aff3-e054bd10e43b`. Local backfill/indexing script referenced by current reports: `/Users/ultrafriday/.hermes/profiles/signal/scripts/signal_reports_db_backfill.py`.
- 2026-05-11: Current automation preference is Signal ≤4 user-facing updates/day; memory-sync and handoff work should remain file-only unless Jet explicitly authorizes external delivery.
- 2026-05-16: `xurl` official X API CLI is configured for Signal's X bookmark workflow via the `jet-x` OAuth app for `@jeditrinupab`; daily bookmark research successfully used `xurl bookmarks -n 50`. Continue to follow secret-safety rules: never read or expose `~/.xurl`, tokens, or OAuth credential files.
- 2026-05-17 X scan: xAI official post `2055745332919808181` says X Premium subscriptions work in Hermes Agent and Hermes can search X posts; treat as duplicate of May 16 Grok/Hermes subscription-as-auth unless new implementation docs or reliability tests appear.


## AI Signals Notion database
- Source of truth for future AI Signal entries: Notion database `AI Signals` — `363d076c-9ad3-8099-bbd9-e9f1d3cd23cf` / https://www.notion.so/363d076c9ad38099bbd9e9f1d3cd23cf
- Schema: `Name` title; `Date` date; `Top Theme` select (`OpenAI`, `Anthropic`, `Google / DeepMind`, `Meta`, `AI Agents`, `SMB AI Tools`, `Industry / Other`); `Content Bet` rich_text; `Status` select (`🆕 New`, `👀 Reviewed`, `✅ Content Made`, `🗄 Archived`); `Items` number.
- Existing template style: quote intro; numbered H2 items; paragraph summary; bullets for `Why you care`, `Teach/try`/`Apply now`, `Sources`; divider; final `🎯 This week's content bet`.
## 2026-05-19 - Anthropic acquires Stainless signal
- X high-alert scan selected Anthropic acquiring Stainless as high-signal: SDK, CLI, and MCP-server generation is moving into Claude Platform as core agent-connectivity infrastructure.
- Official source: https://www.anthropic.com/news/anthropic-acquires-stainless; X source: https://x.com/AnthropicAI/status/2056419620643541012.
- Dedupe guidance: repeat only if Anthropic adds concrete Stainless product integration details, connector marketplace changes, MCP governance/security controls, pricing/availability, or migration requirements.

