# Revenue Reporting Rule

## Official rule
For revenue reporting, use:
- Airtable base: `Limitless Sales`
- Table: `1. transactions`
- Amount field: `ยอดโอน`

## Why
This is the best source of truth because both Stripe and bank-transfer customers complete registration in Airtable.

## Practical interpretation
- Stripe is useful for immediate payment alerts
- Airtable is the official reporting ledger
- Small mismatches can be reviewed, but Airtable remains primary

## Current stance
The April 2026 total based on `ยอดโอน` is close enough to the expected business number to use as the reporting basis.
