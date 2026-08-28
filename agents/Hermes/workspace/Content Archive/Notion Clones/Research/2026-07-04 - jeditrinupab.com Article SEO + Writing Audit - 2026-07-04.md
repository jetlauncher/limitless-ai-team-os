---
title: "jeditrinupab.com Article SEO + Writing Audit — 2026-07-04"
notion_id: 393d076c-9ad3-8166-b12b-e79bbaf2b559
notion_url: https://app.notion.com/p/jeditrinupab-com-Article-SEO-Writing-Audit-2026-07-04-393d076c9ad38166b12be79bbaf2b559
type: "Research"
status: "Done"
created_time: 2026-07-04T05:38:00.000Z
synced_at: 2026-07-14T00:29:36
source: Notion clone
---

# jeditrinupab.com Article SEO + Writing Audit — 2026-07-04

- **Source:** [Open in Notion](https://app.notion.com/p/jeditrinupab-com-Article-SEO-Writing-Audit-2026-07-04-393d076c9ad38166b12be79bbaf2b559)
- **Type:** Research
- **Status:** Done
- **Created:** 2026-07-04T05:38:00.000Z

## Summary

Blaze audited the live jeditrinupab.com blog article corpus and created a Bolt implementation handoff for SEO/content rewrites. Live articles.json returned 198 articles; local Bolt repo copy has 191, so Bolt must reconcile before editing. Main findings: 118 stubs, 25 thin articles, 185 missing LINE CTA signal, 187 zero-link articles, 170 no FAQ-like block, 30 long titles, 23 long meta/excerpts.

## Key artifact paths

- /Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Research/website-article-seo-audit/website-article-seo-writing-audit-2026-07-04.md

- /Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Research/website-article-seo-audit/website-article-rewrite-system-2026-07-04.md

- /Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Research/website-article-seo-audit/article-update-priorities-2026-07-04.json

- /Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Queue/2026-07-04 - Website Article SEO Rewrite Implementation.md

## Main findings

- Live article count: 198

- Placeholder/stub articles: 118

- Thin articles under 2,500 chars: 25

- Missing LINE CTA signal: 185

- Articles with zero links: 187

- Articles without FAQ-like section: 170

- Long titles >70 chars: 30

- Meta/excerpts >160 chars: 23

- Production/repo mismatch: live has 198, local repo has 191

## Recommended writing standard

Every article should read like Jet advising a Thai business owner, not like an AI tool summary: owner scene → sharp thesis → mechanism → framework → use cases → risks/tradeoffs → 7-day action plan → FAQ → CTA.

## Bolt next step

Bolt should reconcile live/repo article JSON first, then replace stubs, upgrade non-stub articles with internal links/FAQ/CTA/schema, run checks/build, and use preview deploy before production unless Jet explicitly approves immediate production.

## V2 update — subagent findings folded in

Two subagents completed: technical SEO audit and writing-quality evaluator. A third rewrite-system subagent timed out, so Blaze retained the V1 scalable rewrite system and strengthened it with the completed findings.

- Sitemap has 197 unique blog URLs while articles.json has 198 records because duplicate slug ai-tier-list-by-jedi exists.

- Critical P0: hide/noindex/remove 118 stubs from sitemap until real content exists.

- Critical P0: add per-article title/meta/canonical/OG/Twitter and Article/Breadcrumb/Video/FAQ schema; consider SSG/prerender instead of pure SPA.

- Writing evaluator: median non-stub article quality is roughly 55/100; only 6 non-stub articles reached 70–84.

- Top rewrite priorities: chatgpt-codex-vs-claude-cowork, nXuwdvn12M0, chatgpt-codex-vs-claude-cowork-vs-google-antigravity, 02-23-what-can-claude-cowork-do, ai-changing-humanity-not-just-jobs.

- V2 report file: /Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Research/website-article-seo-audit/website-article-seo-writing-audit-v2-2026-07-04.md

- Bolt queue handoff updated with V2 findings.
