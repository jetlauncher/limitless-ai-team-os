# SME Workflow Builder

**v0 — Nightly Build 2026-07-20 by Kelly**

## What it is
A single-file, no-server interactive tool that helps Jet (and his Team OS student base) build structured AI agent workflows from business context. Answers the question: "Which agents should I assign to what tasks?" — in 3 steps.

## Why this matters
Jet's content seeds (Oracle, Blaze) and Kaijeaw's Thai ops are all focused on SME/Thai founder audiences. This tool lets anyone answer: "I need an AI workflow for X" and get a ready-to-execute task chain with agent assignments — directly outputting copy-paste-ready instructions.

## Files
- `index.html` — Single HTML file (dark theme, responsive, no dependencies). Open in any browser.
- `verify.py` — Validation script (run after edits to check integrity).

## How to use
1. Open `index.html` in a browser — local file works, no server needed.
2. Step 1: Describe bottleneck. Select business type. Check agents involved.
3. Step 2: Review agent selection (Blaze default-checked since content ops is core).
4. Step 3: State your goal and timeline → hit "Build My Workflow".
5. Get a structured task chain per agent, plus quick-win suggestions.

## Acceptance criteria
- [x] Single HTML file under Bolt/Builds/2026-07-20/sme-workflow-builder/
- [x] Valid HTML structure (DOCTYPE, head, body, script tags)
- [x] No copy-paste syntax errors (double attributes, broken quotes)
- [x] All 8 agents selectable as checkboxes
- [x] Task assignments dynamically generated per agent selection
- [x] Copy-to-clipboard and Print/Save PDF buttons
- [x] Responsive layout for mobile viewing
- [x] Zero external dependencies — works offline

## Bolt next step
When Jet or Blaze wants to expand this into a full student-facing tool:
1. Add localStorage persistence (save workflows between sessions)
2. Export as .md files (for Obsidian/Notion integration)
3. Add Thai language toggle (all labels in Thai)
4. Connect to Hermes profiles via local MCP bridge for live agent dispatch
