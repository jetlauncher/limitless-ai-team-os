# 2026-05-01 Signal Backlog and Output Audit

Created: 2026-05-01 10:10 +07  
Agent: Signal  
Purpose: Backfill where Signal outputs have been stored, because reports were not consistently logged in Obsidian/Notion database form.

## Summary

Jet is correct: Signal outputs were fragmented. The system has been sending many outputs to Telegram and saving automatic cron run logs locally, but not every delivered brief has a clean Obsidian work log or a row in a Notion database.

Current storage buckets:

1. **Telegram DM delivery**
   - Cron jobs deliver final briefs to Jet via `deliver: origin`.
   - These messages are readable in Telegram but not structured as a database.

2. **Hermes cron run archive**
   - Path: `~/.hermes/profiles/signal/cron/output/{job_id}/YYYY-MM-DD_HH-MM-SS.md`
   - This is the most complete raw archive of scheduled work.
   - It includes prompt + response, often with full loaded skill text, so files are noisy.

3. **Signal Obsidian Daily notes**
   - Path: `~/Documents/Obsidian Vault/Agents/Signal/Daily/`
   - Contains explicit daily/bookmark notes, but not every cron report was summarized here until this audit.

4. **Shared Intel Obsidian notes**
   - Path: `~/Documents/Obsidian Vault/Agents/Shared Memory/Intel/`
   - Contains structured daily AI intel reports from the 9pm report job.

5. **Local JSON machine backups**
   - Path: `~/.hermes/limitless/`
   - Contains machine-readable outputs such as `daily_ai_intel_YYYY-MM-DD.json` and `x_signal_posts_YYYY-MM-DD.json`.

6. **Notion loose pages, not a database**
   - Current scripts create child pages under Knowledge Base, not database rows.
   - Parent page ID used by scripts: `2aed076c-9ad3-807b-8fe1-d284f25f9266`.
   - Page title patterns:
     - `Signal Daily AI Intel Report — YYYY-MM-DD`
     - `X/Twitter AI Signal Archive — YYYY-MM-DD`

## Active Signal cron jobs observed

| Job | ID | Schedule | Current storage behavior |
|---|---:|---|---|
| `signal-ai-morning-brief` | `d194c1c29c42` | `30 8 * * *` | Telegram + cron output archive only |
| `signal-ai-evening-brief` | `52bea60a6907` | `30 17 * * *` | Telegram + cron output archive only |
| `signal-high-signal-ai-watch` | `f64fa63e9bc7` | `every 120m` | Telegram/SILENT + cron output archive only |
| `signal-x-twitter-high-alert-scan` | `88d1ac455e7b` | `every 120m` | Telegram/SILENT + cron output archive only |
| `signal-daily-x-posts-to-notion-9pm` | `d86de7da7f30` | `0 21 * * *` | Notion loose page + local JSON + cron output |
| `signal-daily-ai-intel-report-9pm` | `6c5ac6a19886` | `0 21 * * *` | Obsidian Shared Intel + local JSON + Notion loose page + cron output |
| `signal-daily-x-bookmarks-research-5am` | `cea9aafced77` | `0 5 * * *` | Obsidian Daily + Telegram + cron output |

## Backfilled artifact index

### Signal Daily notes

Folder: `~/Documents/Obsidian Vault/Agents/Signal/Daily/`

- [[2026-05-01 X Bookmarks + Signal Research]]
  - File: `2026-05-01 X Bookmarks + Signal Research.md`
  - Modified: 2026-05-01 05:05
  - Size: 13,488 bytes
  - Source job: `signal-daily-x-bookmarks-research-5am`
  - Note: 5am bookmark research fallback reported bookmark capture issue and ran official-source AI sweep.

- [[2026-04-30 X Bookmarks Sweep]]
  - File: `2026-04-30 X Bookmarks Sweep.md`
  - Modified: 2026-04-30 07:12
  - Size: 6,009 bytes
  - Source: manual Signal browser/CDP bookmark read in Telegram session.
  - Note: Captured 23 visible X bookmarks and clustered them around Agent OS, coding workflows, AI-native services, chat-native docs/apps, realtime voice/multimodal agents.

- [[2026-04-29-ai-avenues-bulletin]]
  - File: `2026-04-29-ai-avenues-bulletin.md`
  - Modified: 2026-04-29 21:08
  - Size: 1,990 bytes

- [[2026-04-26]]
  - File: `2026-04-26.md`
  - Modified: 2026-04-26 05:52
  - Size: 256 bytes

- [[_template]]
  - File: `_template.md`
  - Modified: 2026-04-26 05:52
  - Size: 312 bytes

### Shared Memory Intel reports

Folder: `~/Documents/Obsidian Vault/Agents/Shared Memory/Intel/`

- [[2026-04-30 - Signal Daily AI Intel Report]]
  - Modified: 2026-04-30 21:01
  - Size: 7,734 bytes
  - Source job: `signal-daily-ai-intel-report-9pm`
  - JSON backup: `~/.hermes/limitless/daily_ai_intel_2026-04-30.json`

- [[2026-04-29 - Signal Daily AI Intel Report]]
  - Modified: 2026-04-29 21:01
  - Size: 7,937 bytes
  - Source job: `signal-daily-ai-intel-report-9pm`
  - JSON backup: `~/.hermes/limitless/daily_ai_intel_2026-04-29.json`

- [[2026-04-28 - Signal Daily AI Intel Report]]
  - Modified: 2026-04-28 21:02
  - Size: 8,112 bytes
  - Source job: `signal-daily-ai-intel-report-9pm`
  - JSON backup: `~/.hermes/limitless/daily_ai_intel_2026-04-28.json`

- [[2026-04-27 - Signal Daily AI Intel Report]]
  - Modified: 2026-04-27 21:01
  - Size: 10,743 bytes
  - Source job: `signal-daily-ai-intel-report-9pm`
  - JSON backup: `~/.hermes/limitless/daily_ai_intel_2026-04-27.json`

- [[2026-04-26 - Signal Daily AI Intel Report]]
  - Modified: 2026-04-26 21:01
  - Size: 10,210 bytes
  - Source job: `signal-daily-ai-intel-report-9pm`
  - JSON backup: `~/.hermes/limitless/daily_ai_intel_2026-04-26.json`

### Hermes Content Archive / Notion clones

Folder: `~/Documents/Obsidian Vault/Agents/Hermes/Content Archive/Notion Clones/Content Intelligence/`

These appear to be cloned/exported content-intelligence pages, separate from Signal Daily but relevant to the historical AI report archive.

- `2026-04-27 — X Signal Radar — Daily AI Report (2026-04-28).md`
- `2026-04-26 — X Signal Radar — Daily AI Report (2026-04-27).md`
- `2026-04-25 — X Signal Radar — Daily AI Report (2026-04-26).md`
- `2026-04-25 — X Signal Radar — Daily AI Report (2026-04-25).md`
- `2026-04-23 — X Signal Radar — Daily AI Report (2026-04-24).md`
- `2026-04-22 — X Signal Radar — Daily AI Report (2026-04-23).md`

### Local JSON backups

Folder: `~/.hermes/limitless/`

Observed Signal-related JSON outputs:

- `daily_ai_intel_2026-04-30.json` — 26,607 bytes
- `x_signal_posts_2026-04-30.json` — 177 bytes
- `daily_ai_intel_2026-04-29.json` — 27,728 bytes
- `x_signal_posts_2026-04-29.json` — 177 bytes
- `daily_ai_intel_2026-04-28.json` — 34,999 bytes
- `x_signal_posts_2026-04-28.json` — 177 bytes
- `daily_ai_intel_2026-04-27.json` — 44,824 bytes
- `x_signal_posts_2026-04-27.json` — 69,941 bytes
- `daily_ai_intel_2026-04-26.json` — 42,305 bytes
- `x_signal_posts_2026-04-26.json` — 177 bytes
- `ai_news_roundup_state.json` — older AI news state from 2026-04-23

Important: `x_signal_posts_2026-04-26`, `2026-04-28`, `2026-04-29`, `2026-04-30` are only 177 bytes, which likely means the X collector produced near-empty archive files on those days.

### Cron output raw archive

Folder: `~/.hermes/profiles/signal/cron/output/`

Key job folders:

- `d194c1c29c42/` — `signal-ai-morning-brief`
- `52bea60a6907/` — `signal-ai-evening-brief`
- `f64fa63e9bc7/` — `signal-high-signal-ai-watch`
- `88d1ac455e7b/` — `signal-x-twitter-high-alert-scan`
- `d86de7da7f30/` — `signal-daily-x-posts-to-notion-9pm`
- `6c5ac6a19886/` — `signal-daily-ai-intel-report-9pm`
- `cea9aafced77/` — `signal-daily-x-bookmarks-research-5am`

Recent raw runs observed:

- `cea9aafced77/2026-05-01_05-05-35.md` — 5am X bookmark + research job
- `d194c1c29c42/2026-05-01_08-38-30.md` — morning AI brief
- `f64fa63e9bc7/2026-05-01_08-36-00.md` — high-signal AI watch
- `88d1ac455e7b/2026-05-01_09-10-31.md` — X/Twitter high-alert scan
- `6c5ac6a19886/2026-04-30_21-01-30.md` — daily AI intel report
- `d86de7da7f30/2026-04-30_21-00-41.md` — daily X posts to Notion job
- Many 2-hourly watch/scan logs from 2026-04-28 through 2026-05-01.

## Gap analysis

### What is missing

- No single Obsidian “Signal Work Log” existed until this backfill.
- Telegram-delivered morning/evening/watch reports are not being summarized into Daily notes.
- Notion output is not a proper database.
- Some X archive JSON files are effectively empty, meaning the X source collector likely failed or found no posts on those runs.
- The 5am bookmark job writes Obsidian, but did not write Notion.

### What should become source of truth

Recommended source-of-truth architecture:

1. **Notion database**: canonical structured report index and searchable database.
2. **Obsidian Daily/Shared Memory**: human-readable and cross-agent handoff notes.
3. **Local JSON**: machine-readable backup.
4. **Cron output**: raw execution/audit logs only, not primary workspace.

## Backfill action completed now

Created this audit/backlog note:

`~/Documents/Obsidian Vault/Agents/Signal/Daily/2026-05-01 Signal Backlog and Output Audit.md`

This note now acts as the initial Obsidian backlog index for Signal work and storage locations.

## Canonical Notion database created and filled

Created canonical Notion database:

- **Name:** `Signal Reports Database`
- **Database ID:** `353d076c-9ad3-81cd-aff3-e054bd10e43b`
- **URL:** https://app.notion.com/p/353d076c9ad381cdaff3e054bd10e43b
- **Local state file:** `~/.hermes/limitless/signal_reports_notion_db.json`
- **Backfill result:** `~/.hermes/limitless/signal_reports_backfill_result.json`

Backfill completed:

- Total artifacts indexed: **906**
- Latest sync created: **1** new Notion row
- Existing/previously created rows recognized: **905**
- Failed rows: **0**
- Verified Notion row count: **906**

Database properties include:

- `Name` / title
- `Date`
- `Report Type` — Morning Brief, Evening Brief, High-Signal Watch, X Scan, Bookmark Research, Daily Intel, X Archive, Backlog/Audit, Other
- `Job Name`
- `Cron Job ID`
- `Run Time`
- `Source Channels`
- `Top Themes`
- `Status`
- `Telegram Delivered`
- `Obsidian Path`
- `JSON Path`
- `Cron Output Path`
- `Primary Links`
- `Summary`
- `Signal Score`
- `Artifact Key`

Backfilled sources:

1. Obsidian Signal Daily notes
2. Obsidian Shared Memory Intel notes
3. Hermes Content Archive / Notion Clone markdowns
4. Local JSON backups in `~/.hermes/limitless/`
5. Raw cron output logs in `~/.hermes/profiles/signal/cron/output/`

## Remaining pipeline fix

Update every Signal cron prompt/script so each future run writes:

1. Notion DB row/page in `Signal Reports Database`
2. Obsidian note or daily append
3. JSON backup where structured output exists
4. Telegram summary

## Related notes

- [[2026-05-01 X Bookmarks + Signal Research]]
- [[2026-04-30 X Bookmarks Sweep]]
- [[2026-04-30 - Signal Daily AI Intel Report]]
- [[2026-04-29 - Signal Daily AI Intel Report]]
- [[2026-04-28 - Signal Daily AI Intel Report]]
- [[2026-04-27 - Signal Daily AI Intel Report]]
- [[2026-04-26 - Signal Daily AI Intel Report]]
