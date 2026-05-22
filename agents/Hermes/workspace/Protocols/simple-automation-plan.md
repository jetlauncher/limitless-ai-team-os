# Simple Automation Plan

## Principle
Keep it simple.

## What we are using
- **No separate dashboard first**
- **No visible multi-agent swarm first**
- **Telegram** for the important report
- **Obsidian + local files** for quiet storage
- **Airtable** as the source of truth for revenue

## Live setup
1. **Hourly Airtable snapshot**
   - runs quietly
   - stores local snapshots
   - does not spam Telegram

2. **Daily revenue report**
   - sent to Telegram at 09:00 Bangkok time
   - shows today, MTD, targets, and latest sales

## Next extension
- add selective payment alerts once hourly snapshots are stable
- then add viral X / YouTube monitoring with the same quiet-collector pattern
