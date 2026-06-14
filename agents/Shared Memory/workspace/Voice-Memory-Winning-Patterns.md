# Voice Memory — Winning Patterns

> **Auto-maintained by:** Weekly Self-Improve Loop (`weekly-content-self-improve` scheduled task, Sundays 11 PM Bangkok)
> **Read by:** Daily Content Mining task (`daily-content-mining-linkedin-x`, 2 AM Bangkok) at Step 2.5
> **Purpose:** Closed-loop feedback. Daily mining biases scoring toward patterns that have performed well in the last 7 days of Blotato data.

---

## CURRENT WEEK PATTERNS

**Week of:** 2026-06-07 to 2026-06-14
**Posts analyzed:** 24 X + 5 LinkedIn (29 published via Blotato)
**Published successfully:** 29 (24 X, 5 LinkedIn)
**Failed:** 0
**Metrics availability:** partial — X full (24/24); LinkedIn unavailable (Apify actor `apimaestro/linkedin-profile-posts` returned "Wrong input or unknown error" on both attempts; LI impressions aren't publicly scrapeable without owner login)
**Avg Engagement Rate %:** X 1.92% (simple) / 2.09% (weighted) | LinkedIn n/a

> ⚠️ **STILL A LOW-REACH WEEK — READ THIS FIRST.** X reach remains tiny (19–115 impressions/post, 1,148 total, median 42). Engagement is 0–3 actions per post. Theme/hook ER deltas are second-order noise on these denominators. **The bottleneck is still distribution/reach on X, not theme selection.** Reach did grow ~4x vs last week (1,148 vs 289 total impressions) — partly more posts (24 vs 12), partly bigger top posts (115/103/101 views). Apply biases below as gentle leans only.

> 🔁 **BIGGEST REAL SIGNAL THIS WEEK: EN overtook TH.** EN 2.46% / TH 1.38% (12 vs 12 posts), and all three top-reach posts were EN (115, 103, 101 views). This reverses last week's slight TH edge. Direction is consistent across the full EN set, so treat as a soft real signal, not pure noise: English news-reaction posts are currently pulling more reach on X.

### Top-performing themes (use more — LOW/MED confidence)
1. Tool vs Workflow — avg ER 3.16% (n=4) | best: Cloudflare MiniMax gateway 4.92%, Vercel Conductor 3.92%. Consistent top theme 2 weeks running.
2. Operating System — avg ER 3.02% (n=3) | best: "company memory ที่ไหน" 5.13%, JetBrains Mellum2 3.92%. Also top-3 last week.
3. Authority vs Volume — 5.26% (n=1) | "AI content ราคาถูกลง authority". Single post, high ER but tiny reach (19) — watch, don't over-weight.

### Top-performing hook patterns (use more — LOW confidence)
1. Question Swap — avg 2.17% (n=7) — reliable workhorse, highest-volume winning hook.
2. Contrarian Claim — avg 1.96% (n=9) — the default hook this week; steady, not spiky.
3. Hidden Feature — 3.92% (n=1) — only one post, promising, needs more samples.

### Underperforming patterns (deprioritize — LOW confidence)
- Knowledge Loop theme — 0% across 3 posts (100 views, 0 eng) this week. Was a top-3 theme LAST week → likely noise/reversal, but stop over-indexing on it.
- Human Skills theme — 0% (n=1, 54 views). One data point.
- Governance theme — heavy volume (n=6) but low (1.45% avg). Over-produced relative to payoff; trim the count, not the theme.
- Comparison + Direct Address hooks — 0% but n=1 each; ignore as noise.

### Format winners
- **LinkedIn:** 5 LI posts fired (strong cadence) but metrics unavailable this run — fix the Apify LI actor input or add an owner-login impressions pull. No read again this week.
- **X singles:** 23 singles, ER ~1.9% on micro-reach.
- **X threads:** 1 thread ran ("Five questions every CEO", head = 115 views/2.61%). ⚠️ Thread TAILS died — 4/5 and 5/5 tweets got only 12–13 views vs 115 on the head. Thread format is leaking reach on the tail. Either tighten threads to 2–3 tweets or keep value front-loaded in the head.
- **EN vs TH:** EN 2.46% > TH 1.38%. EN carrying reach this week (see signal box).

### Source folder winners
- **Signal** 2.16% (n=8) edged **Oracle** 1.80% (n=16) this week — reverses last week's Oracle lean. Signal sourced the top-reach EN posts (DeepMind Co-Scientist 101v, the CEO thread head 115v). Both folders are within noise; lean Signal very slightly.

### Posting time observations (recency-caveated)
- **Best day:** Sunday 2026-06-07 — ER 2.85% (4 posts, 216 views).
- **Worst day:** Friday 2026-06-12 — ER 1.25%, BUT Friday holds the freshest posts (still accumulating at scrape time) plus the dead thread tails. Recency-depressed, not a quality signal.
- Midweek (Mon–Wed) steady ~2%. Best individual reach landed Sun 14:00 and Fri 14:00 (EN posts).

### Scoring bias for next week (applied by daily 2 AM task — GENTLE, low confidence)
- **Boost themes (+soft):** Tool vs Workflow, Operating System. (These are now 2-week-consistent winners.)
- **Cut themes (−soft):** trim Governance volume (over-produced, n=6, low payoff). No hard cuts.
- **Boost hooks (+soft):** Question Swap, Contrarian Claim.
- **Cut hooks:** none hard. Comparison/Direct Address inconclusive (n=1).
- **Language mix:** shift toward EN slightly — bump EN ratio to ~55–60% on X next week and re-test, since EN is pulling reach. Keep TH strong on LinkedIn (Jedi's TH LI posts are long-form authority and likely his real conversion engine even if unmeasured).
- **Format adjustment:** keep X singles dominant; keep ~1 thread/week BUT cap at 2–3 tweets and front-load the payoff (tails are invisible). Keep 5 LinkedIn/week — cadence is good.
- **Source weighting:** Signal ≈ Oracle; lean Signal a hair.
- **Overarching priority (strategy flag, not a scoring bias):** REACH is still the #1 constraint. Total X impressions are ~1.1k/week. Until distribution grows, theme/hook mining is second-order. Real levers: the EN reach advantage, reply/engagement activity, cross-channel pull from LinkedIn/IG to X, and getting LinkedIn metrics measurable.

---

## STRUCTURE (filled by weekly loop)

### Top-performing hooks (last 7 days)
*Hook patterns with highest engagement, ranked.*

### Top-performing themes (last 7 days)
*Content themes (e.g. governance, knowledge loop, custom GPT) ranked by composite engagement.*

### Underperforming patterns (deprioritize)
*Themes/hooks that flopped — daily mining should reduce weight on these.*

### Format winners
*LinkedIn vs X performance, EN vs TH performance, thread vs single, etc.*

### Day-of-week + time-of-day patterns
*When does Jedi's audience actually show up?*

---

## SCORING BIAS RULES (applied by daily mining task)

When the daily mining task scores candidate posts, apply these biases (default = no bias on first run):

- **Theme bias multiplier:** Themes in "Top-performing" get +1 to leverage score. Themes in "Underperforming" get -1.
- **Hook bias multiplier:** Hooks matching top-performer patterns get +1 to confidence score.
- **Format mix:** If a format underperforms, reduce its quota for the next week (e.g. drop X threads from 2 to 1 if threads flop).

---

## HISTORICAL ARCHIVE

*Each week's snapshot appended below by the self-improve loop. Latest at top.*

### Week of 2026-05-24 to 2026-05-31
- **Posts:** 12 X + 1 LinkedIn. Published 13, failed 0. Metrics: X full, LI unavailable.
- **Avg ER:** X 2.55% simple / 2.77% weighted. Reach tiny (289 total impressions, 8–39/post). Only 4/12 posts drew engagement.
- **Top themes (low conf):** Tool vs Workflow (~8.9%), Operating System (~8.2%), Knowledge Loop (~7.1%).
- **Top hooks:** Direct Address (9.09%, n=1), Question Swap (~6.9%), Contrarian Claim (7.69%, n=1).
- **Underperformers:** Shock Stat hook (0% on 2 posts), Governance×Shock-Stat combo.
- **EN vs TH:** TH 2.97% > EN 2.14% (edge, noise). **→ reversed the next week (EN took the lead).**
- **Source:** Oracle slightly ahead of Signal. **→ also reversed next week (Signal edged Oracle).**
- **Format:** all singles; 0 threads (recommended starting a thread baseline → done in 06-07 week).
- **Verdict:** reach is the constraint; theme/hook deltas = noise. Same conclusion held in the 06-07 week.

### Week of pre-2026-05-24 (pre-loop)
*No snapshot — CURRENT WEEK PATTERNS was an empty placeholder before the first self-improve run. The week of 2026-05-24 → 05-31 is the first real data capture.*
