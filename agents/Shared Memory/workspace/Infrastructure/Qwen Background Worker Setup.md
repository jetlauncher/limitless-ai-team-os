# Qwen Background Worker Setup — 2026-05-11

Qwen is now configured as the local, cheap processing layer.

## Current routing
- Qwen: local high-volume work — memory sync, Obsidian cleanup, summarization, research clustering, first-pass drafts, log/QA notes.
- Kelly: final judgment, reporting, approvals, user-facing coordination.
- Claude Code/Bolt: serious coding and builds.
- Blaze/Kaijeaw: final content voice.
- Signal: external AI research judgment.

## Safety
Qwen jobs should default to local file output. Telegram delivery is reserved for explicit approval or Kelly summaries.

## Subscription experiment
Run this for 7 days, then audit whether Qwen absorbed enough summarization/research/cleanup work to reduce paid model usage or downgrade redundant subscriptions.
