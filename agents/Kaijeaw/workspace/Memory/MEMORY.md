# Kaijeaw Memory

Durable human-readable memory for Kaijeaw. Do not store secrets here.

## Plaud → Iris Content Pipeline
- For scheduled workshop transcript jobs, the live path works: use rclone against Drive folder `1MYsST8lFfSbVyoNGKpRen6tX2fkEAZDS`, copy recent DOCX into Plaud Library `_drive_docx_sync/`, extract with `textutil`, save draft packs under `_content_pipeline_drafts/YYYY-MM-DD/`, and create Iris Content Pipeline drafts via Notion REST when the notion skill/tool is unavailable.
- Iris Content Pipeline DB ID: `043dad6e20c043fbbb4f35f545d2d4b9`; verified Stage option `📝 Draft` and useful channels `Threads`, `Instagram`, `Longform`.
- Calendar-aware runs can query `trinupab@creatuscorp.net` using Hermes Google token JSONs; prefer the token's embedded OAuth client credentials for refresh. If iCloud Plaud files hit `Resource deadlock avoided`, re-copy the exact DOCX from Drive via rclone to `/tmp` and extract with ElementTree.
- For the calendar-aware workshop content pipeline, do not trust the local Plaud iCloud folder alone. Recent `.docx` Plaud transcripts are in Google Drive folder `1MYsST8lFfSbVyoNGKpRen6tX2fkEAZDS`; use `rclone lsf gdrive: --drive-root-folder-id 1MYsST8lFfSbVyoNGKpRen6tX2fkEAZDS --files-only --format 'pt'` when Drive API listing fails or returns empty. Local synced copies may also exist under `/Users/ultrafriday/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Limitless Academy/Plaud Library/_drive_docx_sync`. Iris Content Pipeline Notion DB is `043dad6e20c043fbbb4f35f545d2d4b9`; use draft-only Thai items with marker notes for dedupe.
- 2026-05-22 workshop pipeline processed local source `2026-05-21_rem-koning-ai-native-organizations-money.md` into 6 draft-only Iris Notion pages with marker `Kaijeaw workshop content cron 2026-05-22`; local pack saved at Plaud Library `_content_pipeline_drafts/2026-05-22/rem-koning-ai-native-draft-pack.md`. Latest rclone Plaud `.docx` visible then was still 2026-05-18.
- 2026-05-23 workshop pipeline created 8 draft-only Iris Notion pages from recent Plaud `.docx` transcripts (2026-05-18 Claude Core Work/Codex/memory system; 2026-05-16 AMS/Zapier/Vercel/CRM, CCTV/Gemma, 10-80-10). Exact hooks include `AI Agent ไม่ได้เริ่มจาก Tools แต่เริ่มจาก Memory System`, `ระบบความจำ 3 ชั้นของ AI Agent`, and `AMS + Zapier + Vercel + CRM`. Avoid duplicating these unless making improved variants.

## 2026-07-10 — Thai Threads Daily
- Blotato API:  (key: blt_FV5fy...)
- Threads account: 6182 (@jeditrinupab)
- Notion DB: 043dad6e20c043fbbb4f35f545d2d4b9 (Iris Content Pipeline)
- Source: /Users/ultrafriday/clawd/builds/limitless-club-website/client/public/blog/articles.json
- Blotato API endpoint: https://backend.blotato.com/v2/posts — payload requires: post.content.text, post.content.mediaUrls[], post.content.platform, post.target.targetType, scheduledTime at root
- Notion property types: Hook=title, Type=select, Stage=select, Channel=select, Topic Category=select, Priority=select, Heat=select, Hook Type=select, Urgency=select, Scheduled=date, Notes=rich_text, Related Long-form=rich_text, SEO Tags=rich_text, Target Length=rich_text (was select in old spec — now rich_text!)


## Blotato/Notion payload format fixes (2026-07-14)
- Blotato `accountId` must be at `post.accountId` level (root of post object)
- Notion: use `POST /v1/pages` with `parent.database_id`, NOT `/v1/databases/{id}/pages`
- Notion URL: `https://www.notion.so/{id_without_dashes}`
