# Jet - Top 5 Next Actions Radar

Updated: 2026-05-22 08:17 +07
Owner: Kelly / Hermes

## Current Top 5 — 2026-05-22

1. **Revenue:** Push today’s sales pipeline toward the B3M gap: MTD is THB 2,031,827.71 / 3M, today is still THB 0 at 08:17; latest sales came from FB/IG/upsell yesterday.
2. **Blocker:** Re-auth the personal Gmail token for `jeditrinupab@gmail.com`; morning briefing and inbox-zero both show `invalid_grant`, and the inbox-zero job partly failed while still archiving work-mail items.
3. **Agent health:** Fix two local scanner state-write failures: workspace digest and personal artifacts scan hit `OSError: [Errno 11] Resource deadlock avoided` in Obsidian/iCloud state JSON files.
4. **Memory hygiene:** Pixel and Protocol still have no 2026-05-22 daily note; Qwen’s earlier audit overstated gaps because several agents recovered later, but these two remain stale.
5. **Content/teaching:** Convert Signal’s 08:00 AI training radar into one Blaze-ready teaching/content piece: “AI quality comes from connected systems + feedback loops, not prompts alone.”

## Needs Jet

- Approve/perform Gmail re-auth for the personal account when convenient; Kelly should not overwrite or move tokens without approval.
- Decide whether today’s main content angle should be “systems connected to AI” or “feedback loops beat prompting.”

## Quietly watching

- Revenue scripts, payment alerts, Mission Control health, morning briefing, and Signal radar are currently running OK.
- Qwen Todoist fetch is healthy but found 0 matching tasks; needs a labeled/prefixed test task before relying on it.
- Qwen X-Radar output files are still 1 byte each, so that local radar path needs repair but is not customer-facing.

## Evidence checked

- `hermes cron list --all` at 2026-05-22 08:17 +07.
- `hermes profile list`: active gateways running for default, Blaze, Bolt, Kaijeaw, Oracle, Pixel, Protocol, Qwen, Signal, Zegna, and others.
- `limitless_daily_revenue.py`: MTD THB 2,031,827.71, 82 MTD transactions, latest five sales on 2026-05-21.
- Daily notes: Hermes, Blaze, Bolt, Kaijeaw, Qwen, Signal, Zegna, Oracle present; Pixel and Protocol missing today.
