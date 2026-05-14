# Todoist Setup Needed for Qwen Agent

**Last checked:** 2026-05-15  
**Status:** `TODOIST_NOT_CONFIGURED`

Qwen's automated Todoist scan is not configured. The agent cannot fetch or process tasks until API access is set up.

## What's needed

Store your Todoist API token at one of:

```
~/.config/todoist/api_key
```

or export the environment variable:

```
export TODOIST_API_TOKEN=[REDACTED]
```

## How to get a Todoist API token

1. Go to https://todoist.com/prefs/integrations
2. Scroll to **API** section
3. Copy the **API token** (appears as `xxxxxxxxxx.xxxxxxxxxxxxxxx`)
4. Save it: `echo '<token>' > ~/.config/todoist/api_key`

## After setup

Qwen will automatically:

- Fetch tasks labelled `qwen`, `ai`, `agent`, or `delegate`
- Fetch tasks starting with `Qwen:`, `AI:`, or `Agent:`
- Process safe local/draft/summarization work
- Write outputs under `Agents/Qwen/Outputs/Todoist/`
- Append daily status notes under `Agents/Qwen/Daily/`

## Optional: scan Inbox too

If you want Qwen to also consider Inbox items as candidates, set:

```
export TODOIST_QWEN_INCLUDE_INBOX=1
```

## Reference

- Todoist API docs: https://developer.todoist.com/
- Token should never be committed to git or shared publicly.
