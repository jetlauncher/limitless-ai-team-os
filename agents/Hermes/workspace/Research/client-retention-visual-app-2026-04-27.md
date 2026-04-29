# Client Retention Visual App — 2026-04-27

## Status
Built and launched a visual web app for the Airtable `Client Retention` table.

## Local app
- Script: `/Users/ultrafriday/.hermes/limitless/retention_app_server.py`
- Tests: `/Users/ultrafriday/.hermes/limitless/test_retention_app_server.py`
- Local URL: `http://127.0.0.1:8770/retention`
- Health: `http://127.0.0.1:8770/health`
- Background session at creation: `proc_16d0da878f68`

## Public/mobile tunnel
- Cloudflare Quick Tunnel started for the retention app.
- Public URL at run time: `https://poison-retrieve-enemies-spoken.trycloudflare.com/retention`
- Health check returned HTTP 200.
- Background tunnel session at creation: `proc_da1d44c2d274`

## Authentication
- Uses the existing Mission Control key cookie and passcode flow.
- Airtable tokens stay server-side and are not exposed to the browser.
- Public route goes to `/login` if not authenticated.

## Features built
- Premium Apple-style visual dashboard
- Live Airtable read from `Client Retention`
- KPI cards:
  - total clients
  - total LTV
  - VIP / high-LTV count
  - missing phone count
  - missing email count
- Retention board with:
  - search
  - stage filter
  - next-offer filter
  - priority / LTV / follow-up sort
- Stage map bar chart
- Priority queue
- Client detail drawer
- Editable fields saved back to Airtable:
  - `Retention Stage`
  - `Next Follow-up Date`
  - `Last Touch Date`
  - `Next Best Offer`
  - `Personal Notes`
  - `Sales Owners`
  - `Community Joined?`
  - `Attendance Confirmed?`
- Full sync button that runs `/Users/ultrafriday/.hermes/limitless/client_retention_sync.py`

## Verification
- Tests passed: `3 passed`
- Syntax check passed: `python3 -m py_compile ~/.hermes/limitless/retention_app_server.py`
- Local health passed
- API verified against Airtable:
  - items: 925
  - total clients: 925
  - total LTV: ฿8,429,830
- Public Cloudflare health passed: HTTP 200
- Browser visual check passed: dashboard rendered with live data, filters, KPIs, stage map, priority queue.

## Run commands
Start local app:

```bash
python3 -u ~/.hermes/limitless/retention_app_server.py
```

Run tests:

```bash
pytest -q ~/.hermes/limitless/test_retention_app_server.py
```

Start a public tunnel:

```bash
cloudflared tunnel --no-autoupdate --url http://127.0.0.1:8770
```

## Notes
- Quick Tunnel URLs are ephemeral; restart tunnel if the public link dies.
- Do not put Airtable token, Mission Control key, or dashboard passcode into chat or docs.
