# Daily Agent Fleet Dashboard

## Purpose

Daily operational snapshot for Jet's Hermes / AI Team OS fleet.

The dashboard checks:

- Hermes profile gateway status
- Context7 MCP availability
- active/paused cron counts
- recent relevant gateway/log warning lines
- active cron error status
- basic disk/system notes

## Schedule

- Cron job: `daily-agent-fleet-dashboard-snapshot`
- Job ID: `a460e04ab88b`
- Schedule: `45 7 * * *` Bangkok time
- Delivery: Telegram origin chat
- Mode: `no_agent=true`, script stdout delivered directly
- Script: `~/.hermes/scripts/agent_fleet_dashboard_snapshot.py`

## Output paths

Daily snapshots are saved under:

`~/Documents/Obsidian Vault/Agents/Hermes/Dashboards/Agent Fleet/YYYY-MM-DD/`

Current pointers:

- `current.html`
- `current.png`
- `current.pdf`

Latest verified run:

- Date: 2026-05-15
- Gateways: 9/9
- Context7: 9/9
- Active jobs: 31
- Active cron errors now: 0

## Watchlist logic

The headline `active cron errors now` only reflects active cron status. The watchlist may still surface recent historical/non-blocking warnings from logs, such as:

- Telegram/network reconnect warnings
- old provider/API auth errors that should be monitored if they recur
- Pixel `FAL_KEY` missing if native image generation is expected

## Maintenance notes

If the dashboard fails:

1. Run manually:
   ```bash
   python3 ~/.hermes/scripts/agent_fleet_dashboard_snapshot.py
   ```
2. Check cron:
   ```bash
   hermes cron list --all | grep -A12 daily-agent-fleet-dashboard-snapshot
   ```
3. Check gateway scheduler:
   ```bash
   hermes cron status
   ```
4. If paths change, update `BASE` and `VAULT` in the script.

Do not print or store secrets in generated dashboard artifacts.
