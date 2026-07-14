# Kelly/Hermes Memory

Durable human-readable memory for Kelly/Hermes. Do not store secrets here.

## Nightly build pattern
- 2026-06-16: Kelly's 02:00 Bangkok nightly cron should leave a tangible local artifact, not only a report. First v0 artifact: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-06-16/nightly-agent-control-room/index.html`, with companion queue note under `Agents/Bolt/Queue/`.
- 2026-06-27: Nightly cron built `Agents/Bolt/Builds/2026-06-27/memory-durability-radar/dashboard.html`, a local HTML dashboard that flags agents with active Daily notes but stale/tiny/missing `Memory/MEMORY.md`; this is now a useful check after memory syncs.

## Morning briefing preference
- 2026-06-19: Jet wants one consolidated 7am morning brief instead of multiple morning alerts. Required order/content: Bible verse first; encouragement about progress since starting in September; Airtable revenue; Meta Ads spend from Comet/Meta Ads UI; **10 high-signal AI lab/news items from xAI/Grok `x_search`, each with actual X reference tweet URL**; Blaze Notion shortform idea link.
- Jet's main Meta Ads account is **CobaltBKK**, visible as `CobaltBKK (10101982961...)`; full account id `act_10101982961107455`; URL: `https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=10101982961107455`. Do not use old account `487565457714892` for main morning ad spend unless CobaltBKK is unavailable.

## Voice and source material
- 2026-06-21: Jet wants Plaud transcripts ingested and used as the tone source for ads/copywriting whenever available.

## Google Workspace ops notes
- 2026-06-21: During the weekly CEO review cron, forced OAuth refresh for the default and personal Gmail Google tokens returned `unauthorized_client`, but the cached `token` values were still valid for Gmail/Calendar API calls. If future Calendar/Gmail cron scans fail after token expiry, re-auth Google Workspace rather than debugging Airtable/revenue scripts.
- 2026-07-06: Jet's main Google Calendar/account is `trinupab@creatuscorp.net`; API access verified with Calendar scope. Jet's calendar color system: Red=client/partner calls, Purple=paid speaking/engagements, Dark Blue=deep work/goals, Green=travel, Light Blue=fitness/meals, Yellow=internal team calls.

## Sunday Content Engine
- 2026-06-28: Sunday Content Engine master Notion page is `38dd076c-9ad3-8191-a8b3-db78788fc8a2`; AI Brain OS project path is `Shared Memory/AI Brain OS/Projects/90-Minute Sunday Batch/`.
- 2026-06-28: Readwise MCP server `readwise` is configured for saved-X/Reader inputs and verified via Hermes MCP test. Credentials are local-only; do not store token values in notes.
- 2026-06-29: Jet's YouTube channel `@jeditrinupab` hit 100K subscribers; public channel page showed `100K subscribers` / `1.3K videos`. Use as durable credibility proof, but use YouTube Studio for exact unrounded analytics.

## Nightly sync build runner — 2026-06-29
- Created reusable local script `~/.hermes/scripts/nightly_agent_memory_sync_build.py` for the 02:00 Bangkok cron pattern: file-only all-agent daily-note sync plus one tangible Bolt build artifact.
- First artifact: `Agents/Bolt/Builds/2026-06-29/agent-sync-dashboard-v0/dashboard.html`; summary JSON: `~/.hermes/agent-memory-sync/2026-06-29-nightly-sync-build-summary.json`.
- Safety rule preserved: local files only; no external messages, deploys, payments, deletes, or cron changes from this job.

## Oracle / Pipeline v3 PM cron — 2026-06-29
- Ran first 15-min tick on empty `_inbox/`; route_inbox_item.json is `[]`. Exited silently per spec ("if inbox is empty, exit silently in <2s") — no classifier/dispatcher run, no Telegram ping.
- Pipeline layout confirmed: `~/Documents/Limitless OS/Pipeline/{_inbox, pm, potential_projects, shipped, research, workers, templates, logs}`. Backlog lives under `potential_projects/_backlog/` and kills under `shipped/_killed/`.
- This cron runs as Pipeline PM (Oracle charter, 15-min cadence). Telegram chat_id for human-checkpoint pings: 1460936021. Use Oracle's voice — concise, Top-3/Done/Needs-attention framing, <1,200 chars.
- Silent-by-default rule reinforced: only ping Jet on first dispatch of a new project, worker failure (BLOCKERS.md), or final ship notification. No routine cron output.

- 2026-06-30: Nightly 02:00 cron built `Bolt/Builds/2026-06-30/memory-hygiene-triage-board-v0/dashboard.html`, a local-only agent durable-memory hygiene triage board. Current board reads `sync-status.json` and flagged 9/12 active agent workspaces for durable-memory review after verifying all daily notes are non-empty.

## Hermes model routing
- 2026-07-01: Kelly/default Hermes profile is configured for Anthropic native `claude-sonnet-5` via existing Anthropic/Claude Code OAuth credentials. Config backup for the switch: `~/.hermes/config.yaml.bak-sonnet5-20260701-084700`.

## 2026-07-04 — Shared Memory Routing Anchor
- Nightly build created/verified `Agents/Shared Memory/MEMORY.md` as the durable cross-agent routing anchor after Qwen flagged it missing.
- Artifact path: `Agents/Bolt/Builds/2026-07-04/shared-memory-routing-anchor/index.html`.
- Safety: local file-only; no external sends, cron edits, deletes, deploys, or secrets.
- 2026-05-16: All active agents should follow the shared always-write memory protocol at `Agents/Shared Memory/Protocols/always-write-memory.md`: daily note after meaningful work, durable facts only in each agent's `Memory/MEMORY.md`, cross-agent handoffs in Shared Memory, no secrets/raw transcripts. Qwen/local `qwen3.6:35b` owns low-cost memory hygiene checks; all-agent memory sync script includes Pixel.

- Qwen Hermes profile fix: local Ollama `qwen3.6:35b` must keep `model.context_length: 131072` in `~/.hermes/profiles/qwen/config.yaml`; Hermes rejects the profile if it falls back to 8192. Qwen no-agent scripts resolve under `~/.hermes/profiles/qwen/scripts/`, not only `~/.hermes/scripts/`.

- 2026-05-17: Jet Brain v0 installed: Shared Memory protocol/evals/templates under `Agents/Shared Memory/`; Hermes skill `jet-brain-retrieval`; GBrain CLI 0.35.1.1 via Bun at `~/.bun/bin/gbrain` from `~/gbrain`. Do not import broad vaults or secrets; sidecar is optional until GBrain health/source boundaries are cleaned.

- Oracle Telegram: bot username `@oraclejedihermesbot`; token lives in `~/.hermes/profiles/oracle/.env`; gateway service `ai.hermes.gateway-oracle`.

- Cua Driver installed for local macOS GUI control: `/Applications/CuaDriver.app`, CLI `~/.local/bin/cua-driver`, Hermes MCP server `cua-driver` in default config. Needs Accessibility permission if not already granted.

- J.E.K. Jack (`jekjack`) is Jet's wife's Telegram-only investment research assistant. Bot username: `@Jek_hermesninngai_bot`; gateway service `ai.hermes.gateway-jekjack`; allowed/home Telegram user ID `7657191200`; inherited crons cleared. Token lives in profile `.env` and must never be printed.

## J.E.K. Jack
- JEK Jack profile `~/.hermes/profiles/jekjack` is configured as wife-only Telegram access (`7657191200`), LINE disabled.
- Jack has all built-in Hermes toolsets enabled plus Higgsfield, Context7, and CUA driver MCP tools. Never expose Telegram bot tokens or secret values.

- 2026-05-21: Limitless Club+ crossed 1,000 members; Skool dashboard screenshot showed 1,005 members and 28% engagement.

- 2026-05-23: Main Hermes Discord `#kelly-command` channel ID `1506557603579166830` is configured as `discord.free_response_channels` so Jet can message there without tagging Friday/Kelly; other Discord channels still require mention.

- Skill available: `karpathy-agentic-engineering` (`~/.hermes/skills/software-development/karpathy-agentic-engineering/SKILL.md`) turns Karpathy's Software 3.0 / agentic engineering talk into Jet's reusable build workflow; source transcript is at `/Users/ultrafriday/clawd/youtube-transcripts/karpathy-agentic-engineering-96jN2OCOfLs/transcript.md`.

## Hermes Ops
- Cron health digest script: `~/.hermes/scripts/hermes_cron_health_digest.py`; reports: `Agents/Shared Memory/Ops/Cron Health/`; default cron: `hermes-cron-health-digest` daily 08:10 Bangkok, origin delivery.

## Nightly workflow artifact pattern
- 2026-07-09: Kelly's 2:00 AM cron built a local `Nightly Workflow Radar` dashboard under `Agents/Bolt/Builds/YYYY-MM-DD/notion-sync-triage-dashboard/` and a Bolt queue note. Use this pattern for future nightly runs: sync agent daily notes, choose one blocker, build a local artifact, verify, then report concisely.
- 2026-07-14: Nightly cron built `Agents/Bolt/Builds/2026-07-14/nightly-agent-sync-dashboard/index.html`, a local HTML control-room page summarizing active profile daily-note sync status from `hermes profile list`; companion Bolt queue note lives under `Agents/Bolt/Queue/2026-07-14 - Nightly Workflow Build - nightly-agent-sync-dashboard.md`.

- Limitless Club AI Content Production System project path: `Shared Memory/AI Brain OS/Projects/Limitless Club AI Content Production System/`; operationalizes `agents.pdf` into Long-form Director, Short-form Agent, and Clipping Agent workflows.

- Content positioning: Jet wants to talk only about what he has actually done; avoid generic/niche trend claims unless tied to his real workflows, agents, student cases, numbers, or implemented systems.

- Current planning target: ฿1.5M/month revenue, framed as freedom-aligned rather than maximizing delivery load; avoid defaulting to older ฿2M/month assumption.

## Jedi Personal Brand Strategy — active alignment
- Canonical brand mission: empower builders to create without limits using AI as leverage so they win at business without losing family, faith, or soul.
- Master filter for writing/building: does this move the reader/customer from trapped/body-bound/calendar-owned to free/limitless? If not, kill or reframe.
- Content mix: AI-First Business 50%, Life Design & Leverage 30%, Leadership & Fatherhood 20%. Proof-led only: built/tested/done/taught/broken/measured/lived/student-client cases.
- Sources: processed `{processed}`; project guide `{project}`.
