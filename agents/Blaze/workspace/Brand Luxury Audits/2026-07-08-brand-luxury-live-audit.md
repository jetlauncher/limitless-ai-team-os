# Brand Luxury 1% Live Audit — YouTube (deep-dive) — 2026-07-08

## Scope
- Focus surface: YouTube `youtube.com/@jeditrinupab`
- Rotation rationale: 2026-07-07 audit was YouTube (banner, thumbnails). Today's rotation calls for Instagram, but IG requires login and the logged-out surface returned a sign-up wall — live access blocked. Per protocol, when one priority channel is inaccessible, deepen the accessible priority channel rather than pivoting to non-priority surfaces (X, website, Notion). This audit targets **two areas not covered in yesterday's report**: Playlist curation system and Channel description/metadata hierarchy.
- Live access: Public YouTube channel + Playlists page loaded successfully in logged-out browser. No sign-in, profile edits, posting, scheduling, publishing, ads, payment, or permission dialogs were touched.

## First-impression read (deep-dive)
Yesterday's audit established that the biggest luxury gap is visual noise in banner and thumbnails — already flagged for a draft v2. Today's focus: **system-level signals of premium** that viewers notice subconsciously after scrolling past the hero section.

1. **Playlist page is cluttered with 20+ uncurated, inconsistently named channels.** This creates a "content warehouse" feeling rather than an "editorial library."
2. **Channel description starts with a Line OA CTA**, putting commercial intent first and authority second. The hierarchy of the About section signals what Jet's channel is about before anyone clicks anything.

## Visible observations

### 1) Playlist page: editorial disorganization
- **What I see:** 20+ playlist cards including `AI Agents`, `Students work`, `OpenClaw`, `Claude Cowork`, `AI`, `Jedi Mindset`, `Daily High Podcast`, `Meet the Peak`, `5 Mins with CEO`, `Hacking 101`, `Daily life hack`, `The peak podcast`, `Peak story`, `CEO on the go` — and more (total list truncated in snapshot). Many are single-topic or tool-specific, some are podcast series, a few appear to be personal project tags.
- **Why it matters for luxury:** Premium channels curate; chaotic channels catalog. When a new visitor lands on Playlists and sees 20+ entries with no grouping hierarchy, the signal is "lots of content" not "thoughtful education." Luxury brands organize their library into chapters or volumes — not shelves.
- **Specific issues:**
  - No clear "Start Here", "Course Series", or "Best Of" hero playlist at the top.
  - Tool-specific playlists (`OpenClaw`, `Claude Cowork`) mixed with evergreen concepts (`Jedi Mindset`).
  - Podcast series names are inconsistent (`Daily High Podcast` vs `The peak podcast` vs `Peak story` — likely overlapping).
  - No editorial naming convention: some Thai, some English, no consistent bracket/label system.

### 2) Channel description hierarchy: CTA before authority
- **What I see:** First visible line in the "About" section reads: `เช็ครอบอบรมกับทีมผม Line OA 👉 https://lin.ee/4v2Xsum`. This puts contact/sales first — immediately — with no establishing of who Jet is, what Limitless Club stands for, or why a visitor should trust before they see the CTA.
- **Why it matters for luxury:** Expensive brands establish authority and identity before any ask. The first sentence of your channel description is your elevator pitch to a cold visitor. Leading with sales undermines perceived status even if the conversion rate might be slightly higher (probably not — it likely signals "salesy" instead of "premium").
- **Current state hierarchy vs ideal:** Current: CTA → Link tree button → Subscribe → Community → Videos tab chain. Ideal: Authority line → Mission/offer line → Social proof → CTA → Links.

### 3) Thumbnail system inconsistency (refresh observation)
- **What I see (same as yesterday but refined):** Recent thumbnails alternate between urgent/news style (large faces, yellow Thai text on dark), and `[Full Course]` educational thumbnails — but the `[Full Course]` thumbnails lack a consistent template. Some use different font weights, some have app-screenshot backgrounds with arrows/X-mark overlays, others are solid-color portraits.
- **Refinement from yesterday:** Yesterday flagged this broadly. New insight: YouTube's own `i.ytimg.com/vi/` thumbnail URLs reveal that some thumbnails have custom artwork (`hqdefault_custom.jpg`) while others use YouTube's auto-generated frames (`hqdefault.jpg`). For luxury, custom thumbnails should ALWAYS be used — never rely on auto-frames. The mix of custom and auto suggests manual upload inconsistency.

### 4) Channel metadata: missing editorial framing
- **What I see:** Channel name is `Jedi Trinupab`, handle is `@jeditrinupab`. No channel tagline appears in the YT metadata row (name + handle line). This is YouTube's most-minimal branding surface — it should read like a masthead. Currently reads as just a personal name, which feels more "influencer" than "founder-media institution."
- **Why it matters:** Look at how premium media brands structure this: they either include the brand (e.g., "Lex Fridman | AI & Philosophy") or have an iconic visual anchor that does the framing. Jet's channel currently depends on the banner for brand context — but many mobile viewers see name + subscriber count before the banner loads or in mini-player mode.

### 5) Shorts vs Videos page clarity gap
- **What I see:** The `Shorts` tab exists but is a flat feed. No branded cover system, no series labels. Shorts appear to be recycled YouTube content without distinct editorial packaging.
- **Luxury implication:** Shorts are the cheapest real estate on YouTube right now, meaning they offer the highest ROI for brand injection. But they should feel like "Limitless Club shorts" not generic repurposed clips.

## Micro-upgrades

### 1) Collapse playlists into a structured 6-channel editorial library
- **Exact change:** Reorganize all existing playlists into exactly 6 curated categories, re-name them editorially, and reorder so the most premium/evergreen comes first:
  1. `Start Here: Build With AI` (new hero playlist — best of Jet + foundational content)
  2. `Full Courses` (group all `[Full Course]` videos under one clean series label)
  3. `AI Operating System` (evergreen AI/agent education, formerly "AI Agents" + "AI")
  4. `Founder Strategy` (`Jedi Mindset` + student work + case studies)
  5. `Podcast & Conversations` (merge `Daily High Podcast`, `The peak podcast`, daily life hack, Peak story into one channel)
  6. `Tool Notes` (all tool-specific content — OpenClaw, Claude Cowork, etc.)
- **Why it increases luxury association:** Six well-named channels = an expensive publication's editorial structure vs a warehouse inbox. It forces discipline on future uploads and creates instant navigation clarity for high-intent visitors. This is what premium media brands do (Harvard Business Review's "Management," "Innovation," "Leadership" etc.) — they curate, they don't accumulate.
- **Quick implementation note:** Delete or merge low-value playlists (`Meet the Peak`, `5 Mins with CEO`, `Hacking 101`, `CEO on the go` — these dilute the signal). Keep only videos that serve the visitor journey. Draft playlist cover art in Midnight Luxe Editorial style (charcoal base, white serif title number [I-VI] in gold foil accent, 235px each for YT).
- **Priority:** HIGH

### 2) Rewrite the channel description into authority-first hierarchy
- **Exact change:** Draft new About section text with this structure:
  ```
  Jet Trinupab helps Thai founders and operators use AI to expand their teams, build personal brands, and create automated systems that compound.
  
  Limitless Club — founder-tier AI education. 
  Full courses • Live training • Community

  📺 New videos every week
  💼 Training registration → https://lin.ee/4v2Xsum
  🔗 Join our community: lin.ee/4a9Tnz7
  
  (keep remaining existing text below these lines)
  ```
- **Why it increases luxury association:** Authority before ask. The first two sentences define Jet's offer in institutional language ("helps Thai founders and operators" not "check registration"). The channel name `Jedi Trinupab` gets contextualized by the description — transforming from a personal account into a founder-media brand. This is how premium brands signal status: they don't sell, they describe what they do.
- **Quick implementation note:** Draft text for Jet approval. Two-line structure works on mobile without truncation (YT About first line = 101 chars before "...more"). Test both Thai and English versions.
- **Priority:** HIGH

### 3) Standardize ALL thumbnails to custom artwork — kill auto-frames
- **Exact change:** Audit the last 20 uploaded videos' thumbnail source URLs. Any that are `hqdefault.jpg` (auto-frame) need a custom thumbnail designed in the brand system. For future uploads: mandate 100% custom thumbnails only, no exceptions.
- **Why it increases luxury association:** Auto-generated frames look like "YouTube just grabbed a frame." Custom thumbnails always = intentional production. A premium channel where even mid-tier videos have bespoke visuals signals consistent investment — and that consistency creates perceived value across the entire catalog, not just viral hits.
- **Quick implementation note:** Check thumbnail source URLs via `browser_get_images` on several video pages (I already see a mix). For future uploads: build a Canva/Figma template with brand grid, type scale, and bronze accent rule — export to 1280x720 JPG at quality 90+.
- **Priority:** MEDIUM-HIGH

### 4) Add a channel tagline under the name (YT's "Channel Handle + Tagline" feature if available, or rely on description first line)
- **Exact change:** If YouTube offers a channel tagline field in Channel Settings > Basic Info, add: `Founder | AI Education | Limitless Club`. If not visible, rely on the description-first-line rewrite (#2) to fill this space. In all cases: ensure Jet's name appears alongside "Limitless Club" consistently (banner, description header, Community posts).
- **Why it increases luxury association:** YouTube's handle line is the only text-based brand surface that never changes — unlike banners, which get scrolled past. A tagline anchors your category + authority permanently at the top of the channel. It transforms "Just a name" to "Name + What We Do."
- **Quick implementation note:** Check YT Studio > Customization > Basic Info for tagline field. Draft: `Founder | AI Systems for Thai Entrepreneurs`. Keep it under 40 characters if possible for mobile readability.
- **Priority:** MEDIUM

### 5) Create a "Start Here" hero playlist with branded cover art
- **Exact change:** Build one "hero" playlist featuring 5-7 of Jet's strongest evergreen videos (e.g., the 51K-view AI Agent guide, the 25K-view "AI in 25 min," a Full Course pillar video) under the title `Start Here: AI สำหรับเจ้าของธุรกิจ` with a custom cover art card.
- **Why it increases luxury association:** Premium channels always have a hero entry point. It signals to new visitors that Jet has curated where to begin — reducing overwhelm and creating an intentional first experience. This is "concierge" design vs "self-serve warehouse."
- **Quick implementation note:** Use cover art (1060x595px) in Midnight Luxe Editorial: charcoal background, one serif headline ("Start Here"), thin bronze rule line, gold `Limitless Club` footer. Pull best evergreen content from existing library — no new video production required.
- **Priority:** HIGH

## Today's recommended 1% upgrade
**Collapse the playlist page into a structured 6-channel editorial library + create the "Start Here" hero playlist.**

Why this is the best move today:
- The Playlists page receives high-intent visitors who want to explore Jet's education system. Currently it signals "warehouse" (20+ disorganized entries), not "library" (curated channels).
- This requires ZERO new content production — entirely a reorganization and naming exercise using existing assets.
- A well-structured playlist page is a compounding luxury asset: every new video upload benefits from the editorial context, and it shapes how Jet's channel looks when Google indexes it.
- The "Start Here" hero playlist doubles as an instant onboarding experience for cold traffic — which is what most of Jet's 110K subscribers originally experienced.

## Morning brief summary
- Audited channel: YouTube (second-dive: Playlists + Description hierarchy)
- Instagram live access blocked (logged-out sign-up wall)
- Saved file path: `/Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Brand Luxury Audits/2026-07-08-brand-luxury-live-audit.md`
- Winning 1% upgrade: collapse playlists into a 6-channel structured editorial library + create "Start Here" hero playlist
- What to change: 
  - Consolidate 20+ messy playlists → 6 curated channels with editorial names
  - Build one hero "Start Here" playlist with branded cover art (charcoal, serif title, bronze rule)
  - Use only existing content — zero new video production needed

## Notes from previous daily audit
- Previous audit (2026-07-07): Banner v2 cleanup, thumbnail tier system, series naming tighten, description hierarchy restructure. Today extends on those recommendations into Playlists reorganization and full About-section rewrite.
