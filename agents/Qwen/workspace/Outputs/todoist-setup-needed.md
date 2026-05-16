# Todoist API — Setup Needed

**Last checked:** 2026-05-17T02:58+07:00
**Status:** Not configured

## What to do

1. Create or get a Todoist API token at https://todoist.com/app/settings/api
2. Save it to `~/.config/todoist/api_key` (one line, no print/export of the raw value in logs)
3. Set the environment variable `TODOIST_API_TOKEN` in your shell or Hermes gateway config

## Once configured

Qwen will automatically scan for tasks with labels `qwen`, `ai`, `agent`, or `delegate`,
or tasks starting with `Qwen:`, `AI:`, or `Agent:`.

Set `TODOIST_QWEN_INCLUDE_INBOX=1` if you also want Qwen to scan Inbox candidates.

## Next step

Just add your token and tell Qwen to rescan. No other setup required.
