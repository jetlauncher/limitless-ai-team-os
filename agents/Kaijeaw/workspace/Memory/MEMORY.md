# Kaijeaw Memory

Durable human-readable memory for Kaijeaw. Do not store secrets here.

## Plaud → Iris Content Pipeline
- For scheduled workshop transcript jobs, the live path works: use rclone against Drive folder `1MYsST8lFfSbVyoNGKpRen6tX2fkEAZDS`, copy recent DOCX into Plaud Library `_drive_docx_sync/`, extract with `textutil`, save draft packs under `_content_pipeline_drafts/YYYY-MM-DD/`, and create Iris Content Pipeline drafts via Notion REST when the notion skill/tool is unavailable.
- Iris Content Pipeline DB ID: `043dad6e20c043fbbb4f35f545d2d4b9`; verified Stage option `📝 Draft` and useful channels `Threads`, `Instagram`, `Longform`.
- Calendar-aware runs can query `trinupab@creatuscorp.net` using Hermes Google token JSONs; prefer the token's embedded OAuth client credentials for refresh. If iCloud Plaud files hit `Resource deadlock avoided`, re-copy the exact DOCX from Drive via rclone to `/tmp` and extract with ElementTree.
- For the calendar-aware workshop content pipeline, do not trust the local Plaud iCloud folder alone. Recent `.docx` Plaud transcripts are in Google Drive folder `1MYsST8lFfSbVyoNGKpRen6tX2fkEAZDS`; use `rclone lsf gdrive: --drive-root-folder-id 1MYsST8lFfSbVyoNGKpRen6tX2fkEAZDS --files-only --format 'pt'` when Drive API listing fails or returns empty. Local synced copies may also exist under `/Users/ultrafriday/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Limitless Academy/Plaud Library/_drive_docx_sync`. Iris Content Pipeline Notion DB is `043dad6e20c043fbbb4f35f545d2d4b9`; use draft-only Thai items with marker notes for dedupe.
- 2026-05-22 workshop pipeline processed local source `2026-05-21_rem-koning-ai-native-organizations-money.md` into 6 draft-only Iris Notion pages with marker `Kaijeaw workshop content cron 2026-05-22`; local pack saved at Plaud Library `_content_pipeline_drafts/2026-05-22/rem-koning-ai-native-draft-pack.md`. Latest rclone Plaud `.docx` visible then was still 2026-05-18.
- 2026-05-23 workshop pipeline created 8 draft-only Iris Notion pages from recent Plaud `.docx` transcripts (2026-05-18 Claude Core Work/Codex/memory system; 2026-05-16 AMS/Zapier/Vercel/CRM, CCTV/Gemma, 10-80-10). Exact hooks include `AI Agent ไม่ได้เริ่มจาก Tools แต่เริ่มจาก Memory System`, `ระบบความจำ 3 ชั้นของ AI Agent`, and `AMS + Zapier + Vercel + CRM`. Avoid duplicating these unless making improved variants.
- 2026-08-01 run processed `[Plaud]07-31 ... AI First Team Members...docx` into 6 verified Iris `📝 Draft` rows. Local summary: Plaud Library `2026-07-31_ai-agent-first-team-members.md`; draft pack: `_content_pipeline_drafts/2026-08-01/plaud-2026-07-31-ai-first-team-members-draft-pack.md`. Core angles: AI Team Member, System Prompt as Job Description, connectors/tools, Skills/SOP, Schedule Task, human audit.

## 2026-07-10 — Thai Threads Daily
- 2026-08-05: Jet asked to stop Threads publishing. Cron `kaijeaw-daily-thai-threads-post` (`a8b932969f00`) is paused; do not resume or publish to Threads without explicit approval. Draft-only pipeline work may continue.
- Threads account: 6182 (@jeditrinupab)
- Notion DB: 043dad6e20c043fbbb4f35f545d2d4b9 (Iris Content Pipeline)
- Source: /Users/ultrafriday/clawd/builds/limitless-club-website/client/public/blog/articles.json
- Blotato API endpoint: https://backend.blotato.com/v2/posts — payload requires: post.content.text, post.content.mediaUrls[], post.content.platform, post.target.targetType, scheduledTime at root
- Notion property types: Hook=title, Type=select, Stage=select, Channel=select, Topic Category=select, Priority=select, Heat=select, Hook Type=select, Urgency=select, Scheduled=date, Notes=rich_text, Related Long-form=rich_text, SEO Tags=rich_text, Target Length=rich_text (was select in old spec — now rich_text!)


## Blotato/Notion payload format fixes (2026-07-14)
- Blotato `accountId` must be at `post.accountId` level (root of post object)
- Notion: use `POST /v1/pages` with `parent.database_id`, NOT `/v1/databases/{id}/pages`
- Notion URL: `https://www.notion.so/{id_without_dashes}`
- 2026-08-04: Plaud→Iris pipeline processed distinct 2026-07-30 `AI Transcribe + Codex scheduled ops` transcript into 6 verified Iris `📝 Draft` rows. Existing same-date 07-30 Codex browser/API packs did not exhaust this separate transcript; 08-03 FB Live calendar item still had no Plaud transcript visible at run time.
- 2026-08-05: Plaud→Iris pipeline processed remaining distinct 2026-07-30 `ChatGPT Codex + AI Agents app-building` transcript into 6 verified Iris `📝 Draft` rows. Core angles: business problem before app UI, `design.md` as reusable AI brief, blueprint/mockup/build-guide workflow, and founder skill = explaining systems clearly to AI. Calendar showed 08-05 Private: Panpuri but no matching Plaud transcript visible yet.
- 2026-08-06: Compact workshop-content cron processed newly visible `[Plaud]08-05 ... Claude Co-work` transcript into exactly one Thai pack (8-slide carousel outline + Threads/X post). Local output: `Agents/Kaijeaw/Outputs/Workshop Content/2026-08-06.md`; Iris page: `https://app.notion.com/p/Carousel-Threads-AI-Agent-Chatbot-3b4d076c9ad381ccb4fdc9ad4594a5cc`. Core angle: AI Agent = digital employee needing JD/System Prompt, tools/connectors, Skills/SOP, Schedule Task.
- 2026-08-07: Compact workshop-content cron processed newly available `[Plaud]08-03 ... การสร้าง AI Agent แรกของคุณใน 60 นาทีร่วมกับสภาวิชาชีพบัญช` transcript after confirming it was not covered by local outputs/drafts. Local output: `Agents/Kaijeaw/Outputs/Workshop Content/2026-08-07.md`; Plaud summary: `Plaud Library/2026-08-03_ai-agent-first-tfac.md`; Iris page: `https://app.notion.com/p/AI-Agent-Prompt-Workspace-AI-3b5d076c9ad38189b495e0f1e2aa9533`. Core angle: AI Agent starts from AIOS workspace/JD/context/tools, not perfect prompts.


- 2026-08-10: Processed Plaud source `[Plaud]08-08 การบรรยาย: การประยุกต์ใช้ AI และการสร้าง AI Agent สำหรับผู้นำธุรกิจ.docx` (calendar: Shortcut to AI day 1) into compact Thai content pack `Agents/Kaijeaw/Outputs/Workshop Content/2026-08-10.md`; Iris draft verified at `https://app.notion.com/p/Thai-Carousel-Draft-AI-Tool-3b8d076c9ad381729029dda67f0f8ebe`.

## JediStack local knowledge spine
- JediStack is Jet's non-destructive canonical IP and recall overlay at `/Users/ultrafriday/Projects/jedistack`.
- The original `_IP-Index` remains read-only evidence; JediStack links 16 master frameworks to quotes, operator proof, student proof, ROI, offers, and exact sources.
- Cross-agent local retrieval is available with `python3 /Users/ultrafriday/Projects/jedistack/scripts/search_jedistack.py "<question>"`.
- The private GitHub package is sanitized; raw sessions, credentials, client/private material, and sensitive IP stay local.
