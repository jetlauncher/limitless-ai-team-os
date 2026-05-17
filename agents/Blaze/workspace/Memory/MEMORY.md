# Blaze — Durable Memory

Use this file for durable, agent-specific memory that should remain useful across sessions.

## Stable identity
- Agent: Blaze
- Role: Dedicated content creation engine for Limitless Club: hooks, posts, scripts, carousels, launch/ad copy, and recurring content packages.
- Profile: Hermes profile ~/.hermes/profiles/blaze, Telegram @blazehermesaibot

## Memory rules
- Store only stable facts, preferences, conventions, source-of-truth paths, and reusable context.
- Do not store secrets, raw API keys, passwords, or temporary task progress.
- Put temporary context in `Daily/` or `Scratchpad/`, not here.
- Promote repeated workflows into `Protocols/`.

## Durable notes
- Created/verified on 2026-04-26.
- Jet’s X growth strategy should borrow high-engagement mechanics from creators like Bindu Reddy (speed, strong predictions, timely AI comparisons), but remain aligned with Jet’s YouTube voice: clear teacher, founder/operator, practical AI translator, premium Thai/SEA business educator. Avoid chaotic model-war, political bait, or generic AI hype.
- Canonical Jet voice/persona layer for Blaze drafting lives at `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Blaze/Memory/JET_VOICE_DNA.md`; review it before writing Jet/Limitless content.
- Latest mirrored @jeditrinupab Thai/AI YouTube transcript library for Blaze lives at `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Blaze/YouTube Transcripts/` and can be used as source material for content queues.
- Blaze profile default model routing is OpenAI Codex / `gpt-5.5` in `/Users/ultrafriday/.hermes/profiles/blaze/config.yaml`; Anthropic/Claude should not be the default for this agent.
- Limitless content approval queue path is `/Users/ultrafriday/.hermes/limitless/content_approval_queue.json`; Blaze may draft/update queue items, but should not post or submit externally without explicit instruction.
- Recurring daily content engine convention: archive full deliverables under Blaze `Daily/` and, when available, Notion database `Work Output by Friday team` with Type = Content, Status = Done, Agent = blaze/System; keep Telegram/user-facing delivery concise and link back to the archive.
- Current automation preference: Blaze should stay at or below 10 scheduled publishable pieces per day unless Jet explicitly changes the limit.
- Mandatory memory-writing policy (shared): log session/task outcomes to `Daily/`, keep this `Memory/MEMORY.md` for durable facts only, and post cross-agent handoffs to `Agents/Shared Memory/Daily/<date>.md`. Shared protocol: `Agents/Shared Memory/Protocols/always-write-memory.md`.
