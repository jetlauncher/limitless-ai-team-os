# Meta Ads Manager Report — CobaltBKK

Generated: 2026-06-23 22:40 +07  
Source: local logged-in Comet Ads Manager UI  
Account: CobaltBKK (`act_10101982961107455`)  
Date range in UI: Last 30 days — May 24, 2026 – Jun 22, 2026  
Scope visible: Campaigns table, 1–200 of 250 campaigns

## Summary

- Total ad spend shown by Ads Manager: **฿63,298.17**
- Total impressions: **256,304**
- Reach: **72,212 Meta Accounts**
- Frequency: **3.55**
- CPM: **฿246.97**
- Pending draft/publish queue: **Review and publish (20)**
- Opportunity score visible: **85**

## CAC / CPA calculation

The visible Ads Manager table is optimized around **Messaging conversations started**, not final paid customers. So the reliable calculation from this screen is a **cost per messaging conversation / lead proxy**, not true paid-customer CAC.

Visible active campaigns with messaging results:

| Campaign | Results | Spend | Cost per result |
|---|---:|---:|---:|
| Sales \| Online \| 5,900฿ \| 200 | 110 | ฿6,026.83 | ฿54.79 |
| Sales \| CoWork \| LAL \| 500 >300 | 93 | ฿11,053.64 | ฿118.86 |
| Msg \| Retarget \| Short Cut \| 500 | 258 | ฿15,027.43 | ฿58.25 |
| Sales \| Private \| Carousel \| 500 | 188 | ฿15,188.93 | ฿80.79 |
| Msg \| Shortcut \| Album \| 500 > 200 | 82 | ฿6,030.86 | ฿73.55 |

Visible active subtotal:

- Visible messaging conversations: **731**
- Visible active spend: **฿53,327.69**
- Visible cost per messaging conversation: **฿72.95**

Whole-account spend divided by visible messaging conversations:

- ฿63,298.17 / 731 = **฿86.59 per visible messaging conversation**

Caution: this is conservative/noisy because **฿9,970.48** of total spend is not explained by the visible rows currently on screen. Need full export or scroll/pagination for exact all-campaign lead CPA.

## Campaign notes

### Best visible CPA
1. Sales | Online | 5,900฿ | 200 — **฿54.79 / conversation**
2. Msg | Retarget | Short Cut | 500 — **฿58.25 / conversation**
3. Msg | Shortcut | Album | 500 > 200 — **฿73.55 / conversation**

### Worst visible CPA
- Sales | CoWork | LAL | 500 >300 — **฿118.86 / conversation** on **฿11,053.64** spend.

### Highest visible spend
1. Sales | Private | Carousel | 500 — **฿15,188.93**
2. Msg | Retarget | Short Cut | 500 — **฿15,027.43**
3. Sales | CoWork | LAL | 500 >300 — **฿11,053.64**

## Drafts / operational issue

Ads Manager shows **Review and publish (20)**. Visible draft campaigns include:

- North Business Owners Leads — ฿750/day
- New English Ads - Sale - Copy — ฿600/day
- New Leads Campaign — ฿750/day
- TH 45-65 Leads - Feb 2026 — ฿500/day
- New Sales Campaign — ฿750/day
- New Awareness Campaign — using ad set budget

This is worth checking because expected changes may not be live.

## Recommendation

1. Treat current visible lead/CAC proxy as **฿72.95 per messaging conversation** for the visible active campaigns.
2. If using total account spend against visible conversations only, use **฿86.59** as a conservative proxy.
3. Do **not** treat this as true paid-customer CAC unless we join with paid customer/order data from Airtable/Stripe for the same date range.
4. Review the **20 unpublished drafts** before judging campaign performance.
5. Pull or export the full Ads Manager table for exact all-campaign CPA, including rows outside the visible viewport and purchase/ROAS columns.

## Source artifacts

- Screenshot: `/tmp/ads_manager_report_source.png`
- Active screenshot: `/tmp/ads_manager_cobalt_active.png`
