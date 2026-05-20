# Qwen Todoist Integration — Setup Needed

**Status:** Not configured  
**Checked:** 2026-05-21T01:20:23+07:00

## What's missing
No Todoist API token is configured. Qwen cannot fetch tasks.

## How to set up

1. Get a Todoist API token: [REDACTED]
2. Place it safely:
   ```bash
   echo '<your-token>' > ~/.config/todoist/api_key
   ```
3. Ensure the directory exists first:
   ```bash
   mkdir -p ~/.config/todoist
   ```

## After setup
- Qwen will automatically fetch tasks on its scheduled cron runs.
- Selection rule: tasks labelled `qwen`, `ai`, `agent`, or `delegate`, OR tasks with prefix `Qwen:`, `AI:`, or `Agent:`.
- To also scan Inbox candidates: set `TODOIST_QWEN_INCLUDE_INBOX=1`.

## Notes
- Qwen does NOT complete, modify, or delete Todoist tasks.
- Output is written to `Agents/Qwen/Outputs/Todoist/` in Obsidian.
- No Telegram, email, posting, or external side effects are sent.
