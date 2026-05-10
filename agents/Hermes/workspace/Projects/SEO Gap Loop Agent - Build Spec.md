# SEO Gap Loop Agent — Build Spec

Created: 2026-05-10
Owner: Jet / Kelly

## Goal
Build an agent that runs the SEO growth loop for client brands:
1. Pull real ranking data from Google Search Console per client.
2. Find “gap zone” keywords where the client ranks positions 5–20.
3. Analyze competitors outranking the client.
4. Preserve each brand’s voice, positioning, and customer context.
5. Draft/update content and product listing recommendations.
6. Track ranking movement weekly and feed learnings into the next cycle.

## Product Direction
This is **our own Limitless internal tool first** — an operator engine for our own SEO/content growth loop, not a client SaaS by default.

Primary use cases:
- Grow Limitless Club organic visibility.
- Identify near-page-1 keywords we can win quickly.
- Turn GSC + SERP evidence into brand-specific content updates.
- Build repeatable internal IP before deciding whether to offer it as a productized service.

## MVP Principle
Start narrow: `jeditrinupab.com` as the first Limitless site/property, Google Search Console, competitor SERP scrape, content brief output, weekly ranking tracker. Do not automate publishing until the recommendations prove quality.

## MVP Workflow

### 1. Client onboarding
Store per-client data:
- Brand name
- Domain / GSC property URL
- Target country / language
- Customer personas
- Positioning
- Tone of voice examples
- Products / services
- Excluded topics
- Competitors, if known

Recommended storage:
- Airtable or Supabase for structured client records
- Markdown/Obsidian for long brand context and examples

### 2. Ranking pull
Data source: Google Search Console Search Analytics API.

Pull weekly by:
- Query
- Page
- Country
- Device, optional
- Clicks
- Impressions
- CTR
- Average position

Filter initial opportunities:
- Average position >= 5 and <= 20
- Impressions above threshold, e.g. >= 100/month
- Existing ranking URL is known
- Exclude branded terms unless intentional

### 3. Gap scoring
Score each keyword with a simple opportunity formula:

```text
Opportunity score = impressions_weight + position_weight + business_value - difficulty_penalty
```

Initial factors:
- Current position: 5–10 is higher priority than 15–20
- Impressions: higher is better
- CTR gap: high impressions + low CTR = title/meta opportunity
- Page type: product/service pages may be higher business value
- Keyword intent: commercial > comparison > informational, depending client

### 4. SERP competitor analysis
For top opportunities, use Apify or another SERP provider to fetch current top results.

Capture:
- Top 10 ranking URLs
- Titles/meta descriptions
- Content length / headings
- Search intent pattern
- Freshness dates
- Schema/FAQ/product markup presence
- Missing subtopics vs client page
- Why the client is likely losing

Avoid brittle scraping directly from Google if possible; use a compliant SERP API/Apify actor.

### 5. Brand context memory
Interview client once, then store a reusable brand packet:
- Who they serve
- Pain points
- Differentiators
- Proof points
- Offers/products
- Words to use / avoid
- Voice examples
- Competitive positioning

The agent should never ask repeated positioning questions unless the packet is missing or stale.

### 6. Content output
MVP output should be a content brief, not auto-published article.

For each keyword/page:
- Recommended action: update existing page / create new article / product listing optimization
- Search intent summary
- Competitor gap analysis
- Outline
- Title/meta options
- Internal links to add
- FAQ/schema suggestions
- Product listing fields to optimize
- Draft section examples in brand voice

### 7. Weekly tracking loop
Every week:
- Pull GSC data again
- Compare previous positions/clicks/impressions
- Mark recommendations as improved / flat / declined
- Feed winning patterns into future briefs
- Alert only on meaningful movement or high-value opportunities

## Architecture

### Components
- `connectors/gsc`: Google Search Console API client
- `connectors/serp`: Apify/SERP provider wrapper
- `clients`: client config and brand packet storage
- `ranking`: query/page snapshots and opportunity scoring
- `analysis`: competitor comparison and content gap logic
- `briefs`: LLM-generated briefs using brand packet + SERP evidence
- `scheduler`: weekly job runner
- `dashboard`: simple review UI / Airtable views / Notion mirror

### Suggested stack
- Python FastAPI or Next.js API routes for backend
- Postgres/Supabase for ranking snapshots and jobs
- Airtable for quick MVP client/opportunity dashboards, if speed matters
- Obsidian/Markdown for human-readable specs and brand packets
- Google Search Console API
- Apify SERP actor or DataForSEO/SerpAPI alternative
- LLM: GPT-5.5 for analysis/drafts
- Cron: Hermes cron for prototype; app scheduler later

## Data model MVP

### Client
- id
- brand_name
- domain
- gsc_property
- target_country
- target_language
- brand_packet_path
- status

### KeywordSnapshot
- id
- client_id
- query
- page
- date_start
- date_end
- clicks
- impressions
- ctr
- position
- country
- device

### Opportunity
- id
- client_id
- query
- page
- current_position
- impressions
- opportunity_score
- intent
- recommended_action
- status
- created_at

### SerpAnalysis
- id
- opportunity_id
- captured_at
- top_results_json
- gap_summary
- why_they_win
- recommended_changes

### ContentBrief
- id
- opportunity_id
- title
- brief_markdown
- status: draft / approved / implemented / rejected

## Safety and quality gates
- Never publish without approval.
- Cite the actual SERP evidence used in every brief.
- Keep client brand packet isolated per client.
- Do not mix client data across prompts.
- Log every generated recommendation and source data snapshot.
- Respect Google Search Console/API rate limits.

## Build phases

### Phase 1 — Prototype, one client
- Authenticate GSC.
- Pull one property’s search analytics.
- Find top 20 gap-zone opportunities.
- Scrape/analyze SERP for top 5.
- Generate markdown briefs.
- Store output in Obsidian/Airtable.

### Phase 2 — Multi-client dashboard
- Add client table.
- Add scheduled weekly pulls.
- Add status workflow: new → reviewed → approved → implemented → measured.
- Add weekly movement report.

### Phase 3 — Product listing / AI shopping optimization
- Add product feed/listing fields.
- Generate structured product descriptions, FAQs, comparison copy, schema suggestions.
- Track visibility in AI-shopping/recommendation prompts manually at first.

### Phase 4 — Managed service automation
- Client onboarding form.
- Brand packet generator.
- Human approval queue.
- CMS integrations for approved content updates.
- Revenue dashboard for service delivery.

## Implementation Status

### 2026-05-10
Prototype script created:

```text
~/.hermes/limitless/seo_gap_loop/gsc_gap_report.py
```

It supports:
- `auth-url` — generate Search Console OAuth link
- `auth-code <redirect-url>` — save dedicated Search Console token
- `list-sites` — list accessible Search Console properties
- `report` — generate jeditrinupab.com gap-zone report into Obsidian

Report output directory:

```text
~/Documents/Obsidian Vault/Agents/Hermes/Projects/Limitless Visibility Engine/Reports/
```

Current status:
- Dedicated Search Console OAuth token saved successfully at `~/.hermes/limitless/seo_gap_loop/google_search_console_token.json`.
- Search Console API enabled and verified.
- Accessible properties found:
  - `sc-domain:jeditrinupab.com`
  - `https://jeditrinupab.com/sitemap.xml/`
- First reports generated successfully:
  - Global: 8 gap-zone opportunities
  - Thailand: 11 gap-zone opportunities
- Weekly Monday 09:00 Bangkok-time Telegram cron created:
  - Job: `limitless-visibility-weekly-gsc-gap-report`
  - ID: `6a2606b41e59`
  - Script: `~/.hermes/scripts/limitless_visibility_weekly.py`

Latest report examples:
- Global top: `ai13900` → `/blog`, avg position 8.5, 136 impressions, 0 clicks
- Global top: `ceo intensive membership program` → `/programs/ceo-os`, avg position 5.0
- Thailand top: `limitless club` → `/programs/ai-expert`, avg position 6.2
- Thailand top: `เจได ai` → `/home`, avg position 7.6

## Immediate next steps
1. Run SERP/competitor analysis for top 3–5 opportunities.
2. Generate first page-update briefs for `/blog`, `/programs/ceo-os`, `/`, and `/programs/ai-expert`.
3. Decide whether to add Apify SERP automation or keep first competitor pass manual/search-based.