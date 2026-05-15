# Todoist API Not Configured

**Checked:** 2026-05-16 03:11 +07  
**Status:** API token missing

## What's needed
Add a Todoist API token so the Qwen cron worker can read tasks.

```bash
# Option 1: file-based (recommended)
mkdir -p ~/.config/todoist
echo '<your-token>' > ~/.config/todoist/api_key
chmod 600 ~/.config/todoist/api_key
```

## Selection rule (once configured)
This worker reads tasks matching:

- **Labels:** `qwen`, `ai`, `agent`, or `delegate`
- **Prefixes:** `Qwen:`, `AI:`, or `Agent:`
- **Inbox candidates:** set `TODOIST_QWEN_INCLUDE_INBOX=1` as needed

## After setup
The next cron run will automatically detect the token and begin processing. No manual restart is required.
