# Client Retention Airtable Audit — 2026-04-27

Purpose: quick completeness audit for building a retention system for existing Limitless clients.

Source: Airtable base `Limitless Sales`. No raw customer PII included in this note.

## Executive Summary

The data is usable for a retention system, but it is **not cleanly complete in one place yet**.

- `1. transactions` is strong for revenue, product/class, payment date, status, channel, and staff.
- `Customer Data` is much stronger for email, social name, class, company/tax info, and student details.
- `Registration by Classes` is strong for actual attendee-level contact info.
- Client contact data is fragmented across transaction/customer/registration/student tables.
- The main missing pieces for retention are: normalized customer ID, phone/LINE completeness, engagement state, follow-up owner, next best offer, and follow-up cadence.

## Tables Checked

### `1. transactions`
Records: 621

Strengths:
- Buyer/name proxy: 100.0%
- Course/class: 99.8%
- Amount (`ยอดโอน`): 97.1%
- Status: 100.0%
- Payment date: 100.0%
- Source channel: 98.9%
- Owner/staff: 97.7%

Gaps:
- Direct phone: 1.9%
- Direct email: 1.9%
- Company/accounting info: 53.6%
- Retention notes: 35.9%
- LINE joined flag: 3.1%
- Call confirmed flag: 3.1%

Interpretation:
- This table is excellent for revenue history and purchase segmentation.
- It should not be the only source for retention outreach because direct contact fields are mostly empty here.

### `Customer Data`
Records: 646

Strengths:
- Payer/name: 99.5%
- Payer email: 99.1%
- Student name: 96.9%
- Student email: 99.5%
- Company/tax info: 89.9%
- Class: 99.7%
- Social name: 99.7%

Gaps:
- Payer phone: 57.7%
- Student phone: 54.0%
- Sales owner: 1.2%

Interpretation:
- This is likely the best starting point for a client master/contact table.
- Needs better phone/LINE/owner enrichment for retention operations.

### `Registration by Classes`
Records: 518

Strengths:
- Name: 96.1%
- Phone: 90.2%
- Email: 91.1%
- Course/class: 96.9%

Gaps:
- Company: 55.4%
- Notes: 16.0%
- No revenue/status fields here

Interpretation:
- This is best for attendee-level follow-up because it has stronger phone/email coverage.

### `realtime slips 1 (latest update 30 Jan 26)`
Records: 580

Strengths:
- Name: 99.5%
- Course: 99.3%
- Status: 99.7%
- Amount: 93.6%

Gaps:
- Phone: 0.2%
- Email: 0.2%
- Company: 40.7%
- Notes: 26.4%

Interpretation:
- Useful for older payment/product history, not enough for outreach by itself.

### `Attendees`
Records: 28

Strengths:
- Name/phone/email/course: 92.9%

Interpretation:
- Looks like a newer/cleaner schema, but currently low record count.

### `Orders`
Records: 1

Interpretation:
- Looks like a newer order/checkout structure but is not populated enough yet.

## Retention-Critical Fields We Need

Minimum viable client master:

1. Client / buyer name
2. Attendee name(s)
3. Email
4. Phone
5. LINE / social handle
6. Company
7. Purchased course(s)
8. Purchase date(s)
9. Amount paid / LTV
10. Source channel
11. Sales owner / account owner
12. Class attended / attendance status
13. Community status: joined LINE/Skool or not
14. Feedback / satisfaction / objections
15. Next best offer
16. Follow-up stage
17. Next follow-up date
18. Last touch date
19. Notes / personal context
20. VIP / high-LTV flag

## Current Completeness Verdict

Data is **partially complete**:

- Good enough to build a revenue-based customer segmentation engine.
- Good enough to identify many existing clients and what they bought.
- Not yet complete enough for a reliable always-on retention CRM without unifying tables and filling contact/follow-up fields.

Biggest gap:
- Contact and relationship data are spread across multiple tables.
- `1. transactions` has almost no direct phone/email, while `Customer Data` and `Registration by Classes` have much better contact coverage.

## Recommended Retention System

Create a new Airtable table: `Client Retention` or `Client Master`.

Suggested fields:

- `Client ID` — normalized key from email/phone/social/payment code
- `Name`
- `Nickname`
- `Email`
- `Phone`
- `LINE / Social Name`
- `Company`
- `Courses Purchased`
- `Last Purchase Date`
- `Total Paid / LTV`
- `Number of Purchases`
- `Source Channel`
- `Sales Owner`
- `Community Joined?`
- `Attendance Confirmed?`
- `Last Touch Date`
- `Next Follow-up Date`
- `Retention Stage`
  - New buyer
  - Attended class
  - Needs onboarding
  - Warm upsell candidate
  - VIP / high-LTV
  - Dormant
  - Needs save / support
- `Next Best Offer`
- `Reason / Trigger`
- `Personal Notes`
- `Feedback Summary`

## First Automation Ideas

1. **Post-purchase onboarding**
   - Trigger: new paid transaction
   - Action: ensure client is in client master, check contact completeness, remind team if missing phone/LINE/community status.

2. **Class completion follow-up**
   - Trigger: class date passed or attendance confirmed
   - Action: send/check feedback, ask what they implemented, offer relevant next step.

3. **Next-best-offer detection**
   - Trigger: course purchased but missing natural next course
   - Example: Shortcut AI → Creative AI / Advanced AI / OpenClaw depending on profile.

4. **Dormant client reactivation**
   - Trigger: no purchase/touch for 30/60/90 days
   - Action: personalized check-in or value drop.

5. **VIP care list**
   - Trigger: high LTV, multiple seats, company buyer, corporate potential
   - Action: human touch from Jet/team, not generic broadcast.

## Immediate Next Step

Build a one-time `Client Master` sync script that merges:

- `1. transactions` for revenue/purchases/source/staff
- `Customer Data` for payer/student email/social/company/class
- `Registration by Classes` for attendee phone/email/class attendance

Then generate:

- Top client list by LTV
- Missing-contact cleanup list
- Warm upsell candidates
- Dormant customer list
- VIP relationship list
