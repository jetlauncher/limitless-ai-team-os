# jeditrinupab.com Article SEO + Writing Audit — V2

Date: 2026-07-04 12:44 +07
Owner: Blaze
Implementation owner: Bolt
Source: live `https://jeditrinupab.com/blog/articles.json` extracted into local corpus.

## What changed in V2

V2 folds in two completed subagent passes:

1. Technical SEO/content audit.
2. Limitless Writing & Thought Evaluator audit.

A third rewrite-system subagent timed out after 600s, so Blaze retained the V1 scalable rewrite system and strengthened it with the completed audit findings.

---

## Executive SEO findings

| Issue | Count |
|---|---:|
| Total live article records | 198 |
| Real articles >100 chars | 80 |
| Stub pages / `Content coming soon.` | 118 |
| Duplicate slug | 1 slug duplicated |
| Pages with 0 internal links | 187 / 198 |
| Pages with fewer than 2 links | 198 / 198 |
| Pages with no LINE CTA | 185 / 198 |
| Real articles with no LINE CTA | 67 / 80 |
| Pages with no FAQ | 170 / 198 |
| Real articles with no FAQ | 52 / 80 |
| Pages with no body images | 198 / 198 |
| Pages with H2 = 0 | 118 / 198 |
| Real articles with H2 <= 1 | 15 / 80 |
| Titles >60 chars | 68 / 198 |
| Titles >70 chars | 30 / 198 |
| Titles <30 chars | 69 / 198, mostly stubs |
| Excerpts >160 chars | 23 / 198 |
| Non-ASCII slugs | 71 / 198 |

## Critical production/repo mismatch

- Live production `https://jeditrinupab.com/blog/articles.json` returned **198 article records**.
- Local repo `/Users/ultrafriday/.hermes/exports/limitless-club-v3/public/blog/articles.json` has **191 records**.
- Live sitemap has **197 unique blog URLs** because the live corpus has one duplicate slug: `ai-tier-list-by-jedi`.

**Bolt must reconcile live vs repo before editing or deploying.** Do not accidentally delete the 7 newest live articles.

---

## P0 fixes for Bolt

### P0.1 Remove, hide, or noindex 118 stub articles

118 live URLs contain only `Content coming soon.` with almost no indexable value.

Bolt implementation:

1. Do not render stub articles in `/blog` lists.
2. Add `noindex, follow` for articles where content is empty/placeholder/below threshold.
3. Remove stub URLs from sitemap until real content exists.
4. Publish only when article has:
   - 800+ words / meaningful full content
   - at least 3 H2s
   - at least 3 internal links
   - CTA
   - meta description
   - canonical URL

Examples:
- `15-เคล็ดลับ-ปลดล๊อค-ควา`
- `3-ระบบ-ai-ที่-ceo-ต้องรีบทำ`
- `5-minutes-with-ceo-ep11`
- `ai-tier-list-by-jedi` duplicate stub version
- `02-25-article`
- `02-26-article`
- `02-27-article`
- `02-28-article`
- `03-01-article`
- `QNX13pZCNdw`

### P0.2 Add per-article SEO head tags / canonical / schema

Repo inspection suggests article pages are client-rendered via `BlogArticle.tsx`, fetching `/blog/full-articles.json`, while `index.html` has one global title/description.

Bolt implementation:

For every `/blog/:slug`, generate:

- `<title>{article.title} | Jedi Trinupab</title>`
- `<meta name="description" content="{article.excerpt}">`
- `<link rel="canonical" href="https://jeditrinupab.com/blog/{slug}">`
- `og:title`, `og:description`, `og:image`, `og:type=article`
- `twitter:card=summary_large_image`
- JSON-LD:
  - `Article`
  - `BreadcrumbList`
  - `VideoObject` when `videoId` exists
  - `FAQPage` when FAQ exists

If staying SPA, use `react-helmet-async`. Better long-term: static pre-render/SSG for blog routes.

### P0.3 Fix duplicate slug: `ai-tier-list-by-jedi`

Live corpus has two records with the same slug:

1. Stub version: title `AI Tier list by Jedi`, chars 20.
2. Richer version: title `Jedi's AI Tier List: Which Tools Are S-Tier and Which Are Overhyped`, chars 1293.

Bolt implementation:

- Keep the richer version.
- Remove or redirect the stub duplicate.
- Enforce unique slug validation in content build step.

---

## P1 fixes

### P1.1 Add internal linking system

Problem:

- 187 / 198 pages have 0 links.
- 198 / 198 have fewer than 2 links.
- Among real articles, 69 / 80 have 0 links.

Bolt implementation:

1. In-body contextual links by topic cluster:
   - AI Agent
   - Claude Cowork
   - ChatGPT / Codex
   - Gemini / Google AI
   - Hermes Agent
   - AI for Business / SME
2. Add “Related articles” block under each article:
   - same category
   - shared keywords
   - same tool/entity
   - newest 3 related posts
3. Target minimum:
   - 3 internal links per real article
   - 5 links for pillar articles
   - 1 link to program/contact/resource page where commercially relevant

### P1.2 Standardize CTA placement

Problem:

- 185 / 198 pages lack LINE CTA.
- 67 / 80 real articles lack LINE CTA.

Recommended CTA:

```html
<p class="article-cta">
อยากรู้ว่าธุรกิจของคุณควรเริ่มใช้ AI ตรงไหนก่อน?
แชทกับทีม Jedi ผ่าน LINE OA ได้เลย 👉
<a href="https://lin.ee/BGWbFrEJ" target="_blank" rel="noopener">ทัก LINE OA</a>
</p>
```

Placement:

- soft CTA after intro or around 30% scroll
- strong CTA at article end
- keep existing manual CTAs when present

### P1.3 Add FAQ sections + FAQ schema

Problem:

- 170 / 198 pages have no FAQ.
- 52 / 80 real articles have no FAQ.

Generate 3–5 FAQs per real guide/comparison/review article:

- What is X?
- Who should use X?
- How much does X cost?
- X vs Y: which is better for Thai businesses?
- How should a CEO/SME start?

Emit `FAQPage` JSON-LD.

### P1.4 Expand 25 thin real articles below 2,500 chars

Examples:

- `04-08-openclaw-vs-claude-cowork` — 894 chars
- `openclaw-mac-studio-move` — 1268 chars
- `ai-tier-list-by-jedi` — 1293 chars
- `ai-agent-surprised-me` — 1305 chars
- `save-20-hours-per-week-ai-tools` — 1344 chars
- `future-of-ai-in-thailand` — 1364 chars
- `deepseek-shocked-the-world` — 1478 chars
- `3-ai-systems-ceo-must-build-2026` — 1539 chars
- `9-ai-tools-business-owners-must-know` — 1644 chars

Minimum expansion standard:

- 800–1,200 Thai words or equivalent
- clear intro
- 3–5 H2s
- practical bullets/checklists
- Thai business owner examples
- internal links
- CTA
- FAQ

### P1.5 Improve heading structure

Important examples:

- `ติดตั้ง-hermes-agent-ai-agent-ที่ดีที่สุด` — 12,718 chars but only 1 H2.
- `chatgpt-codex-vs-claude-cowork` — 5,969 chars but only 1 H2.
- `openclaw-vs-claude-cowork` — 894 chars, only 1 H2.
- `ai-changing-humanity-not-just-jobs` — 3,867 chars, only 1 H2.
- `02-16-sam-altman-personal-agents-next-era` — 2,869 chars, only 1 H2.

Normalize body structure:

```html
<h2>เรื่องนี้หมายความว่าอะไร</h2>
<h2>ประโยชน์หลักสำหรับธุรกิจไทย</h2>
<h2>วิธีนำไปใช้จริง</h2>
<h2>ข้อผิดพลาดที่ควรระวัง</h2>
<h2>ขั้นตอนถัดไปที่แนะนำ</h2>
<h2>FAQ</h2>
```

---

## P2 fixes

### P2.1 Rewrite overlong titles and meta descriptions

Titles:

- 68 / 198 titles over 60 chars.
- 30 / 198 titles over 70 chars.

Bolt should add separate `seoTitle` field instead of forcing visible H1 shorter.

Target:

- SEO title: 45–60 chars when possible
- H1 can remain longer if useful

Meta descriptions:

- 23 / 198 excerpts exceed 160 chars.
- 1 excerpt under 80 chars.

Add separate `metaDescription` field:

- 120–155 chars
- Thai-first
- keyword included
- benefit clear

### P2.2 Body image/media optimization

Corpus reports 0 body images across 198 articles. Hero YouTube thumbnails exist, but no in-body visuals.

For high-value guides and comparisons, add:

- comparison tables
- screenshots/tool UI images
- diagrams/checklists
- descriptive `alt` text
- explicit width/height to reduce CLS
- explicit `og:image`

### P2.3 Slug policy and URL hygiene

71 non-ASCII slugs exist. Thai slugs are valid but harder to share/debug.

Policy:

- Do not break existing indexed URLs.
- Keep existing Thai slugs canonical stable.
- For new articles, prefer ASCII transliterated slugs.
- Add slug validation:
  - lowercase
  - no spaces
  - no duplicates
  - no raw YouTube IDs unless intentional
  - max ~70 chars

---

## Writing evaluator findings

The corpus has 60 non-stub articles >=2,000 chars. Approximate score distribution:

| Range | Count | Meaning |
|---|---:|---|
| 70–84 | 6 | Strong / closest to Limitless standard |
| 60–69 | 13 | Useful but needs sharper thesis/mechanism |
| 50–59 | 24 | Average SEO/transcript-derived article |
| 33–49 | 17 | Weak / generic / rewrite-priority |

Median non-stub score: ~55/100.
Mean non-stub score: ~56/100.
Best observed score: ~84/100.
Worst observed score: ~34/100.

## Strongest current articles

### 1. `ติดตั้ง-hermes-agent-ai-agent-ที่ดีที่สุด` — ~80–84

Why it works:
- Specific tool.
- Strong personal conviction.
- Practical promise.
- Founder/operator voice.

Rewrite pattern:
> “Why I replaced X with Hermes Agent — and the exact setup I use to run my business.”

### 2. `ai-agents-sme-thai-2026` — ~76–79

Rewrite pattern:
> “5 AI agents every Thai SME should deploy before hiring the next employee.”

### 3. `ai-trends-sme-thai-2026` — ~75–78

Rewrite pattern:
> “5 irreversible business physics changes for Thai SMEs.”

### 4. `ai-operating-system-claude-cowork` — ~74–77

Rewrite pattern:
> “Stop using AI as an app. Build an AI operating system for your company.”

### 5. `ai-agent-team-expansion` — ~73–76

Rewrite pattern:
> “Before hiring your next employee, build these 3 AI roles first.”

### 6. `ai-agent-review-150-days` — ~70–73

Rewrite pattern:
> “150 days with AI agents: what actually worked, what broke, and what I would deploy again.”

## Top 10 priority slugs to rewrite for quality

| Priority | Slug | Rewrite angle |
|---:|---|---|
| 1 | `chatgpt-codex-vs-claude-cowork` | “Codex beats Claude Cowork when the job is execution, not conversation.” |
| 2 | `nXuwdvn12M0` | “Connect Claude Cowork to business data: the missing bridge between AI chat and real management decisions.” |
| 3 | `chatgpt-codex-vs-claude-cowork-vs-google-antigravity` | “I gave Codex, Claude Cowork, and Gemini the same business task. Only one behaved like an employee.” |
| 4 | `02-23-what-can-claude-cowork-do` | “Claude Cowork is not a chatbot. It is a junior operator inside your computer.” |
| 5 | `ai-changing-humanity-not-just-jobs` | “AI does not replace jobs first. It changes the cost structure of building a company.” |
| 6 | `what-we-use-ai-for` | Evergreen “AI use-case selection” framework. |
| 7 | `02-22-openclaw-took-6000-baht` | Founder risk/control story. |
| 8 | `three-google-ai-tools-underrated` | “Which workflow to deploy” article. |
| 9 | `02-18-india-singapore-thailand-ai-race` | Direct implications for Thai SMEs. |
| 10 | `02-27-claude-cowork-five-employees` | “AI = 5 employees” promise with proof, roles, limits, implementation path. |

---

## Rewrite principles

### 1. Replace generic SEO openings with founder tension

Weak:
> “ในยุคที่ AI พัฒนาอย่างไม่หยุดยั้ง การเลือกเครื่องมือที่เหมาะสม...”

Better:
> “ถ้าคุณยังใช้ AI แค่ถามตอบ คุณไม่ได้มีผู้ช่วย คุณมีภาระงานเพิ่มอีกหนึ่งช่อง.”

### 2. Every article needs one sharp thesis

Strong thesis examples:

- “AI Agents are not better chatbots; they are the first affordable middle managers for SMEs.”
- “The next hire in your company should be a workflow, not a person.”
- “Most Thai SMEs do not have an AI problem. They have a delegation problem.”
- “The winner is not the tool with the best model. It is the tool that reduces owner bottleneck fastest.”

### 3. Move from tool review to business mechanism

Better structure:

1. Business owner has bottleneck.
2. Old way costs time/headcount.
3. AI mechanism changes the cost curve.
4. Tool comparison through that mechanism.
5. Decision rule.

### 4. Add “Monday morning” action paths

Every article should answer:

- What should the owner do today?
- What should they delegate first?
- What should they not automate?
- What metric proves it is working?
- What failure mode should they watch?

Recommended ending:

- Day 1: choose one bottleneck.
- Day 2: document current workflow.
- Day 3: build first AI role.
- Day 4: test on old work.
- Day 5: add human approval.
- Day 6: measure time/cost saved.
- Day 7: decide whether to scale or kill.

### 5. Use Thai business-owner specificity

Examples to inject:

- LINE OA lead handling
- Facebook Ads reporting
- Shopee/Lazada product listing
- clinic appointment follow-up
- real estate lead qualification
- school/course sales pipeline
- factory quotation workflow
- restaurant review analysis
- accounting document preparation
- weekly CEO dashboard

### 6. Add tradeoffs and objections

Strong line pattern:
> “AI Agents are powerful, but they are dangerous in exactly the same way junior employees are dangerous: they move fast before they understand judgment.”

### 7. Turn personal stories into proof

Good raw material:

- 160-person company
- 2,000 students
- 150 days with AI agents
- ฿6,000 OpenClaw mistake
- 10–11 AI agents running business workflows
- 100,000 YouTube subscribers

Story structure:

1. What happened.
2. What I believed before.
3. What broke.
4. What principle I learned.
5. How the reader applies it.

### 8. Avoid repeated generic phrases

Replace:

- “ในยุคที่ AI...”
- “เปลี่ยนแปลงอย่างรวดเร็ว”
- “ยกระดับธุรกิจ”
- “ปลดล็อกศักยภาพ”
- “ก้าวกระโดด”
- “เครื่องมือที่เหมาะสม”
- “มีประสิทธิภาพ”
- “เจาะลึก”

With operational language:

- ลดเวลาตัดสินใจ
- ลดงานเจ้าของ
- ลดจำนวนรอบแก้งาน
- เพิ่ม lead response speed
- ลด CAC
- เพิ่ม conversion
- สร้าง weekly dashboard
- ทำให้ทีมเล็กทำงานเหมือนทีมใหญ่

---

## Highest-impact Bolt work order

1. Hide/noindex 118 stub articles and remove from sitemap until real content exists.
2. Fix duplicate `ai-tier-list-by-jedi` slug.
3. Add per-article SEO metadata, canonical, OG/Twitter, Article/Breadcrumb/Video/FAQ schema.
4. Add automatic internal links + related article blocks.
5. Add default LINE CTA module to every real article.
6. Generate FAQ sections for real guide/comparison/review articles.
7. Expand 25 thin-but-real articles under 2,500 chars.
8. Rewrite long SEO titles and long excerpts using separate `seoTitle` / `metaDescription` fields.
9. Normalize H2/H3 structure across long articles.
10. Add image/table modules for pillar content.

## Acceptance criteria

- Live/repo article count reconciled; no production article loss.
- 0 duplicate slugs.
- 0 indexed stub pages.
- Per-article SEO head tags implemented or SSG/prerender plan created.
- Real articles have CTA, internal links, FAQ where appropriate, readable title/meta.
- Blog builds and renders cleanly.
- Sitemap excludes stubs/noindex pages.
- Handoff back to Blaze/Kelly includes changed counts, deploy URL, and any articles needing human review.

## Safe deployment recommendation

Because this touches SEO and live production content, Bolt should produce a preview branch/deploy first. Production deploy should wait for Jet approval unless Jet explicitly says to push immediately.
