# Kelly Proactive Ops Radar

Updated: 2026-05-16 08:17 +07
Owner: Kelly / Hermes
Purpose: make Kelly proactive without becoming noisy.

## Operating rule

Kelly should maintain a daily **Top 5 Next Actions** radar for Jet across revenue, agent health, teaching assets, content, systems, and blockers.

Telegram should receive only:
- urgent items,
- high-leverage decisions,
- broken automations that affect Jet,
- short morning/evening summaries,
- explicit user-requested updates.

Full detail belongs in Obsidian / Notion / local logs.

## Model / billing rule

- Kelly/default Hermes should stay on GPT-5.5 via OpenAI Codex unless Jet explicitly asks otherwise.
- Routine Kelly cron jobs should not use the direct Anthropic provider by default.
- When Claude-quality writing/coding is needed, prefer delegating through Claude Code CLI with Claude Max/OAuth, not direct Anthropic API billing.
- Verify Claude Code with `claude auth status --text` plus a real `claude -p` smoke test before relying on it.

## Daily radar inputs

1. Revenue and sales
   - Airtable `Limitless Sales`, table `1. transactions`, field `ยอดโอน`.
   - Payment alert script status.
   - Daily revenue report status.

2. Agent fleet health
   - Cron job status.
   - Gateway/profile status when relevant.
   - EOD/memory sync completion.
   - Logs containing max-iteration/partial-write failures.

3. Memory hygiene
   - Agents with missing or empty daily notes after meaningful work.
   - Shared Memory handoffs missing for cross-agent context.
   - Durable `Memory/MEMORY.md` facts that conflict with verified config.

4. Teaching / course assets
   - AI Agent Team OS student pages.
   - Notion mirrors.
   - Obsidian source files.
   - Missing Start Here hubs, checklists, diagrams, demos.

5. Content / audience growth
   - Content queue waiting for approval.
   - X / Notion / Obsidian sync outputs.
   - Research signals from Signal.
   - Blaze/Kaijeaw output cadence and approval bottlenecks.

6. System blockers
   - Missing/expired tokens.
   - Broken tunnels/dashboards.
   - Cron delivery misconfiguration.
   - Local model or provider issues.
   - Disk/process/system pressure if symptoms appear.

## Daily output shape

Keep Telegram concise:

```text
Kelly Radar — YYYY-MM-DD

Top 5 next actions:
1. ...
2. ...
3. ...
4. ...
5. ...

Needs Jet:
- one decision/request only if possible

Quietly watching:
- 1–3 low-priority items
```

## Escalation rules

Escalate immediately if:
- revenue alerts break,
- payment data source is stale,
- public/customer-facing system fails,
- a scheduled job claims success but produced no output,
- an agent memory sync is partial,
- credentials are invalid for a critical workflow,
- content is about to publish without approval.

Do not escalate immediately if:
- a local-only sync has a harmless warning,
- an optional feed has a 403/404 but output quality remains fine,
- a background note update is delayed but not user-facing,
- a non-critical local model task fails and can be retried quietly.

## Verification checklist before saying “done”

- [ ] Output file exists and is non-empty.
- [ ] Relevant cron/job status checked when the task involves automation.
- [ ] Logs checked for partial-failure language when a job reports `ok`.
- [ ] Memory note written for meaningful work.
- [ ] Shared handoff written if another agent should know.
- [ ] No secrets printed or stored.

## Current starting priorities — 2026-05-16

1. Create a single Start Here hub for the three student AI Agent Team OS pages.
2. Let the 08:00 Good Morning Briefing and 09:00 revenue report run, then verify whether the output is useful/low-noise.
3. Watch the existing 07:45 agent fleet dashboard snapshot and use it as the first daily Radar source.
4. Reconcile Zegna scout frequency if Jet wants more than the verified daily 09:00 scout.
5. Unblock Qwen Todoist integration only when Jet provides or approves the Todoist API token path.
