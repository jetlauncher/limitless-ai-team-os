# Airtable Revenue Report Protocol

## Source of truth
- Base: `Limitless Sales`
- Table: `1. transactions`
- Main revenue field: `ยอดโอน`

## Reporting rule
Use Airtable as the official ledger because both Stripe and bank-transfer customers complete registration there.

## Default inclusion logic
Include transactions when:
- `slip date` is inside the reporting window
- `ยอดโอน` is present
- `status` indicates the payment is effectively complete

## Default exclusion logic
Exclude by default:
- obvious pending rows
- empty or zero-value rows unless Jedi later wants them counted for operational tracking
- rows that are later confirmed as duplicates

## Core report sections
### 1. Revenue today
- sum of `ยอดโอน` for today
- count of included transactions today

### 2. Month-to-date revenue
- sum of `ยอดโอน` for current month
- count of included month-to-date transactions

### 3. Target tracking
- progress to B2,000,000
- progress to B3,000,000
- remaining gap to each target

### 4. Recent sales snapshot
For latest included transactions, show:
- slip date
- customer name or chat name
- course / class
- channel
- `ยอดโอน`

### 5. Notes / anomalies
Flag:
- zero-value paid rows
- status mismatches
- rows that may need manual review

## Useful Airtable fields
- `slip date`
- `status`
- `ยอดโอน`
- `ชื่อลูกค้า`
- `ชื่อแชท`
- `channel`
- `Courses`
- `Class and date (from Classes)`
- `ช่องทางชำระเงิน`
- `Email`
- `Phone`

## Delivery recommendation
- Daily Telegram summary for revenue
- Quiet storage of raw details in Obsidian or local files
- Stripe alerts can remain separate for instant dopamine, but Airtable stays official for reporting
