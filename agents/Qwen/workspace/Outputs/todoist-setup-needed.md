# Todoist API Setup Required

**Status:** Not configured  
**Detected:** 2026-05-21  
**Path:** `~/.config/todoist/api_key`

## What's needed

Qwen's scheduled cron job is running but cannot fetch tasks because the Todoist API token is not configured.

1. Get an API token from https://todoist.com/app/settings/api
2. Save it securely:

```bash
mkdir -p ~/.config/todoist
# Token value must NOT be printed or logged
echo -n '<your-token>' > ~/.config/todoist/api_key
chmod 600 ~/.config/todoist/api_key
```

3. Or set the environment variable:

```bash
export TODOIST_API_TOKEN='<your-token>'
```

4. To scan Inbox candidates (e.g., unsynced tasks), also set:

```bash
export TODOIST_QWEN_INCLUDE_INBOX=1
```

## Selection rule (already configured)

Qwen processes tasks that match **any** of:
- Labels: `qwen`, `ai`, `agent`, `delegate`
- Prefix: `Qwen:`, `AI:`, `Agent:`

## What Qwen does once configured

- Fetches matching tasks from Todoist
- Processes safe local/draft/summarization work only
- Writes one output markdown per task under `Agents/Qwen/Outputs/Todoist/`
- Appends a compact status to `Agents/Qwen/Daily/YYYY-MM-DD.md`
- **Never** completes, modifies, or deletes Todoist tasks
- **Never** sends Telegram/email/posts/deploys/spends money
