# Kelly/Hermes Memory

Durable human-readable memory for Kelly/Hermes. Do not store secrets here.

## System founding date
- **21 April 2026** is the defensible founding/setup date of Jet’s Hermes/Limitless AI system. Live filesystem evidence: Hermes installed at 19:07 +07, persona at 19:13, state database at 19:16, and first preserved Telegram session at 19:17:57. Jet renamed Hermes to Kelly in that first session; core revenue reporting, Telegram, shared-memory, monitoring, and automation foundations were already operating that evening.
- The first original `Limitless Superhero Universe` concept batch was generated on 2026-08-16 and remains unratified pending Jet’s character selections. Canonical source folder: `~/Pictures/Hermes/limitless-superhero-team/20260816-first-universe/`; Team B/Midnight Ops is the art-director recommendation for current-team canon and Team D/Thai Future for public-facing cover art.
- The 2026-08-16 `Limitless Lightguard` iteration adds five original giant-of-light/tokusatsu directions. `Pure Giants of Light` is the recommended aesthetic, while `Full Suit Roster` is the exact 15-member design reference. These remain unratified pending Jet’s selection.

## Nightly build pattern
- 2026-06-16: Kelly's 02:00 Bangkok nightly cron should leave a tangible local artifact, not only a report. First v0 artifact: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-06-16/nightly-agent-control-room/index.html`, with companion queue note under `Agents/Bolt/Queue/`.
- 2026-06-27: Nightly cron built `Agents/Bolt/Builds/2026-06-27/memory-durability-radar/dashboard.html`, a local HTML dashboard that flags agents with active Daily notes but stale/tiny/missing `Memory/MEMORY.md`; this is now a useful check after memory syncs.

## Morning briefing preference
- 2026-06-19: Jet wants one consolidated 7am morning brief instead of multiple morning alerts. Required order/content: Bible verse first; encouragement about progress since starting in September; Airtable revenue; Meta Ads spend from Comet/Meta Ads UI; **10 high-signal AI lab/news items from xAI/Grok `x_search`, each with actual X reference tweet URL**; Blaze Notion shortform idea link.
- Jet's main Meta Ads account is **CobaltBKK**, visible as `CobaltBKK (10101982961...)`; full account id `act_10101982961107455`; URL: `https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=10101982961107455`. Do not use old account `487565457714892` for main morning ad spend unless CobaltBKK is unavailable.
- 2026-08-18: Claude Desktop has Meta's official Ads MCP (`https://mcp.facebook.com/ads`) connected, but Hermes does not. Meta rejects Hermes dynamic OAuth client registration; direct Hermes access requires a pre-registered Meta app client ID or a locally stored user access token. Prefer read-only tools/scopes for reporting and require explicit approval for writes.

## Voice and source material
- 2026-06-21: Jet wants Plaud transcripts ingested and used as the tone source for ads/copywriting whenever available.

## Google Workspace ops notes
- 2026-06-21: During the weekly CEO review cron, forced OAuth refresh for the default and personal Gmail Google tokens returned `unauthorized_client`, but the cached `token` values were still valid for Gmail/Calendar API calls. If future Calendar/Gmail cron scans fail after token expiry, re-auth Google Workspace rather than debugging Airtable/revenue scripts.
- 2026-07-06: Jet's main Google Calendar/account is `trinupab@creatuscorp.net`; API access verified with Calendar scope. Jet's calendar color system: Red=client/partner calls, Purple=paid speaking/engagements, Dark Blue=deep work/goals, Green=travel, Light Blue=fitness/meals, Yellow=internal team calls.
- 2026-08-15: Evening Shutdown cron may list `google-workspace` as unavailable. Direct Calendar API fallback works for `trinupab@creatuscorp.net` through the default `~/.hermes/google_token.json` calendar-scoped token; the `~/.hermes/google-accounts/jeditrinupab-gmail/google_token.json` token currently lacks Calendar scope and returns 403. Do not print token contents.

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
- Hostinger VPS runs **Atlas — Limitless Cloud Operator** on Hermes v0.20.5/Debian 13 with `openai/gpt-5.6-sol` through dedicated Nous Portal auth. Private endpoint: `hermes@100.66.96.99` / `hermes-unit.tail3b403f.ts.net`; Tailscale SSH only, no sshd/root/TUN. Model and terminal smoke tests passed. Telegram bot `@LimitlessAtlasBot` is verified with Jet-only allowlist. Hermes 8642 is loopback-only; dashboard 9119 is off; zero crons. Private A2A and sanitized repo connection remain required. Canonical work charter: `Agents/Shared Memory/AI Brain OS/Projects/Hostinger Hermes VPS/Atlas Operating Charter.md`.
- Kelly/default and Signal Telegram gateways are protected by independent launchd watchdog `ai.hermes.gateway-watchdog` (`~/.hermes/scripts/hermes_gateway_watchdog.sh`), running every 30 seconds. It re-bootstraps unloaded services, kickstarts stopped services, and restarts after four consecutive Telegram adapter-health misses; disable only via `~/.hermes/disable-gateway-watchdog`.
- Mac Studio can SSH over Tailscale into Jet's `jedim5max` MacBook at `100.69.255.80` as OS user `jedijiratritarnm5max`; the Studio's existing `~/.ssh/id_ed25519` key is authorized there.
- Public student SOP for Mac-to-Mac remote access via Tailscale + macOS Remote Login: https://fate-revolve-020.notion.site/Remote-Access-Between-Two-Macs-with-Tailscale-SSH-Beginner-Guide-3aed076c9ad3810791d7e2a8542bc9bc (local source: `Agents/Hermes/Outputs/2026-07-31-tailscale-ssh-student-guide.md`).

## Nightly workflow artifact pattern
- 2026-07-09: Kelly's 2:00 AM cron built a local `Nightly Workflow Radar` dashboard under `Agents/Bolt/Builds/YYYY-MM-DD/notion-sync-triage-dashboard/` and a Bolt queue note. Use this pattern for future nightly runs: sync agent daily notes, choose one blocker, build a local artifact, verify, then report concisely.
- 2026-07-14: Nightly cron built `Agents/Bolt/Builds/2026-07-14/nightly-agent-sync-dashboard/index.html`, a local HTML control-room page summarizing active profile daily-note sync status from `hermes profile list`; companion Bolt queue note lives under `Agents/Bolt/Queue/2026-07-14 - Nightly Workflow Build - nightly-agent-sync-dashboard.md`.
- 2026-07-16: Nightly cron built `Agents/Bolt/Builds/2026-07-16/nightly-agent-ops-board/index.html`, a local static HTML cockpit summarizing all synced agent daily notes plus blocker lines from recent Obsidian context; companion queue note: `Agents/Bolt/Queue/2026-07-16 - Nightly Workflow Build - nightly-agent-ops-board.md`.
- 2026-07-29: Nightly cron built `Agents/Bolt/Builds/2026-07-29/agent-write-access-safety-gate/index.html`, a printable student/founder checklist for granting AI agents write access; source context was Signal's Opus 5 / METR eval-gaming / Anthropic misalignment risk scan.

- Limitless Club AI Content Production System project path: `Shared Memory/AI Brain OS/Projects/Limitless Club AI Content Production System/`; operationalizes `agents.pdf` into Long-form Director, Short-form Agent, and Clipping Agent workflows.

- Content positioning: Jet wants to talk only about what he has actually done; avoid generic/niche trend claims unless tied to his real workflows, agents, student cases, numbers, or implemented systems.

- Current planning target: ฿1.5M/month revenue, framed as freedom-aligned rather than maximizing delivery load; avoid defaulting to older ฿2M/month assumption.

## Jedi Personal Brand Strategy — active alignment
- Canonical brand mission: empower builders to create without limits using AI as leverage so they win at business without losing family, faith, or soul.
- Master filter for writing/building: does this move the reader/customer from trapped/body-bound/calendar-owned to free/limitless? If not, kill or reframe.
- Content mix: AI-First Business 50%, Life Design & Leverage 30%, Leadership & Fatherhood 20%. Proof-led only: built/tested/done/taught/broken/measured/lived/student-client cases.
- Canonical Jet IP library: `/Users/ultrafriday/Library/Mobile Documents/com~apple~CloudDocs/AI OS/_IP-Index/`. For Jet-derived content, curriculum, offers, or proposals, search it before generic web research; use exact public-safe quotes/proof and exclude sensitive/third-party/client material unless Jet approves the source.
- Jet IP architecture review: processed source `Agents/Shared Memory/Sources/Brain Dumps/Processed/2026-08-11 - Jet IP Index Deep Review.md`; promoted concept `Agents/Shared Memory/AI Brain OS/Concepts/Jet IP Architecture.md`. Golden Triangle is canonical; KOI is a retired alias.
- 2026-07-30: Nightly cron built `Agents/Bolt/Builds/2026-07-30/weekly-focus-picker/` to address recurring fleet blocker: agents need one weekly priority before producing daily outputs.
- 2026-07-31: Nightly cron built `Agents/Bolt/Builds/2026-07-31/agent-handoff-command-center/index.html`, a local morning dashboard summarizing all present profile daily sync cards, recent workflow signals, and a review checklist; companion queue note lives under `Agents/Bolt/Queue/2026-07-31 - Nightly Workflow Build - agent-handoff-command-center.md`.

- 2026-08-02: Nightly cron built `Agents/Bolt/Builds/2026-08-02/agent-memory-sync-console/`, a local Agent Memory Sync Console v0 that summarizes file-only Obsidian sync coverage, gateway status, and latest local signal per Hermes profile.
- 2026-08-03: Nightly cron built `Agents/Bolt/Builds/2026-08-03/memory-freshness-triage-board/`, a local file-only triage dashboard/generator for agent daily-note coverage, gateway state, and `Memory/MEMORY.md` freshness; companion queue note: `Agents/Bolt/Queue/2026-08-03 - Nightly Workflow Build - memory-freshness-triage-board.md`.
- 2026-08-04: Nightly cron built `Agents/Bolt/Builds/2026-08-04/daily-command-card/`, a local one-screen Daily Command Card that consolidates Kelly email attention, shared calendar/revenue context, Qwen AI radar, ops blockers, and all-agent sync verification; companion queue note: `Agents/Bolt/Queue/2026-08-04 - Nightly Workflow Build - daily-command-card.md`.

## Apple Notes access
- 2026-08-03: Kelly/default has the `apple-notes` skill installed at `~/.hermes/skills/apple/apple-notes/`; `/opt/homebrew/bin/memo` has verified read access to Notes.app. Keep note contents private and remove temporary exports after use.

## Kelly phone voice agent
- 2026-08-03: Production route is Twilio/ElevenLabs → authenticated Tailscale Funnel `/fast-llm/v1` → fast streaming conversation or detached Hermes `phone-voice-task` → Telegram result. Project/runbook: `~/Projects/elevenlabs-fast-llm/`. Historical failure signature was ElevenLabs `custom_llm generation failed` from running full Hermes work synchronously; the hybrid acknowledgement + async worker route is verified through API, ElevenLabs simulation, Hermes exit 0, and Telegram delivery. A real phone call remains the final acceptance gate.

## Todoist and desktop-work routing
- Todoist API access is configured via `~/.config/todoist/api_key`; Qwen's `qwen-todoist-worker` polls every 2h and is intentionally read-only. The existing `delegate` label is an intake trigger; specialist labels are not yet configured.
- Hermes profiles share the canonical human-readable workspace at `~/Documents/Limitless OS/Agents/`, with a nightly 02:00 file-only memory sync. This is periodic/agent-written Markdown sync, not real-time mirroring of every external chat.
- ChatGPT/Codex Desktop is separate from Hermes. Files it writes inside AI OS are visible to Hermes, but its chat context and decisions do not automatically enter Hermes sessions or AI OS memory notes.

- 2026-08-05: Nightly cron built `Agents/Bolt/Builds/2026-08-05/agent-sync-control-room/`, a local HTML Agent Sync Control Room v0 summarizing 13 present agent daily-note syncs, recent files, and review flags; companion queue note: `Agents/Bolt/Queue/2026-08-05 - Nightly Workflow Build - agent-sync-control-room.md`.
- 2026-08-06: Nightly cron built `Agents/Bolt/Builds/2026-08-06/agent-permission-ladder-workshop/`, a student/founder Read / Draft / Action permission ladder kit rooted in the Aug 5 agent-safety handoff and no-auto-publish operating rule.
- 2026-08-07: Nightly cron built `Agents/Bolt/Builds/2026-08-07/geo-fix-sprint-dashboard-v0/`, a local GEO / AI visibility fix sprint dashboard converting the Aug 6 audit into P0/P1 Bolt/Blaze/Kelly workstreams; companion queue note: `Agents/Bolt/Queue/2026-08-07 - Nightly Workflow Build - geo-fix-sprint-dashboard-v0.md`.
- 2026-08-08: Nightly cron built `Agents/Bolt/Builds/2026-08-08/agent-memory-repair-triage-v0/`, a local static dashboard/generator that turns the all-agent file-only sync into a ranked memory/gateway repair queue; companion queue note: `Agents/Bolt/Queue/2026-08-08 - Nightly Workflow Build - agent-memory-repair-triage-v0.md`.
- 2026-08-09: Nightly cron built `Agents/Bolt/Builds/2026-08-09/agent-morning-command-center-v0/`, a local HTML morning command center plus `data.json` for synced agents, blockers, and next tiny actions; companion queue note: `Agents/Bolt/Queue/2026-08-09 - Nightly Workflow Build - agent-morning-command-center-v0.md`.

- 2026-08-10: Nightly build produced `Blog Ops Drift Watch v0` under `Agents/Bolt/Builds/2026-08-10/blog-ops-drift-watch-v0/` to preflight the Limitless Club blog/YouTube-to-blog pipeline. It flagged a review item: recent note claimed live index 205 articles while local main repo `client/public/blog/articles.json` currently parses 201; no cron edits or deploys were performed.

## JediStack local knowledge spine
- JediStack is Jet's non-destructive canonical IP and recall overlay at `/Users/ultrafriday/Projects/jedistack`.
- The original `_IP-Index` remains read-only evidence; JediStack links 16 master frameworks to quotes, operator proof, student proof, ROI, offers, and exact sources.
- Cross-agent local retrieval is available with `python3 /Users/ultrafriday/Projects/jedistack/scripts/search_jedistack.py "<question>"`.
- The private GitHub package is sanitized; raw sessions, credentials, client/private material, and sensitive IP stay local.

## AI OS source of truth
- Private GitHub source of truth: `https://github.com/jetlauncher/limitless-agent-memory-backup`; reproducible local workspace: `/Users/ultrafriday/Projects/limitless-agent-memory-backup`.
- Google Drive archive location: `Limitless AI OS Source of Truth/Snapshots/`. The repository exporter and zero-finding secret validator live under `scripts/`.
- Framework retrieval order: `_IP-Index/` for read-only evidence, JediStack for curated framework/proof/ROI relationships, and compact Kelly memory for routing facts only. Canonical operating anchors are Golden Triangle (KOI retired alias), 10-80-10, Workflow → Skill → Automation, agent folder portability, and the Knowledge Loop.
- Concept note: `Agents/Shared Memory/AI Brain OS/Concepts/AI OS Source of Truth.md`.

## AI expense tracking
- The original Google Sheet `Fixed Expenses 2026`, ID `1mcJnxxlEnIBw4q504sLOeO7Husu9E0oRViIiCd7gLkk`, remains untouched and contains the historical ฿50,000/month budget source.
- The reconciled 2026 AI-expense tracker is the native Google Sheet `AI Cost Tracker 2026 - Reconciled 2026-08-15`, ID `1tfzyQndMgSX2qkqlWVfCRa7AVhJE7sTJyMIEK_atqFo`, in Drive folder `AI Cost Tracker 2026`. It contains summary, 148-row ledger, missing-receipt, and 33-document crosswalk tabs; remote export/read-back was verified.
- The personal Google account `jeditrinupab@gmail.com` was re-authorized in August 2026 using the dedicated external OAuth client; Gmail and Drive access are verified. Sheets API access for the original tracker still returns HTTP 403, while rclone Drive import successfully creates native Google spreadsheets.

## Bolt model routing
- Bolt's quality route is `gpt-5.6-sol` via OpenAI Codex with 262,144 context and high reasoning; quality fallback is `openai/gpt-5.6-sol-pro` via Nous. Local Qwen was deliberately removed from Bolt's fallback chain after silent fallback caused severe coding and persona degradation in August 2026.
- If Bolt becomes childish (“Sparkle-chan”) or unusually error-prone, inspect the actual session model/provider in Bolt's `state.db`; profile status alone can conceal an active fallback. Reset the Telegram route with Hermes `SessionStore.reset_session()` after correcting the model so the bad context is preserved but no longer active.

## CG Day 2026 keynote
- Khun Jedi's CG Day 2026 evidence pack is `Agents/Shared Memory/AI Brain OS/Projects/CG Day 2026/CG-Day-2026-Speaker-Evidence-Pack.md`; its anchor is `AI เตรียม คนตัดสินใจ ระบบจดจำ` / `AI prepares. Humans decide. Systems remember.` The talk is people/work-design/trust first, not a tool demo; Jet must verify exact public headcount/financial claims and private screenshots before stage use.

## Public-safe system overview
- The canonical 116-day system-story landing page is `~/Projects/limitless-ai-os-116-days/`; production is `https://limitless-ai-os-116-days.vercel.app`. Its source ledger and reproducible browser QA ship with the page. It is a point-in-time 16 Aug 2026 snapshot and requires live count/claim revalidation before future redeployments.

## Fleet model routing
- Non-Qwen human-facing profiles use `gpt-5.6-sol` through OpenAI Codex with 262,144 context and `openai/gpt-5.6-sol-pro` via Nous as the only fallback. The dedicated Qwen profile remains local Qwen. Five low-stakes default crons remain explicitly Qwen-pinned and do not set agent chat models.
- `gpt-5.6` without `-sol` is rejected by Codex/ChatGPT and previously caused silent local-Qwen fallback plus sticky Telegram sessions; inspect recent `state.db` rows, not config alone, when behavior degrades.

## Limitless business model — 2026-08-22 audit
- Live Airtable audit supports a **course-powered implementation** model, not abandoning courses: education → AI Leverage Diagnostic → one-workflow Proof Sprint → 90-day AI OS Adoption → selective managed support.
- Courses remain the proven cash/trust engine; new SKUs should wait until existing offers track contribution margin, Jet hours, refunds, downstream conversion and corporate leads.
- Highest-confidence white space: owner-led Thai SMEs/mid-market teams needing one measurable workflow implemented between standardized training and large-enterprise consultancies.
- Canonical report: `Agents/Shared Memory/AI Brain OS/Projects/Limitless Business Audit/2026-08-22-whole-business-audit.md`.

## Limitless Strategy Blueprints
- Jet prefers a McKinsey-style signature slide system for explaining offer promises and customer journeys. The distinct Limitless version uses charcoal/bronze/ivory, Thai-first conclusion headlines, one consulting exhibit, a reusable formula strip, and vertically centered 1080×1350 layouts. Canonical concept: `Agents/Shared Memory/AI Brain OS/Concepts/Limitless Strategy Blueprints.md`.

## Brain Jarvis V6.1 reference
- The Skool Brain Jarvis V6.1 package is installed at `~/.claude/skills/brain-jarvis/`; audit workspace is `~/Projects/jarvis-v6-reverse-engineering/`. It is a reference prototype, not an approved production replacement for Hermes/Nova. Keep its external credentials, public tunnels, calls, Google/Telegram writes and screen takeover inactive unless a hardened sandbox fork passes explicit security review.

## Claude Code Fable 5 content route
- Claude Code `--model fable` routes to canonical `claude-fable-5` through Jet's authenticated Claude Max account. For current-news content, verify sources outside Claude first, disable Claude web/tools, run a deep-dive pass, resume the same session for writing, then fact/length audit and revise. Canonical demo: `Agents/Hermes/Outputs/Claude Fable 5 Demo/2026-08-30-ai-news-content-demo.md`.

## Document delivery preference
- Jet cannot open `.md` attachments. Keep Markdown as internal archive/source only; deliver user-facing documents as standalone HTML attachments or Notion pages.
