---
name: jedi-shape-first-carousel
description: "Create Jedi/Jet minimalist Thai Instagram carousels from transcripts using the proven 8-slide shape-first structure: first 3 slides illustrated with simple geometric shapes, slides 4-8 text-led, consistent header/footer, HTML/CSS Chrome rendering, and spacing QA."
version: 1.0.0
author: Kelly / Hermes Agent
tags: [jet, jedi, thai-carousel, instagram, transcript-to-carousel, html-rendering, minimalist-shapes]
---

# Jedi Shape-First Carousel

Use when Jet asks to create a new carousel based on a transcript in the minimalist Jedi/Limitless style discovered from the IG carousel workflow.

## Core format

- 8 slides, 1080×1350 PNG.
- Thai-first copy unless user asks otherwise.
- Render via **HTML/CSS + Chrome screenshots**. Do not use Pillow for final Thai text.
- First **3 slides** are concept/shape slides using simple geometry.
- Slides **4–8** are text-led lesson/CTA slides.
- Same header and footer on every slide.

## Current visual system

Use the current approved V5/V7 style unless user provides a new reference:

```css
--bg: #111f2a;      /* sampled from user reference image */
--cream: #f1ead7;
--soft: #b3bde2;
--soft2: #8493c4;
```

Fonts from Jedi brand page:

```css
headline: 'Trirong', serif;
body: 'Noto Sans Thai', 'Space Mono', sans-serif;
metadata: 'Space Mono', monospace;
```

Consistent chrome:
- Header top-left: `LIMITLESS CLUB`.
- Footer bottom-left: `@jeditrinupab`.
- Slide number bottom-right.
- Flat/near-flat dark background when user asks for sampled color.

## Narrative structure

1. **Shape slide / Hook** — one strong tension.
2. **Shape slide / False choice** — show the trap or wrong model.
3. **Shape slide / New model** — simple diagram/framework.
4. **Principle 1** — what the first part means.
5. **Principle 2** — what AI should carry.
6. **Principle 3** — what the human must audit.
7. **Proof / example / business-owner reframe** — make it concrete.
8. **CTA** — keyword comment.

For transcript conversion: extract **one core idea**, not a full summary. Turn it into a clean carousel thesis.

## Shape rules for slides 1–3

Keep shapes simple and symbolic:
- circles/orbits for systems, compounding, invisible team
- blocks/bars for ratios or frameworks
- split-screen lines for false choices
- small dots for agents/work units
- arrows for flow, not decoration

Do not over-illustrate. The shapes should support the text, not compete with it.

## Copy rules

- Big lines, short Thai.
- Avoid long paragraph bodies.
- Prefer business-owner language: `เจ้าของธุรกิจ`, `ทีม`, `ระบบ`, `งานซ้ำ`, `ตัดสินใจ`.
- Keep CTA simple: `พิมพ์ “AI”`, `พิมพ์ “10”`, etc.
- If user gives corrected copy, preserve the exact phrase unless there is an obvious typo; mention if corrected.

## Spacing rules

Before delivery, QA at least:
- contact sheet
- slide 1
- one dense middle slide
- slide 8

Check:
- header identical across slides
- footer identical across slides
- safe margins around border
- no Thai clipping or diacritic issues
- titles do not collide with shapes
- CTA not too close to footer
- long Thai lines split before they visually hit edges

If line spacing is requested, adjust `line-height`, not font size. Example: +0.2 from 1.18 → 1.38.

## Rendering steps

1. Create `carousel.html` with full deck.
2. Split into one HTML file per slide before screenshotting. Chrome URL fragments can capture the same first slide repeatedly; do **not** rely on fragment anchors.
3. Render each with Chrome:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1080,1350 \
  --screenshot=/path/to/png/slide_01.png \
  file:///path/to/html_slides/slide_01.html
```

4. Verify all PNG dimensions are 1080×1350.
5. Create contact sheet and ZIP.
6. Run vision QA and iterate once if spacing is off.

## Delivery

If Jet asks to see/run a draft, send:
- contact sheet preview
- individual PNGs if asked or if the next step is obvious
- ZIP bundle if useful
- brief note on what transcript idea was used

If Jet says “build me the next one,” treat it as permission to pick the next strong Plaud/Notion idea autonomously and render another full run rather than asking for a transcript.

For session-specific examples and proven copy patterns, see `references/run01-run02-lessons.md`.

Keep chat concise. The work should be visible in files, not over-explained.
