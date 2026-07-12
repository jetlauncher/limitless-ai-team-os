# AI Content Team by Limitless - Internal SaaS Operating Model

Date: 2026-07-06
Repo: `/Users/ultrafriday/Projects/limitless-content-engine-internal`

## Product decision
Build this first as an internal SaaS/operator console that Kelly, Blaze, and Jet can run. Do not start with a public self-serve dashboard.

## Why internal first
- Premium offer needs QA and taste.
- Customer source material can be messy.
- Jet's hourly rate and brand imply high-touch outcomes.
- The repeated workflow needs to be observed before automation gets hardened.

## Internal app v0
The v0 app tracks:
- Client accounts
- Pricing tier
- MRR snapshot
- Intake/source status
- Voice calibration progress
- Weekly pipeline stage
- QA and delivery status

## Automation ladder
1. Manual client creation
2. Form/LINE intake creates account automatically
3. Source material creates voice map draft
4. Weekly cron generates content package draft
5. QA checklist blocks delivery until approved
6. Approved delivery posts to Notion/Google Doc and notifies customer
7. Feedback updates next week's voice profile

## Premium guardrails
- Pricing starts at ฿15K/mo.
- Core product is ฿25K/mo.
- Flagship is ฿50K/mo.
- No cheap public tier.
- No assets generated without customer source material.
- No social posting without explicit approval.

## Next build sprint
- Add persistence with SQLite/D1/Supabase.
- Add operator auth.
- Add file/source upload.
- Add Notion/Google Docs delivery connector.
- Add a weekly package generation script wired to the existing Jet content-engine workflow.
