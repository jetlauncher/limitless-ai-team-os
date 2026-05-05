# Mission Control Content OS Upgrade Plan — 2026-05-05

## Decision
Use the existing GitHub repo `jetlauncher/limitless-mission-control` as the main Command Center foundation, rather than building a separate new dashboard.

Local repo:
- `/Users/ultrafriday/Projects/limitless-mission-control`

GitHub:
- `https://github.com/jetlauncher/limitless-mission-control`

## Current repo status checked
- Repo exists and is private.
- Description: Private Mission Control dashboard and social approval queue for Limitless Club.
- Main app: `src/mission_control_server.py`
- Tests: `tests/test_mission_control_approvals.py`
- Tests currently pass: `5 passed`.
- Current local working tree has uncommitted changes adding a Blaze Content Library route/API.

## What Mission Control already includes
- Beautiful Apple-style dashboard.
- Revenue dashboard backed by Airtable / Limitless Sales.
- Content approval queue for X, LinkedIn, Threads.
- Blotato publishing integration.
- Protected passcode login.
- Cloudflare tunnel helper.
- Local storage in `~/.hermes/limitless/`.
- Obsidian Social Posting log integration.

## Problems to fix before relying on it daily
1. Mission Control is not running as an always-on service.
2. `/api/data` can hang because it waits on external Airtable/Notion calls inside the request path.
3. Local queue status and Blotato status are not fully synchronized.
4. Published URLs are not consistently written back into the queue.
5. Signal, Blaze, Notion, Obsidian, and queue outputs are still split across too many mental locations.
6. The existing beautiful dashboard is underused because it is not the daily default review surface.

## Recommended target architecture
Mission Control should become the single daily action layer:
- Revenue
- Signal Intel
- Blaze Library
- Draft Queue
- Approvals
- Scheduled
- Published
- Failed
- Website / SEO Articles
- Agent Health

Notion remains the executive database layer.
Obsidian remains the detailed archive / memory layer.
Blotato remains the publishing engine.

## Phase 1 — Stabilize
- Convert HTTP server to a threaded server or move slow external calls behind cached jobs.
- Add hard timeouts and graceful fallbacks for Airtable/Notion.
- Keep `/health`, `/api/approvals`, and `/api/content-library` responsive even if Airtable/Notion hangs.
- Run tests and start Mission Control locally.
- Add launchd/service startup so the dashboard stays running.

## Phase 2 — Content visibility
- Finish Blaze Content Library page.
- Add tabs/filters: Queue, Ready for Review, Approved, Scheduled, Published, Failed, Notion Archive.
- Show where each item lives: Queue JSON, Notion, Obsidian clone, Blotato URL.
- Add source labels: Signal, Blaze, Kelly, Bolt, manual.

## Phase 3 — Sync engine
- Add Blotato status sync job.
- Poll `postSubmissionId`s.
- Update queue status: scheduled, published, failed.
- Write `publicUrl` back into each item.
- Mirror a compact publish log into Obsidian and optionally Notion.

## Phase 4 — Signal → Blaze pipeline
- Add Signal Inbox page to Mission Control.
- Parse latest Signal notes from `Agents/Signal/Daily/`.
- Extract Blaze-ready content angles.
- Add one-click action: “Send to Blaze Draft Queue”.

## Phase 5 — Website / SEO lane
- Add Website Articles tab.
- Connect Bolt’s YouTube → SEO article cron output.
- Track article statuses: source_found, transcript_ready, draft_created, seo_review, ready_to_publish, published, needs_update.

## Phase 6 — Weekly operating rhythm
- Sunday Content CEO Review inside Mission Control:
  - best signals
  - best drafts
  - published URLs
  - failed posts
  - unused high-quality drafts
  - next week content themes

## Product principle
Do not make Jet search through files. Mission Control should answer:
- What did the agents find?
- What did they write?
- What needs my review?
- What is scheduled?
- What published?
- What failed?
- Where is the source/archive?
