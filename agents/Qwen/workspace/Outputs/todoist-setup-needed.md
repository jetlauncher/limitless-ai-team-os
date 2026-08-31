# Todoist Fetch — Setup Needed

**Last run attempt:** 2026-07-24  
**Error:** Script timed out after 3600s (1 hour)  
**File:** `~/.hermes/profiles/qwen/scripts/qwen_todoist_fetch.py`

## Credential Status
- **`~/.config/todoist/api_key`:** EXISTS ✅ (file present, contains token)
- **`~/.config/todoist/token`:** Missing (fallback path)
- **`TODOIST_API_TOKEN` env var:** Not set

## Diagnosis
The script found the credential file but hung on the API call for >1 hour. This almost certainly means:
1. The API key in `~/.config/todoist/api_key` is expired/invalid (Todoist tokens rotate)
2. Network may also be a factor, but 3600s timeout suggests silent auth rejection

## Fix
1. Verify the token still works: open Todoist app → Settings → Integrations → Developer docs → check token validity
2. Or regenerate: go to https://todoist.com/app/settings/integrations and create a new token
3. Update `~/.config/todoist/api_key` with the new token
4. Reduce cron timeout from 3600s to ~60s — a hung network call should fail fast, not drain a whole hour

**Status:** Needs Kelly review for token refresh.
