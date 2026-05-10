# Mission Control Approval Fix — 2026-05-10

## Issue

Jet could not approve Threads/social drafts on the Vercel Mission Control dashboard.

## Root cause

The `/api/approvals/update` endpoint successfully updated the queue, then called `log_approval_event()`.

On Vercel, the serverless runtime can write to `/tmp`, but not to the home/Obsidian path:

- `~/Documents/Obsidian Vault/Agents/Hermes/Social Posting/`

That best-effort log write raised:

```text
[Errno 30] Read-only file system: '/home/sbx_user1051'
```

The exception bubbled up and made the approval POST return HTTP 500.

## Fix

- Made `log_approval_event()` best-effort and non-blocking.
- Approval state changes now continue even if the Obsidian log path is read-only/unavailable on Vercel.
- Added regression test: `test_log_approval_event_does_not_break_approval_when_log_dir_is_read_only`.

## Verification

Local tests:

```text
pytest -q → 19 passed
```

Production verification:

- `POST /api/approvals/update` on `https://limitless-mission-control.vercel.app` now returns `200 { ok: true }`.

## Commit

- `889ba57 Fix Vercel approval logging`
