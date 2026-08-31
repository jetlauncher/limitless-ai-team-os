# Pipeline PM Tick — BLOCKER

**Time:** 2026-07-21 19:56 +07 (2026-07-21T12:56Z UTC)
**Tick:** Pipeline PM (every 15 min)
**Status:** ❌ BLOCKED — vault directory unreadable

## What happened
Every filesystem access to `~/Documents/Limitless OS/` (including
`Pipeline/`, `Pipeline/_inbox/`, `Pipeline/pm/`, `Agents/Oracle/Daily/`)
returns `Interrupted system call` (errno = EINTR) for both `ls`, `stat`,
`find`, and Hermes' `read_file`.

## Root cause (likely)
- `df` shows disk at 98% capacity (18 GiB free on `/System/Volumes/Data`).
- iCloud Drive is backing `Documents/Limitless OS/` and is likely
  stalling or evicting the local cache due to space pressure.
- The `Documents/` mount point itself returns EINTR — not a permission
  issue, a sync/IO stall.

## What was NOT done
- Could NOT classify `Pipeline/_inbox/*.md` (path unreadable).
- Could NOT dispatch new items to `potential_projects/<slug>/`.
- Could NOT process `pm/route_inbox_item.json`.
- Could NOT spawn any workers.
- Could NOT write the daily note to `Agents/Oracle/Daily/2026-07-21.md`
  (same directory tree blocked).

## What Jet should do
1. Free disk space (`~/Library/Developer/Xcode/DerivedData`,
   `~/Library/Caches`, Docker images, `~/Movies` raw footage are
   typical wins).
2. Wait for iCloud Drive to finish syncing / re-evict, then re-check
   `ls ~/Documents/Limitless\ OS/`.
3. If still failing after that, the next tick will retry automatically.

The next scheduled tick should attempt again — no manual restart needed.
