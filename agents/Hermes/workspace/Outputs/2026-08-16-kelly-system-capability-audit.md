# Kelly / Hermes System Capability Audit

**Audited:** 2026-08-16 08:06 +07  
**Profile:** default / Kelly  
**Hermes:** 0.20.1 on macOS 26.5.2 arm64  
**Purpose:** A truthful map of what Kelly can use now, what is installed but gated, and what Jet can provide to improve performance.

---

## 1. Executive snapshot

- **228 callable surfaces in this session:** 26 direct tools, one parallel-call wrapper, and 201 on-demand MCP/deferred endpoints.
- **19 enabled built-in toolsets** plus the Google Meet plugin.
- **151 active Hermes skills**: 8 hub-installed, 20 built-in, and 123 local.
- **5 enabled MCP servers:** AgentMail, Context7, cua-driver, Higgsfield, and Readwise.
- **14 Hermes profiles**, with **10 gateways currently running**.
- **22 active scheduled jobs** out of 42 total.
- **Connected messaging:** Telegram and Discord.
- **Healthy core:** Hermes doctor found no security advisories or suspicious MCP commands; OpenAI Codex, xAI OAuth, MiniMax OAuth, OpenRouter, Anthropic, Firecrawl, local terminal, file system, GitHub, Google Drive, Notion, Todoist, AgentMail, Readwise, and macOS computer control are available.
- **Primary broken integration:** Higgsfield MCP is installed but its session has expired and must be re-authorized.

---

## 2. Direct tools callable in this Telegram session

### Research and browser
1. `web_search` — current web search.
2. `web_extract` — clean extraction from webpages and online PDFs.
3. `browser_exec` — real browser navigation, interaction, extraction, and screenshots.
4. `computer_use` — background macOS GUI control without taking Jet’s cursor.
5. `vision_analyze` — inspect screenshots and images.

### Local computer, files, and code
6. `terminal` — shell commands, builds, tests, Git, CLIs, networking, and scripts.
7. `process` — monitor or control long-running background processes.
8. `execute_code` — Python orchestration across multiple Hermes tools.
9. `read_file` — read text, PDF text layers, DOCX, XLSX, and other documents.
10. `search_files` — search filenames and file contents.
11. `write_file` — create or overwrite files with validation.
12. `patch` — targeted edits and multi-file patches.

### Intelligence, memory, and reusable workflows
13. `session_search` — search and reopen past Hermes conversations.
14. `memory` — save compact, durable facts across sessions.
15. `skills_list` — list installed skills.
16. `skill_view` — load a skill and its references.
17. `skill_manage` — create, patch, edit, or remove skills.
18. `todo` — track complex work in the current session.
19. `clarify` — ask structured questions when a real decision is needed.

### Automation and agents
20. `cronjob` — create, update, pause, run, and remove scheduled work.
21. `delegate_task` — send independent research/reasoning work to subagents.
22. `multi_tool_use.parallel` — run independent tools concurrently.

### Media
23. `image_generate` — OpenAI image generation and image editing.
24. `text_to_speech` — generate deliverable audio.

### On-demand integration broker
25. `tool_search` — search the deferred tool catalog.
26. `tool_describe` — load the schema for a deferred tool.
27. `tool_call` — invoke a deferred MCP/integration tool.

---

## 3. On-demand MCP and deferred tools

There are **201 additional endpoints** grouped into six systems.

### AgentMail — 26 tools — working
Capabilities include:
- create/manage inboxes;
- list/search/read messages and threads;
- create/update/delete drafts;
- send messages, replies, forwards, and drafts;
- retrieve attachments;
- update message/thread state;
- manage organizations.

Live smoke test succeeded and returned Kelly’s AgentMail inboxes.

### Context7 — 6 tools — working
Capabilities include:
- resolve software library IDs;
- query current library/framework documentation;
- list/read MCP resources;
- list/get reusable prompts.

The server responded normally. Its resource list is empty, which is not an authentication failure.

### cua-driver — 54 tools — working
Capabilities include:
- screen capture and accessibility trees;
- background click/type/scroll/drag;
- app and window discovery/control;
- browser navigation, typed semantic page actions, downloads, uploads, and dialogs;
- permissions, diagnostics, health reports, recording, zoom, and cursor state.

Live health report: **overall OK**. Accessibility and Screen Recording are granted; the MCP session is active.

### Higgsfield — 88 tools — installed, authentication expired
Capabilities include:
- image, video, audio, 3D, motion-control, outpainting, background removal, reframing, and upscaling;
- Soul Character and voice creation;
- video analysis and personal clipper workflows;
- TikTok trend/search/publishing operations;
- website creation, deployment, database, secrets, and publishing;
- marketing studio, workspaces, credits, and generation history.

Live smoke test failed because the Higgsfield session has expired. Reauthorization is required before these tools are dependable.

### Readwise / Reader — 26 tools — working
Capabilities include:
- create/search/list/export Reader documents;
- read document details and highlights;
- create/update/delete Readwise highlights;
- tags, notes, metadata, and document movement;
- daily review access.

Live smoke test succeeded. The current Reader tag list is empty.

### X Search — 1 tool — available
- `x_search` performs current X/Twitter search through the configured xAI path.

---

## 4. Enabled Hermes toolsets

Enabled in the live CLI configuration:

- Web search/extraction
- Browser automation
- Terminal/processes
- File operations
- Code execution
- Vision/image analysis
- Image generation
- Video generation
- BFL FLUX video toolset
- X search
- Text-to-speech
- Skills
- Todo planning
- Persistent memory
- Session search
- Clarifying questions
- Delegation
- Cron jobs
- Computer use
- Google Meet plugin

### Enabled but currently dependency-gated
Hermes doctor reports system requirements are not fully met for:
- generic `browser` plugin path;
- BFL video backend;
- Google Meet plugin.

This does **not** remove our working browser paths: `browser_exec` and cua-driver are both available, and cua-driver passed its health test.

### Disabled in the current profile/session
- Direct video analysis
- Speech-to-text toolset
- Context Engine
- Home Assistant
- Spotify
- Yuanbao

Tool changes require a new session/reset before they appear in the prompt.

---

## 5. Active skill library

Hermes currently exposes **151 enabled skills** across these practical groups:

### Research and evidence
Web/X research, blocked-page recovery, grounded citations, competitive intelligence, market monitoring, equity research, social-handle audits, and AI-news monitoring.

### Chief-of-staff and operations
Daily/weekly briefings, revenue monitoring, sales monitoring, approvals, mission control, cron operations, fleet health, model routing, cost audits, memory hygiene, handoffs, and workflow documentation.

### Documents, knowledge, and productivity
PDF, DOCX, XLSX, forms, meeting actions, workshop recaps, NotebookLM, Notion pipelines, Google/Gmail workflows, Readwise, Obsidian memory, Linear, Box, and cloud-storage operations.

### Creative production
Premium image generation, carousels, quote cards, article illustration, comics, brand kits, avatars, product photography, visual audits, TouchDesigner, Hyperframes, pixel art, event-photo processing, and high-end visual design systems.

### Content and growth
Jet/Jedi voice, Thai/English content, newsletters, YouTube scripts and repurposing, social posting with approvals, ads research, sales copy, Substack covers, and content engines.

### Software and engineering
Planning, agentic execution, subagent development, debugging, code review, GitHub issue-to-PR, private repo publishing, static websites, landing pages, frontend redesign, image-to-code, and Hermes extension/troubleshooting.

### Media and communication
Video editing, clipping, transcription, YouTube upload, HeyGen avatars/videos, voice agents, ElevenLabs phone agents, LINE OA bridge, and Google Meet.

### AI/ML
DSPy, Outlines, Axolotl, TRL, Unsloth, local inference, fine-tuning, and research workflows.

The full generated local catalog also sees archived skills. The authoritative operational number is the live `hermes skills list`: **151 active, zero disabled**.

---

## 6. Connected systems and verified access

### Verified working now
- Telegram home channel
- Discord home channel
- Local macOS files, apps, terminal, and background GUI control
- OpenAI Codex OAuth
- xAI OAuth
- MiniMax OAuth
- OpenRouter API
- Anthropic API
- Firecrawl API
- GitHub account `jetlauncher` through `gh` with repository access
- Google account token sets for Drive, Gmail, Search Console, and YouTube workflows
- Google Drive via `rclone` remote `gdrive:`
- Claude Code through Claude Max account
- Notion API: live identity request returned HTTP 200
- Todoist API: live read request returned HTTP 200
- AgentMail MCP
- Readwise MCP
- Context7 MCP
- cua-driver MCP

### Present but not fully verified in this audit
- YouTube upload token/configuration
- Gmail workflow tokens
- Search Console token
- Meta Ads via authenticated local Safari session
- Airtable source-of-truth workflow; no dedicated `~/.config/airtable` directory or `AIRTABLE_*` variable was found in the default profile, so API-write access should be treated as unverified until tested.

### Not configured in the default gateway
- WhatsApp
- Signal messenger
- Slack
- conventional Email gateway
- SMS
- DingTalk
- Feishu
- WeCom
- Weixin/WeChat
- BlueBubbles/iMessage gateway
- QQBot
- Yuanbao

AgentMail email is available independently of the conventional Email gateway.

---

## 7. Agent fleet

### Running gateways
- **Kelly/default:** chief of staff, operations, automation, coordination
- **Blaze:** content production
- **Bolt:** apps, sites, and build execution
- **JekJack:** dedicated private/family profile
- **Kaijeaw:** Thai content
- **Oracle:** knowledge-network ideas
- **Protocol:** newsletter operation
- **Qwen:** local/private worker on `qwen3.6:35b`
- **Signal:** AI research/search
- **Zegna:** taste, brands, and product intelligence

### Stopped or incomplete
- **Pixel:** visual design profile, stopped
- **Tiff:** dedicated profile, stopped
- **UncleChris:** dedicated profile, stopped
- **qron:** incomplete profile; missing configuration and alias

Scheduled work: **22 active jobs / 42 total** in the default profile status report.

---

## 8. What Jet can provide to make Kelly materially better

### P0 — Highest leverage

#### 1. One canonical priority scoreboard
Maintain one short source containing:
- top three outcomes for the month;
- the one revenue number that matters;
- owner and deadline for each outcome;
- current status and blocker;
- links to the canonical project sources.

This prevents excellent execution on the wrong priority.

#### 2. A public-claim and case-study registry
For speaking, sales, and content, provide approved facts for:
- team-size before/after;
- time or cost savings;
- revenue/client/student results;
- which company/client names may be used;
- screenshots that are public-safe;
- claims that must remain anonymous or private.

This is the largest remaining blocker for turning the CG Day evidence pack into a powerful, trustworthy deck.

#### 3. An explicit autonomy/approval matrix
Confirm the default policy for each class:
- **Auto:** read, research, analyze, draft, organize local files.
- **Prepare then approve:** email replies, social posts, calendar changes, CRM/Notion/Airtable writes, live deployments.
- **Always explicit:** payments, purchases, destructive actions, account/security changes, public claims using private data.

Clear boundaries let me act faster without crossing a trust line.

#### 4. Reauthorize Higgsfield
The connector exists, but the live session is expired. Reauthorization restores the largest external creative tool surface: 88 endpoints for image/video/audio/3D/website/TikTok workflows.

### P1 — Improves output quality

#### 5. Canonical brand and speaker asset pack
Provide one stable folder containing:
- latest speaker bio in Thai and English;
- approved portrait/headshots and human B-roll;
- logos and partner-logo permissions;
- brand fonts/colors/templates;
- stage-safe case-study visuals;
- preferred slide examples and anti-examples.

#### 6. Better briefs using seven fields
For any important assignment, include:
1. desired outcome;
2. audience;
3. deadline;
4. source of truth;
5. constraints/non-negotiables;
6. one example you like;
7. definition of done.

A short brief with these fields is more valuable than a long prompt with no decision criteria.

#### 7. Give raw source material early
Send transcripts, decks, screenshots, spreadsheets, URLs, voice notes, and existing drafts. I can extract and structure them; you do not need to clean them first.

#### 8. Mark every source as public, internal, client-confidential, or family-private
This reduces hesitation and prevents accidental leakage while allowing faster reuse of safe evidence.

### P2 — Optional integrations, only if useful

- Enable speech-to-text if you want automatic voice-note and meeting-audio workflows.
- Enable direct video analysis for video QA and clip selection in the core profile.
- Connect Spotify or Home Assistant if you want personal-environment controls.
- Configure WhatsApp, Slack, SMS, or conventional Email gateway only if they are real operating channels.
- Add an unattended cloud browser provider only if local Safari/Chrome sessions are insufficient.
- Add Gemini or Nous Portal only for model redundancy/cost routing; the current model stack is already sufficient.
- Repair or remove the incomplete `qron` profile after confirming whether it is still wanted.
- Address two build-time npm advisories reported by `hermes doctor`; neither is currently a runtime/security blocker.

---

## 9. What Jet does not need to do

- Do not paste tokens, passwords, or OAuth codes into ordinary chat. Use approved OAuth flows or credential files.
- Do not explain routine technical steps; state the outcome and constraints and let Kelly execute.
- Do not add more tools merely because they exist. The current system is already capability-rich.
- Do not approve every read-only step. Reserve approvals for live writes, public actions, payments, credentials, and destructive operations.

---

## 10. Bottom line

Kelly already has enough tools to research, build, design, automate, monitor, coordinate agents, operate the Mac, work with documents, create media, manage schedules, and ship verified software artifacts.

The next performance jump will come from:

1. **one canonical priority scoreboard;**
2. **approved evidence and case-study claims;**
3. **clear autonomy boundaries;**
4. **a stable brand/speaker asset pack;**
5. **reauthorizing Higgsfield.**

More access should be added only when it unlocks a specific recurring outcome.
