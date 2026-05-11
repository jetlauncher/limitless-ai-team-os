# Qwen Todoist Workflow

Qwen's primary task source is Todoist.

## How Jet should assign work to Qwen
In Todoist, create a task using either:
- Label: `qwen`, `ai`, `agent`, or `delegate`
- Prefix: `Qwen:`, `AI:`, or `Agent:`

Examples:
- `Qwen: summarize this transcript in Obsidian`
- `AI: cluster yesterday's research notes`
- Task labelled `qwen`: `Draft 10 content angles from this note`

## What Qwen does
Every 2 hours, Qwen reads selected Todoist tasks using:
`~/.hermes/scripts/qwen_todoist_fetch.py`

Then Qwen writes local outputs to:
`Agents/Qwen/Outputs/Todoist/`

## Safety
Qwen is read-only against Todoist by default.

It should not:
- Complete Todoist tasks
- Modify Todoist tasks
- Delete Todoist tasks
- Send/post/email/deploy/spend money

Anything external or high-stakes should be marked:
`Needs Kelly review`

## Setup requirement
A Todoist API token is still needed.
Store it at:
`~/.config/todoist/api_key`

Do not paste or print the token in chat/logs.
