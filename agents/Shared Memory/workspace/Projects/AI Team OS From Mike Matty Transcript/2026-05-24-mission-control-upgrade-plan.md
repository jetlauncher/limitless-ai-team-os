# Mission Control Upgrade Plan — AI Team OS Layer

Date: 2026-05-24
Correction: Jet is right — we already have the Command Center. Do **not** build a separate Founder Command Center app. Improve the existing Mission Control repo.

## Existing source of truth

- Repo: `/Users/ultrafriday/Projects/limitless-mission-control`
- Production URL: `https://limitless-mission-control.vercel.app`
- Health verified: `/health` returns `200 OK`
- Homepage is protected: `/` returns `401 Unauthorized` when unauthenticated
- Main server: `src/mission_control_server.py`
- Unified endpoint already exists: `/api/command-center`
- Tests verified on 2026-05-24: `19 passed`

## Current Command Center already includes

- Revenue dashboard backed by Airtable
- Content approval queue
- Blotato publishing integration
- Protected login/access key
- `/api/command-center` aggregate payload
- Approval counts / failed posts / media-ready counts
- Retention summary
- Automation health summary
- Agent health summary
- Signal inbox / Blaze library / Website SEO lane hooks

## Upgrade direction from the transcript

The transcript should inform the next layer, not create a new product surface.

### Level 1 upgrade — better internal tools

Improve Mission Control so it replaces fragmented admin views:

1. Add real source-status cards:
   - Airtable revenue
   - student count
   - Blotato queue
   - Notion/Obsidian clone freshness
   - cron health digest
2. Add “source broken” states instead of green-but-broken cards.
3. Make cached snapshots visible with freshness labels.

### Level 2 upgrade — AI team operating cockpit

Mission Control should show the agent team as a working pipeline:

1. Signal Intel lane: high-signal research items ready for Blaze/Kaijeaw.
2. Blaze Library lane: drafts and approved English content.
3. Kaijeaw lane: Thai content and workshop repurposing.
4. Pixel lane: visual assets needing review.
5. Bolt lane: sites/apps/SEO articles.
6. Qwen lane: local ops/hygiene issues.
7. Kelly lane: priority actions and system blockers.

### Level 3 upgrade — productize the system

Once Mission Control works internally, turn the pattern into the student-facing AI Team OS offer:

- Private internal Mission Control remains Jet's real cockpit.
- Student version becomes a template/demo with safe synthetic data.
- Teaching materials explain the 3-level ladder: tools → team → product.

## Concrete next implementation backlog

### P0

1. Wire the new cron health digest into `/api/command-center`.
   - Source: `~/.hermes/state/cron_health/latest.json`
   - Show issue count, noisy profile count, report path, generated timestamp.
2. Replace static automation status labels with real job health from cron configs.
3. Add student-count truth panel from Airtable field `จำนวนนักเรียน`.
4. Add a “Next actions” priority strip:
   - Revenue source broken
   - Approval queue waiting
   - Failed posts
   - Agent stale/missing
   - Cron health issues

### P1

1. Add Agent Inbox cards from Shared Memory handoff folders.
2. Add publish reconciliation status from Blotato `postSubmissionId` polling.
3. Add cached snapshots so dashboard never hangs on live APIs.
4. Add a student/demo mode for productized screenshots.

### P2

1. Add beautiful executive screenshot/PDF export.
2. Add weekly CEO review page.
3. Add AI Team OS teaching/demo page.

## Verification gates

Before sharing any improvement as done:

- `python3 -m py_compile src/mission_control_server.py`
- `pytest -q tests/test_mission_control_approvals.py tests/test_vercel_deployment.py`
- Local `/health` OK
- Production `/health` OK after deploy
- Protected homepage still requires auth
- `/api/command-center` includes no secret-shaped fields

## Decision

Build inside Mission Control. No new app unless Mission Control's architecture blocks a required product/demo mode.
