# CobaltBKK Meta Ads — Full Live Pull

**Captured:** 2026-08-18 10:31 +07  
**Account:** CobaltBKK (`act_10101982961107455`)  
**Performance range:** 2026-07-19 through 2026-08-17 (Meta Ads Manager “Last 30 days”)  
**Mode:** Read-only

## Scope and reconciliation

- Ads Manager UI totals: **256 campaigns / 320 ad sets / 872 ads**.
- Published Graph inventory: **249 campaigns / 318 ad sets / 869 ads**.
- Unpublished UI drafts preserved separately: **7 campaign drafts / 2 ad-set drafts / 3 ad drafts**.
- Reconciled totals: **256 / 320 / 872**, matching Ads Manager exactly.
- Performance rows with delivery in the period: **9 campaigns / 9 ad sets / 62 ads**.
- Ads Manager also showed **Review and publish (23)**, which represents unpublished changes, not necessarily 23 distinct objects.

## KPI snapshot

| Metric | Value |
|---|---:|
| Spend | **฿88,919.78** |
| Impressions | **740,309** |
| Reach | **269,918** (live UI snapshot immediately before API pull) |
| All clicks | **25,355** |
| Calculated CPM | **฿120.11** |
| Calculated all-click CPC | **฿3.51** |
| Calculated all-click CTR | **3.42%** |
| Messaging-optimized spend | **฿78,002.94** |
| Messaging conversations from messaging campaigns | **937** |
| Blended messaging CPA | **฿83.25** |
| Tracked purchases in messaging campaigns | **39** |
| Blended tracked cost/purchase | **฿2,000.08** |

Meta’s UI snapshot was changing live during extraction; the API pull is a few seconds newer than the first UI total (a difference of ฿0.27 and 3 impressions).

## Messaging campaign performance

| Campaign | Conversations | Spend | CPA | Purchases | Cost/purchase |
|---|---:|---:|---:|---:|---:|
| Sales \| Private \| Carousel \| 750 | 318 | ฿23,090.51 | ฿72.61 | 8 | ฿2,886.31 |
| Sales \| CoWork \| LAL \| 750 | 284 | ฿21,976.30 | ฿77.38 | 8 | ฿2,747.04 |
| Msg \| Retarget \| Short Cut \| 500 | 197 | ฿19,763.55 | ฿100.32 | 5 | ฿3,952.71 |
| Sales \| Online \| 5,900฿ \| 300 | 106 | ฿7,729.56 | ฿72.92 | 16 | ฿483.10 |
| Sales Codex \| Online \| 5,900฿ \| 300 | 32 | ฿5,443.02 | ฿170.09 | 2 | ฿2,721.51 |

## Top messaging ads by volume (minimum 10 conversations)

| Ad | Campaign | Conversations | Spend | CPA |
|---|---|---:|---:|---:|
| Reel \| 8 AI Agent - Copy | Sales \| Private \| Carousel \| 750 | 164 | ฿9,853.03 | ฿60.08 |
| Reel \| 8 AI Agent | Sales \| CoWork \| LAL \| 750 | 127 | ฿6,248.45 | ฿49.20 |
| Album \| เราไม่สอนแค่ Tool | Msg \| Retarget \| Short Cut \| 500 | 88 | ฿8,006.49 | ฿90.98 |
| Single Mix \| 5,900 (Light Theme) | Sales \| Online \| 5,900฿ \| 300 | 64 | ฿4,131.24 | ฿64.55 |
| Reel \| GPT ตอบไม่ตรงใจ | Sales \| Private \| Carousel \| 750 | 53 | ฿3,656.55 | ฿68.99 |
| Album \| 22MAR25 | Msg \| Retarget \| Short Cut \| 500 | 50 | ฿5,615.40 | ฿112.31 |
| Reel \| คุณแบงค์ Maru Waffel | Sales \| Private \| Carousel \| 750 | 47 | ฿3,176.01 | ฿67.57 |

## Findings

1. **Strongest scalable campaign cluster:** `Sales | Private | Carousel | 750`, `Sales | CoWork | LAL | 750`, and historical `Sales | Online | 5,900฿ | 300` produced **708 conversations** at roughly **฿72.61–฿77.38 CPA**.
2. **Best purchase efficiency:** `Sales | Online | 5,900฿ | 300` recorded **16 purchases at ฿483.10 tracked cost/purchase**, but Ads Manager currently shows **ad sets inactive / ad errors**. Verify whether that pause is intentional before reactivating anything.
3. **Underperformer:** `Sales Codex | Online | 5,900฿ | 300` is at **฿170.09 per conversation**, about **2.0×** the blended messaging CPA, with **2 purchases at ฿2,721.51 each**.
4. **Best creative family:** `Reel | 8 AI Agent - Copy` produced **164 conversations at ฿60.08**, while `Reel | 8 AI Agent` produced **127 at ฿49.20**. Together: **291 conversations on ฿16,101.48 spend (฿55.33 blended CPA)**.
5. **Efficient secondary concept:** `Reel | อายุไม่สำคัญ` had variants below **฿60 CPA**, including one retargeting variant at **฿42.90** on 18 conversations.
6. **Retargeting is mixed:** `Msg | Retarget | Short Cut | 500` delivered **197 conversations at ฿100.32 CPA** overall; good individual creatives are being diluted by weaker variants.
7. **Measurement gap:** 39 purchases are tracked, but this pull does not include purchase value/revenue. Do not infer ROAS or profitability from purchase count alone; reconcile with sales/CRM revenue before aggressive scaling.
8. **Account hygiene:** Ads Manager shows `Review and publish (23)`, 12 unpublished draft objects, and at least one no-ads campaign. Clean these deliberately after review; this pull made no changes.

## Recommended next actions (no changes made)

- Protect budgets on the three efficient messaging campaigns while checking downstream lead quality.
- Review `Sales Codex` creative/audience/offer path before further spend; pause or cap only after confirming lead quality.
- Build new controlled variants around the `8 AI Agent` and `อายุไม่สำคัญ` concepts rather than replacing the winners.
- Inspect the inactive/error state on `Sales | Online | 5,900฿ | 300`; it has the best tracked purchase efficiency.
- Join Meta purchase events to Airtable/actual revenue to calculate true CAC and ROAS.

## Files

- `meta-insights-2026-07-19-to-2026-08-17.json` — full raw performance payload.
- `performance-campaigns-...csv`, `performance-adsets-...csv`, `performance-ads-...csv` — flattened performance data.
- `inventory-campaigns.json`, `inventory-adsets.json`, `inventory-ads.json` — published object inventory.
- `published-campaigns.csv`, `published-adsets.csv`, `published-ads.csv` — flattened published inventory.
- `inventory-unpublished-drafts.json` — UI-only draft objects and reconciliation.
- Original Meta export: `/Users/ultrafriday/Downloads/Co-altBKK-Campaigns-Jul-19-2026-Aug-17-2026.csv`.
