# Qwen Todoist Integration — Setup Needed

**Last checked:** 2026-05-14 03:22 +0700

## Status
Todoist API is **not configured**. The cron job cannot fetch tasks because no API token is present.

## What to do

1. **Add your Todoist API token:[REDACTED]
   ```bash
   mkdir -p ~/.config/todoist
   # Paste your token (create one at https://todoist.com/app/settings/integrations/api)
   echo 'YOUR_TODOIST_API_TOKEN_HERE' > ~/.config/todoist/api_key
   ```
   Or set `TODOIST_API_TOKEN` in the cron environment.

2. **Verify** the fetch script works:
   ```bash
   python3 ~/.hermes/scripts/qwen_todoist_fetch.py
   ```

3. **Select your workspace** (if you haven't already):
   - Kelly/ops inbox → your default agent queue
   - Separate workspace for Jet's personal/agent tasks

## Selection rule (once configured)
Tasks are selected when they:
- Have **label** `qwen`, `ai`, `agent`, or `delegate`, OR
- Start with `Qwen:`, `AI:`, or `Agent:`
- Set `TODOIST_QWEN_INCLUDE_INBOX=1` to also scan Inbox candidates

## Notes
- No token value is ever printed or logged.
- Task completion/modification requires explicit user approval — Qwen marks outputs instead.
