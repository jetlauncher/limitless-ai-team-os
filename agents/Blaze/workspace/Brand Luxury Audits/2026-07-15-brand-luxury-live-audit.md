# Brand Luxury 1% Live Audit — YouTube Channel Surface — 2026-07-15

## Scope
- **Focus surface:** YouTube `youtube.com/@jeditrinupab`
- **Rotation rationale:** 2026-07-14 covered Instagram profile. Per rotation, today focuses on YouTube.
- **Access:** Page loaded successfully in logged-out browser. Screenshots captured for analysis only. No sign-in, profile edits, posting, scheduling, publishing, ads, payment, or permission dialogs were touched.
- **Stats observed:** 117K subscribers, 1.3K videos, verified.

---

## First-impression read: Authoritative channel, luxury leaking at the edges

At 117K subscribers with a clear mission banner ("คนไทย 1,000,000 คนต้องเก่ง AI") and consistent high-value AI content, the channel has real weight. The avatar is a clean professional headshot with dramatic lighting. Limitless Club branding appears in the banner. The content itself is premium — full courses, tool comparisons, founder education.

But the luxury gap is in **visual discipline on the surface layer**. The underlying brand is strong; the packaging is creating friction. Here are 5 micro-upgrades.

---

## Micro-upgrades

### 1. Remove the fake red SUBSCRIBE button from the channel banner

**Exact change:** Redesign the banner without the red YouTube-style "SUBSCRIBE" button graphic that's currently baked into the banner art.

**Why it increases luxury association:** A fake Subscribe button painted onto the banner is the single most anti-luxury element on the entire channel. It mimics a cheap "YouTube growth hack" aesthetic, it's redundant (the real Subscribe button is pixel-inches away), and it creates visual dissonance against the otherwise premium dark/stage-photo banner. Luxury brands never add fake UI to their real estate — they trust the real UI to do its job. Removing this single element instantly elevates the banner from "growth-hacker channel" to "established media brand."

**Implementation note:** Design v2 banner in the Midnight Luxe Editorial system. Same stage photo, same mission text, same Limitless Club + Jedi logos. Just remove the red Subscribe graphic. Keep the banner clean. Takes ~15 minutes in Figma/Canva, then one profile edit (draft for Jet approval).

**Priority:** HIGH — one edit, immediate visual impact, affects every single profile visit.

---

### 2. Unify thumbnail backgrounds to dark/charcoal palette

**Exact change:** Establish a rule that all future thumbnails use `#17181A` (near-black) or `#2A2A2E` (charcoal) as the base background. Existing thumbnails with white or bright-colored backgrounds should not be reuploaded (too much loss of established views), but every new upload follows the dark rule.

**Why it increases luxury association:** The current thumbnail grid has a "checkerboard" effect — thumbnails alternate wildly between dark backgrounds, white backgrounds, blue gradients, orange, and green. This creates visual vibration that reads as chaotic. A curated publication uses a consistent base canvas. The Midnight Luxe system already defines `#17181A` as the brand background. When someone scrolls the video grid and sees consistent dark backgrounds with controlled accent colors, the channel reads as intentional, not accidental.

**Implementation note:** No need to reupload old thumbnails. Apply the dark-background rule to the thumbnail template going forward. Use bronze `#94764A` as the rare accent (not every thumbnail needs it). Test for 4 weeks, evaluate grid cohesion visually.

**Priority:** HIGH — compounds with every new upload. Zero cost to implement, permanent brand benefit.

---

### 3. Establish a thumbnail typography system: one font, consistent placement

**Exact change:** Choose one typeface for all thumbnail text (recommend: the same editorial serif used in Midnight Luxe for headlines, OR a clean heavy sans-serif like Inter/Roboto for maximum legibility at small sizes). Standardize placement: headline always bottom-left or always centered, never drifting. Max 2–3 Thai words per thumbnail.

**Why it increases luxury association:** Currently, thumbnail fonts vary wildly — some use bold shouting sans-serif, some use thinner elegant fonts, Thai and Latin scripts mix with no hierarchy, text placement drifts from center to bottom-left to scattered. Every luxury brand has a typographic grid. Thumbnail text that follows consistent rules (same font, same weight rules, same placement zone) creates an unconscious "this is a professional operation" signal. Random fonts signal "uploaded whenever, however."

**Implementation note:** Add to the existing thumbnail template. Document the rule: "Font = X, size = Y, placement = always bottom-left, max words = 3 Thai / 5 English." Apply to new uploads only to avoid reuploading existing content.

**Priority:** MEDIUM-HIGH — requires design discipline upfront but compounds forever. Pairs with micro-upgrade #2.

---

### 4. Fix the Shorts section rendering gap

**Exact change:** The Shorts section currently renders as an empty header with a row of text-only titles below it (visible in the current page state: "ChatGPT is really playing hardball," "AI is not as hard as you think," etc.) with no accompanying vertical video thumbnails. Investigate if this is a YouTube rendering issue (may resolve with login/region) or a content packaging problem. If it's packaging: ensure all Shorts have custom cover frames.

**Why it increases luxury association:** An empty section header with floating text titles looks like a loading error or a half-finished page. Luxury interfaces are never partially loaded — every section delivers what it promises. If the Shorts section appears broken to visitors, it undermines confidence in the entire channel's polish.

**Implementation note:** Check in a logged-in session and different region/browser. If this is a YouTube-side caching bug, no action needed. If it's a content gap, add simple dark cover frames to unbranded Shorts using the existing Midnight Luxe template (headline + black background + @jeditrinupab footer). 10 minutes per Short.

**Priority:** MEDIUM — may be a transient YouTube bug, but worth verifying. If real, it's a visible credibility gap.

---

### 5. Remove emojis from Community Posts

**Exact change:** In the Posts section, the current posts use emojis like 🙏💙 in milestone and community text. Replace with clean text-only posts or use a single brand-appropriate symbol (e.g., a thin bronze horizontal rule between paragraphs) if visual separation is needed.

**Why it increases luxury association:** The Community tab is the cleanest part of the channel page right now — simple card layout, readable text. But the emojis undercut the premium founder/media positioning. They signal "casual creator" not "Limitless Club." Premium brands communicate warmth through word choice, not pictographs. The content (100K subscriber感谢, milestone posts) is important — it should be presented with the same editorial restraint as the rest of the brand.

**Implementation note:** This is a forward-looking rule, not a re-edit of historical posts. Add to the channel's posting guidelines: "Community posts: no emojis. Use clean text only. Line breaks and spacing for structure."

**Priority:** LOW — affects only the bottom of the channel page, but consistency matters for the brand memory audit.

---

## Today's 1% Upgrade: Remove the fake red SUBSCRIBE button from the channel banner

This is the single highest-ROI visual edit available. It takes 15 minutes, costs nothing, and immediately eliminates the one element on the channel that actively works against the premium positioning. Everything else in the banner is strong — the mission text, the stage photo, the Limitless Club branding. The fake red Subscribe button is the only thing dragging it down.

**Spec:**
- Same banner composition (stage photo + mission text + logos)
- Remove the red SUBSCRIBE graphic
- Keep the dark background, white/ivory text, Limitless Club mark
- Result: clean, confident, no-gimmick banner

Draft the v2 banner in the Midnight Luxe system and present for Jet approval before any upload.

---

## Summary

| # | Upgrade | Priority | Effort |
|---|---------|----------|--------|
| 1 | Remove fake red SUBSCRIBE from banner | HIGH | 15 min |
| 2 | Unify thumbnail backgrounds to dark palette | HIGH | Template change |
| 3 | Thumbnail typography system | MEDIUM-HIGH | Template change |
| 4 | Fix Shorts section rendering | MEDIUM | 10 min each |
| 5 | Remove emojis from Community Posts | LOW | Guidelines update |
