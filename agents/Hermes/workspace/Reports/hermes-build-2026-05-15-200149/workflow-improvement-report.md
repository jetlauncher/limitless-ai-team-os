# Hermes Workflow Improvement Report

Generated: 2026-05-15 20:05

## Executive Summary

The Hermes fleet is mostly healthy. All nine profiles are running, Context7 MCP is enabled across the fleet, and model-routing smoke tests passed. The next highest-leverage work is not more agents, but clearer control surfaces: a dashboard, a visual capability map, a repair pass for one blocked cron, and a reusable Business Agent OS template.

## What is healthy

- Kelly/default, Blaze, Bolt, Kaijeaw, Pixel, Protocol, Qwen, Signal, and Zegna gateways are running.
- Context7 MCP is enabled on every profile.
- Qwen local profile smoke test passed on `qwen3.6:35b`.
- Revenue, payment alerts, Notion sync, Gmail, and daily briefings are active.
- Specialist ownership is clear: Kelly ops, Signal research, Blaze content, Pixel visuals, Bolt builds, Kaijeaw Thai, Zegna taste, Qwen local worker, Protocol newsletter.

## Issues to fix

1. **Fixed blocked X daily report**
   - Job: `limitless-x-daily-report`
   - Fix: script now strips zero-width Unicode before handing output to the agent.
   - Verification: manual cron run at 20:08 finished `ok`.

2. **Reduce Telegram delivery fragility**
   - Signal X scan had `cannot schedule new futures after interpreter shutdown`.
   - Action: rerun after gateway restart, and consider local-first delivery with explicit alerts only for high signal.

3. **Prune storage**
   - Data volume: 85% used.
   - `~/.hermes`: 109G.
   - Action: prune old sessions, logs, cache, generation artifacts, and profile backups after a backup check.

4. **Pixel image generation dependency**
   - Log: `FAL_KEY environment variable not set`.
   - Action: either configure FAL or route Pixel image generation through Higgsfield/OpenAI image workflow.

## Build roadmap

### Phase 1: Visual clarity
- Hermes Capability Map.
- Agent Fleet Dashboard.
- Workflow Improvement Report.

### Phase 2: Operating system packaging
- One playbook per agent.
- Shared routing matrix.
- Approval gates for social/email/deploy/revenue actions.
- Business Agent OS starter template.

### Phase 3: External story
- Landing-page section: “This is what an AI Team OS looks like.”
- 60–90 sec demo video.
- Client/student reusable package.

## Recommended next actions

1. Turn the static dashboard into a lightweight daily HTML snapshot from cron/profile status.
2. Investigate Signal delivery failure and decide Pixel image backend.
3. Add one-click export: dashboard + report to PNG/PDF.
4. Write agent playbooks into Obsidian and mirror executive summaries to Notion.
5. Build the Business Agent OS template once the fleet dashboard is stable.
