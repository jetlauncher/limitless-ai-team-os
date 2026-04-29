# Client Retention Sync Run — 2026-04-27

## Status
Built and synced the first working **Client Retention** table in Airtable for Limitless Sales.

## Source tables merged
- `1. transactions`
- `Customer Data`
- `Registration by Classes`

## Airtable output
- Table: `Client Retention`
- Verified Airtable records: **925**
- Local generated rows: **925**
- Unique Client IDs: **925**

## Local outputs
- Script: `/Users/ultrafriday/.hermes/limitless/client_retention_sync.py`
- Tests: `/Users/ultrafriday/.hermes/limitless/test_client_retention_sync.py`
- JSON export: `/Users/ultrafriday/.hermes/limitless/client_retention_master.json`
- CSV export: `/Users/ultrafriday/.hermes/limitless/client_retention_master.csv`

## Verification
- Unit tests: **4 passed**
- Airtable record count verified after sync: **925**
- Duplicate Client IDs in local output: **0**
- Stale records from first sync pass pruned: **21**

## Retention stage counts
| Stage | Count |
|---|---:|
| Needs onboarding | 311 |
| Corporate potential | 293 |
| Warm upsell candidate | 158 |
| Dormant | 132 |
| VIP / high-LTV | 30 |
| New buyer | 1 |

## Data quality gaps
- Missing phone: **217** clients
- Missing email: **215** clients

## Fields generated
- Client ID
- Name
- Nickname
- Email
- Phone
- Social Name
- Company
- Courses Purchased
- Last Purchase Date
- Total Paid / LTV
- Number of Purchases
- Source Channels
- Sales Owners
- Community Joined?
- Attendance Confirmed?
- Last Touch Date
- Next Follow-up Date
- Retention Stage
- Next Best Offer
- Reason / Trigger
- Personal Notes
- Missing Info
- Data Sources
- Last Synced

## Current interpretation
The retention base is now usable by the team as a CRM/action list.

Priority actions:
1. **Needs onboarding — 311**: confirm community access, welcome message, class prep, and basic follow-up.
2. **Corporate potential — 293**: review company/tax/company-name signals and route strong accounts to B2B follow-up.
3. **Warm upsell candidate — 158**: prioritize next-best-offer outreach after attendance/class confirmation.
4. **Dormant — 132**: run reactivation campaign with useful update, alumni offer, or new workshop invite.
5. **VIP / high-LTV — 30**: personal founder/team touch, invite into premium implementation or corporate AI offer.

## Notes
- Credentials were used only from local config and were not stored in this report.
- The sync script currently rebuilds from Airtable sources and upserts into `Client Retention` by `Client ID`.
- The table can be re-synced by running:

```bash
python ~/.hermes/limitless/client_retention_sync.py
```
