# Airtable Credential Readiness Kit

Generated: 2026-06-28T02:01:51

## What this is
A local v0 dashboard and runbook for the recurring Airtable snapshot blocker. It checks whether safe credential files exist and whether they appear to contain `AIRTABLE_API_KEY` without exposing any secret values.

## Open
- `dashboard.html`
- `data.json`

## Verify
```bash
python3 build_airtable_credential_readiness.py
python3 -m json.tool data.json >/dev/null
grep -qi '<html' dashboard.html
```

## Safety
No external calls, no credential values printed, no cron edits.
