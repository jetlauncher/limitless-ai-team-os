---
type: geo-audit
date: 2026-08-06
site: https://jeditrinupab.com
status: completed-with-gsc-blocker
scope: [technical-crawlability, ai-search-visibility, entity-consistency, content-architecture, citations]
source_reference: "Shared Memory/Sources/References/2026-08-06-silicon-valley-girl-how-to-rank-1-in-ai-geo.md"
---

# jeditrinupab.com GEO / AI Visibility Audit — 2026-08-06

## Executive finding

The site is **technically much stronger than the earlier May smoke-check state**. It now exposes server-rendered titles, H1s, body text, canonicals, and JSON-LD across the sitemap. AI crawlers are not blocked.

However, the live AI-answer tests show a clear business problem: **AI systems recognize Jet when asked by name, but do not recommend Jet or Limitless Club for generic Thai AI trainer/course queries.** Direct identity answers remain fragmented across his historical CEO/lifestyle identity, a sponsored Forbes profile, and an obsolete `manus.space` site.

The constraint is no longer basic crawlability. It is now **category authority, entity consolidation, source quality, and explicit video/transcript attribution**.

## Method

- Crawled the live homepage, robots, sitemap, core commercial pages, and all sitemap URLs with a crawler user agent.
- Bulk-checked status, redirects, canonicals, H1s, titles, meta descriptions, JSON-LD, and visible server-response text.
- Audited all blog detail pages for YouTube attribution, VideoObject schema, code-fence artifacts, and H1 structure.
- Inspected Person/Course/BlogPosting JSON-LD.
- Tested direct-identity and generic-category prompts using OpenAI web search and Perplexity Sonar in English and Thai.
- Ran public web searches for brand/entity and category phrases.
- Attempted the live Search Console report; the dedicated GSC token failed with `invalid_grant`.

## What is working

### Crawlability and index plumbing

- `robots.txt`: 200 and allows `User-agent: *`.
- Sitemap: 200 with **226 URLs**.
- All 226 sitemap URLs returned 200 during this audit.
- Zero missing canonicals.
- Zero canonical mismatches among sitemap URLs.
- Zero missing H1s.
- Zero missing JSON-LD.
- `www` correctly redirects to apex with HTTP 308.
- Core page body copy is available in initial HTML without requiring client-side JavaScript.

### Content footprint

- Sitemap contains 203 blog-detail URLs plus the blog landing page.
- Most blog details have several thousand characters of readable Thai/English content.
- Blog pages include BlogPosting and BreadcrumbList schema.
- Homepage includes Person, WebSite, and Course schema with `sameAs`, `knowsAbout`, and Thailand/AI positioning.

### Branded discoverability

Exact searches for “Jedi Trinupab” plus AI return:
- `jeditrinupab.com/press`
- YouTube
- Forbes Thailand
- Skool
- Social profiles

ChatGPT’s direct-identity test recognized Jet as Creatus CEO and Limitless Club founder/AI business coach.

## High-priority problems

### P0 — Soft-404 routing

A fabricated URL returned HTTP 200, homepage HTML, and a homepage canonical:

`https://jeditrinupab.com/definitely-not-a-real-page-kelly-audit`

This is a real technical-quality issue. Unknown routes should return a genuine 404 page/status, not the homepage as 200. The current behavior can generate soft-404 indexing noise, waste crawl resources, and dilute site-quality signals.

### P0 — Obsolete `manus.space` site is still live and self-canonical

Both of these return 200, are indexable, and self-canonicalize:

- `https://limitlessclub.manus.space/`
- `https://limitlessclub.manus.space/programs/ai-expert`

ChatGPT cited the old Manus program page instead of `jeditrinupab.com` in the direct-identity test. This is direct evidence of entity/authority fragmentation.

Preferred fix: 301 every useful legacy URL to the closest official URL. If redirects are impossible, apply `noindex` and prominent canonical/links to the official site.

### P0 — Category recommendation visibility is currently weak

Across five generic category tests:

1. OpenAI: credible AI trainers/coaches for Thai business owners
2. Perplexity English: AI trainers/coaches in Thailand
3. Perplexity English: practical AI courses in Thailand
4. Perplexity Thai: วิทยากร/โค้ช AI สำหรับเจ้าของธุรกิจ
5. Perplexity Thai: คอร์ส AI สำหรับเจ้าของธุรกิจและผู้บริหาร

**Jet/Limitless appeared in zero of five recommendation lists.** Competitors and institutions such as AI Trainer Thailand, Sasin, Chulalongkorn, AIT, RealSmart, AIGEN, PiR Academy, NIDA, and other trainers appeared instead.

Direct-name recognition exists; unbranded category authority does not yet.

### P1 — Historical identity still dominates some AI answers

Perplexity’s direct-name answer described Jet mainly as:

- Creatus CEO
- Husband of Ning Sophida
- Business/lifestyle public figure

It mentioned Limitless Club but did not establish the current AI educator/AI business coach identity strongly. ChatGPT did better, but relied on the old Manus site and Forbes sponsored content.

This means current first-party schema is moving in the right direction, but external corroboration has not caught up.

### P1 — English surname inconsistency

The official site/schema uses **“Jedi Trinupab Jiratraitharn.”** Multiple longstanding external profiles use **“Jedi Trinupab Jiratritarn.”** Confirm the canonical English spelling, then align the website, JSON-LD, social profiles, directories, and press materials. Do not change this without Jet’s confirmation.

### P1 — Blog pages are not connected to their YouTube source

Across all **203 blog-detail pages**:

- 0 contained a visible YouTube link or embed.
- 0 used `VideoObject` schema.

Many routes appear to use YouTube video IDs as slugs, but the source video is not explicitly attributed. This misses the strongest GEO opportunity from the reference playbook: connect each article to the original video, creator, upload date, thumbnail, embed URL, duration, and transcript.

Recommended pattern: BlogPosting + VideoObject + visible embedded/source link + server-rendered transcript or faithful transcript section.

### P1 — Content-generation artifacts

- 7 blog pages expose literal `````html`` code-fence artifacts in content or meta descriptions.
- 8 blog pages have multiple H1s, often an English title plus a Thai title.
- One page has only about 1,591 visible text characters.
- Some article text includes probable transcription/entity errors such as “Close Coverk,” “Wins.ai,” “Amplifi,” or “เจด/ตรินุภาพ.” These should be human-reviewed before being treated as authority content.

### P1 — Commercial/category pages are readable but thin

Eighteen pages contain only roughly 800–1,499 visible text characters. Important examples:

- `/ai-os`
- `/ai-training`
- `/ai-for-business`
- `/programs`
- `/programs/ai-expert`
- `/programs/ceo-os`
- `/workshop`
- `/about`
- `/press`

These pages have the right technical structure but need stronger evidence, use cases, outcomes, FAQs, original frameworks, and links from credible third parties to win category prompts.

### P2 — `/llms.txt` is not a real text file

`/llms.txt` currently returns homepage HTML with status 200 and homepage canonical. Either publish a valid plain-text `llms.txt` or return 404. This is not a magic ranking factor; the value is clean machine documentation and avoiding another soft-404 route.

### P2 — Homepage metadata cleanup

The live homepage meta description ends with a literal ellipsis and incomplete phrase (`led…`). Write a complete, stable description. The live title differs from the title still shown in search/Jina caches, indicating recent title changes and reindex lag.

### P2 — Structured-data cleanup

The homepage emits two overlapping Person definitions with slightly different `sameAs` and `knowsAbout` sets. Consolidate around stable `@id` references and one canonical Person entity. Consider linking Course providers/instructors by `@id` rather than repeating disconnected objects.

## Earned-media gap

The press page is a good start, but discoverable authority is still dominated by:

- Forbes Thailand sponsored content
- Older Marketeer coverage
- Lifestyle/relationship profiles
- Jet’s own site and social channels

The missing layer is recent, independent coverage proving AI/business expertise: partner case studies, university/event speaker pages, client implementation stories, credible podcasts, original benchmarks, and press articles that cite measurable outcomes.

## Recommended execution order

1. Fix soft-404 routing.
2. Redirect/noindex the legacy Manus site.
3. Confirm and normalize the canonical English surname.
4. Remove seven code-fence artifacts and eight duplicate-H1 patterns.
5. Link video-derived articles to YouTube and add VideoObject + transcript architecture.
6. Deepen priority category pages around buyer questions and real evidence.
7. Build an earned-citation campaign around original implementation results.
8. Establish a weekly prompt tracker across Thai/English buyer-intent prompts.
9. Restore Search Console OAuth and combine AI visibility with clicks, impressions, and revenue.

## Search Console blocker

The dedicated Search Console refresh token returned:

`google.auth.exceptions.RefreshError: invalid_grant`

A fresh PKCE OAuth URL was generated for Jet. After he approves and returns the full `http://localhost:1/?...` redirect URL, exchange it with `gsc_gap_report.py auth-code`, verify `list-sites`, and rerun the live report.

## Local evidence

Temporary machine-readable outputs from this run:

- `/tmp/jeditrinupab_geo_technical_audit.json`
- `/tmp/jeditrinupab_bulk_geo_audit.json`
- `/tmp/jeditrinupab_blog_geo_audit.json`
- `/tmp/jeditrinupab_ai_visibility_test.json`
- `/tmp/openai_geo_visibility_raw.json`
- `/tmp/openai_jedi_identity_raw.json`
- `/tmp/perplexity_thai_geo_visibility_raw.json`

No live-site changes were made during this audit.
