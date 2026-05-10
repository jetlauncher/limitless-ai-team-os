# Mission Control Vercel Deployment — 2026-05-10

## Production URL

- https://limitless-mission-control.vercel.app

Access uses the private Mission Control key. Do not paste the key into shared notes.

Key file on local Mac:

- `~/.hermes/limitless/mission_control_key.txt`

Open format:

- `https://limitless-mission-control.vercel.app/?key=<mission_control_key>`

## Deployment details

Vercel project:

- `jetlaunchers-projects/limitless-mission-control`

GitHub repo:

- `git@github.com:jetlauncher/limitless-mission-control.git`

Latest local deployment alias:

- https://limitless-mission-control.vercel.app

Commit pushed:

- `d5e603a Deploy mission control to Vercel`

## Changes made

- Added Vercel Python serverless entrypoint: `api/index.py`
- Added `vercel.json` routing all requests to the serverless handler.
- Added `src/__init__.py` so Vercel can import `src.mission_control_server`.
- Added environment-based config support:
  - `AIRTABLE_TOKEN`
  - `AIRTABLE_BASE_ID`
  - `AIRTABLE_TABLE`
  - `MISSION_CONTROL_KEY`
  - `MISSION_CONTROL_PASSCODE`
  - `BLOTATO_API_KEY`
- Added `/tmp/limitless` runtime root for Vercel ephemeral state.
- Added tests for Vercel env config and serverless wrapper.

## Verification

Local tests:

- `pytest -q` → 18 passed

Production checks:

- `/health` → 200
- `/` with key → 200 HTML
- `/api/command-center` with key → 200 JSON
- `/api/approvals` with key → 200 JSON
- Home page contains `/api/command-center` and section markers.
- Command Center JSON includes money, approvals, and agent health.

## Caveats

- Vercel uses ephemeral serverless filesystem. Queue/state files are not durable there. Revenue dashboard and Airtable-backed data work via environment variables.
- Local Mission Control remains better for durable content approval queue edits unless/until queue state is moved to Airtable/Notion/another database.
