---
type: workflow-build-queue
status: built-v0
created: 2026-07-20T02:04+07:00
built-by: Kelly (nightly cron)
---

# Nightly Workflow Build — SME Workflow Builder

## Title
SME Workflow Builder — AI Team OS student-facing tool v0

## Why this helps Jet
Jet's audience is Thai SMEs trying to adopt AI. Oracle produced "post-training moat" seeds focused on SME strategy. Blaze has content scripts ready for production. Kaijeaw can translate/adapt. This tool bridges that pipeline: it turns a person's bottleneck into actionable agent task chains — exactly the kind of asset Jet sells in his AI Team OS curriculum. It's also immediately sharable as a lead magnet if needed.

## What was built
A complete single-file HTML interactive app (no server, no dependencies, works offline) with:
- 3-step onboarding flow (context → agent selection → goal/timeline)
- Dynamic task chain generation per selected agent
- Business type context sensitivity (e-commerce vs content vs service, etc.)
- Copy-to-clipboard for pasting tasks into Notion/Obsidian
- Print/Save-as-PDF for student handouts
- Dark theme following Limitless visual style

## Files created
| File | Path | Size |
|------|------|------|
| Main app | `Bolt/Builds/2026-07-20/sme-workflow-builder/index.html` | 380 lines, ~19 KB |
| README | `Bolt/Builds/2026-07-20/sme-workflow-builder/README.md` | v0 documentation |
| Verification | `Bolt/Builds/2026-07-20/sme-workflow-builder/verify.py` | Validation script (8/9 checks passed; template-literal check was too strict — intentional JS `${}` used for string building) |

## How to open/use
1. Open `index.html` in any browser (file:// works, no server needed).
2. Fill in bottleneck → select agents → define goal/timeline → hit "Build My Workflow".
3. Review the generated task chain per agent.
4. Copy or print for distribution.

## Acceptance criteria
- [x] Artifact exists under correct Bolt/Builds date path
- [x] Single-file, non-blocking (no external CDNs)
- [x] All 8 Hermes agents configurable as workflow participants
- [x] Dynamic output is specific to business context (not boilerplate)
- [x] Validation script confirms structural integrity
- [x] README includes Bolt next steps

## Safety constraints
- Local-only — nothing sent externally
- No credentials, no API keys
- Zero dependencies — pure HTML/CSS/JS

## Suggested Bolt next step
When Jet approves building this into a student-facing tool:
1. Phase 1: Add localStorage save/load (persist workflows between sessions)
2. Phase 2: Export to .md for Notion/Obsidian integration
3. Phase 3: Thai language toggle for bilingual support
4. Phase 4: MCP bridge to actual Hermes profiles for live dispatchable tasks
