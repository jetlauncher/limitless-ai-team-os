# Todoist Setup Needed

**Checked:** 2026-05-20 02:14 AM ICT

Todoist API is not configured for Qwen. No tasks can be fetched or processed.

## What's missing
- No API token found in `~/.config/todoist/api_key` or `TODOIST_API_TOKEN`.

## To enable
1. Get a Todoist Personal Access Token from [Todoist Settings > Developer](https://todoist.com/app/settings/integrations).
2. Store it safely:
   ```
   mkdir -p ~/.config/todoist
   echo '<your-token>' > ~/.config/todoist/api_key
   ```
3. Set `TODOIST_QWEN_INCLUDE_INBOX=1` if you want Inbox candidates included.
4. Restart the Qwen cron or run `~/.hermes/scripts/qwen_todoist_fetch.py` manually.

## Safety reminder
- Qwen only reads/summarizes tasks; it never completes, modifies, or deletes Todoist tasks.
- Tasks are filtered by label (`qwen`, `ai`, `agent`, `delegate`) or prefix (`Qwen:`, `AI:`, `Agent:`).
