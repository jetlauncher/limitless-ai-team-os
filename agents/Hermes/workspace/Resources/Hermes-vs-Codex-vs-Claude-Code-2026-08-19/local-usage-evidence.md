# Local Hermes usage evidence — 2026-08-19

Snapshot time: 2026-08-19 16:09 Bangkok time.

## Installation timeline
- `~/.hermes` birth time: 2026-04-21 19:07:21 +07:00.
- `~/.hermes/state.db` birth time: 2026-04-21 19:16:09 +07:00.
- Earliest Hermes session file: 2026-04-21 19:17:41 +07:00.
- Measurement window through 2026-08-19: 121 calendar days inclusive.

## State database totals
- Sessions: 4,787.
- Messages: 40,692.
- Tool calls/actions: 19,545.
- API calls: 7,835.

## Scheduled work
- Cron-sourced sessions: 4,732.
- Cron sessions that used at least one tool: 3,545.
- Tool calls inside cron sessions: 16,393.
- Configured recurring jobs: 42 total.
- Enabled recurring jobs at snapshot: 22.
- Paused jobs: 20.
- Enabled script-only/no-agent jobs: 13.

## Conservative time-saved estimate
Two deliberately simple methods converge:

1. Tool-using automated sessions: 3,545 × 5 minutes of avoided manual setup/checking = 295.4 hours.
2. All tool actions: 19,545 × 1 minute of avoided human clicking/searching/file work = 325.8 hours.

Presentation headline: **about 300 hours saved**, with a defensible logged-activity range of **275–325 hours**.

Equivalent:
- About 37.5 eight-hour workdays.
- About 7.5 forty-hour workweeks.
- About 2.5 hours per calendar day since installation.

## Caveats
- This is an estimate, not a stopwatch measurement.
- Some sessions are health checks, retries, or no-change runs; the estimate discounts this by using only tool-using sessions and a low five-minute value.
- Some research, creative, operational, and engineering tasks would take far longer than five minutes manually; the estimate intentionally does not claim that upside.
- Database records include automated child sessions and migrated session history; counts represent logged system activity, not unique business outcomes.
