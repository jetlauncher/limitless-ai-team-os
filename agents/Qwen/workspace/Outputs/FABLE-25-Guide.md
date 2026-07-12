# The Guide — How FABLE 25 was made

Source: https://fable-25.netlify.app/guide/  
Scraped: 2026-07-08

---

## Overview

This entire project — every design decision, every line of code and copy, every image brief, every fix — was executed autonomously by **Claude Fable 5** running in Claude Code, from a single prompt. Here is the exact workflow, written so you can reproduce it.

---

## 01 — The architecture: one director, twenty-five studios

The core trick is not "generate a website 25 times." It's an **orchestrator/builder split**:

- A single **orchestrator session** wrote a shared design constitution (`BRIEFS.md`): a non-negotiable build standard — real copy only, distinctive type, custom easing, responsive, accessibility, zero console errors — plus twenty-five individually art-directed briefs, each specifying concept, palette, typefaces, signature techniques, and one thing the site had to prove.
- **Twenty-five parallel builder agents** (subagents of the same model) each received one brief and full autonomy over one folder. No templates, no shared components — deliberately, so no two sites could converge.

The orchestrator then acted as a design director: reviewing every finished site's screenshots itself and sending sites back with specific QA notes (a mid-word line break, a low-contrast button, a paragraph drowning in artwork).

---

## 02 — The self-critique loop (this is the part that matters)

Every site went through **three mandatory iteration passes**. One pass =

1. **Render** the real page in headless Chrome via a tiny Puppeteer harness — desktop and mobile, top/mid-scroll/bottom, capturing console errors and document height.
2. **Look at the pixels.** The agent reads its own screenshots with vision and critiques them like a hostile design director: rhythm, alignment, contrast, widows, dead zones, anything that smells like "AI default."
3. **Fix everything found — then add one deliberate complexity upgrade** (a texture, a micro-interaction, marginalia, an easter egg). The upgrade rule stops iteration from converging on bland safety.

```javascript
// shot.js — the whole harness is ~25 lines
node shot.js http://localhost:4179/strata/ out.png 1440x900 4000 [scrollY]
// → {"out":"out.png","docHeight":3834,"errors":[]}
```

Why it works: code review can't see a widow or a muddy button. Closing the loop between written code and rendered pixels is what turns "plausible output" into design judgment. The 3D terrain site shipped its first pass as a black void — its own screenshot critique caught it and rebuilt the fog, camera, and lighting.

---

## 03 — The asset pipeline: generated, then treated like production media

Ten sites use cinematic media. All of it was generated on demand via the Higgsfield API/MCP, then optimized like any professional asset:

| Asset | Model | Used On |
|-------|-------|---------|
| Cloudscapes, deco lobby, ceramics, sumi-e ink, brutalist concrete, statue, paper-cutout fox, perfume bottles | nano_banana_2 (text→image) | reverie, meridian, kiln, yamanaka, massvoid, newsincerity, papermoon, ambre |
| Fashion editorial ×4, lighthouse keeper portraits | Soul 2.0 | vanta, keepers |
| 5-second cinematic loops (cloud drift; molten amber) | Kling 3.0 Turbo, image-to-video from the hero still | reverie, ambre |
| Textured GLB chair mesh, scanned from its own generated product photo | image_to_3d | orbitchair |

**Every image:** `ffmpeg → WebP`, ≤1920w — 5 MB PNGs became 40–190 KB.  
**Every video:** h264, CRF 26, muted, faststart — under 600 KB, safe to autoplay.

Generating the video from the hero still keeps poster and loop visually continuous.

Total generation cost: ≈ 40 credits (~27 assets). The other fifteen sites are fully procedural — GLSL, canvas flow fields, SVG illustration, CSS — because restraint is also a budget.

---

## 04 — What the sites had to prove

Each brief targeted a different axis of capability, so the set covers the space rather than repeating one trick: real-time 3D (custom vertex-shader terrain; a configurable GLB product), generative art (seeded flow fields), kinetic and variable typography, scroll-driven data storytelling on real NASA GISTEMP data, audio synthesized from raw oscillators, an interactive terminal, print-grade editorial typography with margin footnotes, and disciplined excess (brutalism, vaporwave, Y2K chrome) where the chaos is gridded underneath.

---

## 05 — Shipping

```
fable-25/
├── netlify.toml          # publish = "sites", asset cache headers
├── BRIEFS.md             # the design constitution
├── tools/shot.js         # puppeteer critique harness
└── sites/
    ├── index.html        # this gallery
    ├── guide/            # you are here
    ├── strata/ … frequency/   # 25 self-contained sites
    └── assets/thumbs/    # gallery thumbnails (from the QA shots)
```

Everything is static — no build step, no framework, fonts from Google Fonts, Three.js from a CDN. One `netlify deploy --prod` ships all 26 surfaces atomically.

---

## 06 — Every site documents itself

This page is the systems view. For the craft view, every one of the 25 sites carries its own `/guide` route — written by the agent that built it, in that site's own visual language: the brief it received, the signature techniques with real code excerpts from its source, where its assets came from, and what its three critique passes actually found and changed.

Visit any site and follow the "how this was built →" link by its credit, or go directly to `/<site>/guide/` — e.g. `/strata/guide/`, `/degrees/guide/`, `/orbitchair/guide/`.

---

## 07 — Reproduce it (the five requirements)

1. Write a **build standard** your agents cannot negotiate away (copy quality, motion, a11y, zero errors).
2. Write **real briefs** — name the palette, the typefaces, the signature technique, the thing to prove.
3. Give every agent a **screenshot harness** and require N critique passes with a complexity-upgrade rule.
4. Generate media **async and early**; optimize it like production assets.
5. Keep one session as **director**: review every hero shot cold, send back specific findings.

> Deploy static. Complexity in the pixels, not the pipeline.

---

Honesty note: the imagery is AI-generated, the brands are fictional, the data on the climate essay is real (NASA GISTEMP v4, cited in-page), and the total wall-clock time from prompt to deploy was about **three hours** — most of it spent in parallel critique passes, which is exactly where it should go. After launch the set grew to **thirty**: five 3D encores (raymarched liquid metal, particle typography, soft-body cloth, a point-cloud museum, an infinite procedural night-flight) commissioned by request and built by the same process — plus post-launch revisions driven by real feedback (a rebrand, a cursor fix, a playable minigame), each handled by the original builder agent with its context intact.

---

## Wave 1 — Public Works (the autonomous loop begins)

The portfolio now grows in waves without a human in the loop: an orchestrator session reads a registry of every site's "DNA" (domain / technique / palette / type / mood), invents six new strings that may share at most one axis with anything already live, generates hero media on frontier models first (stills, an image-to-video sea loop, and a photograph lifted into a 3D GLB mesh), then runs six parallel builder agents through the same three-pass critique gauntlet and a cold director review.

Wave 1's theme is **Public Works** — six civic institutions that don't exist:
- A metro authority with a working split-flap board
- An office of tides whose WebGL sea computes real harmonic constituents
- A society of speculative cartography with a procedurally inked globe
- A horology institute whose specimen was reconstructed from a single generated photograph
- A risograph co-op that screens every dot live
- A national weather teletext service

**New lessons for practitioners:**
- Headless-Chrome screenshot modes can hang machine-wide under parallel load (pin the stable one in the shared harness)
- A 12 MB GLB is a design flaw, not an asset (1 K WebP textures brought it to 2 MB with no visible loss)
- Asset generation belongs to the director, not the builders — one queue, one budget, no cap collisions

**Batch two** doubled the wave to twelve:
- A water authority whose scroll is 312 metres of descent
- A grid operator's pylon vigil where one load figure drives both the HUD and the wire-glow shader
- A seed library that grows real stochastic L-systems stem-by-stem
- A dead letter office you ride through pneumatic tubes
- A fountains bureau running 40,000 stateless GPU particles (whole arcs computed in the vertex shader — pre-warming a screenshot costs nothing, you just start the clock at t=40s)
- A carbonless-triplicate municipal form that stamps you APPROVED

**New lessons:**
- Delegating asset generation back to builders works fine at ≤2 jobs each under a shared cap
- `CanvasTexture` needs its `colorSpace` set to sRGB or night scenes wash out to pale slabs
- A `.stage` class name colliding across DOM and scene code will put your camera one section ahead of your copy
- The cheapest fix for a dead hero corner is fog — distant silhouette boxes let the depth cueing do the painting

**Batch three** pushed the wave to eighteen:
- A carillon office whose bells are coupled damped pendulums (the clapper is its own pendulum — a strike is a real impact whose velocity drives nine inharmonic WebAudio partials)
- A planetarium you stand inside where one az/alt star dataset drives the dome geometry, the hover detection, and the index-card charts alike
- A bascule bridge raised entirely by scroll (one smoothed progress value animates leaves, counterweights, gates, ship, and camera — parent the counterweight behind the pivot and its motion is free)
- A grain elevator whose heaps are a 34×34 heightfield with angle-of-repose relaxation instead of per-grain physics
- An avalanche service whose blizzard streaks each flake along its screen-space velocity in the fragment shader
- A night pilotage radar that abandoned accumulation-buffer phosphor (alpha rounding leaves permanent ghosts) for a deterministic pre-rendered afterglow wedge

**Recurring lesson made rule:** hero kicker lines over bright 3D scenes always need a text-shadow — three of six sites shipped without one and all three needed it in cold review.

---

## Wave 2 — Closing Ceremonies (the collection completes)

The final batch closed the portfolio at exactly **fifty-five** with seven farewells:
- A fireworks conservatory whose shells solve their own ballistic launch velocities so they burst at the clicked apex, with trail persistence from a never-cleared render target faded by a reverse-subtract quad
- An opera house whose velvet curtain is a vertex-displaced plane that parts on scroll to reveal volumetric spotlight cones
- A sunset society whose entire sky is a single-scattering Rayleigh–Mie integral — drag the sun from golden hour to astronomical twilight and the light is computed, not painted
- A lantern festival of hundreds of GPU-instanced flames whose rise, sway, flicker and burn-out all derive from one per-instance seed
- A farewell comet with two physically distinct shader tails (straight gusting ion, curved dust fan) over an internally consistent invented ephemeris
- A time-capsule bureau that seals your letter to 2126 under feTurbulence-displaced molten wax
- A carousel whose carved horse was generated as a still, lifted to a textured GLB mesh, and instanced six times around a procedural canopy — the image-to-3D pipeline, one last time

Six of seven fully 3D. **Closing lessons:** text over a live scene sometimes needs more than a shadow — when the background is a rim of blazing bulbs, give the line a soft scrim plate; and a portfolio needs an ending the way a site needs a footer.

> Fifty-five sites, three waves, zero templates. The collection is complete.

---

*Designed & built by Claude Fable 5 · 2026*
