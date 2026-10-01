# AI Cost Receipt Reconciliation — 2026-08-15

## Scope
- 8 user-supplied scanned PDFs
- 45 pages OCR'd with Apple Vision (Thai + English)
- 33 attached expense documents cross-referenced to the existing 2026 AI-cost ledger
- 15 net-new AI/agent expense entries
- 13 already-existing entries enhanced with voucher/card-conversion evidence
- 5 non-AI or internal business expenses excluded from the AI-cost total

## Updated verified totals through 2026-08-15
- Net USD ledger: **$10,505.32**
- Direct THB ledger: **฿54,397.68**
- Planning estimate at flat ฿34/USD: **฿411,578.56**
- More accurate hybrid total (exact card THB where stated; ฿34/USD fallback otherwise): **฿412,996.18**
- Jan–Aug budget: **฿400,000.00**
- Hybrid budget usage: **103.25%**
- Hybrid amount over budget: **฿12,996.18**

## What the new PDFs added
- Net-new USD expenses: **$3,110.45**
- Net-new direct THB payments: **฿29,323.58**
- Actual THB represented by the 15 new entries: **฿136,131.63**

Net-new vendors/products include Google Cloud payments, Nous Research, Kimi, 1of10, Eden Studio/Creator Bootcamp, ChatGPT Pro (work account), Lindy, Railway, Adrian Viral AI Marketing, and AI for Non-Techies.

## Voucher validation
Seven vouchers reconcile exactly to their attached expense documents.

**Mismatch:** `PV0000020260815-00006`
- Voucher total / voucher line sum: **฿9,150.40**
- Attached documents sum: **฿9,162.66**
- Difference: **฿12.26**
- Cause: Firecrawl invoice `LJPDSX9S-0003`, receipt `2922-1322`, states **฿310.16**; the voucher records **฿297.90**.

## Excluded from AI-cost totals
- Visualize Value annual membership
- Lifestyle Founders membership
- Limitless Club+ subscriptions (two entries)
- Million Dollar Coach Black Belt deposit

## Evidence gaps still requiring follow-up
1. Paid receipt for 1of10 invoice `D2408F6B-62762` — **$35.00**. The supplied vendor page still says amount due; reimbursement voucher supports the company cash expense.
2. Paid receipt for 1of10 invoice `D2408F6B-63902` — **$89.00**. Same evidence limitation.
3. ChatGPT Business paid invoice for Jedi Enterprise, six seats.
4. August ChatGPT Pro renewal receipt, if charged.
5. Apify invoice `#202604220287` payment confirmation, if it was paid.
6. Any paid Cursor/Anysphere receipt from a different inbox/card.
7. Confirmation that the **฿100 Google AI refund** posted.
8. Card-statement confirmation for the two separate **$10.70 OpenAI API funding charges** received 19 seconds apart on 2026-02-03.

## Files
- `final_ai_cost_ledger_updated.csv` — complete transaction ledger
- `final_ai_cost_ledger_updated.json` — JSON copy
- `received_receipt_crosswalk.csv` — all 33 attached documents and match/exclusion status
- `received_receipt_crosswalk.json` — JSON copy
- `voucher_validation.json` — voucher arithmetic and mismatch status
- `hybrid_thb_summary.json` — exact/fallback THB summary

## Live Google Sheet status
The canonical Google Sheet remains unchanged because Google Sheets API writes return HTTP 403. Do not claim the live tracker is updated until a write and read-back verification succeeds.
