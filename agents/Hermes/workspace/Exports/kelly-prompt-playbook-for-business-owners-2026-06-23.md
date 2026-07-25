# The Kelly Prompt Playbook

**A field guide for business owners using their Hermes system — built from Jet’s real prompts to Kelly.**

- Source: local Hermes session database (`~/.hermes/state.db`)
- Time span: **2026-04-21 → 2026-06-23**
- Raw user messages reviewed: **3,418**
- Non-trivial prompts cataloged: **3,396**
- Unique sanitized prompts/patterns: **1,073**
- Privacy: emails, phone-like strings, API keys/tokens/password-shaped text, and URL query strings were redacted.

## How to read this

This is not a generic AI prompt list. It is a practical operating manual for business owners who have a Hermes-style agent team. The examples are based on real prompts, rewritten or lightly sanitized where needed. The important lesson is not the exact wording; it is the **management motion** behind each prompt.

A strong Hermes prompt usually has 5 parts:

1. **Outcome** — what should exist when the agent is done.
2. **Source of truth** — where to look: file, dashboard, transcript, account, URL, repo, memory, prior session.
3. **Operating rule** — constraints, safety, quality bar, owner, cadence, format.
4. **Verification** — run it, open it, test it, show output, cite source.
5. **Packaging** — document, send, attach, publish, make it student/customer-ready.

## Prompt distribution

| Category | Non-trivial prompts |
|---|---:|
| Operate / fix my Hermes system | 3,009 |
| General commands / iteration | 229 |
| Research / find / monitor | 51 |
| Content / teaching asset creation | 35 |
| Build / code / deploy | 27 |
| Computer/browser control | 13 |
| Business / strategy / revenue | 13 |
| Creative media generation | 10 |
| Personal productivity / ops | 9 |

| Prompt type | Count |
|---|---:|
| Iteration / refinement | 1,965 |
| Question / diagnosis | 761 |
| Directive / context | 632 |
| Action prompt | 34 |
| Creation prompt | 4 |

## The 12 business-owner prompt moves

### 1. Turn the agent into an operator, not a chatbot
- **Principle:** Ask for an outcome and verification, not advice.
- **Prompt shape:** “Can you try and run it? Show me the actual output.”
- **Best for:** Use when you need proof that a workflow, code path, dashboard, or automation really works.

### 2. Ask for ownership and failure modes
- **Principle:** Make the agent surface who/what owns the process and how it can break.
- **Prompt shape:** “Is there someone responsible? What is the update cadence and failure mode?”
- **Best for:** Use for alerts, dashboards, cron jobs, automations, and revenue monitors.

### 3. Convert raw context into teaching assets
- **Principle:** Ask the agent to turn internal work into student-facing guides, decks, or frameworks.
- **Prompt shape:** “Create a full document of all the prompts I’ve used so students know how to leverage Hermes.”
- **Best for:** Use for course material, workshops, onboarding, playbooks, and repeatable frameworks.

### 4. Make it source-grounded
- **Principle:** Force the agent to read the real file/source/session before synthesizing.
- **Prompt shape:** “Use our previous work. Search sessions and memory first.”
- **Best for:** Use whenever the answer depends on prior context or internal truth.

### 5. Delegate to the agent team
- **Principle:** Assign work to the best agent/runtime instead of one overloaded chat.
- **Prompt shape:** “Route content to Blaze and research to Signal where appropriate.”
- **Best for:** Use when tasks split into research, creative, coding, ops, and QA.

### 6. Ask for a production artifact
- **Principle:** Request a file, URL, deploy, dashboard, attachment, or published page.
- **Prompt shape:** “Don’t just explain it — create the document and send me the file.”
- **Best for:** Use when the result must be used by students/customers/team members.

### 7. Demand an audit before action
- **Principle:** Make the agent inspect the current state before changing it.
- **Prompt shape:** “Check what exists first. Don’t create a duplicate.”
- **Best for:** Use for Notion pages, dashboards, repos, crons, and memory systems.

### 8. Iterate with taste
- **Principle:** Give fast, concrete refinements after seeing a draft.
- **Prompt shape:** “Make it more premium. Less generic. More math-grounded.”
- **Best for:** Use for brand, design, copy, carousels, offers, and decks.

### 9. Turn business intuition into numbers
- **Principle:** Ask the agent to model ROI, capacity, pricing, conversion, or time budgets.
- **Prompt shape:** “Play forward the scenarios and show the math.”
- **Best for:** Use for offers, cohort pricing, ads, hiring, time allocation, and strategy.

### 10. Build monitoring loops
- **Principle:** Ask for recurring checks plus alerts only when action is needed.
- **Prompt shape:** “Monitor this 4x daily and only alert me on meaningful changes.”
- **Best for:** Use for revenue, spend, newsletters, search visibility, feeds, and ops risks.

### 11. Package internal systems into student templates
- **Principle:** Strip private details and turn the workflow into reusable instructions.
- **Prompt shape:** “Depersonalize this so business owners can copy the pattern.”
- **Best for:** Use for productizing your AI operating system.

### 12. Preserve institutional memory
- **Principle:** Ask the agent to write the durable note and handoff after non-trivial work.
- **Prompt shape:** “Save the decision, files changed, blocker, and next owner.”
- **Best for:** Use so your agent team compounds rather than starts over.

## Prompt library by operating category

### Build / code / deploy

**What this category teaches:**
Ask for working software, not plans. The agent should inspect, edit, run, test, deploy, and verify.

| Real prompt pattern | How students can adapt it |
|---|---|
| “[Your active task list was preserved across context compression] / - [ ] do-check. DigitalOcean account termination - review and act (pending) / - [ ] thai-reg. Thai business registration letter - review Thai text for…” | Add repo/path, desired behavior, test command, and deployment target. |
| “Return exactly: GROK_SUBSCRIPTION_OK” | Add repo/path, desired behavior, test command, and deployment target. |
| “Return exactly: DEFAULT_CODEX_OK” | Add repo/path, desired behavior, test command, and deployment target. |
| “[Your active task list was preserved across context compression] / - [ ] retry-sync. Run sync script again with backoff to catch the 4 failed pages (pending)” | Add repo/path, desired behavior, test command, and deployment target. |
| “[Your active task list was preserved across context compression] / - [>] retry-sync. Run sync script again with backoff to catch the 4 failed pages (in_progress)” | Add repo/path, desired behavior, test command, and deployment target. |
| “can you turn the book into a live html file so i can view it and also deploy it to vercel” | Add repo/path, desired behavior, test command, and deployment target. |
| “when you're done redeploy it to vercel” | Add repo/path, desired behavior, test command, and deployment target. |
| “Consolidate the top-level + domain-specific CLAUDE.md files (brand, social, sales, coaching, finance, team ops, content library) into a clean "Foundations" library for the AI Team Build Sprint product.” | Add repo/path, desired behavior, test command, and deployment target. |
| “Extract the Vibe Coding patterns + reusable prompt library from the Vibe Coded Projects tree and Customer Projects for the AI Team Build Sprint product.” | Add repo/path, desired behavior, test command, and deployment target. |
| “https://build.nvidia.com/spark/vss /  / าำสสั ะ้รห  ีืแะรนื สนนาห หียำพ แนนส+” | Add repo/path, desired behavior, test command, and deployment target. |
| “https://x.com/undefinedki/status/[phone]?[query-redacted] /  / I want to build this system for us” | Add repo/path, desired behavior, test command, and deployment target. |
| “[IMPORTANT: Background process proc_a209c42f9172 completed (exit code 0). / Command: python3 /tmp/jet_podcast_transcript/transcribe.py > /tmp/jet_podcast_transcript/transcribe.log 2>&1 / Output: / ]” | Add repo/path, desired behavior, test command, and deployment target. |
| “But I also have Gemini subscription at the $100 plan. /  / Can we wire Gemini into u too?” | Add repo/path, desired behavior, test command, and deployment target. |
| “https://www.instagram.com/p/DZizqkvk-nH/?[query-redacted] /  / I want to build my own version” | Add repo/path, desired behavior, test command, and deployment target. |
| “[System note: Your previous turn was interrupted before you could process the last tool result(s). The conversation history contains tool outputs you haven't responded to yet. Please finish processing those results an…” | Add repo/path, desired behavior, test command, and deployment target. |
| “[IMPORTANT: Background process proc_[phone]d1 completed (exit code 0). / Command: GOOGLE_OAUTH_PORT=8766 python3 /tmp/google_loopback_reauth.py / Output: / GOOGLE_OAUTH_LISTENER_READY port=8766 targets=2 / GOOGLE_OAUT…” | Add repo/path, desired behavior, test command, and deployment target. |
| “i want you to connect to claude code cli. /  / please help me wire it up so you can use it to help me on certain tasks.” | Add repo/path, desired behavior, test command, and deployment target. |
| “[IMPORTANT: Background process proc_f55740cf585f completed normally (exit code 0). / Command: claude auth login --claudeai --email [email] / Output: / Opening browser to sign in… / If the browser didn't open, visit: h…” | Add repo/path, desired behavior, test command, and deployment target. |

### Business / strategy / revenue

**What this category teaches:**
Use Hermes as a strategy partner that can model numbers, compare offers, monitor revenue, and challenge assumptions.

| Real prompt pattern | How students can adapt it |
|---|---|
| “I will launch the cohort method in October onwards. /  / 6 days with me total” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “Check our Airtable it should be in there” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “Give me a stripe link for 60,400 bht” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “[The user sent a voice message~ Here's what they said: "I thought I added the stripe key already, check in our system, it should be there."]” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “Help me check  /  /  how many registrations are on the August 29th inside our airtable” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “Give me a stripe link for 10,300 Thai baht for Ai online courses package” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “the stripe link doesn't work” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “need stripe link” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “awesome whats our revenue now for this month” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “https://x.com/businessbarista/status/[phone]?[query-redacted]” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “send me a screenshot of the meta spend” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “send me a screenshot of the meta spend /  / which URL did you use?” | Add assumptions, numbers, constraints, and the decision you are trying to make. |
| “Give me 10 angles for me to write as ads, make sure it’s in Thai” | Add assumptions, numbers, constraints, and the decision you are trying to make. |

### Computer/browser control

**What this category teaches:**
Use computer control for web apps and dashboards, but require verification and never rely on screenshots alone.

| Real prompt pattern | How students can adapt it |
|---|---|
| “[Note: model was just switched from gpt-5.5 to minimax/minimax-m3 via OpenRouter. Adjust your self-identification accordingly.] /  / Awesome based on my data when will I hit 100k subs on my YouTube?” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Use the built-in browser and just go and check it for me” | Replace private source names with your own file, dashboard, customer, or business process. |
| “alright now. switch the model to sonnet 4.6 using openrouter and make sure you proof read everything and make sure that the thai language is written correctly” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Check the .openclaw docs before I have it saved somewhere for sure” | Replace private source names with your own file, dashboard, customer, or business process. |
| “[Note: model was just switched from gpt-5.5 to moonshotai/kimi-k2.6 via OpenRouter. Adjust your self-identification accordingly.] /  / hey dude” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Tier 1 - if we move it would it affect my website?” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Use my built in comet browser” | Replace private source names with your own file, dashboard, customer, or business process. |
| “[System note: Your previous turn was interrupted before you could process the last tool result(s). The conversation history contains tool outputs you haven't responded to yet. Please finish processing those results an…” | Replace private source names with your own file, dashboard, customer, or business process. |
| “[System note: Your previous turn was interrupted before you could process the last tool result(s). The conversation history contains tool outputs you haven't responded to yet. Please finish processing those results an…” | Replace private source names with your own file, dashboard, customer, or business process. |
| “help me wire up GLM 5.2 into the model selector with our openrouter api key” | Replace private source names with your own file, dashboard, customer, or business process. |
| “save it into your memory and the URL as well. /  / now close he browser and see if u can pull up the correct data again” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Yep /  / Why don’t u use open my comet browser like operating like me?” | Replace private source names with your own file, dashboard, customer, or business process. |

### Content / teaching asset creation

**What this category teaches:**
Turn real work into reusable intellectual property: guides, decks, prompts, scripts, student resources.

| Real prompt pattern | How students can adapt it |
|---|---|
| “Return exactly: DEFAULT_POST_CLEANUP_OK” | Name the audience, output format, source material, and quality bar. |
| “where is the documents?” | Name the audience, output format, source material, and quality bar. |
| “Prepare deck for tomorrow class /  / Pack for my Singapore trip” | Name the audience, output format, source material, and quality bar. |
| “[Replying to: "You're all set for tomorrow. Quick recap of what's locked in: /  / Today (before you sleep) / - ⚠️ Reserve Disney Cruise activities — deadline is today → disneycruise.disney.go.com, Reservation #4420521…” | Name the audience, output format, source material, and quality bar. |
| “Open this slide up on my computer and make a copy, then translate all the text that is in Thai to English” | Name the audience, output format, source material, and quality bar. |
| “Make a copy then translate to English” | Name the audience, output format, source material, and quality bar. |
| “https://postviral.ai/?[query-redacted]” | Name the audience, output format, source material, and quality bar. |
| “Anything we can use from this post?” | Name the audience, output format, source material, and quality bar. |
| “https://x.com/zaimiri/article/[phone] go to this article and read it and then help me buidl a teaching deck off of it” | Name the audience, output format, source material, and quality bar. |
| “now use the xai oauth and fetch the post. to see if u got it” | Name the audience, output format, source material, and quality bar. |
| “Extract this guide” | Name the audience, output format, source material, and quality bar. |
| “Love the carousel post /  / Need to generate the graphics  /  / With gpt image 2” | Name the audience, output format, source material, and quality bar. |
| “The text is switched /  / It should be /  / วิธีการสร้าง Brand ที่ AI copy ไม่ได้  /  / อีก 6 เดือนข้างหน้า / Content AI จะหน้าตาเหมือนกันหมด /  / คำถามคือ / แบรนด์ของคุณเหลืออะไร” | Name the audience, output format, source material, and quality bar. |
| “Use this file and create a full teaching deck with gamma” | Name the audience, output format, source material, and quality bar. |
| “https://www.instagram.com/p/DK9aLWYTnTl/?[query-redacted] /  / Hey dude go capture all the images here these are my carousels  /  / Then help me create new ones” | Name the audience, output format, source material, and quality bar. |
| “[The user sent a voice message~ Here's what they said: "Try and render the posts inside an HTML file and say, let's see if it looks better."]” | Name the audience, output format, source material, and quality bar. |
| “can you change slides 4 - 8 to align with the same header as the rest of thes lides” | Name the audience, output format, source material, and quality bar. |

### Creative media generation

**What this category teaches:**
Use the system for asset production pipelines: brief → generate → QA → revise → package.

| Real prompt pattern | How students can adapt it |
|---|---|
| “Return exactly: IMAGE_GEN_SESSION_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “what is this api error? /  / [Image attached at: /private/var/folders/r6/m24kg71s4xz49nkyr0zy49j40000gn/T/TemporaryItems/NSIRD_screencaptureui_y5Uh3w/Screenshot [phone] at 09.28.25.png] / [screenshot]” | Replace private source names with your own file, dashboard, customer, or business process. |
| “test to see if we can use the gemini cli to generate images with nano banana” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Extract the learning from this video” | Replace private source names with your own file, dashboard, customer, or business process. |
| “how can i give you access to my photos?” | Replace private source names with your own file, dashboard, customer, or business process. |
| “i want to give u access to my photos so u can help me extract my photos” | Replace private source names with your own file, dashboard, customer, or business process. |
| “open the folder with the videos” | Replace private source names with your own file, dashboard, customer, or business process. |
| “wait why did you choose these weird videos?” | Replace private source names with your own file, dashboard, customer, or business process. |
| “resend the video. i don't see it here” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Send me the images here” | Replace private source names with your own file, dashboard, customer, or business process. |

### General commands / iteration

**What this category teaches:**
Short steering prompts are valuable after the agent has enough context; they are not enough at kickoff.

| Real prompt pattern | How students can adapt it |
|---|---|
| “Reply with exactly: gpt55-ok” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Reply with exactly: default-now-gpt55” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: GPT55_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: DEFAULT_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: OK_minimax_minimax_m2_7. Then add 5 words describing your best use case.” | Replace private source names with your own file, dashboard, customer, or business process. |
| “In 2 sentences, describe your best use case for a founder-level AI ops team. Then return: TAG_anthropic_claude_sonnet_4_6” | Replace private source names with your own file, dashboard, customer, or business process. |
| “In 2 sentences, describe your best use case for a founder-level AI ops team. Then return: TAG_google_gemini_3_1_pro_preview” | Replace private source names with your own file, dashboard, customer, or business process. |
| “In 2 sentences, describe your best use case for a founder-level AI ops team. Then return: TAG_x_ai_grok_4_20” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: DEFAULT_SMOKE_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: SONNET_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: GROK_API_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: GPT55_DEFAULT_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: XAI_API_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “You just executed tool calls but returned an empty response. Please process the tool results above and continue with the task.” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: GROK_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Return exactly: GROK_OAUTH_OK” | Replace private source names with your own file, dashboard, customer, or business process. |
| “ok what about the discord? it just seemd to turn off” | Replace private source names with your own file, dashboard, customer, or business process. |
| “what is the problem?” | Replace private source names with your own file, dashboard, customer, or business process. |

### Operate / fix my Hermes system

**What this category teaches:**
Treat Hermes like business infrastructure: configure it, test it, assign ownership, monitor it, and fix the weak links.

| Real prompt pattern | How students can adapt it |
|---|---|
| “hey kelly u there?” | Add the system component, expected behavior, current failure, and proof required. |
| “is this instance different from the one on Telegram?” | Add the system component, expected behavior, current failure, and proof required. |
| “Find 3-4 fresh market/business signals from the last 7 days relevant to founders: pricing shifts, distribution changes, adoption patterns, infrastructure changes, or strategic moves that signal where AI business lever…” | Add the system component, expected behavior, current failure, and proof required. |
| “Find 3-4 fresh AI/company signals from the last 7 days that matter to founders/operators, especially agentic AI, voice workflows, automation, and business leverage. Focus on product/company announcements from major AI…” | Add the system component, expected behavior, current failure, and proof required. |
| “Find 3-4 fresh workflow or operator-level signals from the last 7 days: case studies, demos, creator/operator experiments, or examples of AI replacing/augmenting workflows (sales, support, marketing, research, product…” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: HERMES_OLLAMA_OK” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: HERMES_UPDATE_OK” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: HERMES_V013_OK” | Add the system component, expected behavior, current failure, and proof required. |
| “You've reached the maximum number of tool-calling iterations allowed. Please provide a final response summarizing what you've found and accomplished so far, without calling any more tools.” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: NOUS_OK_qwen_qwen3_6_plus” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: NOUS_OK_qwen_qwen3_6_max_preview” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: NOUS_OK_qwen_qwen3_6_35b_a3b” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: NOUS_OK_nousresearch_hermes_4_405b” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: HERMES_CUSTOM_NOUS_QWEN36PLUS_OK” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: OK_qwen_qwen3_6_plus. Then add 5 words describing your best use case.” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: OK_qwen_qwen3_6_max_preview. Then add 5 words describing your best use case.” | Add the system component, expected behavior, current failure, and proof required. |
| “Return exactly: OK_nousresearch_hermes_4_405b. Then add 5 words describing your best use case.” | Add the system component, expected behavior, current failure, and proof required. |
| “In 2 sentences, describe your best use case for a founder-level AI ops team. Then return: TAG_nousresearch_hermes_4_405b” | Add the system component, expected behavior, current failure, and proof required. |

### Personal productivity / ops

**What this category teaches:**
Let Hermes handle admin workflows across calendar, email, Drive, Notion, transcripts, and daily coordination.

| Real prompt pattern | How students can adapt it |
|---|---|
| “[Your active task list was preserved across context compression] / - [>] 1. Identify high-priority new emails from the API response (in_progress)” | Replace private source names with your own file, dashboard, customer, or business process. |
| “can you check my apple notes on what was written in the past 48 hours” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Check my calendar should all be in there and yes, give me the full prep” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Give me the link to this email” | Replace private source names with your own file, dashboard, customer, or business process. |
| “give me the email link about the training in Singapore” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Remind me to reply back to Khun Na from Odoo about the rate cars” | Replace private source names with your own file, dashboard, customer, or business process. |
| “Save these learnings into a notion” | Replace private source names with your own file, dashboard, customer, or business process. |
| “now we need to connect to the jeditrinupab.com / [email]” | Replace private source names with your own file, dashboard, customer, or business process. |
| “are u back? / I thought we just verified the Gmail again / Is it not working again?” | Replace private source names with your own file, dashboard, customer, or business process. |

### Research / find / monitor

**What this category teaches:**
Use agents as always-on analysts: search current sources, cite evidence, summarize signal, and keep watchlists fresh.

| Real prompt pattern | How students can adapt it |
|---|---|
| “You have access to web search. Search for: latest AI news May 11 2026 OR May 12 2026. Return only news items you can VERIFY with a source link. For each result, include: 1) exact headline, 2) publication date, 3) sour…” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “[Your active task list was preserved across context compression] / - [>] 2. Fetch unread Gmail messages (in_progress) / - [ ] 3. Filter for important items (pending) / - [ ] 4. Compare against seen_ids and report (pen…” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “https://x.com/zodchiii/status/[phone]/video/1?[query-redacted] /  / Find me the full video” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “[Your active task list was preserved across context compression] / - [>] fix_safe. Apply safe delivery fixes if clearly wrong, then verify one or more jobs (in_progress) / - [ ] report. Write daily note and summarize …” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “Where’s the pocket brief?” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “theres a new model Minimax M3 / i want to try it” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “yep lets try out building out a landing page and maybe some browser automation like navigating to my twitter and browsing what trump has said in the last 24 hours” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “open the html file for me go through my AI OS folder inside my icloud to see if u can pick up something big to work on so we can test out minimax m3 properly” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “เจได จิรัฏฐ์ ตรินุพับ /  / เจได ไตรนุภาพ จิระไตรธาร fix this\” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “Fix the navigation for the pages” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “You are auditing the navigation routing on a single-page book website at https://ai-native-book-beta-one.vercel.app” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “What would a 10x from now look like😍” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “[System note: Your previous turn was interrupted before you could process the last tool result(s). The conversation history contains tool outputs you haven't responded to yet. Please finish processing those results an…” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “I'm thinking of getting the dgx spark to add into our system” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “Find out the group of customers who are coming today” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “go and find out which one will give me instand response like in the demo” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “https://x.com/vicky_grok/status/[phone]?[query-redacted] /  / find me the real video of this” | Add timeframe, source priority, citation requirement, and decision you need to make. |
| “Find me the demo viral from fable” | Add timeframe, source priority, citation requirement, and decision you need to make. |

## Student-ready master templates

### Operational diagnostic
```text
Audit `[system/process]`. Check the real source first: `[dashboard/file/account/log]`. Tell me what is working, what is broken, who/what owns it, the failure modes, and the next 3 fixes. Verify with actual output or citations.
```

### Build and verify
```text
Build `[artifact]` for `[audience/use case]`. Use `[source materials]`. Save it to `[destination]`. Run/preview/test it, fix issues, then send me the final file/URL plus the verification result.
```

### Research brief
```text
Research `[topic/company/market]` from current sources. Prioritize `[source types]`. Give me the 5 highest-signal findings, cite each source, explain why it matters for `[business decision]`, and flag uncertainty.
```

### Teaching asset
```text
Turn `[source/workflow/transcript]` into a student-facing guide. Make it practical for business owners, include examples, prompt templates, common mistakes, and a 7-day implementation plan.
```

### Revenue/ops monitor
```text
Set up or inspect a monitor for `[metric]` from `[source of truth]`. It should run `[cadence]`, alert only on `[threshold/condition]`, and include owner, log location, and recovery steps.
```

### Creative production
```text
Create `[asset type]` for `[brand/audience]` using `[style constraints]`. Produce drafts, QA them against mobile readability/brand fit, revise the weakest parts, and package final exports.
```

### Strategy model
```text
Model `[decision]` with assumptions, scenarios, upside/downside, bottlenecks, and a recommendation. Show the math in simple terms and state what would change your mind.
```

### Memory/handoff
```text
After you finish, write a concise handoff: decision, files changed, verification, blocker, next owner. Save only durable facts; do not store secrets.
```

## Common mistakes students should avoid

- Asking for advice when they need an artifact.
- Giving a vague goal without the source of truth.
- Accepting “it should work” instead of requiring a run/test/preview.
- Letting the agent create duplicates before checking existing systems.
- Putting secrets directly in prompts instead of referencing credential paths or approved secret stores.
- Treating the agent as one chat instead of a managed team with roles, memory, and handoffs.
- Over-alerting themselves instead of defining thresholds and escalation rules.
- Failing to package successful workflows into reusable student/team templates.

## Appendix A — category counts

```json
{
  "category_counts": {
    "Operate / fix my Hermes system": 3009,
    "General commands / iteration": 229,
    "Research / find / monitor": 51,
    "Build / code / deploy": 27,
    "Personal productivity / ops": 9,
    "Creative media generation": 10,
    "Content / teaching asset creation": 35,
    "Computer/browser control": 13,
    "Business / strategy / revenue": 13
  },
  "type_counts": {
    "Question / diagnosis": 761,
    "Iteration / refinement": 1965,
    "Action prompt": 34,
    "Directive / context": 632,
    "Creation prompt": 4
  },
  "source_counts": {
    "cli": 153,
    "cron": 2803,
    "telegram": 455,
    "subagent": 1,
    "tui": 6
  }
}
```

## Appendix B — raw prompt appendix

A full sanitized CSV appendix was generated alongside this guide: `kelly-prompts-raw-sanitized-2026-06-23.csv`. It contains every active user message from the local Kelly/default Hermes session database with date, session, category, type, and sanitized prompt text.