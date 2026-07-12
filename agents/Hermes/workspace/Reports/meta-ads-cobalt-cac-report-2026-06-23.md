# CobaltBKK Meta Ads → Airtable CAC Report

Generated: 2026-06-23 22:45 +07  
Ads source: Meta Ads Manager local Comet UI  
Customer/revenue source: Airtable `Limitless Sales` → `1. transactions`  
Date window matched to Ads Manager: **2026-05-24 through 2026-06-22**  
Ad account: **CobaltBKK / act_10101982961107455**

## Headline

- Meta Ads spend: **฿63,298.17**
- Airtable paid records in same period with channel `fb`: **29**
- Student/seat count from those `fb` paid records: **38**
- Revenue from those `fb` paid records: **฿627,705.17**
- ROAS proxy: **9.92x**

## CAC

Two useful versions:

| Metric | Formula | Result |
|---|---|---:|
| CAC per paid transaction/customer record | ฿63,298.17 / 29 | **฿2,182.70** |
| CAC per student/seat | ฿63,298.17 / 38 | **฿1,665.74** |

Use **฿2,182.70** if you mean paying customer/order.  
Use **฿1,665.74** if you mean student/seat acquired.

## Revenue efficiency

| Metric | Formula | Result |
|---|---|---:|
| Revenue per paid `fb` record | ฿627,705.17 / 29 | **฿21,645.01** |
| Revenue per student/seat | ฿627,705.17 / 38 | **฿16,518.56** |
| ROAS proxy | ฿627,705.17 / ฿63,298.17 | **9.92x** |

## Airtable paid-channel breakdown for same period

Only rows with positive `ยอดโอน` and no pending/cancel/refund status were included.

| Channel | Paid records | Revenue | Seats |
|---|---:|---:|---:|
| upsell | 33 | ฿1,454,691.34 | 65 |
| line oa | 30 | ฿710,241.12 | 30 |
| fb | 29 | ฿627,705.17 | 38 |
| pjedi | 2 | ฿75,300.00 | 2 |
| Note | 1 | ฿24,514.00 | 1 |

## Caveat

Airtable uses `channel = fb`, which I am treating as the paid-ads/customer-source proxy. If `fb` mixes paid ads and organic Facebook/manual sales, this is a blended Facebook CAC, not a perfect Meta Ads platform-attributed CAC.

For a stricter report, Airtable needs either UTM fields, campaign/adset IDs, or a separate `source_type = paid_ad / organic / referral` field.

## Operational note

Ads Manager also shows **Review and publish (20)** pending draft changes. That should be reviewed separately because unpublished changes may affect forward-looking performance but not this historical CAC window.
