# Bolt Durable Memory

No durable facts added by the 2026-07-22 nightly sync.

## Limitless AI Leverage Audit landing
- Project: `/Users/ultrafriday/Projects/limitless-ai-leverage-audit-landing`.
- As verified 2026-08-17, `https://limitless-ai-leverage-audit-landing.vercel.app/` and `/api/health` are anonymously reachable (HTTP 200), but `jeditrinupab.com` still has no live link/offer bridge to the audit.
- A tested, uncommitted bilingual homepage bridge patch exists in `/Users/ultrafriday/.hermes/exports/limitless-club-website-main-youtube` (`Home.tsx`, `LanguageContext.tsx`); it needs Jet approval before production deployment.
- As verified 2026-08-24, the deployed audit had no outbound parent-brand, proof, or privacy links. A tested local trust-bridge patch now exists in `public/index.html` plus `test-integration.js`; reversible patch/screenshots are under `/Users/ultrafriday/.hermes/exports/limitless-ai-leverage-audit-2026-08-24/`. It is not deployed and needs Jet approval.
- The form intentionally returns failure unless a durable adapter acknowledges storage. Confirm the production CRM/email destination and test receipt before treating lead capture as production-complete.
- 2026-08-31 live evidence: the deployed production endpoint still returns a false-success 302 to `/thank-you.html` despite zero Vercel env vars. A newer tested local rescue (`public/form-submit.js`) now requires `?status=saved` and offers LINE on failure; it is not deployed.

## JediStack local knowledge spine
- JediStack is Jet's non-destructive canonical IP and recall overlay at `/Users/ultrafriday/Projects/jedistack`.
- The original `_IP-Index` remains read-only evidence; JediStack links 16 master frameworks to quotes, operator proof, student proof, ROI, offers, and exact sources.
- Cross-agent local retrieval is available with `python3 /Users/ultrafriday/Projects/jedistack/scripts/search_jedistack.py "<question>"`.
- The private GitHub package is sanitized; raw sessions, credentials, client/private material, and sensitive IP stay local.

## Thai Wealth Planner
- Project: `/Users/ultrafriday/Projects/wealth-planner-lead-magnet`; canonical production URL: `https://wealth-planner-lead-magnet.vercel.app`.
- It is a static Thai-first no-login planner (`index.html`, `styles.css`, `app.js`) linked to the Vercel project `wealth-planner-lead-magnet`; the local Git repo currently has no remote.
- Investment-return assumptions are user-selectable at 3%, 4%, 5%, or 7% per year and are explicitly presented as educational estimates, not guarantees.
- The production results page can email a personalized Thai report through `/api/send-report` using dedicated sender `wealth-planner@agentmail.to`. Provider credentials are server-only Vercel variables; the active credential is limited to inbox read and message send permissions.
- The report endpoint accepts structured calculator data, recomputes financial results server-side, and renders controlled templates; it is not an arbitrary email relay.

## jeditrinupab.com YouTube blog pipeline
- Daily checker: `/Users/ultrafriday/.hermes/profiles/bolt/scripts/youtube_blog_daily_check.py`; transcript fallback order is YouTube captions → Apify → audio transcription.
- As of 2026-08-17, the checker resolves its index to `/Users/ultrafriday/.hermes/exports/limitless-club-website`, whose `thai-seo-pages` branch is dirty and heavily divergent from `origin/main`. A local “already in blog” result does not prove production publication.
- Always compare the latest IDs against fresh production `https://jeditrinupab.com/blog/articles.json`; if local-only entries exist, recover in a clean `origin/main` worktree. Rebuild the index from `origin/main` plus only the new item (do not copy a dirty export index wholesale), then stage only the index and matching article JSON.
- Recovery commit `14b4f92` published four missing IDs (`ydIO1-Sd7xg`, `Swap30KH4C4`, `DgsdH92i88E`, `M0P3HqctSP4`) and was live-verified.

## AI Event Opportunity Survey
- Project: `/Users/ultrafriday/Projects/ai-event-opportunity-survey`; canonical production URL: `https://ai-event-opportunity-survey.vercel.app`.
- The Thai-first public survey writes through `/api/submit-survey` to the dedicated Airtable table `Event AI Opportunity Survey — Aug 2026` in the AI Readiness Leads base. Airtable credentials are Vercel production variables and never belong in browser code.
- The live form is a three-step, eight-question intake: legal name, nickname, mobile, role, optional company, most-used AI + use cases, email, and a required Selfie with Jedi/Booth. It keeps required PDPA/photo consent separate from optional marketing consent.
- Selfies are compressed in the browser, validated server-side, and uploaded to Airtable's attachment endpoint. The endpoint deletes an incomplete record if its attachment fails and returns a draw code only after both record and photo succeed.
- Print-ready event QR assets live at `assets/ai-event-survey-qr.png` and `.svg`; the QR includes offline event UTM attribution.
- The app intentionally has no email sending or tracking pixels. Marketing follow-up must be limited to respondents whose `Marketing Consent` is checked.

## Your Kids’ Memories
- Project: `/Users/ultrafriday/.hermes/exports/your-kids-memories`; canonical production URL: `https://your-kids-memories.vercel.app`; Vercel project: `jetlaunchers-projects/your-kids-memories`.
- The current release is an installable local-first PWA: images are compressed and stored in browser IndexedDB, not uploaded to a server. Backup export/import is built in.
- Cross-device sync is intentionally absent; adding it requires private authentication plus protected cloud object storage.
