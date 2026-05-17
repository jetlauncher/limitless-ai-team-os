# Todoist API Setup Needed

**Last checked:** 2026-05-18 01:56 AM

A valid API token is not configured in `~/.config/todoist/api_key` or the `TODOIST_API_TOKEN` environment variable. This cron job can currently see or fetch no tasks.

## What to do

1. Open your **Personal Access Tokens** page at: https://todoist.com/app/settings/api
2. Generate or copy a token (scope: `tasks:read` is sufficient).
3. Place it in `~/.config/todoist/api_key`:

   ```bash
   mkdir -p ~/.config/todoist
   # Paste only the token value (no spaces, no quotes)
   ```

4. If you want inbox items included in future scans, also set:

   ```bash
   export TODOIST_QWEN_INCLUDE_INBOX=1
   ```

## Selection rule (once configured)

- Tasks labelled `qwen`, `ai`, `agent`, or `delegate`
- Tasks whose title starts with `Qwen:`, `AI:`, or `Agent:`

No tasks were processed this run.
