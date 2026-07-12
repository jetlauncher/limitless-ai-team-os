# Brand Luxury 1% Live Audit — Instagram Carousel System (Local Asset Audit) — 2026-07-12

## Scope
- **Focus surface:** Instagram `instagram.com/jeditrinupab` — carousel / post creative system
- **Rotation rationale:** 2026-07-06 was the last Instagram live audit; 2026-07-10 covered YouTube. Per rotation, today focuses on Instagram.
- **Live access:** Blocked. Instagram returned a blank screen in browser (login wall). `web_extract` refused the surface. Per protocol, audited local carousel assets under `/Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Assets/carousel-renders/` and local drafts as proxy for the IG creative system.
- **Assets examined:** 12 carousel render files (2 contact sheets + 20 slide jpgs from the Higgsfield-blaze system), plus 2 draft carousel text packages (2026-06-18 and 2026-06-16 Founder Field Notes).
- **No sign-in, profile edits, posting, scheduling, publishing, ads, payment, or permission dialogs were touched.**

---

## First-impression read: The carousel system is strong — but inconsistent between versions

The Higgsfield carousel renders are the most premium asset I've seen across all daily audits. They genuinely feel editorial: dark charcoal backgrounds, ivory Thai typography, restrained bronze accents, and consistent header/footer architecture. This system, if used for all future IG posts, would immediately elevate Jet's grid from "energetic creator feed" to "founder-media publication."

But there are two systems in circulation — Version A (contact-sheet-higgsfield.jpg) and Version B (hybrid_exact_text) — and they differ in small but visible ways. This creates a risk that if both go live, the grid will signal "two design teams" rather than "one brand."

---

## Micro-upgrades

### 1) Lock the Carousel System to ONE Version — Kill the Fork

**Exact change:** Choose Version A OR Version B as the canonical template. Delete or archive the other. Do not let two variants ship to Instagram. From vision analysis:
- **Version A** uses a textured/gradient charcoal background with crosshairs/gridlines and a central text card with a bronze border. Header: "LIMITLESS CLUB".
- **Version B** uses a flat black background with ghost Thai text behind the card and a white/glass-style border. Header has two lines ("CAROUSEL OS" + "LIMITLESS CLUB").

**Why it increases luxury:** Luxury brands have one system, not options. When followers see alternating grid tiles that are "almost the same but not quite," the signal is "inconsistent curation." The brain registers difference even when it cannot articulate it. Picking one variant eliminates the invisible brand leak.

**Quick implementation note:** My recommendation: **Version A.** It reads warmer and more editorial. The crosshair marks give it a blueprint/studio feel that is richer than Version B's flat black. Version B's glass border also reads "SaaS UI" (slightly generic). Archive Version B to `/Brand Luxury Audits/Archived/`.

**Priority:** HIGH — this must be decided before any carousel goes live.

---

### 2) Replace "START WITH CANVA" on Slide 10 with a Proprietary Framing

**Exact change:** On all carousel templates, change the CTA slide headline from "อย่าเริ่มที่ Canva" ("Don't start at Canva") to a proprietary frame. Example:
- "อย่าเริ่มที่ Canva เริ่มที่โครงสร้าง" → "ก่อนเปิด Canva มี 3 ข้อที่ต้องตอบ"
- Or more premium: "ระบบที่ควรเปิดก่อน Canva"

Alternatively, remove the Canva brand name entirely from the copy and frame it generically: "อย่าเริ่มที่โปรแกรม" ("Don't start in software").

**Why it increases luxury:** Naming Canva in a premium brand's content — even negatively — anchors the brand to Canva in the viewer's memory. It signals "we compete in the Canva tier." A true luxury brand never names its cheaper alternatives; it names what it aspires to be. Removing Canva from the slide makes the message about *structure*, not about software comparison.

**Quick implementation note:** Edit the CTA copy in the Figma template file. This takes 2 minutes and changes perception permanently across every future carousel.

**Priority:** MEDIUM-HIGH — subtle but permanently re-frames the brand tier.

---

### 3) Upgrade the Thai Typeface from System Sans to an Editorial Pair

**Exact change:** Replace the current Thai font (appears to be Sukhumvit Set / Kanit / Noto Sans Thai — a clean but very common Google Font) with a premium editorial pairing:
- **Thai Headline:** IBM Plex Sans Thai (cleaner, more geometric) or Anuphan (newer, more premium feel)
- **Body:** Same family, lighter weight
- **English metadata:** Keep the current Inter/Helvetica system — it works fine for small caps/labels

**Why it increases luxury:** The current Thai font is legible and clean, but it is the "default" Thai web font — it feels like a system font, not a chosen typeface. Premium brands commission or carefully select typefaces. The switch to IBM Plex Sans Thai or Anuphan costs nothing but changes the perception from "Google Font" to "editorial choice." This is what differentiates luxury from generic at the micro level: font selection is invisible until it's wrong.

**Quick implementation note:** Download IBM Plex Sans Thai (Google Fonts, free). Replace in Figma template. Re-export slides. No layout changes needed — the metrics are similar.

**Priority:** MEDIUM — takes a Figma template pass but the visual difference is measurable.

---

### 4) Tighten Footer System: Add "Limitless Club" to Every Footer, Not Just Header

**Exact change:** Add a quiet "LIMITLESS CLUB" micro-label to the footer line, creating a brand bookend:
- current footer: `@jeditrinupab  |  01 / 10`
- upgraded footer: `LIMITLESS CLUB · @jeditrinupab  |  01 / 10`

The "LIMITLESS CLUB" should be in warm ivory (#E2D7C8) at ~8px, same tracking as the header. The handle remains bronze (#94764A) or white.

**Why it increases luxury:** The header already says "LIMITLESS CLUB" and the footer says "@jeditrinupab" — but they never appear together as a unified brand sentence in the footer. By pairing them, every slide becomes a self-contained brand artifact that works even when cropped, shared out of context, or screenshotted. It's a signature, not just a handle. Luxury brands sign their work twice — once for recognition, once for memory.

**Quick implementation note:** One Figma master change affects all 10 slides in every template pass.

**Priority:** MEDIUM-Low — small but compounds with every share.

---

### 5) Create a Cover-Only "Grid Tile" Test Before Publishing

**Exact change:** Before any carousel post goes live, export the cover slide alone as a 1080x1080 JPG, place it on a mock 3x3 Instagram grid, and assess:
- Does it look like it belongs to *this* brand or could it be anyone's?
- Does it create a curiosity gap in 1 second?
- Is the Thai text readable at phone-screen size without zooming?

**Why it increases luxury:** The grid is the brand's first impression. A carousel cover that works as a full-screen 1080x1350 image may fail as a 1:1 grid tile (cropped, smaller text). Premium channels never ship covers that only work in isolation; they ship covers that work *in context* of the full grid. This is an editorial discipline, not a design problem.

**Quick implementation note:** Create a Figma template with a 3x3 grid placeholder. Drop the cover tile in the bottom-right position (where the most recent post appears). Assess on actual phone screen, not desktop.

**Priority:** MEDIUM — adds a 2-minute QA step per carousel but prevents grid dilution.

---

## Today's Recommended 1% Upgrade: Lock ONE Carousel Version & Archive the Other

**Why this one:**
- The fork between Version A and Version B is an invisible brand risk — if both ship, the grid will look inconsistent without knowing why
- It takes zero design work — just a decision and an archive action
- It compounds immediately: every future post uses one system, building recognition
- Version A is genuinely premium; the problem isn't quality, it's duplication

---

## Audit Notes
- The carousel system itself is the best creative output I've seen for Limitless Club so far — genuinely Midnight Luxe
- The Instagram live profile remains un-audited since 07-06; next audit with live IG access should focus on: actual grid first-impression, highlight cover consistency, bio evolution, Reel cover system
- YouTube was fully audited on 07-12 (subscribe button removal, thumbnail palette, expression system, course badge, description copy)
- All carousel assets examined are drafts — none confirmed posted to live Instagram
- The "Founder Field Notes" concept (2026-06-16) is a strong premium content series idea that could be a recurring IG format
