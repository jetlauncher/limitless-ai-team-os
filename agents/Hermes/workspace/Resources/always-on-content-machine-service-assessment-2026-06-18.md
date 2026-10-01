# Always-On Content Machine — Service Assessment

**Source doc:** Google Doc `1J7eWEj8-53lp9IwOWxbmOkoY3mMcFzq73uXSwtKCzeM`  
**Local source export:** `~/Documents/Limitless OS/Agents/Hermes/Resources/always-on-content-machine-source-2026-06-18.txt`  
**Prepared for:** Jet / Limitless  
**Date:** 2026-06-18

## Executive take

Yes — this is broadly what we are already building and operating internally, but the Google Doc describes a **client-facing, productized, multi-channel content service** that is more polished and more automated than our current internal operating system.

My read:

- **We already have ~65–75% of the operating pieces.**
- **We do not yet have the exact packaged client delivery system.**
- The biggest gap is not AI generation. The gap is **client onboarding, QA, approval UX, analytics feedback loop, and repeatable implementation SOPs for students/operators.**
- The strongest sale is not “AI writes content.” It is:  
  **“We install a 24/7 content operating system that turns your direction into approved, measured, multi-channel output every week.”**

## What the doc proposes

The doc is an **Always-On Content Machine**:

- 4 core agents:
  1. Strategist
  2. Scout
  3. Producer
  4. Gatekeeper
- 5 channels:
  - SEO / Blog
  - Instagram
  - Facebook
  - TikTok
  - YouTube
- Optional paid ads extension:
  - Auto-boost top organic posts
  - Pause underperformers
  - Feed results back into strategy
- Measurement loop:
  - Daily platform metrics
  - Weekly performance log
  - Strategy reads past performance before making the next calendar
- Human role:
  - Direction
  - Approval
  - Brand feedback

The key promise:

> ระบบ AI ทำ content ให้คุณ 56–88 ชิ้น/เดือน ใน 5 ช่องทาง คุณใช้เวลา 35 นาที/สัปดาห์ แค่บอกทิศทางและกด Approve

## Are we already doing this?

### Short answer

**Partially yes — internally. Not yet fully as a client service.**

We already have the foundations:

- Hermes/Kelly as orchestration layer
- Blaze for content generation
- Signal for research/X intelligence
- Kaijeaw for Thai content
- Pixel/creative skills for visuals/carousels
- Notion + Obsidian archives
- Mission Control approval queue
- Blotato/social approval posting workflow
- GSC/YouTube/revenue monitoring scripts
- Higgsfield/video/image tools available
- Cron jobs for daily/recurring agent work

But the Google Doc’s offer assumes:

- one clean Airtable/CRM state machine per client
- per-client Brand Bible + embeddings/QA
- auto-generated cross-platform content packs
- client approval dashboard
- metrics pulled from every platform
- a repeatable onboarding/install process
- support/maintenance capacity
- clear scope and guarantees

We have some of those, but not all in a repeatable template yet.

## Feature-by-feature comparison

| Component in doc | Are we doing it now? | Current evidence / equivalent | Gap before selling |
|---|---:|---|---|
| Strategist weekly content calendar | **Partial** | Daily content engine, Blaze crons, content research sweeps | Need client-facing calendar state: `CALENDAR_PENDING → APPROVED` |
| Research Scout every 6–8h | **Yes internally** | Signal X/radar, research sweep, X-to-Obsidian, AI intel | Need per-client industry/competitor research config |
| Producer creates text/images/video | **Partial/Yes** | Blaze, Kaijeaw, carousel skills, Higgsfield, image/video generation tools | Need standardized production pack: blog + captions + script + visual specs |
| Multi-platform conversion | **Partial** | Some FFmpeg/media workflows exist; carousel/video skills exist | Need reliable per-channel export templates and tests |
| Gatekeeper brand/QA check | **Partial** | Mission Control approval, brand rules, visual QA skills | Need automated Brand Bible scoring and technical asset QA per client |
| Human approval queue | **Yes internally** | `content_approval_queue.json`, Mission Control approval workflows, Blotato workflow | Need client-safe UI/auth and easy approval instructions |
| Auto-publish to platforms | **Partial** | Blotato approval posting, platform APIs available in concept | Keep human approval gate; avoid claiming full auto-post everywhere until verified |
| Paid ads auto-boost | **Not yet / risky** | Not productionized | Sell as manual/assisted add-on first, not default automation |
| Measurement loop | **Partial** | GSC weekly, YouTube daily, revenue dashboard, some cron scripts | Need unified content performance log across Meta/TikTok/YT/Blog per client |
| Brand Bible onboarding | **Partial** | Jet brand template, brand skills, Mission Control | Need packaged 90-min intake + 48h Brand Bible build SOP |
| Student/operator repeatability | **Not yet enough** | Skills exist, but scattered | Need templates, checklists, videos, Airtable base, scripts, prompts |

## What we should NOT overclaim yet

Before selling broadly, avoid promising these as fully automated from day one:

1. **Auto-publishing to every platform**  
   Some APIs are brittle, account-specific, or require business verification.

2. **Paid ads automation**  
   Good upsell, but risky to run automatically without budget and approval rules.

3. **56–88 high-quality pieces/month for every client at ฿55k/mo**  
   This is doable only if the output mix is scoped clearly. If it includes real video, custom visuals, SEO blogs, paid ads, QA, and reporting, ฿55k/mo is underpriced.

4. **35 min/week human time for all clients immediately**  
   Month 1 usually needs more calibration.

Better first claim:

> “Within 14 days, we install a content operating system that produces a weekly approved content pipeline across your chosen channels, with AI-assisted research, production, QA, and performance tracking.”

## Recommended product positioning

### Product name options

- Limitless Content Machine
- AI Content Operating System
- Always-On Content Engine
- 24/7 Content Team OS
- AI Content Machine Implementation Sprint

### Best angle for Thai market

Do not sell “AI automation.” Sell:

> “จากไอเดีย → เป็นคอนเทนต์ทุกช่องทาง → พร้อม approve → วัดผลได้ — โดยเจ้าของใช้เวลาแค่เลือกทิศทางและตัดสินใจ”

Thai buyers are likely to respond to:

- seeing their brand output first
- competitor comparison
- consistency without hiring a team
- clear reduction in founder/team bottleneck
- proof that it produces real assets, not just a report

## Recommended offer ladder

### 0. 24-Hour Sample — Free / qualifying tool

Use this as lead magnet only for qualified prospects.

Deliver:
- 1 mini blog preview or LinkedIn/Facebook long post
- 3 caption concepts
- 1 carousel outline or visual mock
- 1 short video script
- 1-page PDF preview

Purpose:
- Show “future version of their brand”
- Build trust fast
- Create emotional contrast versus competitors

Do not make this too labor-heavy. It should be template-driven.

### 1. 7-Day Trial Run — ฿35,000–75,000

This should not be free for everyone. Make it credited toward setup if they sign.

Deliver:
- Brand mini-intake
- 1-week calendar
- 5–10 draft assets
- approval board
- simple performance baseline
- final recommendation call

Use this as the strongest sales bridge.

### 2. Brand Bible + System Setup — ฿120,000–250,000

This is the install fee.

Deliver:
- Brand Bible
- channel strategy
- Airtable/Notion/Mission Control workspace
- approval workflow
- content templates
- first 2 weeks of calendar
- measurement dashboard
- training for client/team

### 3. Monthly operation packages

#### SEO Machine

Recommended pricing:
- Setup: **฿120,000–180,000**
- Monthly: **฿35,000–55,000**
- Minimum: 6 months

Good for:
- service business
- clinics
- agencies
- B2B experts
- local SEO / organic lead generation

Deliver:
- 4–8 SEO articles/month
- keyword map
- on-page SEO
- internal linking
- GSC tracking
- monthly report

#### Social Machine

Recommended pricing:
- Setup: **฿100,000–180,000**
- Monthly: **฿38,000–65,000**
- Minimum: 6 months

Deliver:
- 20–30 IG/FB/LinkedIn/X style posts/month
- captions
- carousel designs from templates
- posting queue
- brand voice QA
- monthly report

#### Video Machine

Recommended pricing:
- Setup: **฿150,000–250,000**
- Monthly: **฿55,000–90,000**
- Minimum: 6 months

Deliver:
- 8–12 short video scripts/month
- 4–8 AI-assisted videos/month depending quality level
- thumbnails/hooks
- repurposing to Shorts/Reels/TikTok
- virality scoring / QA

#### Full Stack Machine

Recommended pricing:
- Founding clients: **Setup ฿200,000 + ฿55,000/mo** only if tightly scoped
- Standard: **Setup ฿250,000–400,000 + ฿80,000–150,000/mo**
- Minimum: 6 months

If the promise includes SEO + social + video + paid + dashboard + support, I would not standardize at ฿55k/mo. That is a founding-client beta price, not mature pricing.

### 4. Paid Ads Automation Add-on

Start assisted, not fully automatic.

Recommended pricing:
- **฿15,000–30,000/mo management layer**
- plus ad spend
- plus separate creative volume if needed

Rules:
- no auto-spend without budget cap
- human approval for campaigns
- auto-pause can be allowed before auto-scale

### 5. Industry exclusivity

Recommended pricing:
- Local category exclusivity: **+฿15,000–30,000/mo**
- Full national industry exclusivity: quote separately, likely **+฿50,000+/mo** or a minimum annual commitment

## Student-ready product version

For students, I would not start with the full Hermes-agent version. Too complex.

Teach them a **3-level stack**.

### Student Level 1 — Manual AI Content System

Best for beginners.

Tools:
- ChatGPT / Claude
- Perplexity
- Canva Pro
- Google Sheets or Airtable
- Meta Business Suite / Buffer / Publer / Blotato
- Google Drive

What they can sell:
- 24-hour sample
- 7-day content sprint
- 20-post/month social package
- Brand Bible Lite

Suggested student pricing:
- Trial: ฿9,900–25,000
- Monthly social package: ฿15,000–35,000

### Student Level 2 — Semi-automated Content Machine

Best for serious operators.

Tools:
- Airtable as content OS
- Make/Zapier/n8n for triggers
- Claude / OpenAI API
- Perplexity or Brave Search API
- Canva templates
- Blotato / Publer / Buffer
- GA4 + GSC + Meta Insights exports
- Looker Studio dashboard

What they can sell:
- SEO Machine Lite
- Social Machine
- approval dashboard/board
- monthly performance report

Suggested student pricing:
- Setup: ฿50,000–120,000
- Monthly: ฿25,000–60,000

### Student Level 3 — Agency/Partner Content Machine

Best for advanced students or certified partners.

Tools:
- Hermes Agent / custom agent runner
- Airtable or Supabase state machine
- Notion/Obsidian knowledge base
- Claude/OpenAI/Gemini model routing
- Perplexity/Brave/DataForSEO
- Canva API or template-renderer
- Higgsfield / Runway / ElevenLabs for video
- FFmpeg for format conversion
- Blotato/platform APIs for publishing
- Mission Control-style approval dashboard
- GSC/GA4/Meta/YouTube/TikTok analytics pull

What they can sell:
- Full Stack Machine
- per-client AI content OS installation
- maintenance retainer

Suggested student/partner pricing:
- Setup: ฿120,000–300,000
- Monthly: ฿50,000–120,000

## Minimum tool stack for our own client delivery

### Core system

| Layer | Recommended tool |
|---|---|
| State / workflow | Airtable first, Supabase later |
| Agent orchestration | Hermes Agent |
| Research | Perplexity API, Brave Search, X Search, YouTube Data API |
| Writing | Claude Sonnet/Opus, GPT-5.5/OpenAI, Gemini as backup |
| Thai content | Claude/GPT + Kaijeaw-style Thai brand rules |
| Visuals | Canva templates, OpenAI/Grok/Higgsfield images, optional Magnific/upscale |
| Video | Higgsfield, Runway, ElevenLabs, FFmpeg |
| Approval | Mission Control dashboard or Airtable Interface first |
| Publishing | Blotato first, native APIs later |
| Measurement | GSC, GA4, Meta Insights, YouTube Analytics, TikTok Analytics, DataForSEO |
| Reporting | Notion/Google Docs/PDF/Looker Studio |

### Why Blotato first

For client service, Blotato/Buffer/Publer-style posting is safer than going native Meta/TikTok/YouTube APIs immediately. Native APIs create onboarding friction, app reviews, permissions, token expiry, and debugging cost.

### Why Airtable first

Airtable is easier for students and clients to understand than Supabase. Use Airtable for:

- Direction
- Calendar
- Briefs
- Production status
- Approval status
- Performance log
- Budget rules

Move to Supabase when you need scale, embeddings, auth, or custom dashboards.

## Recommended Airtable schema

Tables:

1. Clients
2. Brand Bible
3. Content Calendar
4. Topic Briefs
5. Assets / Deliverables
6. Approval Queue
7. Platform Accounts
8. Performance Log
9. Paid Boost Rules
10. Monthly Reports

Important statuses:

- `DIRECTION_PENDING`
- `CALENDAR_PENDING`
- `CALENDAR_APPROVED`
- `BRIEF_READY`
- `IN_PRODUCTION`
- `READY_FOR_QA`
- `NEEDS_REVISION`
- `READY_FOR_CLIENT_APPROVAL`
- `APPROVED_TO_PUBLISH`
- `PUBLISHED`
- `MEASURED`

## What to build next before selling

### Must-have before first paid client

1. **Client Airtable base template**
2. **Brand Bible intake template**
3. **24-hour sample generator workflow**
4. **7-day trial SOP**
5. **Approval board/UI**
6. **Monthly report template**
7. **Clear content quality scope**
8. **Tool access checklist**
9. **Client contract terms: IP, data, approvals, ad spend, cancellation**
10. **Demo case study using Limitless itself**

### Nice-to-have after first 3 clients

1. Per-client Hermes profile / isolated workspace
2. Supabase Brand Bible embeddings
3. More automated performance loop
4. Paid auto-boost rules
5. Native platform API integrations
6. Student certification / operator dashboard

## Sales recommendation

Use the doc’s funnel, but tighten qualification:

1. **Public hook:** “Your business gets 56–88 content assets/month without hiring a content team.”
2. **Lead magnet:** 24-hour sample.
3. **Sales call:** live demo using their brand/topic.
4. **Paid pilot:** 7-day trial, credited toward setup.
5. **Close:** 6-month implementation retainer.

Do not lead with “AI audit.” For Thai market, the doc is right: they pay when they see the future, not when they are told the diagnosis.

## Bottom line

This is absolutely sellable.

But I would frame the first version as:

> **Founding Client Beta: We install your AI Content Machine in 14 days. You get a weekly content calendar, AI-assisted production, human approval queue, and performance dashboard. We operate it with you for 6 months.**

Recommended first founding offer:

- **Setup:** ฿200,000
- **Monthly:** ฿55,000–75,000
- **Minimum:** 6 months
- **Limit:** 3 clients
- **Scope:** Full Stack, but cap video/custom visual volume clearly

Recommended standard offer after proof:

- **Setup:** ฿250,000–400,000
- **Monthly:** ฿80,000–150,000
- **Minimum:** 6 months

The real business is not content production. The real business is installing an AI-powered operating system that compounds distribution for the client.
