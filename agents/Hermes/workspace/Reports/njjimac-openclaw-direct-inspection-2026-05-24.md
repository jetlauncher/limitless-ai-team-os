# njjimac OpenClaw Direct Inspection — 2026-05-24

## Access
- Direct SSH over Tailscale verified: `njjimac@100.76.50.113`
- Remote host: `NJJs-iMac-2.local`
- macOS: 15.3.1
- Inspected paths directly on njjimac:
  - `/Users/njjimac/.openclaw`
  - `/Users/njjimac/clawd`
  - `/Users/njjimac/clawd/content-output`

## Safety
- Did not print or copy secrets.
- Avoided credential/auth/token/cookie/session/env files in detailed reads.
- Only inventory, metadata, and selected non-secret skill docs were reviewed.

## Scale
- `.openclaw`: ~412,450 files, ~13.5 GB
- `clawd`: ~246,064 files, ~6.9 GB
- `clawd/content-output`: ~23,402 files, ~1.3 GB

## Important legacy assets found

### Legacy OpenClaw skills
Located in `/Users/njjimac/.openclaw/skills`:
- `airtable-student-count-rule`
- `antfarm-workflows`
- `character-sheet`
- `grok-social-intel`
- `jedi-million-dollar-copy`
- `marketing-analytics`
- `marketing-content-strategist`
- `marketing-copywriter`
- `marketing-social-manager`
- `marketing-team-system`
- `ops-skills-v2`
- `quote-cards`
- `thai-carousel`
- `youtube-repurpose-factory`
- `youtube-script-format`
- `youtube-script-jedi`
- `youtube-thumbnail-beast`

### Legacy cron system
`/Users/njjimac/.openclaw/cron/jobs.json` contains 58 jobs, including:
- Email invoice tagging / reply monitoring
- Weekly Skool draft and posting
- Daily content production pipeline: trend scout, content brief, lead magnet, carousel, SEO article, YouTube script, QA, Notion push
- Morning/evening briefings
- Competitor watch
- Meta inbox / FB Messenger checks
- Stripe payment monitor
- Airtable revenue and signup alerts
- YouTube repurpose daily/weekly
- Second Brain memory/freshness jobs
- Daily Meta competitor + growth command center
- Plaud daily content extraction
- Hourly AI viral posts update on X

### Agent personas
Legacy agents found under `/Users/njjimac/.openclaw/agents`:
- `main`, `blaze`, `nova`, `forge`, `coach-marc`, `jamerson`, `line-admin`, `pastor-david`, `uncle-chris`, `venice`
- Multiple task-agent templates: bug-fix, feature-dev, security-audit

### High-value content/output libraries
`/Users/njjimac/clawd/content-output` includes:
- Daily briefs, trend reports, competitor watch reports
- YouTube scripts and repurpose packs
- Lead magnets and AI library HTML
- Thai/English SEO articles
- Carousel scripts and rendered design folders
- Thumbnail SOPs and prompt libraries
- Sales/landing-page copy
- Research packs, including Yang Yang/free-assets research

## Strong Hermes migration candidates

1. **Airtable student count rule**
   - Stable business rule: official class headcount should use Airtable `Limitless Sales` → `1. transactions` → `จำนวนนักเรียน`.
   - I compressed this into durable Kelly memory.

2. **YouTube repurpose factory**
   - Useful as a Hermes skill or cron pattern.
   - Generates carousel, X thread, LinkedIn, Instagram caption, TikTok short script, weekly newsletter, Skool post.
   - Need path adaptation from `/Users/njjimac/clawd/...` to current Kelly/Obsidian/Hermes paths before importing.

3. **Jedi YouTube script style**
   - Useful as a Blaze/content-writing skill.
   - Encodes Jedi Thai+English script structure and title formulas.

4. **Jedi million-dollar copy**
   - Useful as a conversion-copy skill.
   - Has Thai Business Owner Mode and International Operator Mode.

5. **Thai carousel / quote cards**
   - Mostly superseded by current premium HTML/Chrome workflow, but still useful for programmatic Thai text rendering and quote-card batch generation.

6. **Legacy cron map**
   - Not safe to import directly.
   - Should be mined selectively into current Hermes cron jobs only after checking current duplicates and destinations.

## Recommended next action
- Do not bulk-import the whole `.openclaw` tree: it is huge and contains credentials, browser profiles, node_modules, and stale backups.
- If Jet wants, next safe step is to import only 3–5 selected legacy skills into Hermes after path cleanup:
  1. `airtable-student-count-rule`
  2. `youtube-repurpose-factory`
  3. `youtube-script-jedi`
  4. `jedi-million-dollar-copy`
  5. `quote-cards` or `thai-carousel`
