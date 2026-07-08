# Website Article SEO Rewrite Implementation — jeditrinupab.com

## From Blaze to Bolt
Jet asked Blaze to read all website articles, audit them, rewrite direction using the Limitless Writing & Thought Evaluator, and pass the implementation to Bolt so the website articles and SEO can be updated.

## Source artifacts
Blaze audit folder:
`/Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Research/website-article-seo-audit/`

Key files:
- Full live corpus JSON: `live-articles-2026-07-04.json`
- Audit corpus JSONL: `live-articles-audit-corpus-2026-07-04.jsonl`
- **V2 main audit report:** `website-article-seo-writing-audit-v2-2026-07-04.md`
- V1 audit report: `website-article-seo-writing-audit-2026-07-04.md`
- Rewrite system: `website-article-rewrite-system-2026-07-04.md`
- Priority JSON: `article-update-priorities-2026-07-04.json`

## V2 subagent additions
- SEO subagent verified live checks for `robots.txt`, `sitemap.xml`, and `blog/articles.json`.
- Sitemap has **197 unique blog URLs** while articles JSON has **198 records** because duplicate slug `ai-tier-list-by-jedi` exists.
- Current app appears SPA/client-rendered with one global title/meta; Bolt should add per-article metadata/canonical/OG/Twitter and Article/Breadcrumb/Video/FAQ schema via `react-helmet-async` or, preferably, SSG/prerender for blog routes.
- Writing evaluator subagent found median non-stub quality around **55/100**, with only **6** non-stub articles in the 70–84 range.
- Third rewrite-system subagent timed out; use Blaze V2 audit + V1 rewrite system as implementation source.

## Important production/repo mismatch
- Live production `https://jeditrinupab.com/blog/articles.json` returned **198 articles**.
- Local repo `/Users/ultrafriday/.hermes/exports/limitless-club-v3/public/blog/articles.json` currently has **191 articles**.
- Before implementation, reconcile production/live JSON vs repo source. Do **not** accidentally delete the 7 newest production articles.

## Audit summary
- Live article count: **198**
- Placeholder/stub articles: **118** (`Content coming soon.`)
- Thin articles under 2,500 chars: **25**
- Missing LINE CTA signal: **185**
- Zero links: **187**
- No FAQ-like section: **170**
- Long titles >70 chars: **30**
- Meta/excerpts >160 chars: **23**

## Content standard to implement
Every article should read like Jet advising a Thai business owner, not like an AI tool summary.

New article structure:
1. Thai SEO title: keyword + business outcome, ideally <=70 chars.
2. Concrete owner scene opening.
3. Sharp thesis / POV.
4. Mechanism: how/why the workflow creates leverage.
5. Founder framework: Founder AI OS, 10-80-10, CLEAR, KOI when relevant.
6. 3–5 concrete Thai business use cases.
7. Risks/tradeoffs: privacy, data, hallucination, cost, team adoption.
8. 7-day implementation plan.
9. FAQ block with 3–5 search-intent questions.
10. CTA: LINE OA / relevant program / relevant YouTube video / internal links.

## Implementation recommendation
1. Backup live/repo article JSON.
2. Reconcile 198 live records into repo source.
3. First pass: hide/noindex/remove from sitemap all `Content coming soon.` stubs until real articles exist.
4. Fix duplicate slug `ai-tier-list-by-jedi`; keep richer article, remove/redirect stub duplicate, enforce unique slug validation.
5. Add per-article SEO metadata/canonical/OG/Twitter/Article/Breadcrumb/Video/FAQ schema.
6. First content pass: replace priority stubs with full Thai SEO articles.
7. Second content pass: upgrade non-stub articles with stronger openings, internal links, FAQ blocks, and CTAs.
8. Add/validate fields if supported by renderer: `seoTitle`, `metaDescription`, canonical slug, image/ogImage, videoId/youtubeUrl, updatedAt.
9. Add validator script that enforces:
   - no duplicate slugs
   - no indexed stubs
   - content length >3,500 Thai chars unless intentionally short/noindexed
   - title <=70 chars or separate seoTitle <=60 chars
   - excerpt/metaDescription 90–160 chars
   - >=4 H2s
   - >=3 internal links for real articles
   - FAQ block
   - LINE CTA
10. Run `npm run check` and `npm run build`.
11. Verify `/blog`, `/blog/articles.json`, sitemap, duplicate slug resolution, top 10 priority slugs, and JSON article count.
12. Prefer preview deploy first; production deploy after Jet approval unless Jet explicitly says to push immediately.

## Acceptance criteria
- Live/repo article count reconciled; no production articles lost.
- 0 duplicate slugs.
- 0 indexed stub pages; stubs are hidden/noindexed/removed from sitemap until full content exists.
- Per-article SEO head tags and schema implemented or documented with SSG/prerender plan.
- All real articles have CTA, internal links, FAQ where appropriate, readable title/meta.
- Blog builds and renders cleanly.
- Handoff back to Blaze/Kelly includes changed counts, deploy URL, and any articles needing human review.

## Quality rewrite priorities from Blaze evaluator
Top non-stub rewrite priorities:
1. `chatgpt-codex-vs-claude-cowork` — angle: Codex beats Claude Cowork when the job is execution, not conversation.
2. `nXuwdvn12M0` — fix formatting artifact; angle: Claude Cowork connectors bridge AI chat and real management decisions.
3. `chatgpt-codex-vs-claude-cowork-vs-google-antigravity` — angle: same business task, only one behaved like an employee.
4. `02-23-what-can-claude-cowork-do` — angle: Claude Cowork is a junior operator inside your computer.
5. `ai-changing-humanity-not-just-jobs` — angle: AI changes company cost structure before it replaces jobs.
6. `what-we-use-ai-for` — evergreen AI use-case selection framework.
7. `02-22-openclaw-took-6000-baht` — founder risk/control story.
8. `three-google-ai-tools-underrated` — deploy workflows, not tool roundup.
9. `02-18-india-singapore-thailand-ai-race` — Thai SME macro implications.
10. `02-27-claude-cowork-five-employees` — AI = 5 employees promise with proof/roles/limits.

## Suggested first priority slugs
See `article-update-priorities-2026-07-04.json`; top examples:
- `prompt-engineering-guide`
- `02-16-openai-vs-deepseek-ai-cold-war`
- `02-17-ai-agent-price-crash`
- `02-21-is-ai-coming-for-computer-jobs`
- `02-22-article`
- `02-25-article`
- `02-26-article`
- `02-27-article`
- `02-28-article`
- `03-01-article`
