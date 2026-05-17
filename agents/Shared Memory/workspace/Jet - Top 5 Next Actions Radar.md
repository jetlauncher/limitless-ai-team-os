# Jet — Top 5 Next Actions Radar

Updated: 2026-05-17 08:17 +07  
Owner: Kelly / Hermes  
Mode: concise, proactive, low-noise.

## Top 5 next actions

1. **Fix/re-auth the default Google Workspace token.**
   - Why: today’s Good Morning briefing was marked ok, but calendar failed with `invalid_grant`; the 2-account inbox job also failed on the Work token.
   - Scope: re-auth only; do not modify calendar/email content.

2. **Protect today’s revenue push to the ฿2M line.**
   - Current: MTD ฿1,745,882.83 from Airtable, 65 transactions, 87.29% to ฿2M, gap ฿254,117.17.
   - Today so far: ฿0 / 0 transactions; latest paid rows were May 16.

3. **Ship one Start Here hub for the student AI Agent Team OS kit.**
   - Why: playbook, simple prompts, and tool links exist separately; students need one entry point.
   - Suggested flow: Start here → install tools → copy prompts → advanced commands.

4. **Keep agent fleet healthy, but treat green cron status as not enough.**
   - Fleet dashboard says all gateways running; important partial failure is Google token despite cron `ok` on the briefing.
   - Keep checking logs/output, not just job exit status.

5. **Unblock Qwen/Todoist only when Jet wants task capture active.**
   - Current blocker: no Todoist API token at the configured local path/env.
   - Until approved, Qwen stays quiet and file/local only.

## Needs Jet

- Approve/perform Google Workspace re-auth for `trinupab@creatuscorp.net` so calendar + Work Gmail automations recover.
- Decide whether the student kit Start Here hub should be polished today as the main teaching asset.

## Quietly watching

- 09:00 daily revenue report and 15-minute Airtable payment alerts.
- Limitless Club email alerts 4x/day; currently ok.
- Notion → Obsidian sync and YouTube transcript capture; both currently ok.

## Radar protocol

Protocol note: `Agents/Hermes/Protocols/kelly-proactive-ops-radar.md`
