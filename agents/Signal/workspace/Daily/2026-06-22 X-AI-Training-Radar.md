# Signal X AI Training Radar — 2026-06-22

## Status: NO SIGNAL (all collection paths down)

No major signal worth interrupting you for.

### Collection path status
| Path | Status | Detail |
|------|--------|--------|
| x_search (xAI OAuth) | ❌ Disabled | API endpoint returns HTTP 400 |
| xurl bookmarks/search | ❌ Credits depleted | Account 1861030322831581184 has no credits |
| Nitter RSS feeds | ❌ Empty bodies | All 8 accounts (OpenAI, AnthropicAI, xai, GoogleDeepMind, sama, karpathy, rowancheung, demishassabis) return 200 with zero-body response |
| web_search / FIRECRAWL | ❌ Not configured | No API key set |
| Grok API-key mode | ⚠️ Not requested in this run | Cron prompt did not include xai-api-key config path |

### Watch for next run
- **Nitter infrastructure** appears to be returning empty responses — possible instance shutdown, DDOS mitigation at Caddy level, or rate-limiting. If persistent, switch to alternative RSS (if available) or add a Nitter mirror list rotation in the context script.
- **xurl credits replenish?** When Jet adds credits, re-enable xurl bookmarks as the first collection path.
- **x_search HTTP 400** — endpoint may have changed; could be a rate-limit window (usually resets after ~24h).

### Last meaningful signals (from daily X-Monitor notes)
Yesterday's note had 0 new items because candidates were stale or empty. The two most recent useful signals:
- **@OpenAI — GPT-5.5 Instant** (2026-06-19): Near-premium medical reasoning on free tier → Thai clinic/pharmacy owners can embed as 24/7 triage co-pilot.
- **@AnthropicAI — Claude Corps program** (2026-06-11): Subsidizing AI-skilled talent in mission-driven orgs → Thai SMEs can replicate with university partnerships for part-time AI-fluent support.

### Recommendation
Next run: If Nitter remains empty, try a different approach path such as:
1. Add `provider=xai-oauth` model flag if Hermes cron supports it
2. Manually fetch a curated account's page via browser tool
3. Temporarily use any available RSS source (Hacker News AI feed, etc.)
