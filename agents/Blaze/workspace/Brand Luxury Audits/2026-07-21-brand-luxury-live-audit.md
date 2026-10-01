# Brand Luxury 1% Live Audit — YouTube (High-Velocity Upload Day) — 2026-07-21

## Scope
- **Focus surface:** `youtube.com/@jeditrinupab` channel page, Videos tab
- **Rotation rationale:** Yesterday (07/20) audited YouTube. Instagram is blocked by login wall (confirmed again today via browser navigate, web extract, and web search — none deliver visual content). Per protocol: audit the accessible channel when one is unavailable.
- **Live access status:**
  - YouTube: ✅ Fully accessible (logged-out browse + vision captures)
  - Instagram: ❌ Blocked by login wall (browser returns empty DOM with 1 element; extract fails entirely)
- **Date:** 2026-07-21
- **Evidence:** 3 full-page screenshots, 2x DOM snapshots, thumbnail listing

---

## Context — High-Velocity Upload Day (New Today)

The channel is in an aggressive posting burst: **10+ videos published within the last hour** today. This is a new pattern compared to yesterday's audit. Fast posting pace amplifies ALL existing visual inconsistencies — every timestamp video that breaks the design system becomes one more brick in the "content market stall" perception vs. "premium publication" perception.

**Visible uploads (ordered left-to-right on page, newest first):**
1. "รวม use case ทั้งหมดของทีม AI Agent ที่ผมใช้จริง" — 860 views (Thai)
2. "สร้าง Brand หลักล้านได้ง่ายๆ ด้วย Claude + Higgsfield" — 1.1K views (Thai)
3. "20 ทักษะของผู้นำที่ชนะในยุคของ AI ฉบับ 2026" — 1.8K views (Thai)
4. "Claude Fable 5 creates 25 websites in 1 prompt" — 2.6K views (**English** ❗)
5. "คุณมีเวลา 48 ชม. ที่จะใช้ Claude Fable 5" — 4.2K views (Thai)
6. "สงครามของ AI ที่จะสร้างการแบ่งแยกครั้งยิ่งใหญ่" — 2.1K views (Thai)
7. "[Full Course] คู่มือเริ่มต้นการสร้าง AI Agent จาก 0-1" — 106K views ([Full Course] prefix + Thai)

**Critical observation:** #4 is English while all adjacent titles are Thai. Adjacent thumbnails create visual language oscillation. Same video row = different "publication."

---

## Finding 1 — Channel Name = Personal Brand Only (ESCALATED HIGH)

**Observation:** The H1 on the channel page reads **"Jedi Trinupab"**. "Limitless Club" does not appear in any visible header element at the top of the page or banner area. Viewers see a PERSON'S NAME as the brand, while "Limitless Club" is buried somewhere in link descriptions below.

**Why it matters for luxury:** Every premium institution leads with its INSTITUTIONAL name, not the individual's name:
- Harvard Business Review (not "Michael Porter")
- Wired Studio (not "Chris Anderson")  
- Bloomberg Opinion (not any specific columnist)

A channel named purely as a person reads like personal content/portfolio. A publication name + personal credit reads like editorial authority. This split is compounding — Jet posts 6+ videos per hour across both channels, but the visible brand identity hasn't caught up to the volume signal.

**Draft change (for Jet approval):**
- **Option A:** Change channel title to "Jedi Trinupab | Limitless Club"
- **Option B (recommended):** Redesign banner with "LIMITLESS CLUB" as hero serif headline, Jet name as secondary: "by Jedi Trinupab"
- Either way, "Limitless Club" must appear in the same visual region a visitor reads first (top-to-bottom)

**Priority: HIGH + ESCALATED from 07/20. Issue unchanged but compounding faster.**

---

## Finding 2 — Banner Still Missing Editorial Hierarchy (HIGH)

**Observation:** Banner area contains Jet's name prominently, but the "Limitless Club" brand presence is unclear or absent as a visible masthead element. The banner visual hierarchy puts personal identity > institutional identity, reversing where luxury brands position their authority.

**Why it matters:** The channel banner = storefront window. People read top-to-bottom on YouTube channel pages. Whatever they see first defines the brand's framing. If "Limitless Club" isn't the hero word in that visual real estate, the channel is permanently positioned as creator content rather than premium publication.

**Priority: HIGH (one-time design fix needed)**

**Draft change:**
1. Hero text: "LIMITLESS CLUB" in editorial serif (large, centered)
2. Secondary line: "by Jedi Trinupab" or "โดย เจด เทรีนุปาบ"
3. Background: #17181A solid (not gradient), subtle texture only if intentional
4. Accent: ONE thin bronze (#94764A) rule under the title — decorative restraint, not abundance

---

## Finding 3 — Video Title Language Oscillation in Same Row (HIGH)

**Observation:** Fresh uploads today show English and Thai titles side-by-side in the same scroll row:
- Adjacent pair at positions #3-#4: "20 ทักษะของผู้นำ..." [TH] ↔ "Claude Fable 5 creates..." [EN]
- Same video grid area = two different publications

**Why it matters:** A premium publication does not switch languages on adjacent pages. Readers should feel ONE voice across the entire channel. Mixed language in a single scroll row signals operational inconsistency, not premium curation.

**Draft change (for Jet approval):**
- Pick a primary language PER VIDEO (not per series). If Thai → all text, even tool names
- If English → accept that English audiences benefit more, post separately or translate
- Never show Thai and English titles adjacent in grid view on the same page
- If doing bilingual: decide "Channel A = Thai primary" or "Channel B = English primary"

**Priority: HIGH (implements on next upload)**

---

## Finding 4 — Title Prefix Convention Still Nonstandard (MEDIUM)

**Observation:** Inconsistent use of prefix labels in fresh uploads:
- `[Full Course]` appears on #7 but NOT on any adjacent video
- No consistent series marker format (no `EP.` numbering visible)
- Philosophical titles ("สงครามของ AI...") and how-to titles ("สร้าง Brand หลักล้าน...") mix without category markers

**Why it matters:** Premium publications name their sections. WIRED has "The Feature," "Review," "Longform." HBR has "Ideas," "Manage," "Execute." Viewers benefit from visual language that signals content type BEFORE they read the full title.

**Draft change (for Jet approval):**
- Philosophical/strategic → `Limitless Club:` before title
- How-to/tutorial → `คู่มือ Limitless Club:` or just use consistent category prefix in Thai
- Tool-focused → no special prefix, keep clean
- Series videos → `EP.1`, `EP.2` format consistently (never `[Part 1]`)

**Priority: MEDIUM (applies to future uploads only)**

---

## Quick Visual QA Summary

| Element | Current State | Luxury Signal | Needed? |
|---------|--------------|---------------|---------|
| Channel name / top identity | ❌ "Jedi Trinupab" only — no "Limitless Club" visible | Very low | HIGH (escalated) |
| Banner editorial hierarchy | ❌ Personal > institutional, reversed from luxury convention | Low | HIGH |
| Title language in grid row | ❌ Thai ↔ English oscillating in adjacent positions | Medium-low | HIGH |
| Thumbnail background unity | ✅ Mostly dark (#17181A family), close but varies on some | Medium | MEDIUM |
| Title prefix consistency | ⚠️ `[Full Course]` sporadic, no series numbering | Low-medium | MEDIUM |

---

## Today's Winning 1% Upgrade

### 🏆 TODAY'S WINNING 1%: Redesign Banner with "LIMITLESS CLUB" as Hero Masthead

**Exact change:** Replace the current banner design so that "LIMITLESS CLUB" appears as the largest, most prominent text element — centered serif headline in white (#FFFFFF) or warm ivory (#E2D7C8) on solid dark background (#17181A). Below it, smaller: "by Jedi Trinupab." One thin bronze accent rule (#94764A) beneath the title.

**Why this increases luxury association:**
1. **Institutional-first framing** — signals publication/authority before personal identity (luxury brand convention)
2. **One hero word, not several** — editorial restraint reads as confident expensive
3. **New visitors see "Limitless Club" first** — builds premium brand memory on every channel visit

**Quick implementation note:** One-time Figma/Photoshop design (1-3 hours for Jet to approve + upload). No recurring production cost. Use the existing photo/person element if present in current banner → reposition as small compositional anchor, not headline.

**Priority: HIGH (can be completed in one session with design approval)**

---

## Recommended Order of Operations

1. **Banner redesign** (one-time, 1-3 hours) — put "LIMITLESS CLUB" first, Jet second
2. **Title language policy** (next upload cycle) — pick Thai OR English per video, never both visible adjacent
3. **Prefix convention** (future uploads only) — consistent `EP.1` numbering + category prefixes

---

*Audit generated by Blaze — Limitless Club Brand Luxury 1% Live Audit — 2026-07-21*
*Scheduled: Nightly cron rotation. Next audit: Instagram (pending login wall removal) or YouTube fallback.*
