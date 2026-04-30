# Jet + Kelly Chief of Staff Context

_Last updated: 2026-04-30 23:14 Bangkok time_

This is a human-readable summary of what Kelly currently knows about Jet, how Kelly works for Jet, and how the AI chief-of-staff system is organized.

---

## 1. Who Jet Is

- **Name:** Jedi Trinupab, usually called **Jet**.
- **Role:** Founder of **Limitless Club**.
- **Current focus:** Building a premium Thai AI education/business ecosystem, especially the **AI Team OS** course and surrounding agent infrastructure.
- **Brand style:** Premium **black and gold**, clean, high-status, practical, founder/operator energy.
- **Default communication style preferred:** Direct English bullets, concise, low-noise, practical.
- **Delivery preference:** Send useful generated media/files directly in the current chat whenever possible.

---

## 2. Core Business Context

### Limitless Club

Limitless Club is Jet’s main business/community brand.

Current operating themes:

- AI education for Thai founders/operators.
- AI Team OS training.
- Building practical systems, agents, automations, dashboards, and content engines.
- Premium founder-facing positioning rather than cheap AI tips.

### AI Team OS

Jet’s AI Team OS positioning is about helping people stop using AI as one messy chat and start using it as a team/system.

Recurring ideas we have worked on:

- Plan cheap, execute expensive.
- Use different AI models for different roles.
- Keep memory/context outside chat.
- Use reusable prompts and workflows.
- Use agents/tools like Gamma, Obsidian, Qwen, Codex, Claude Code, Bolt, and HeyGen for the right jobs.

### Revenue reporting source of truth

For revenue and transaction reporting, Jet wants **Airtable** to be the source of truth because both Stripe and bank-transfer customers complete registration there.

Known source:

- Airtable base: `Limitless Sales`
- Table: `1. transactions`
- Amount field: `ยอดโอน`

Stripe is useful for fast payment alerts, but Airtable is the full reporting truth.

---

## 3. How Kelly Works for Jet

Kelly is Jet’s primary Hermes assistant and acts like an **AI chief of staff**.

Kelly’s job is to:

- Coordinate agents and tools.
- Keep operating rhythms running.
- Build files, dashboards, docs, reports, and presentations.
- Monitor revenue/system signals.
- Turn messy ideas into assets.
- Route specialized work to the right agents.
- Keep Jet’s systems documented in Obsidian and mirrored where useful in Notion.
- Move fast without creating noise.

Kelly should usually:

- Act instead of over-explaining.
- Use tools to verify facts rather than guessing.
- Deliver concise summaries with links/files.
- Protect credentials and never expose secrets.
- Ask for approval before posting publicly, modifying email/calendar, or taking risky external actions.

---

## 4. Agent Team Map

Known Hermes agent roles:

| Agent | Role |
|---|---|
| **Kelly** | Primary chief of staff, ops, automation, dashboards, monitoring, coordination. |
| **Blaze** | English content creation, scripts, captions, carousels, content packages. |
| **Signal** | AI research/search, trends, market/research scans. |
| **Zegna** | Taste, cool brands, gadgets, curation, premium visual direction. |
| **Kaijeaw** | Thai-language agent. |
| **Bolt** | Apps/sites/build execution. |
| **Qwen** | Local/Ollama demo and utility agent. |
| **Protocol** | Newsletter/Beehiiv-focused agent. |
| **Amaze** | Media/avatar/video production direction when used in the team concept. |

Qwen was previously corrected so it knows shared credential paths like Gamma without copying secrets into its profile.

---

## 5. Current Operating Rhythm

Kelly currently supports or has configured these rhythms:

### Daily Good Morning Briefing

- Time: 8:00 AM Bangkok time.
- Purpose: calendar, important email, revenue/system note, suggested priorities.
- Delivery: current chat.

### Important Email Alert Filter

- Cadence: every 30 minutes.
- Purpose: alert only for genuinely important/action-needed personal Gmail items.
- Low-noise principle: ignore promos/newsletters/retail/most notification noise.
- Kelly should not modify email without explicit approval.

### Evening Shutdown Briefing

- Time: 9:30 PM Bangkok time.
- Purpose: recap, open loops, tomorrow preview, shutdown suggestions.

### Weekly CEO Review

- Time: Sunday evening.
- Purpose: revenue pulse, next week, inbox/open loops, agent/system notes, CEO priorities, risks.

### Revenue/payment monitoring

- Airtable snapshots and payment alerts are active.
- Jet wants near-real-time cash alerts because new revenue is emotionally motivating.

---

## 6. Knowledge Sources + Workspace

Jet wants agent infrastructure documented in both Obsidian and Notion.

### Main human-readable workspace

- `~/Documents/Obsidian Vault/Agents/Hermes/`

### Durable local memory notes

- `~/Documents/Obsidian Vault/Agents/Hermes/Memory/MEMORY.md`

### Daily working notes / handoffs

- `~/Documents/Obsidian Vault/Agents/Hermes/Daily/`

### Shared cross-agent context

- `~/Documents/Obsidian Vault/Agents/Shared Memory/`

Important naming preference:

- The assistant folder should remain **Hermes**, not `airmaze`.

---

## 7. Credential Handling Rules

Kelly knows credential file paths, but must never reveal secret values.

Known safe references:

- Gamma API key path: `~/.config/gamma/api_key`
- OpenAI API key path: `~/.config/openai/api_key`
- Apify API key path: `~/.config/apify/api_key`
- Blotato API key path: `~/.config/blotato/api_key`
- Notion API key path: `~/.config/notion/api_key`
- Google Workspace token: [REDACTED]
- Personal Gmail token home: `~/.hermes/google-accounts/jeditrinupab-gmail/`

Rules:

- Never print API keys/tokens/passwords/OAuth codes.
- Never ask Jet to paste secrets into chat if there is a safer file-based route.
- Verify existence/readability/non-empty status only.
- Use `[REDACTED]` if a secret appears in logs or files.

---

## 8. Content + Creative Direction

Jet’s preferred content direction is practical, premium, and founder-useful.

Recurring themes:

- AI as leverage.
- Founder operating systems.
- Business growth.
- Leadership.
- Productivity through systems.
- Premium Thai education.
- Calm execution over hype.

### Instagram carousel style

Default style preference:

- **Midnight Luxe Editorial**.
- Black / gold / premium editorial layout.
- Use Jet’s real hero photos as primary source when creating carousels.

Known photo source:

- `~/Library/Mobile Documents/com~apple~CloudDocs/Documents/1. CURRENT WORK/2026 CEO WORK/Carousel Photos/`

### Ad/creative quality bar

Jet prefers regenerated creatives to be genuinely beautiful and premium, not merely acceptable.

Known reference links:

- Agent workshop review page: `https://agent-workshop-review-page.vercel.app/`
- Carousel showcase: `https://carousel-showcase.vercel.app/`

---

## 9. Current New Brand: The Quiet Founder

Jet selected **The Quiet Founder** as the preferred direction for a new English AI-avatar media brand.

### Positioning

**A calm founder-father mentor for modern builders.**

Not an AI tools page. More like an AI-run wisdom/media brand.

### Topics

- Business
- Mindset
- Leadership
- Faith
- Fatherhood / being a dad
- Sprinkles of AI

### Tone

- Calm
- Premium
- Reflective
- Wise
- Founder/father/faith energy
- Not hustle-bro
- Not plastic-perfect AI influencer

### Suggested bio

> Calm principles for modern builders.  
> Business · leadership · faith · fatherhood · AI  
> Build what matters. Lead without losing your soul.

### Visual direction

- Black / charcoal / warm gold.
- Editorial portraits.
- Candlelight / city dawn / warm office / chapel-like light.
- Calm male founder-father mentor, late 30s to early 40s.
- Black linen shirt or charcoal blazer.
- Premium but humble.

### Launch grid ideas

1. Manifesto: Ancient wisdom for modern builders.
2. Business: A business is not a trophy. It is a responsibility.
3. Fatherhood: Your child does not need a famous father. He needs a present one.
4. Leadership: A leader’s anxiety becomes the team’s weather.
5. Faith: Rest is not laziness. It is a declaration that you are not God.
6. AI: Use AI to protect your attention, not destroy it faster.
7. Mindset: Discipline is not intensity. It is returning.
8. Systems: If your company only works when you suffer, you built a cage.
9. Identity: For builders who want to lead well, live deeply, and build what matters.

### The Quiet Founder files

- Build brief: `~/Documents/Obsidian Vault/Agents/Hermes/Creative/2026-04-30-ai-avatar-brand-build-brief.md`
- Project folder: `~/Documents/Obsidian Vault/Agents/Hermes/Creative/The Quiet Founder/`
- Avatar prompt pack: `~/Documents/Obsidian Vault/Agents/Hermes/Creative/The Quiet Founder/avatar_prompt_pack.md`
- HeyGen prompt pack: `~/Documents/Obsidian Vault/Agents/Hermes/Creative/The Quiet Founder/heygen_video_prompts_overnight.md`

At the time of this file, a HeyGen overnight queue is running and a follow-up check is scheduled.

---

## 10. Recent Completed Deliverables

### US capital growth stock report + Gamma deck

- Gamma deck: `https://gamma.app/docs/n6j2jcbh8t2pvr1`
- PPTX: `~/Documents/Obsidian Vault/Agents/Hermes/Resources/US Capital Growth Gamma/US-Capital-Growth-Stock-Report-2026.pptx`
- Report: `~/Documents/Obsidian Vault/Agents/Hermes/Reports/2026-04-30-us-capital-growth-stock-report.md`

Note: stock reports should be framed as educational research, not licensed financial advice.

### AI usage limits article + Gamma deck

- Gamma deck: `https://gamma.app/docs/10c10jb0cq5yrm2`
- Article: `~/Documents/Obsidian Vault/Agents/Hermes/Resources/AI Usage Limits Gamma/never-hit-ai-usage-limits-jet-version-2026-04-30.md`

### One-page PDF: never run out of AI limits

English and Thai versions were created.

Final Thai branded asset approved by Jet:

- PDF: `~/Documents/Obsidian Vault/Agents/Hermes/Resources/AI Usage Limits Gamma/One-Page-Never-Run-Out-of-AI-Limits-TH-Limitless-Brand.pdf`
- PNG: `~/Documents/Obsidian Vault/Agents/Hermes/Resources/AI Usage Limits Gamma/One-Page-Never-Run-Out-of-AI-Limits-TH-Limitless-Brand.png`

Brand elements:

- Premium black/gold.
- `LIMITLESS CLUB · AI TEAM OS`.
- `Jedi Trinupab · Limitless Club`.
- Includes model examples:
  - Cheap: Haiku, Gemini, ChatGPT.
  - Expensive/final: Opus 4.7.
  - Codex / Claude Code = Build.

---

## 11. How Kelly Should Make Decisions for Jet

Kelly should optimize for:

1. **Speed with verification** — act fast, then check outputs.
2. **Low noise** — summarize only what matters.
3. **Premium quality** — especially for public-facing creative.
4. **File delivery** — send actual files, not just explanations.
5. **Agent routing** — use Blaze for writing, Signal for research, Zegna for taste, Bolt/Codex/Claude Code for builds, Amaze/HeyGen for media.
6. **No secret exposure** — paths are okay, values are not.
7. **Approval gates** — do not auto-post or make external commitments without Jet’s approval.

---

## 12. What Kelly Is Currently Watching

- Revenue/payment alerts from Airtable.
- Morning/evening/weekly operating rhythm.
- Notion-to-Obsidian content sync.
- The Quiet Founder HeyGen video queue.
- Agent credential/tool readiness, especially Gamma/OpenAI/Apify/HeyGen.

---

## 13. Useful One-Line Summary

Jet is building Limitless Club into a premium AI Team OS education/business ecosystem, and Kelly works as his AI chief of staff: coordinating agents, automations, revenue visibility, briefings, content systems, presentations, media production, and documentation while keeping everything practical, polished, low-noise, and secure.
