# OpenClaw Legacy Triage + Hermes Import Plan — 2026-05-24

Remote `njjimac` retry: Tailscale ping works, but SSH/Tailscale SSH and file sharing are still refused. I proceeded with local matching OpenClaw/clawd folders on this Mac, which appear to contain the same legacy workspace and outputs. Secret-like paths were excluded from reads.

## Inventory summary
- Full safe manifest: `safe_manifest.csv`
- Focused candidate CSV: `focused_candidates.csv`
- Full inventory note: `2026-05-23-local-openclaw-inventory.md`
- Focused candidate note: `2026-05-23-focused-openclaw-candidates.md`

## Classified high-value buckets
- **profile_rules**: 10 files
- **shared_protocols**: 2 files
- **skills**: 7 files
- **scripts_tools**: 35 files
- **content_pipelines**: 406 files
- **research_assets**: 4883 files
- **course_transcripts**: 8 files
- **archives**: 205 files

## Recommended installs / changes
1. **Install an OpenClaw legacy migration skill** — repeatable safe inventory + triage workflow for future remote archive/import work.
2. **Patch/extend Hermes memory protocol** with OpenClaw lessons: no mental notes, daily + curated memory split, group-chat privacy, heartbeat-vs-cron decision rule. Much of this already exists in Kelly SOUL; keep as a protocol/reference rather than duplicate hard rules everywhere.
3. **Promote shared INTEL-FEED pattern into Hermes/Obsidian**: use Shared Memory/Daily + project files as the equivalent coordination feed, not legacy `INTEL-FEED.md`.
4. **Review content pipeline assets**: Blaze-era carousel/content-output and YouTube transcript scripts map to existing Hermes skills (`jet-daily-content-engine`, `youtube-content`, carousel generation skills). Patch those later instead of creating many duplicate skills.
5. **Archive plugin catalog imports**: cloned `.tmp/plugins` contains many generic SKILL.md files. Do not bulk-install; import only on demand after checking overlap with existing Hermes skills.

## Top files to inspect next

### profile_rules
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-line-admin/AGENTS.md` — .md, 4330 bytes, 2026-03-12 18:57:41
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-main/AGENTS.md` — .md, 6365 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-forge/AGENTS.md` — .md, 2822 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-canvas/AGENTS.md` — .md, 4263 bytes, 2026-03-12 18:57:41
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-kai/AGENTS.md` — .md, 3369 bytes, 2026-03-12 18:57:41
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-scout/AGENTS.md` — .md, 3002 bytes, 2026-03-12 18:57:41
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-nova/AGENTS.md` — .md, 3732 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-uncle-chris/AGENTS.md` — .md, 3564 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-blaze/AGENTS.md` — .md, 5144 bytes, 2026-03-12 18:57:41
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-coach-marc/AGENTS.md` — .md, 3103 bytes, 2026-03-12 18:57:40

### shared_protocols
- `/Users/ultrafriday/.openclaw/workspace/HEARTBEAT.md` — .md, 1293 bytes, 2026-05-19 16:49:50
- `/Users/ultrafriday/.openclaw/workspace/AGENTS.md` — .md, 8328 bytes, 2026-05-01 12:13:02

### skills
- `/Users/ultrafriday/.openclaw/skills/higgsfield-soul-id/SKILL.md` — .md, 3355 bytes, 2026-05-06 16:23:09
- `/Users/ultrafriday/.openclaw/skills/higgsfield-soul-id/references/troubleshooting.md` — .md, 538 bytes, 2026-05-06 16:23:09
- `/Users/ultrafriday/.openclaw/skills/higgsfield-soul-id/references/photo-guide.md` — .md, 720 bytes, 2026-05-06 16:23:09
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-main/skills/youtube-to-gamma.md` — .md, 1831 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/skills/youtube-thumbnail-beast-skill.md` — .md, 1370 bytes, 2026-03-01 22:00:25
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/skills/CLAUDE-CODE-SKILLS-REFERENCE.md` — .md, 917 bytes, 2026-03-20 19:12:07
- `/Users/ultrafriday/clawd/second-brain/src/app/api/mc/skills/route.ts` — .ts, 2081 bytes, 2026-04-02 08:15:58

### scripts_tools
- `/Users/ultrafriday/.openclaw/workspace/scripts/friday-recall.sh` — .sh, 706 bytes, 2026-05-17 18:09:12
- `/Users/ultrafriday/.openclaw/workspace/scripts/sync-friday-memory-to-gbrain.sh` — .sh, 1605 bytes, 2026-05-22 04:19:12
- `/Users/ultrafriday/.openclaw/workspace/scripts/friday_os.py` — .py, 15719 bytes, 2026-05-08 21:16:30
- `/Users/ultrafriday/clawd/youtube-transcripts/download-corpus.sh` — .sh, 3703 bytes, 2026-03-03 04:43:57
- `/Users/ultrafriday/clawd/youtube-transcripts/pipeline/outlier-scanner.py` — .py, 4661 bytes, 2026-03-14 22:31:57
- `/Users/ultrafriday/clawd/youtube-transcripts/pdf-perks/generate_companion_pdf.py` — .py, 11923 bytes, 2026-04-30 08:39:06
- `/Users/ultrafriday/clawd/youtube-transcripts/testimonials/download_transcripts.py` — .py, 10752 bytes, 2026-03-03 12:21:15
- `/Users/ultrafriday/clawd/youtube-transcripts/gamma-summaries/generate_gamma_summaries.py` — .py, 6734 bytes, 2026-04-30 08:48:16
- `/Users/ultrafriday/clawd/second-brain-imac/docs/deliverable/2026-02-25-openclaw-classroom-installer/install-openclaw-students.sh` — .sh, 2066 bytes, 2026-02-25 22:51:45
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-forge/sync-memories-to-supabase.py` — .py, 4997 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-forge/jetcompressor-fix/pdf-compressor/app.py` — .py, 13780 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-scout/carousel/generate_slides.py` — .py, 6355 bytes, 2026-03-12 18:57:41
- `/Users/ultrafriday/clawd/backups/2026-03-12_1857/agents-blaze/carousel/generate_slides.py` — .py, 6355 bytes, 2026-03-12 18:57:40
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/mc-health-check-cron.sh` — .sh, 919 bytes, 2026-03-12 16:02:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/mc-health-check.sh` — .sh, 3727 bytes, 2026-03-26 16:06:30
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/forge-2026-04-07-status-checker.sh` — .sh, 2190 bytes, 2026-04-07 16:06:54
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/mc-health-check.py` — .py, 2856 bytes, 2026-03-12 16:02:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/mc-health-check-v1.1.py` — .py, 3237 bytes, 2026-03-21 16:02:35
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/5-mistakes-thai-v2/composite_v4.py` — .py, 6993 bytes, 2026-03-01 22:00:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/5-mistakes-thai-v2/generate_cover.py` — .py, 3438 bytes, 2026-03-01 22:00:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/5-mistakes-thai-v2/composite.py` — .py, 5598 bytes, 2026-03-01 22:00:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/5-mistakes-thai-v2/generate_all.py` — .py, 13553 bytes, 2026-03-01 22:00:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/youtube-transcripts/download-corpus.sh` — .sh, 3599 bytes, 2026-03-01 22:00:22
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/lead-magnets/push-to-notion.py` — .py, 3194 bytes, 2026-03-01 22:00:24
- `/Users/ultrafriday/clawd/second-brain/docs/deliverable/nova/sops/line-oa-setup.sh` — .sh, 13976 bytes, 2026-03-01 22:00:25

### content_pipelines
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-05-14-instagram-carousel-idea-bank-thai-business-owners.md` — .md, 32930 bytes, 2026-05-14 08:44:02
- `/Users/ultrafriday/clawd/second-brain-imac/docs/deliverable/2026-02-16-carousel-ai-works-while-you-sleep.md` — .md, 6468 bytes, 2026-02-25 22:51:45
- `/Users/ultrafriday/clawd/second-brain-imac/docs/deliverable/2026-02-10-full-all-carousels---complete-slides.md` — .md, 4711 bytes, 2026-02-15 10:44:17
- `/Users/ultrafriday/clawd/second-brain-imac/docs/deliverable/2026-02-16-carousel-vibe-managing.md` — .md, 6462 bytes, 2026-02-25 22:51:45
- `/Users/ultrafriday/clawd/second-brain-imac/docs/deliverable/2026-02-16-carousel-vs.md` — .md, 5887 bytes, 2026-02-25 22:51:45
- `/Users/ultrafriday/clawd/second-brain-imac/docs/deliverable/2026-02-16-carousel-ceo-falling-behind-without-ai.md` — .md, 6291 bytes, 2026-02-25 22:51:45
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/linkedin-carousel-research-feb-2026.md` — .md, 5009 bytes, 2026-02-04 18:46:36
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/carousel-scripts-feb-2026.md` — .md, 10438 bytes, 2026-02-04 18:57:49
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/carousel-ideas-feb-2026.md` — .md, 6001 bytes, 2026-02-04 18:21:52
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/02-5-signs-ai-wrong-english.md` — .md, 3812 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/CONTENT-PACKAGE-INDEX.md` — .md, 3139 bytes, 2026-02-04 17:54:25
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/03-automated-80-percent-english.md` — .md, 4606 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/03-automated-80-percent-thai.md` — .md, 8531 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/viewer-5-signs-ai-wrong.html` — .html, 16086 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/01-10k-ai-stack-english.md` — .md, 4054 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/README.md` — .md, 1502 bytes, 2026-02-04 17:53:56
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/viewer-automated-80.html` — .html, 20460 bytes, 2026-02-04 17:54:25
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/viewer-10k-ai-stack.html` — .html, 13697 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/00-caption-bank-cta-variations.md` — .md, 11158 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/01-10k-ai-stack-thai.md` — .md, 8072 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/second-brain-imac/docs/content/instagram-carousels/02-5-signs-ai-wrong-thai.md` — .md, 7376 bytes, 2026-02-04 17:53:44
- `/Users/ultrafriday/clawd/content-output/carousel-before-vs-after-ai.md` — .md, 4225 bytes, 2026-03-01 21:59:13
- `/Users/ultrafriday/clawd/content-output/carousel-ai-marketing-2026.md` — .md, 956 bytes, 2026-03-06 07:01:30
- `/Users/ultrafriday/clawd/content-output/carousel-chatgpt-vs-claude-th.md` — .md, 1719 bytes, 2026-03-03 07:01:53
- `/Users/ultrafriday/clawd/content-output/carousel-1-blaze-20260307.md` — .md, 2925 bytes, 2026-03-07 14:00:43

### research_assets
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/yHwng5oP4E0.th.txt` — .txt, 63114 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/INDEX.md` — .md, 1212 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/RH_pM1wzo18.th.txt` — .txt, 7911 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/oyw9Wjx7M8s.th.txt` — .txt, 41770 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/qsh-vqC5Dck.th.txt` — .txt, 51664 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/yoJmVOLfVnU.th.txt` — .txt, 30438 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/thai-ai-outliers/creativerich-39k-สอนใช้ AI หาเงิน 10,000 ต่อเดือน ep.108.txt` — .txt, 6881 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/thai-ai-outliers/dashboard-37k-🔥 สร้าง Dashboard วิเคราะห์ข้อมูลขาย แบบอัตโนมัติ ด้วย AI.txt` — .txt, 8064 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/thai-ai-outliers/9arm-620k-ผมสรุปตลาด AI ในปี 2025.txt` — .txt, 7735 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/thai-ai-outliers/README.md` — .md, 6625 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/thai-ai-outliers/woody-261k-AI เปลี่ยนชีวิต! ใช้ AI ยังไงให้สร้างเงินล้านใน 30 วัน？ ｜ WOODY FM.txt` — .txt, 8024 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/team-assets/youtube/youtube-transcripts/thai-ai-outliers/mewsocial-44k-วิธีสร้างเครื่องจักร AI ทำเงินจากศูนย์ ｜ 7 หลักใน 5 เดือน.txt` — .txt, 8097 bytes, 2026-03-02 19:23:56
- `/Users/ultrafriday/clawd/youtube-transcripts/sL_KBnYB17I-codex-marketing-skills-transcript.txt` — .txt, 54640 bytes, 2026-05-19 14:36:33
- `/Users/ultrafriday/clawd/youtube-transcripts/20260320 - AI ร่างโคลน คู่แข่ง Claude Cowork จากค่าย Meta.md` — .md, 68665 bytes, 2026-05-13 08:34:54
- `/Users/ultrafriday/clawd/youtube-transcripts/20251013 - คู่มือสร้างความมั่งคั่งจากคุณ Kim Property Live.md` — .md, 198667 bytes, 2026-05-13 08:34:54
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-03-20 - Claude Code, Anti-Gravity IDE และการสร้างระบบ AI สำหรับธุรกิจ.md` — .md, 9350 bytes, 2026-03-21 06:08:55
- `/Users/ultrafriday/clawd/youtube-transcripts/20260212 - 6 OpenClaw use cases I promise will change your life.md` — .md, 22294 bytes, 2026-05-13 08:34:54
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-05-20_uncapped-50-tobi-lutke-shopify.json` — .json, 144636 bytes, 2026-05-20 22:02:43
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-05-20_uncapped-50-tobi-lutke-shopify.txt` — .txt, 76551 bytes, 2026-05-20 22:03:32
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-02-10-bible-money-lessons.md` — .md, 22727 bytes, 2026-05-13 08:34:54
- `/Users/ultrafriday/clawd/youtube-transcripts/sL_KBnYB17I-codex-marketing-skills-transcript.md` — .md, 55820 bytes, 2026-05-19 14:36:33
- `/Users/ultrafriday/clawd/youtube-transcripts/LAVwtZS_QwY-clean-transcript.txt` — .txt, 154442 bytes, 2026-03-07 21:35:38
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-05-13 - Nick from Orgo - One Person AI Agent Business Playbook.md` — .md, 42643 bytes, 2026-05-13 08:47:34
- `/Users/ultrafriday/clawd/youtube-transcripts/20250314 - 3 เครื่องมือ ที่นักการตลาด และ เจ้าของธุรกิจห้ามพลาด !!.th.txt` — .txt, 70106 bytes, 2026-03-01 21:59:13
- `/Users/ultrafriday/clawd/youtube-transcripts/2026-02-10-bible-money-lessons.en.txt` — .txt, 22488 bytes, 2026-03-01 21:59:13

## System improvements to carry forward
- Use a single visible coordination layer: Obsidian Shared Memory daily/project notes replace OpenClaw `INTEL-FEED.md`.
- Keep delivery routing explicit per agent, but store it in Hermes profiles/skills, not scattered AGENTS.md backups.
- For proactive checks, prefer batched low-noise heartbeat/local scanner work; reserve cron for exact timing or isolated scheduled deliveries.
- Never bulk-copy legacy configs; inventory and classify first, then import only reusable, non-secret workflows.
- Convert repeated outputs into skills/protocols; leave raw generated outputs as archive/reference.
