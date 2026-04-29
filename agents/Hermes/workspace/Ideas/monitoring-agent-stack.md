# Monitoring Agent Stack

## Brief summary
Jedi wants a small set of monitoring agents that watch business signals, store raw findings without flooding Telegram, and surface only the best summaries or revenue alerts.

## Main goal
Build an operator dashboard layer across content, revenue, leads, ads, schedule, and teaching prep.

## Recommended system design
Use a 3-layer model:

1. **Collector agents**
   - Run often
   - Gather raw data
   - Save results to files, notes, or databases
   - Do not spam Telegram

2. **Analyst agents**
   - Review collected data
   - Score relevance
   - Summarize only what matters
   - Turn noisy signals into usable insight

3. **Alert agents**
   - Send Telegram messages only for high-value events
   - Examples: new sale, unusual revenue spike, exceptional viral post, urgent schedule prep

## What Hermes can help with

### 1. Viral AI post and video monitoring
**Goal:** Find X posts and YouTube videos on AI that are starting to pop off, then convert them into content opportunities for Jedi's Thai non-technical business-owner audience.

**Best setup:**
- Collector runs hourly for X and several times daily for YouTube
- Store raw hits in Obsidian or a local folder/database
- Analyst reviews relevance for:
  - business-owner usefulness
  - non-technical clarity
  - repurpose potential for YouTube / LinkedIn / school community
- Alert agent sends only top picks to Telegram

**What Hermes can do:**
- build the collection workflow
- score posts against Jedi audience fit
- summarize the gist in plain language
- suggest Jedi-angle versions of the topic

### 2. Stripe payments + Airtable student registrations
**Goal:** Real-time or hourly cash notifications when new payments land and students appear in Limitless Sales.

**Important rule:** Airtable base `Limitless Sales` is the main source of truth for revenue because both Stripe and bank-transfer customers complete registration there.

**Best setup:**
- Airtable becomes the reporting ledger for revenue
- Stripe webhook or hourly poll is still useful for instant card-payment alerts
- Airtable poll or webhook captures the full business picture, including bank transfers
- Join payment events with student records where possible
- Telegram alert for each real payment or batched hourly summary

**What Hermes can do:**
- define event flow
- format cash alerts
- maintain a clean ledger note or report
- compare Stripe events to Airtable registrations
- build daily revenue reporting from Airtable as the main source of truth

### 3. Daily revenue updates against monthly target
**Goal:** Know current monthly revenue and progress toward B2M-B3M target.

**Best setup:**
- Daily scheduled job
- Pull Stripe revenue + optionally Airtable enrollment count
- Compute month-to-date revenue and gap to target
- Send concise morning summary

**What Hermes can do:**
- generate the daily revenue brief
- track pace against target
- identify whether current run rate is ahead or behind plan

### 4. Meta ad spend and cost per paying customer
**Goal:** Know total ad spend and customer acquisition cost from Facebook-driven workshop buyers.

**Best setup:**
- Pull ad spend from Meta Ads
- Pull paid customer list from Stripe/Airtable
- Match source attribution where possible
- Compute:
  - spend to date
  - paying customers from Facebook
  - CAC = ad spend / paid customers

**What Hermes can do:**
- build the daily or weekly CAC report
- highlight if spend rises while paid conversions slow
- separate raw lead volume from actual paid customer count

### 5. Daily new leads from Line Official
**Goal:** Track daily incoming leads, especially likely YouTube-origin traffic.

**Best setup:**
- If API access exists, use API
- If not, browser automation can log in and capture daily counts
- Save count to daily report

**What Hermes can do:**
- use browser automation if needed
- record lead counts daily
- compare lead volume with sales and content activity

### 6. Payment slips from Facebook chats or Line Official
**Goal:** Detect payment slips quickly and log them somewhere reliable.

**Best setup:**
- Browser or inbox checking agent
- OCR step on new slip images
- Save parsed details to a database or note
- Optional alert for unmatched slip requiring manual confirmation

**What Hermes can do:**
- inspect chats where accessible
- analyze screenshots / slips
- extract amount and timestamp where visible
- create a pending-payment log

### 7. Social channel growth + content writing agents
**Goal:** Track TikTok, Instagram, and YouTube growth, then use that to power content writing for multiple channels.

**Best setup:**
- Daily metrics pull per platform
- Weekly growth summary
- Content agent uses:
  - top-performing posts
  - latest audience signals
  - current launches and class calendar

**What Hermes can do:**
- create daily / weekly social summaries
- identify what content themes are gaining momentum
- draft content for school community, LinkedIn, and X
- repurpose insights from viral monitoring into original content

### 8. Schedule-aware teaching prep agent
**Goal:** Track classes on calendar and prepare use cases, prompts, and ideas based on class descriptions.

**Best setup:**
- Daily calendar scan
- For upcoming classes, generate prep packet:
  - use cases
  - prompts
  - examples
  - likely student objections
  - class-specific demo ideas

**What Hermes can do:**
- read schedule data
- prepare class briefs automatically
- tailor material to each program and audience

## Recommended rollout order

### Phase 1: Highest joy and easiest wins
1. Stripe payment alerts
2. Daily revenue summary
3. Viral AI trend collector + analyst
4. Schedule-aware class prep briefs

### Phase 2: Performance visibility
5. Social channel growth tracker
6. Meta ad spend + CAC reporting
7. Line Official daily lead tracking

### Phase 3: Harder but high value
8. Payment slip detection from chats
9. Full cross-source attribution between YouTube -> Line -> payment

## Best Telegram behavior
To avoid spam:
- raw data stays in files / Obsidian / database
- hourly collectors stay silent unless something exceptional happens
- Telegram gets:
  - new payment alerts
  - daily revenue report
  - top 3-5 viral opportunities
  - class prep packet when relevant
  - urgent anomalies only

## Suggested agent roles
- **Scout** -> watches X, YouTube, social growth
- **Cashier** -> Stripe, Airtable, slips, revenue, CAC
- **Line Watch** -> Line Official leads and conversion clues
- **Professor** -> schedule-aware class prep
- **Writer** -> turns insights into content drafts

## What is likely needed from Jedi
- access to Stripe
- access to Airtable base `Limitless Sales`
- Meta Ads access
- Line Official login or API
- social analytics access where needed
- calendar access for class prep

## My recommendation
Start with a 4-agent stack first:
1. Viral trend monitor
2. Cash alert + revenue monitor
3. Class prep agent
4. Social summary + writing agent

That gets the biggest operational upside without trying to automate every edge case on day one.
