# AI Agents are the New SaaS — Limitless Club Playbook

**Source:** Greg Isenberg, "AI Agents are the new SaaS" (YouTube, July 2026)
**Live page:** https://agent-saas-playbook.vercel.app
**Adapted for:** Limitless Club / Jedi Trinupab by Kelly / Hermes Agent

---

## Core Thesis

SaaS sells software. Agent SaaS sells **work**. The TAM is labor (trillions), not software (billions).

---

## The 7-Step Playbook (from the video)

### 1. Pick a workflow with a paycheck attached
Don't invent a problem. Find a job where someone is already paying a human: receptionist, coordinator, dispatcher.

**5 traits of a good agent workflow:**
- High frequency (hourly > daily)
- Clear finish line (job booked, ticket categorized, refund approved)
- Touches existing software (Gmail, Slack, Shopify, HubSpot, Stripe)
- Edge cases are annoying but learnable (not so simple a Zap handles it, not so complex only a human can)
- The buyer feels the pain (missed calls, slow replies, dropped leads)

### 2. Shadow the human first
Before writing a single prompt, watch 10-20 real jobs. Screen record. Ask: what makes a case easy? What makes it weird? Where do mistakes happen? **The detail is the product.**

### 3. Spec the agent (7 parts)
Trigger, Context, Tools, Allowed actions, Approval points, Escalation rules, Success definition.

### 4. Build the minimum useful agent (MUA)
Four shapes, from simplest to most autonomous:
1. **Draft-and-approve** — reads context, drafts reply/quote/summary, human approves
2. **Triage** — classifies inbound work, routes to the right place
3. **Coordinator** — goes between systems and people, keeps work moving
4. **Bounded action** — does one specific thing under clear rules (book appointment, process refund under $50)

Key insight from Anthropic: many agent problems should start as predictable workflows. Earn autonomy by adding judgment only where it creates value.

### 5. The wrapper makes it SaaS
The agent does the work, but the **wrapper** (logs, approvals, controls, handoff rules, evals, analytics) creates the trust customers pay for. Build an eval set from 50 real examples.

### 6. Sell the pilot like labor, then productize
- Start with 3 customers in one niche, same workflow
- Sell the outcome, not the tool
- Pricing: ~$1,500 setup + $1,000/mo per workflow, or $2,000 setup + $30/qualified appointment, or $3,000/mo up to 500 tickets
- Move toward outcome pricing
- Productize the repeatable parts

### 7. Distribution: workflow teardowns
Show the painful old way. Show the smooth agent way. Sell the painkiller. Make 50 example posts. Pick one platform. Put paid ads behind the winners.

---

## What You Already Have

Greg's talking to people starting from zero. **You're not starting from zero.**

| Agent / Capability | What it does | Productizable as |
|---|---|---|
| Kelly Voice (Twilio + ElevenLabs + Hermes) | Answers phone calls, takes requests, executes work, reports back | AI receptionist / dispatcher |
| Blaze (content engine) | Daily content packages, carousels, scripts, social posts | Content-as-a-service |
| Signal (AI research radar) | 4x/day AI intel scans, X monitoring | Industry intelligence subscription |
| Class Roster Intelligence | Calendar + Airtable + student context + Notion brief | Course/cohort ops agent |
| Revenue Monitoring (Airtable + Stripe) | Near-real-time payment alerts, daily revenue reports | Finance ops agent for SMEs |
| Pipeline PM (Oracle) | 15-min cron: classify, scaffold, approve, ship | Project intake agent for agencies |
| Mission Control | Approval workflows, social posting gates | Operations control room |

---

## The $50K/Month Math

| Revenue stream | Clients | Price/mo | Monthly |
|---|---|---|---|
| Agent SaaS: AI receptionist (Kelly Voice) | 8 | $3,000 | $24,000 |
| Agent SaaS: Content engine (Blaze) | 5 | $2,500 | $12,500 |
| Agent SaaS: Revenue/ops monitor (Airtable + Stripe) | 5 | $2,000 | $10,000 |
| Cohort upsell: "AI Team OS" license | 3 | $1,500 | $4,500 |
| **Total** | **21** | | **$51,000** |

Conservative: no consulting, no setup fees, no outcome pricing upside.

---

## Three Products to Build First

### Product 1: AI Receptionist + Work Dispatcher (highest leverage, already built)
1. Pick one niche: Thai service businesses (dental clinics, real estate, property management)
2. Shadow: call 10, ask them to show what happens when they miss a call
3. Spec: trigger=inbound call, context=business info + calendar, tools=calendar/CRM/SMS, allowed actions=book/reschedule, approval=high-value bookings, escalation=complaints/VIPs, success=qualified booking
4. MUA: already running (Kelly Voice)
5. Wrapper: simple dashboard (call summaries, booking outcomes, missed handoffs) — Bolt builds in a day
6. Sell: "We answer your missed calls, qualify the lead, book the appointment, and text you the summary. $2,000 setup + $1,500/mo."
7. Distribution: workflow teardown showing missed call → lost customer vs Kelly answering → booking → texting summary

### Product 2: Content Engine as a Service
- Target: Thai coaches/creators/SMEs
- Offer: "Daily IG/X/LinkedIn content, approved by you. $2,500/mo."
- Already have: carousel engine, transcript pipeline, approval workflow
- Wrapper: Mission Control approval dashboard

### Product 3: Revenue + Ops Monitor
- Target: Thai SMEs with messy revenue tracking
- Offer: "Track every transaction, instant alerts, daily revenue report, anomaly flagging. $2,000/mo."
- Wrapper: daily revenue Telegram report (already working)

---

## Your Unfair Advantages

1. **You already built the agent fleet** — 15+ profiles, skills, cron jobs, memory, phone bridge
2. **You have an audience** — @jeditrinupab, Limitless Club, students who trust you
3. **You have the content engine** — Blaze produces the workflow teardown content
4. **You have the cohort** — students are first pilot clients, upsell them agent SaaS
5. **You have the "AI Team OS"** — entire fleet is the product, $10K+ setup offer

---

## 30-Day Action Plan

| Day | Action |
|---|---|
| 1-2 | Pick the 3 products. Define pricing. |
| 3-5 | Bolt builds 3 simple dashboards |
| 6-7 | Blaze produces 10 workflow teardown posts |
| 8-14 | Post teardowns daily. DM 20 Thai service businesses. |
| 10-14 | Pitch 10 existing cohort students on "AI Team OS" |
| 15-21 | Close 2-3 pilots. Run manually if needed. |
| 22-28 | Turn pilots into case studies. Post. Run paid ads. |
| 28-30 | Productize. Set up Stripe payment links. |

**By Day 30:** 3-5 paying clients, case studies, content engine running, sales pipeline. $10-15K MRR. Scale to $50K within 3-4 months.

---

**Live page:** https://agent-saas-playbook.vercel.app
**Source video:** https://youtu.be/83fWzQSWB10
