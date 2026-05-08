

---

## 2026-05-08 01:54:52 +07 — X High-Alert: OpenAI realtime voice models move from demo layer to production voice-agent API

### Collection path
- Preferred logged-in X/CDP unavailable: `http://127.0.0.1:18800/json` returned `ConnectionRefusedError(61, 'Connection refused')`.
- Fallback used curated Nitter RSS feeds; collected 124 recent posts from official/lab/founder/operator accounts.
- Selected cluster because it was official, fresh, API-available, and directly relevant to founder/operator voice-agent workflows.

### Actual X/Nitter post text captured
- `@OpenAI` — https://nitter.net/OpenAI/status/2052438194625593804#m
  > Introducing GPT-Realtime-2 in the API: our most intelligent voice model yet, bringing GPT-5-class reasoning to voice agents. Voice agents are now real-time collaborators that can listen, reason, and solve complex problems as conversations unfold. Now available in the API alongside streaming models GPT-Realtime-Translate and GPT-Realtime-Whisper — a new set of audio capabilities for the next generation of voice interfaces.

- `@OpenAI` — https://nitter.net/OpenAI/status/2052438196454379986#m
  > Our new voice models are now available in the Realtime API: GPT-Realtime-2: Build production-ready voice agents that can think harder, take action, handle interruptions, and keep conversations flowing. GPT-Realtime-Translate: Translate while streaming across more than 70 input and 13 output languages, breaking down language barriers and helping people communicate more naturally. GPT-Realtime-Whisper: Transcribe streaming audio as words are spoken to generate captions and notes in real time. https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/

- `@OpenAIDevs` — https://nitter.net/OpenAIDevs/status/2052440907933474954#m
  > Voice agents are getting more capable. Here’s what’s new: GPT-Realtime-2 for voice agents that reason and take action; GPT-Realtime-Translate enabling translation from 70 input languages into 13 output languages; GPT-Realtime-Whisper, making transcription even faster.

- Ecosystem confirmations captured in the same cluster:
  - `@Vimeo` RT by `@OpenAIDevs` — real-time live-event dubbing with GPT-Realtime-Translate: https://nitter.net/Vimeo/status/2052442588201029684#m
  - `@glean` RT by `@OpenAIDevs` — Glean real-time voice capability powered by GPT-Realtime-2; claimed 42.9% relative helpfulness increase in internal evals: https://nitter.net/glean/status/2052440702169108990#m
  - `@ScaleAILabs` RT by `@OpenAIDevs` — GPT-Realtime-2 top on Audio MultiChallenge S2S with instruction retention rising from 36.7% to 70.8% APR: https://nitter.net/ScaleAILabs/status/2052451341071683732#m

### Verification sources
- OpenAI official RSS verified article title/date/description:
  - `Advancing voice intelligence with new models in the API`, Thu, 07 May 2026 10:00:00 GMT
  - https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api
  - RSS description: “Explore new realtime voice models in the OpenAI API that can reason, translate, and transcribe speech, enabling more natural and intelligent voice experiences.”
- Direct OpenAI page fetch returned HTTP 403 in this environment, so detailed implementation wording was verified through Microsoft/Azure AI Foundry’s official page:
  - https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/a-new-chapter-for-realtime-ai-reasoning-translation-and-real-time-transcription/4517124
  - Verified: `GPT-realtime-translate`, `GPT-realtime-2`, and `GPT-realtime-whisper` rolling into Microsoft Foundry; translation without segmented/buffered pipeline processing; low-latency original-audio transcription; GPT-realtime-2 internal reasoning, expanded context window, and adjustable `{reasoning.effort}`.

### What changed
- OpenAI’s realtime audio stack now includes a reasoning voice model (`GPT-Realtime-2`), live streaming translation (`GPT-Realtime-Translate`), and faster realtime transcription (`GPT-Realtime-Whisper`) in the API.
- This shifts voice AI from “speech interface around a chatbot” toward live audio agents that can listen, reason, translate, transcribe, take action, and keep conversation context flowing in one realtime pipeline.

### Why it matters
- **Founders/operators:** support, sales, onboarding, training, and internal helpdesk workflows can now be designed as continuous voice loops rather than IVR/chatbot handoffs.
- **Educators/Limitless Club:** strong teaching angle for Thai business owners: voice agents become practical when they can reason and translate during the call, not after it.
- **Builders:** evaluate latency, cost, transcript retention, handoff/approval, and audit logs now; voice-agent products will need production ops discipline, not just better prompts.

### Who should care
- Call-center/contact-center builders, B2B SaaS onboarding teams, language-localization services, enterprise knowledge assistants, live event/video platforms, and Thai SMEs serving multilingual customers.

### Recommended action / Jedi angle
- Run a small demo benchmark this week: Thai/English customer-support call → live translation + transcript + reasoning agent summary + action draft.
- Content angle: “The next AI employee may not type — it listens, translates, reasons, and writes the follow-up while the conversation is still happening.”

### De-dupe note
- A same-night recall/search session already investigated this model cluster; this X high-alert note keeps the actual official X post text and direct status links in the X High-Alert archive because the current scan independently surfaced the official OpenAI/OpenAIDevs posts as the top cluster.


---

## X High-Alert: OpenAI ships Codex Chrome extension for signed-in browser work

**Run time:** 2026-05-08 04:11:48 +07  
**Collector:** Curated Nitter RSS fallback; OpenClaw Chrome CDP unavailable (`127.0.0.1:18800` connection refused)  
**Cluster:** Agentic browser work / coding-agent-to-business-ops expansion / browser permissions and governance

### Actual X post text captured

**@OpenAI** — Thu, 07 May 2026 20:08:50 GMT  
Nitter: https://nitter.net/OpenAI/status/2052480800004956323#m  
X: https://x.com/OpenAI/status/2052480800004956323

> Codex now works directly in Chrome on macOS and Windows.
>
> It’s even better at working with apps and sites in Chrome, and now works in parallel across tabs in the background without taking over your browser.
>
> To get started, install the Chrome plugin in the Codex app.

**@OpenAIDevs** — Thu, 07 May 2026 20:10:10 GMT  
Nitter: https://nitter.net/OpenAIDevs/status/2052481136971125158#m  
X: https://x.com/OpenAIDevs/status/2052481136971125158

> Codex can now take on more of your browser dev work. With the new Chrome plugin in the Codex app, it can test web apps, gather context across tabs, use web DevTools efficiently in parallel, and keep results organized without taking over your browser.

**@OpenAI thread details captured** — Thu, 07 May 2026 20:08:50–20:08:51 GMT  
Nitter: https://nitter.net/OpenAI/status/2052480801435189708#m  
Nitter: https://nitter.net/OpenAI/status/2052480803318468770#m  
Nitter: https://nitter.net/OpenAI/status/2052480804971028879#m

> With the new Chrome extension, Codex can quickly move through repetitive browser work, like navigating structured pages and complex data entry flows.
>
> Under the hood, it writes and runs code to navigate and complete tasks.
>
> If a task needs multiple tools, Codex chooses the best one for each step.
>
> It uses plugins when they can handle the job, Chrome when it needs a logged-in website, and combines approaches as needed.
>
> The Chrome extension expands what Codex can do for coding and work.
>
> From debugging browser flows to checking dashboards, conducting research, or updating CRMs, Codex can take on more of the tasks that already happen in your browser.
>
> Available today in the Codex app in all regions except EU and UK, with support coming soon.

**@sama** — Thu, 07 May 2026 20:25:44 GMT  
Nitter: https://nitter.net/sama/status/2052485051812909530#m  
X: https://x.com/sama/status/2052485051812909530

> way cooler to help software developers pokemon-evolve into superheroes than to try to replace them
>
> it is insane what one really good person can do now

### Verification beyond X

Official OpenAI Developers docs page fetched successfully:
https://developers.openai.com/codex/app/chrome-extension

Key verified doc details:
- The **Codex Chrome extension** lets Codex use Chrome for browser tasks that need signed-in browser state.
- OpenAI examples include LinkedIn, Salesforce, Gmail, and internal tools.
- Codex can switch between plugins, Chrome for logged-in context, and the in-app browser for localhost or public pages.
- Setup path: open Codex → Plugins → add Chrome plugin → install/connect Chrome extension → approve Chrome permission prompts → confirm extension shows **Connected**.
- Codex can be invoked with prompts like `@Chrome open Salesforce and update the account from these call notes`.
- Chrome browser tasks run in Chrome tab groups so thread work stays grouped.
- Default posture: Codex asks before interacting with each new website; users can allow current chat, always allow host, or decline.
- Security-relevant permissions include page debugger, read/change website data, browsing history on signed-in devices, notifications, bookmarks, downloads, native app communication, and tab groups.
- OpenAI says it does not store a separate complete record of Chrome actions; browser activity is stored only when included in Codex context such as page text, screenshots, tool calls, summaries, messages, or thread content.

Official OpenAI changelog also includes a May 7 entry: `Codex for Chrome`, stating that the extension works in parallel across tabs in the background and that users control which websites Codex can use.
https://developers.openai.com/codex/changelog

### What changed

OpenAI moved Codex from code/workspace automation toward **logged-in browser automation**: dashboards, CRMs, SaaS admin screens, web app testing, research, data entry, and multi-tab browser work can now be delegated from the Codex app through Chrome with website approvals.

### Why it matters

- This is a practical bridge from “coding agent” to “business operations agent.” Many founder workflows live inside authenticated SaaS tabs, not APIs.
- It lowers the barrier for non-technical operators to automate CRM updates, dashboard checks, QA flows, research, and internal web tooling without building integrations first.
- It also raises governance issues: browser history, page data, extension permissions, domain allowlists/blocklists, and human approval now become part of the operating model.

### Who should care

- Founders and operators using CRM, dashboards, admin panels, analytics tools, and internal web apps.
- Product and engineering teams testing authenticated web apps or reproducing browser-only bugs.
- Limitless Club educators teaching practical AI delegation and SOP automation.

### Recommended action / Jedi angle

Run a short internal experiment: choose one repetitive browser SOP, e.g. `check dashboard → update CRM → summarize exceptions`, then map it into a safe Codex Chrome workflow with strict allowlists, no sensitive secrets, and a human approval checkpoint. Content angle: **“AI agents just entered your logged-in browser. The skill is no longer prompting — it’s designing safe browser SOPs.”**

### Sources

- OpenAI X: https://x.com/OpenAI/status/2052480800004956323
- OpenAI Devs X: https://x.com/OpenAIDevs/status/2052481136971125158
- OpenAI Developers docs: https://developers.openai.com/codex/app/chrome-extension
- OpenAI Developers changelog: https://developers.openai.com/codex/changelog

---

## 2026-05-08 06:28:22 +0700 - X High-Alert Scan: browser and office agents moved into daily work surfaces

### Cluster
Browser and productivity-suite agents are moving from chat/sidebar helpers into authenticated work surfaces: Chrome tabs, Microsoft 365 apps, local Mac apps/files, and parallel coding-agent workflows.

### Actual post text captured from X/Nitter

**OpenAI / Codex for Chrome**
- Source post: https://x.com/OpenAI/status/2052480800004956323#m
- Captured text: "Codex now works directly in Chrome on macOS and Windows. It is even better at working with apps and sites in Chrome, and now works in parallel across tabs in the background without taking over your browser. To get started, install the Chrome plugin in the Codex app."
- Thread detail: https://x.com/OpenAI/status/2052480804971028879#m
- Captured text: "The Chrome extension expands what Codex can do for coding and work. From debugging browser flows to checking dashboards, conducting research, or updating CRMs, Codex can take on more of the tasks that already happen in your browser. Available today in the Codex app in all regions except EU and UK, with support coming soon."
- OpenAI Devs post: https://x.com/OpenAIDevs/status/2052481136971125158#m
- Captured text: "Codex can now take on more of your browser dev work. With the new Chrome plugin in the Codex app, it can test web apps, gather context across tabs, use web DevTools efficiently in parallel, and keep results organized without taking over your browser."

**Anthropic / Claude for Microsoft 365**
- Source post: https://x.com/claudeai/status/2052445786651168849#m
- Captured text: "Claude for Excel, PowerPoint, and Word are now generally available, and Claude for Outlook is in public beta. As Claude moves between your Microsoft apps, it carries the full context of your conversation."
- Availability post: https://x.com/claudeai/status/2052445787930468704#m
- Captured text: "Available on all paid plans. Give it a try: http://claude.com/claude-for-microsoft-365"

**Cursor / parallel agent execution**
- Source post: https://x.com/cursor_ai/status/2052489388895195399#m
- Captured text: "Cursor can now split plans up into parallel subtasks by multitasking. Click Build in Parallel to have it identify independent tasks and run them simultaneously using async subagents."
- Source post: https://x.com/cursor_ai/status/2052489390379925721#m
- Captured text: "When multitasking, Cursor can now break up your diffs into smaller, more mergeable PRs with the Create PRs quick action. It will identify logical slices and propose a split plan for your approval."

**Perplexity / Personal Computer**
- Source post: https://x.com/perplexity_ai/status/2052445405754040816#m
- Captured text: "Personal Computer is now available to all users in a new Perplexity Mac app. Personal Computer is an advanced version of Perplexity Computer. It operates on any Mac, running tasks across your local files, native Mac apps, the web, and Perplexity secure servers."
- Thread detail: https://x.com/perplexity_ai/status/2052445424640983301#m
- Captured text: "Personal Computer in the Mac app allows Perplexity Computer to run continuously, autonomously, and locally. Paired with the Comet browser, it operates web-based tools without direct connectors. Local or remote, it takes agentic operations anywhere they are needed."

### Official verification
- OpenAI Codex Chrome docs: https://developers.openai.com/codex/app/chrome-extension
  - Verified: Codex Chrome extension lets Codex use Chrome for tasks needing signed-in browser state, including LinkedIn, Salesforce, Gmail, and internal tools. Docs describe website approval prompts, domain allowlist/blocklist, elevated risk for always-allow browser content, and browser-history/page-data risks.
- OpenAI Codex changelog: https://developers.openai.com/codex/changelog
  - Verified 2026-05-07 entry: Codex for Chrome; new extension works in parallel across browser tabs in the background and users control which websites Codex can use.
- Anthropic Claude for Microsoft 365 page: https://claude.com/claude-for-microsoft-365
  - Verified: Claude works inside Excel, PowerPoint, Word, and Outlook; page describes Excel cell/model help, PowerPoint slide/chart/diagram generation, Word tracked-changes editing, and Outlook email/thread handling.
- Cursor changelog: https://cursor.com/changelog/05-07-26
  - Verified: Cursor 3 adds PR review, Build in Parallel from plans using async subagents, Split changes into PRs with backup snapshot and approval plan, and pinned skills as quick actions.
- Perplexity official product page fetch hit a JS/cookie challenge in this environment, so Perplexity details are from the official @perplexity_ai X post text only.

### What changed
- Agents are gaining direct operating access to authenticated work surfaces: browser tabs, M365 documents/email, local Mac files/apps, and coding-agent PR workflows.
- Product language has shifted from assistant answers to agents performing structured work where business already happens.

### Why it matters
- For founders/operators: CRM updates, dashboard checks, document creation, web-app QA, sales/admin workflows, and PR work can be delegated in-place, but only if approval, permissions, and audit loops are designed first.
- For educators/Limitless Club: this is a curriculum shift from prompt libraries to workflow design: trigger -> context -> tool surface -> action -> review -> audit.

### Who should care
- Non-technical business owners using Microsoft, CRM, and browser-heavy workflows.
- Operators building SOPs around finance, sales, reporting, support, or documents.
- Dev/product teams adopting coding agents and browser QA.

### Recommended Jet angle
Teach a safe agent in your work apps framework: choose one repetitive browser/M365 task, define allowed websites/files/apps, set human approval checkpoints, run the agent in parallel, and audit the output before the business process changes. Emphasize permissions and review gates over prompt hacks.

### Source links
- https://x.com/OpenAI/status/2052480800004956323#m
- https://x.com/OpenAI/status/2052480804971028879#m
- https://x.com/OpenAIDevs/status/2052481136971125158#m
- https://developers.openai.com/codex/app/chrome-extension
- https://developers.openai.com/codex/changelog
- https://x.com/claudeai/status/2052445786651168849#m
- https://x.com/claudeai/status/2052445787930468704#m
- https://claude.com/claude-for-microsoft-365
- https://x.com/cursor_ai/status/2052489388895195399#m
- https://x.com/cursor_ai/status/2052489390379925721#m
- https://cursor.com/changelog/05-07-26
- https://x.com/perplexity_ai/status/2052445405754040816#m
- https://x.com/perplexity_ai/status/2052445424640983301#m


---

## X High-Alert Scan: Agents moved into real work surfaces

**Run time:** 2026-05-08 08:46:33 UTC+07:00+0700  
**Collector:** Nitter RSS fallback. OpenClaw CDP was unavailable on `127.0.0.1:18800` (`connection refused`).  
**Decision:** Non-silent. This is a source-rich cluster, not a single rumor: OpenAI, Anthropic/Claude, Cursor, and Perplexity all posted or documented agents moving into authenticated browser, Office, local Mac, and parallel coding workflows.

### Cluster

Agents are shifting from chat sidebars into where work already happens:

- signed-in Chrome tabs and SaaS sites
- Microsoft Excel, PowerPoint, Word, and Outlook
- local Mac files/apps plus browser workflows
- parallel coding-agent subtasks and split PRs

### Actual X post text captured

**OpenAI - Codex in Chrome**  
Status: https://x.com/OpenAI/status/2052480800004956323#m

> Codex now works directly in Chrome on macOS and Windows. It's even better at working with apps and sites in Chrome, and now works in parallel across tabs in the background without taking over your browser. To get started, install the Chrome plugin in the Codex app.

Thread details captured:

- https://x.com/OpenAI/status/2052480801435189708#m
  > With the new Chrome extension, Codex can quickly move through repetitive browser work, like navigating structured pages and complex data entry flows. Under the hood, it writes and runs code to navigate and complete tasks.
- https://x.com/OpenAI/status/2052480803318468770#m
  > If a task needs multiple tools, Codex chooses the best one for each step. It uses plugins when they can handle the job, Chrome when it needs a logged-in website, and combines approaches as needed.
- https://x.com/OpenAI/status/2052480804971028879#m
  > The Chrome extension expands what Codex can do for coding and work. From debugging browser flows to checking dashboards, conducting research, or updating CRMs, Codex can take on more of the tasks that already happen in your browser. Available today in the Codex app in all regions except EU and UK, with support coming soon.

Official verification:

- OpenAI Codex Chrome extension docs: https://developers.openai.com/codex/app/chrome-extension
- OpenAI Codex changelog: https://developers.openai.com/codex/changelog
- Extracted official facts: docs say the extension lets Codex use Chrome for browser tasks that need signed-in browser state, including LinkedIn, Salesforce, Gmail, and internal tools. Changelog lists `2026-05-07 Codex for Chrome` and says it works in parallel across tabs in the background while the user controls which websites Codex can use.

**Claude - Microsoft 365 work surface**  
Status: https://x.com/claudeai/status/2052445786651168849#m

> Claude for Excel, PowerPoint, and Word are now generally available, and Claude for Outlook is in public beta. As Claude moves between your Microsoft apps, it carries the full context of your conversation.

Availability post: https://x.com/claudeai/status/2052445787930468704#m

> Available on all paid plans. Give it a try: http://claude.com/claude-for-microsoft-365

Official verification:

- Claude for Microsoft 365 page: https://claude.com/claude-for-microsoft-365
- Extracted official facts: page says Claude works inside Excel, PowerPoint, Word, and Outlook; "Start in your inbox, end in the deck. It remembers everything in between." It includes install calls for Microsoft 365 and Outlook plus app-specific sections for Excel, PowerPoint, Word, and Outlook.

**Perplexity - Personal Computer for Mac**  
Status: https://x.com/perplexity_ai/status/2052445405754040816#m

> Personal Computer is now available to all users in a new Perplexity Mac app. Personal Computer is an advanced version of Perplexity Computer. It operates on any Mac, running tasks across your local files, native Mac apps, the web, and Perplexity's secure servers.

Thread details captured:

- https://x.com/perplexity_ai/status/2052445424640983301#m
  > Personal Computer in the Mac app allows Perplexity Computer to run continuously, autonomously, and locally. Paired with the Comet browser, it operates web-based tools without direct connectors. Local or remote, it takes agentic operations anywhere they're needed.
- https://x.com/perplexity_ai/status/2052445440390615458#m
  > Personal Computer is built for the Mac ecosystem, so you can manage it from anywhere. Start tasks from your iPhone with local files on your Mac. Add a Mac mini for full continuity and always-on agents. Manage agentic actions wherever you are.

Verification note: official Perplexity product page returned HTTP 403 in this environment, so details are cited as official X/Nitter-captured post text, not independently extracted product-page text.

**Cursor - parallel coding agents and split PRs**  
Status: https://x.com/cursor_ai/status/2052489388895195399#m

> Cursor can now split plans up into parallel subtasks by multitasking. Click "Build in Parallel" to have it identify independent tasks and run them simultaneously using async subagents.

Split-PR post: https://x.com/cursor_ai/status/2052489390379925721#m

> When multitasking, Cursor can now break up your diffs into smaller, more mergeable PRs with the "Create PRs" quick action. It will identify logical slices and propose a split plan for your approval.

Official verification:

- Cursor changelog: https://cursor.com/changelog/05-07-26
- Extracted official facts: changelog confirms Build in Parallel, async subagents, dependent-step ordering, split changes into PRs, backup snapshot, and proposed split plan for approval.

### What changed

- Codex is no longer limited to repo/app surfaces; it can operate in the user's signed-in Chrome context with permission controls.
- Claude has moved into Microsoft 365 work documents, with context moving across Office apps.
- Perplexity is pitching a Mac-native always-on computer-use agent that can work across local files/apps, web, and secure servers.
- Cursor is operationalizing coding-agent parallelism with async subagents and PR-splitting review gates.

### Why it matters for Jet / Limitless Club

- This is the practical operator shift: agents are becoming work-surface automation, not just chat answers.
- Non-technical business owners will need a new workflow checklist: allowed apps/sites, sensitive data boundaries, human approval, audit log, rollback, and spend/time caps.
- The teaching opportunity is bigger than prompting: show business owners how to convert one repetitive process into a governed agent workflow.

### Who should care

- Founders/operators with browser-heavy workflows: CRM updates, dashboards, data entry, web QA, research, admin ops.
- Educators and consultants teaching AI adoption to non-technical teams.
- Software teams using coding agents who need parallel execution without chaotic PRs.
- Any team with sensitive browser/Office data; the permission and audit model now matters as much as the prompt.

### Recommended action / angle

Build a Limitless mini-framework: **Safe Agent in Your Work Apps**.

1. Pick one repeated task in Chrome, Microsoft 365, or code review.
2. Define allowed sites/files/apps and forbidden data.
3. Give the agent a tiny task with a review checkpoint.
4. Require an output diff, audit trail, or before/after summary.
5. Scale only after the process has rollback and owner approval.

Suggested content angle: **"AI agents are leaving chat and entering your browser, Excel, and Mac. The winners will not have better prompts; they will have better permissions, process design, and review loops."**

### Primary links

- https://x.com/OpenAI/status/2052480800004956323#m
- https://developers.openai.com/codex/app/chrome-extension
- https://developers.openai.com/codex/changelog
- https://x.com/claudeai/status/2052445786651168849#m
- https://claude.com/claude-for-microsoft-365
- https://x.com/perplexity_ai/status/2052445405754040816#m
- https://x.com/cursor_ai/status/2052489388895195399#m
- https://cursor.com/changelog/05-07-26


---

## 2026-05-08 11:06:21 +0700 - X High-Alert Scan: Anthropic moves Petri alignment evals to independent governance

### Cluster
- Anthropic/open-source AI evaluation tooling and agent/model governance.
- Source X post: https://x.com/AnthropicAI/status/2052494460966019137
- Captured Nitter link: https://nitter.net/AnthropicAI/status/2052494460966019137#m
- Official source: https://www.anthropic.com/research/donating-open-source-petri

### Actual post text captured from X/Nitter
> We are donating Petri, our open-source alignment tool, to @meridianlabs_ai, so its development can continue independently.
>
> Working with Meridian Labs, we have also released a major update that improves the adaptability, realism, and depth of Petri's tests.
>
> https://www.anthropic.com/research/donating-open-source-petri

Adjacent same-feed post, lower alert priority:
- https://x.com/AnthropicAI/status/2052466175540629965
- Text captured: Our security bug bounty program is now public on HackerOne. We have run the program privately within the security research community, and their findings have strengthened our products. Now anyone can report vulnerabilities and get rewarded. Read more: http://hackerone.com/anthropic

### What changed
- Anthropic says Petri is an open-source toolbox of alignment tests for any large language model.
- Petri has been part of Anthropic's alignment assessment for every Claude model since Claude Sonnet 4.5.
- Anthropic says Petri tests concerning tendencies such as deception, sycophancy, and cooperation with harmful requests using an auditor model and judge model.
- Petri 3.0 adds:
  - Adaptability: auditor and target model split into separately tweakable components.
  - Realism: the Dish add-on can test with the model's real system prompt and real deployment scaffold.
  - Depth: integration with Bloom for deeper assessment of selected behaviors.
- Anthropic handed Petri development to Meridian Labs, an AI evaluation nonprofit, comparing the move to donating MCP to the Linux Foundation so results can be neutral and credible across labs, researchers, and governments.
- Anthropic says UK AISI used Petri as a major part of evaluating models for propensity to sabotage AI research.

### Why it matters
- This is an evaluation/governance signal, not a model-launch signal: frontier labs are separating safety/eval infrastructure from any one lab's product roadmap.
- For founders building agents, the important shift is that evals are moving closer to production reality: real system prompts, real scaffolds, and behavior-specific assessments.
- For regulated operators and educators, Petri is a concrete example of how to explain AI governance beyond policy language: define risky behaviors, simulate realistic tasks, score transcripts, then create review gates before deployment.

### Who should care
- AI product teams shipping autonomous agents or internal copilots.
- Security/compliance leaders who need model-behavior evidence, not just vendor assurances.
- Limitless Club operators teaching non-technical business owners how to adopt agents safely.

### Recommended Jet angle
- Teach a practical "agent behavior test before rollout" checklist:
  1. Pick 3 failure behaviors to test, such as deception, unsafe compliance, or hallucinated authority.
  2. Run the agent in a realistic workflow scaffold, not a toy prompt.
  3. Use a separate reviewer or judge model plus human spot checks.
  4. Require a pass/fail gate before giving the agent broader tool or customer access.

### Storage/status
- CDP X collection unavailable in this cron run; used curated Nitter RSS fallback.
- Official Anthropic article fetched and verified locally.


---

## Signal X High-Alert Scan — Google Cloud storage becomes agent-ready context infrastructure

**Run time:** 2026-05-08 13:20:04 UTC+07:00

### Cluster
- **GoogleCloudTech / Google Cloud Storage / MCP / enterprise data layer**

### Actual post text captured from curated X/Nitter RSS
> Storage innovations to accelerate your AI workloads: High-performance storage infrastructure, Smart Storage, and more!
>
> Unlock unstructured data with automated metadata annotation and AI agent connectivity via MCP -> https://goo.gle/49wXquT

**Direct status link:** https://x.com/GoogleCloudTech/status/2052508778616983813
**Nitter mirror:** https://nitter.net/GoogleCloudTech/status/2052508778616983813#m
**Official source:** https://cloud.google.com/blog/products/storage-data-transfer/next26-storage-announcements

### Official verification
Google Cloud's official blog article, **Storage innovations to accelerate your AI workloads at Next '26** dated **April 23, 2026**, verifies:
- Google Cloud is announcing storage innovations across performance, intelligence, and management so data is useful for AI models, apps, and agents.
- Storage is framed as the access layer that supplies context for AI agents during inference.
- **Smart Storage** is described as unlocking unstructured data with **automated metadata annotation** and **AI agent connectivity via MCP**.
- The same article lists Cloud Storage Rapid with **10x performance enhancements**, a Dynamic tier for Google Cloud Managed Lustre, and Storage Intelligence dashboards/activity/batch operations.

### What changed
- Google Cloud is explicitly moving agent-readiness down into the **storage/data layer**, not just the model or chatbot layer.
- The notable phrase is not only MCP support, but **automated metadata annotation + MCP connectivity** for unstructured data.

### Why it matters
- For founders/operators: many AI-agent projects fail because company files, media, docs, and logs are unstructured and missing trusted metadata. Google is positioning storage as the place where that context is created and exposed to agents.
- For educators/Limitless Club: this is a practical way to teach that "AI readiness" is not just prompting; it is organizing data so agents can safely find, understand, and use it.
- For technical teams: MCP-connected storage suggests future agent workflows where governed data access is a platform primitive, not a custom integration each time.

### Who should care
- SMB and enterprise operators with large document/media/file archives.
- AI builders designing internal agents or RAG systems.
- Limitless/Jedi learners who need a simple mental model for preparing business data before deploying agents.

### Recommended action / angle
- **Angle:** "Before you hire an AI agent, clean the agent's desk." Teach a 3-step data-readiness checklist: identify high-value unstructured data, add metadata/tags/owners, then expose only approved folders/tools to agents through governed connectors such as MCP.
- **Operator action:** pick one messy knowledge bucket such as customer FAQs, invoices, training videos, or SOP docs and define the metadata an agent would need: owner, date, customer/product, permission level, task type, and review requirement.

### Storage note
- This section was appended by the scheduled Signal X high-alert cron. Standard Notion backfill is attempted after this write; direct Notion fallback should patch the same dated X High-Alert Scan row if the backfill stalls.


---

## 2026-05-08 15:42:10 UTC+07:00 - X High-Alert Scan: Google Cloud Agents CLI turns coding agents into agent-platform builders

### Collection
- Preferred logged-in X/CDP was unavailable: `http://127.0.0.1:18800/json` connection refused.
- Fallback used curated Nitter RSS/X sources. Candidate set: 88 recent posts from official/lab/builder accounts.

### Actual post text captured
- Account: `@GoogleCloudTech`
- Direct status: https://x.com/GoogleCloudTech/status/2052463476702933171
- Nitter mirror: https://nitter.net/GoogleCloudTech/status/2052463476702933171#m
- Captured text: "Take your tech to the terminal. @Saboo_Shubham_ breaks down the new Agents CLI--the specialized tool that gives your AI coding agent a direct line to build, evaluate, and deploy on Google Cloud -> https://goo.gle/4n88i86"

### Official verification
- Shortlink `https://goo.gle/4n88i86` resolves to Google Cloud YouTube video: https://www.youtube.com/watch?v=X-5C_LZK_Js
- Video title: `A closer look at Agents CLI`
- Official channel: Google Cloud
- Video description says Agents CLI, ADK, and Skills are developer tools to move AI agents from "cool demos" to "production-ready powerhouses".
- Description says Agent CLI and Agent Platform are the entry point for the agent lifecycle and use integrated context to scaffold, build, and deploy agents across Gemini Enterprise.
- Description says Skills give agents modular capabilities they can execute at runtime, and ADK graph-based workflows add deterministic routing/task execution for regulated industries.
- Description also lists long-running agents up to 7 days, pause/resume for human approvals or network drops, and Agent Garden templates/patterns.
- GitHub repo verified: https://github.com/google/agents-cli
  - Repo description: "The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud."
  - README says Agents CLI works with Gemini CLI, Claude Code, Codex, Antigravity, and other coding agents.
  - Install command: `uvx google-agents-cli setup`
  - Skills-only install: `npx skills add google/agents-cli`
  - README lists skills for workflow, ADK code, scaffolding, evals, deployment, publishing, and observability.
  - GitHub API check during this run: created 2026-04-08, pushed 2026-05-06, updated 2026-05-08, 2,130 stars.

### Cluster
- Agent-platform builder tooling: Google is not just shipping a console product; it is giving existing coding agents a CLI/skills layer for creating, evaluating, deploying, observing, and publishing enterprise agents.
- Cross-agent adoption: explicit support for Gemini CLI, Claude Code, Codex, and Antigravity makes this a tool-agnostic bridge into Google Cloud/Gemini Enterprise.
- Productionization primitives: eval skills, deployment skills, observability, pause/resume, long-running state, and graph workflows are the real signal; not another chat UI.

### What changed
Google Cloud re-amplified Agents CLI as a terminal-first workflow where coding agents can scaffold, evaluate, deploy, and observe agents on Google Cloud/Gemini Enterprise using CLI commands and reusable skills.

### Why it matters
For operators/builders, this is another sign that the winning agent stack is becoming: coding agent + skills/playbooks + cloud runtime + evals + observability + human approvals. Google is packaging that into a workflow usable from Claude Code/Codex/Gemini CLI rather than forcing teams into one assistant UI.

### Who should care
- Technical founders building internal agents on Google Cloud.
- Operators comparing agent-platform stacks: AWS AgentCore, OpenAI Agents SDK/Codex, Anthropic Managed Agents, Google Gemini Enterprise/Agents CLI.
- Limitless Club educators explaining why "AI agents" require runtime, eval, deployment, and governance skills beyond prompting.

### Recommended action / Jedi angle
Angle: "Stop teaching agents as prompts. Teach the agent production checklist: scaffold -> tools/skills -> eval -> deploy -> observe -> pause/resume -> human approval." If Jet wants a hands-on demo, test `google/agents-cli` with Claude Code or Codex on one small internal workflow and compare against AWS AgentCore and OpenAI Agents SDK.

### Sources
- GoogleCloudTech post: https://x.com/GoogleCloudTech/status/2052463476702933171
- Google Cloud video: https://www.youtube.com/watch?v=X-5C_LZK_Js
- GitHub repo: https://github.com/google/agents-cli
- Docs: https://google.github.io/agents-cli/
