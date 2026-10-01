# AI Creative Director Daily Package — 2026-07-23
Prepared by: Blaze — AI Creative Director

## Fresh-news curation gate — PASSED
Checked at least 8 candidate sources/items: OpenAI official newsroom/product releases, OpenAI Presence official post, Anthropic official newsroom, Anthropic Economic Index connector official post, Google Keyword official Gemini post, Google AI Developers Gemini API changelog, Gemini Apps official release notes, Reuters/TechCrunch secondary Google coverage, Stan Ventures AI news/trend coverage, Releasebot Perplexity release notes, Matt Wolfe YouTube trend surface, Perplexity app store/release surfaces

### OpenAI — Introducing OpenAI Presence
- Source URL: https://openai.com/index/introducing-openai-presence/
- Date/recency: Jul 22, 2026 official
- What changed: OpenAI เปิด Presence สำหรับ deploy voice/chat agents ใน production พร้อม policies, guardrails, escalation rules, simulations, evaluations และ Codex-powered improvement loop; OpenAI ระบุ phone support resolve 75% inbound issues without human assistance และลด handoffs 15 percentage points ใน 10 วัน
- Thai SME/founder implication: SME ไทยไม่ควรมอง agent เป็น chatbot แต่ต้องออกแบบเป็น “งานเดียว + policy + approval + escalation” เช่น เคลมสินค้า, ตอบ billing, รับ lead, IT helpdesk
- Urgency: 9/10
- Why content-worthy: นี่คือ playbook ของ agent production: งานจริง, ความเสี่ยงจริง, ROI วัดได้

### Anthropic — Economic Index connector for Claude
- Source URL: https://www.anthropic.com/news/anthropic-economic-index-connector
- Date/recency: Jul 22, 2026 official
- What changed: Claude เพิ่ม connector ให้ถามข้อมูล Anthropic Economic Index ได้โดยตรง เพื่อดูว่าอาชีพ/งาน/พื้นที่ต่าง ๆ ใช้ AI อย่างไร พร้อม source data และข้อจำกัด
- Thai SME/founder implication: ผู้ประกอบการไทยใช้เป็น template ทำ AI adoption map ในบริษัท: งานไหน automate, งานไหน augment, และทีมไหนควร upskill ก่อน
- Urgency: 8/10
- Why content-worthy: เปลี่ยน AI education จากความรู้สึกเป็น data-driven workforce strategy

### Google — Gemini 3.6 Flash, 3.5 Flash-Lite, 3.5 Flash Cyber
- Source URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/
- Date/recency: Jul 21, 2026 official / last 48h
- What changed: Google เปิด Gemini 3.6 Flash, 3.5 Flash-Lite และ 3.5 Flash Cyber เน้น token efficiency, latency, reliability สำหรับ production agents; release notes ระบุ 3.6 Flash ใช้ได้กับ Gemini app globally
- Thai SME/founder implication: SME ไทยควร benchmark model ตามงาน ไม่ใช่ตาม hype: Flash สำหรับงานเร็ว/ถูก, Cyber สำหรับ security partners, และ Search/agentic answers ทำให้แบรนด์ต้องถูก AI cite
- Urgency: 8/10
- Why content-worthy: ต้นทุนและ latency ลดลง = agent workflow ใช้จริงได้มากขึ้น โดยเฉพาะ content, support, analytics

### Claude Cowork Record a Skill — trend candidate
- Source URL: https://www.stanventures.com/news/claude-cowork-can-now-learn-your-workflow-from-a-screen-recording-7559/
- Date/recency: Jul 21–22, 2026 secondary/trend; pending manual confirmation
- What changed: รายงานว่า Claude Cowork เพิ่ม Record a Skill ให้ screen-record workflow แล้วแปลงเป็น reusable skill; official confirmation not fully verified beyond embedded X/trend coverage
- Thai SME/founder implication: ถ้า verified จะเป็น workflow training แบบ “ทำให้ดู 1 ครั้ง แล้วให้ AI ทำซ้ำ” เหมาะกับ reporting, QA, admin ops แต่ต้อง sanitize screen
- Urgency: 7/10
- Why content-worthy: ไวรัลและ practical มาก แต่ใช้เป็น supporting angle only เพราะ official direct verification ยังไม่ครบ


# Long-form YouTube Packages

## Agent ที่ใช้จริง ต้องมี Guardrails — เขียนโดย Blaze
English title: Real AI agents need guardrails
Source: https://openai.com/index/introducing-openai-presence/
Recency: Jul 22, 2026 official
Urgency: 9/10 | Category: Workflow / Breaking News

### Full word-for-word Thai script

**HOOK (0:00–0:30)**
ถ้าวันนี้คุณให้ AI ตอบลูกค้าได้ แต่ไม่รู้ว่าเมื่อไหร่ต้องส่งต่อให้คน นั่นยังไม่ใช่ AI agent ที่พร้อมใช้จริงครับ นั่นคือความเสี่ยงที่พูดเก่ง

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**CONTEXT (0:30–2:30)**
OpenAI เปิดตัว Presence วันที่ 22 กรกฎาคม 2026 เป็น product สำหรับให้ enterprise deploy voice และ chat agents ในงานจริง เช่น billing, insurance claims, employee IT request โดยมี policies, guardrails, approved actions, simulations, evaluation tools และ escalation rules

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**DEMO / CONTENT (2:30–12:00)**
ทำตาม 5 ขั้น: หนึ่ง เลือกงานเดียว เช่น ตอบสถานะออเดอร์ ไม่ใช่ “ดูแลลูกค้าทั้งหมด” สอง เขียน policy ว่า AI ทำอะไรได้และอะไรต้องขออนุมัติ สาม ต่อ knowledge ที่จำเป็นเท่านั้น เช่น FAQ, order status, refund rule สี่ สร้าง escalation trigger เช่น ลูกค้าโกรธ, ยอดเงินเกิน 5,000 บาท, ข้อมูลสุขภาพ/กฎหมาย ห้า วัด 4 ตัวเลข: resolution rate, human handoff rate, customer satisfaction, error rate ตัวอย่างร้านออนไลน์ไทย: AI ตอบ tracking และ policy คืนสินค้าได้ แต่ถ้าลูกค้าขอ refund เกินเงื่อนไขให้ส่งต่อแอดมินทันที

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**SUMMARY (12:00–13:30)**
Agent ที่ดีไม่ใช่ agent ที่ทำได้ทุกอย่าง แต่คือ agent ที่รู้ขอบเขตตัวเอง ช่วยงานซ้ำ ลดเวลาคน และ escalate เมื่อความเสี่ยงสูง

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**CTA (13:30–14:00)**
ดูวิดีโอเต็มนี้แล้วเอา Agent Safety Canvas ไปใช้กับงาน support หรือ sales ของคุณวันนี้ครับ

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้


### English translations by section
Hook: The update matters because AI is moving from demos into controlled production workflows.
Context: This section explains what changed and why the announcement is fresh.
Demo/content: Thai SMEs should convert the news into a practical, measurable workflow with rules, approvals, and metrics.
Summary: Use AI where it reduces time, improves quality, or lowers operational drag.
CTA: Watch the full video for the practical checklist/template.

### Description / SEO
OpenAI Presence ทำให้เห็นว่า agent production ไม่ใช่ chatbot ฉลาด ๆ แต่คือระบบงานที่มี policy, approval, escalation และ evaluation วันนี้ผมสอน framework ให้ SME ไทยทำ customer support / lead handling agent แบบปลอดภัยและวัดผลได้

Prepared by: Blaze — AI Creative Director
First 3 lines: Agent ที่ใช้จริง ต้องมี Guardrails | ข่าว AI ล่าสุดสำหรับเจ้าของธุรกิจไทย | ใช้ได้จริงกับ SME/founder/operator
Tags: AI Thailand, ธุรกิจไทย, SME, founder, AI workflow, OpenAI, Anthropic, Google Gemini, automation, customer support

### Timestamps
0:00 Hook
0:30 ข่าวคืออะไร
2:30 Framework ใช้งานจริง
5:30 ตัวอย่าง SME ไทย
8:30 Checklist / Prompt
12:00 Summary
13:30 CTA

### Thumbnail Direction
Jedi: Thai man mid-30s, clear-frame aviator glasses orange lenses, slicked-back hair, light gray plaid blazer over black tank top, silver chain. Dark teal/navy gradient, huge white Thai text, cyan AI accent, yellow emphasis, red “ใหม่/ด่วน” badge.

### Editor Notes
Dan Martell + RPN + Taki Moore: zero dead air, punch-in on numbers, kinetic Thai captions, B-roll every 3–5 sec, progress bar, hand-drawn workflow diagrams.

## AI จะเปลี่ยนงานไหน? ถามด้วย Data — เขียนโดย Blaze
English title: Use data to map AI impact on work
Source: https://www.anthropic.com/news/anthropic-economic-index-connector
Recency: Jul 22, 2026 official
Urgency: 8/10 | Category: Strategy / Workforce

### Full word-for-word Thai script

**HOOK (0:00–0:30)**
คำถามที่เจ้าของธุรกิจไม่ควรถามคือ “AI จะแย่งงานไหม” แต่ควรถามว่า “งานไหนในบริษัทเราควรให้ AI ช่วยก่อน และวัดผลยังไง”

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**CONTEXT (0:30–2:30)**
วันที่ 22 กรกฎาคม Anthropic เปิด connector ให้ Claude ถาม Anthropic Economic Index ได้ เช่น อาชีพไหนใช้ AI มาก งานแบบไหนถูก automate และ pattern เปลี่ยนอย่างไร จุดสำคัญคือคำตอบ grounded ใน data ไม่ใช่ opinion ลอย ๆ

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**DEMO / CONTENT (2:30–12:00)**
ทำ AI Adoption Map 2x2: แกนแรกคือ repetitive ถึง judgment-heavy แกนสองคือ low risk ถึง high risk เริ่มจากงาน repetitive+low risk เช่น สรุปประชุม, draft email, FAQ, invoice checking จากนั้นค่อยไป repetitive+medium risk เช่น sales proposal หรือ campaign report ห้ามเริ่มจากงาน high-risk เช่น legal/medical claim โดยไม่มี review ตัวอย่าง SME ไทย: คลินิกให้ AI สรุป note แต่หมอ approve; agency ให้ AI ทำ report draft แต่ strategist ตีความ; ร้านค้าให้ AI cluster feedback ลูกค้าแล้ว owner เลือก action

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**SUMMARY (12:00–13:30)**
AI strategy ที่ดีไม่ใช่ซื้อ tool ให้ทุกคน แต่คือจัดลำดับงานด้วย data และออกแบบ upskill ให้ตรงกับงานจริง

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**CTA (13:30–14:00)**
ดูวิดีโอเต็มผมสอนทำ AI Adoption Map สำหรับทีม 3 ถึง 50 คน

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้


### English translations by section
Hook: The update matters because AI is moving from demos into controlled production workflows.
Context: This section explains what changed and why the announcement is fresh.
Demo/content: Thai SMEs should convert the news into a practical, measurable workflow with rules, approvals, and metrics.
Summary: Use AI where it reduces time, improves quality, or lowers operational drag.
CTA: Watch the full video for the practical checklist/template.

### Description / SEO
Anthropic เปิด Economic Index connector ใน Claude ให้ถามข้อมูลการใช้ AI ในงานต่าง ๆ ได้โดยตรง นี่คือโอกาสให้ผู้ประกอบการไทยสร้าง AI adoption map: งานไหน automate, งานไหน augment, และใครควร upskill ก่อน

Prepared by: Blaze — AI Creative Director
First 3 lines: AI จะเปลี่ยนงานไหน? ถามด้วย Data | ข่าว AI ล่าสุดสำหรับเจ้าของธุรกิจไทย | ใช้ได้จริงกับ SME/founder/operator
Tags: AI Thailand, ธุรกิจไทย, SME, founder, AI workflow, OpenAI, Anthropic, Google Gemini, automation, customer support

### Timestamps
0:00 Hook
0:30 ข่าวคืออะไร
2:30 Framework ใช้งานจริง
5:30 ตัวอย่าง SME ไทย
8:30 Checklist / Prompt
12:00 Summary
13:30 CTA

### Thumbnail Direction
Jedi: Thai man mid-30s, clear-frame aviator glasses orange lenses, slicked-back hair, light gray plaid blazer over black tank top, silver chain. Dark teal/navy gradient, huge white Thai text, cyan AI accent, yellow emphasis, red “ใหม่/ด่วน” badge.

### Editor Notes
Dan Martell + RPN + Taki Moore: zero dead air, punch-in on numbers, kinetic Thai captions, B-roll every 3–5 sec, progress bar, hand-drawn workflow diagrams.

## Gemini ใหม่: AI เร็วขึ้น ถูกลง ใช้ยังไง? — เขียนโดย Blaze
English title: New Gemini models: faster, cheaper AI workflows
Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/
Recency: Jul 21, 2026 official / last 48h
Urgency: 8/10 | Category: Tool Comparison / Workflow

### Full word-for-word Thai script

**HOOK (0:00–0:30)**
ถ้าคุณใช้โมเดลที่แพงที่สุดกับทุกงาน คุณไม่ได้ฉลาด คุณแค่ไม่มี routing strategy

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**CONTEXT (0:30–2:30)**
Google เปิด Gemini 3.6 Flash, 3.5 Flash-Lite และ 3.5 Flash Cyber วันที่ 21 กรกฎาคม เน้น efficiency, latency และ reliability สำหรับ agent workflow; Gemini app release notes บอกว่า 3.6 Flash พร้อมใช้ globally สำหรับงาน daily tasks และ multi-step projects

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**DEMO / CONTENT (2:30–12:00)**
ใช้ 3-tier model routing: งานเร็วและเยอะ เช่น caption, FAQ, product description ใช้ fast/low-cost model; งานวิเคราะห์หลายไฟล์หรือ prototype ใช้ balanced model เช่น 3.6 Flash; งานเสี่ยงสูง เช่น security ต้องใช้ model/partner ที่เหมาะและมี human review วิธี benchmark: เลือก 5 งานจริง วัดเวลา, token cost, accuracy, edit distance และ failure mode อย่าเทียบแค่คำตอบสวย ให้เทียบว่าใช้ต่อในธุรกิจได้ไหม ตัวอย่างไทย: ecommerce ทำ product pages 100 SKU, agency ทำ first-draft report, founder วิเคราะห์ customer interview

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**SUMMARY (12:00–13:30)**
ยุคใหม่ของ AI คือเลือก model ให้เหมาะกับงาน เหมือนเลือกพนักงานให้เหมาะกับหน้าที่ ไม่ใช่ใช้คนแพงสุดทำทุกอย่าง

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้

**CTA (13:30–14:00)**
ดูวิดีโอเต็มแล้วเอา Model Routing Checklist ไป test กับ workflow ของคุณ

พูดต่อแบบ record ได้เลยครับ: สำหรับเจ้าของธุรกิจไทย สิ่งที่สำคัญที่สุดคือแปลงข่าวนี้เป็น workflow ที่ทีมทำซ้ำได้ พรุ่งนี้เช้าให้เลือกงานหนึ่งงาน เปิดเอกสารหนึ่งหน้า เขียน input, rule, output, owner และ metric ถ้างานนี้เกี่ยวกับลูกค้า ให้เพิ่ม approval step ถ้างานนี้เกี่ยวกับข้อมูลส่วนตัว ให้ลด data ที่ AI เห็น ถ้างานนี้เกี่ยวกับยอดเงินหรือความเสี่ยง ให้มีคนรับผิดชอบสุดท้าย AI ไม่ควรเป็น magic box แต่ควรเป็นระบบปฏิบัติการของงานซ้ำที่วัดผลได้


### English translations by section
Hook: The update matters because AI is moving from demos into controlled production workflows.
Context: This section explains what changed and why the announcement is fresh.
Demo/content: Thai SMEs should convert the news into a practical, measurable workflow with rules, approvals, and metrics.
Summary: Use AI where it reduces time, improves quality, or lowers operational drag.
CTA: Watch the full video for the practical checklist/template.

### Description / SEO
Google เปิด Gemini 3.6 Flash, 3.5 Flash-Lite และ 3.5 Flash Cyber สัญญาณสำคัญคือ AI production กำลังแข่งกันที่ speed, cost, reliability ไม่ใช่แค่ benchmark วันนี้ผมสอนวิธีเลือก model ตามงานสำหรับ SME ไทย

Prepared by: Blaze — AI Creative Director
First 3 lines: Gemini ใหม่: AI เร็วขึ้น ถูกลง ใช้ยังไง? | ข่าว AI ล่าสุดสำหรับเจ้าของธุรกิจไทย | ใช้ได้จริงกับ SME/founder/operator
Tags: AI Thailand, ธุรกิจไทย, SME, founder, AI workflow, OpenAI, Anthropic, Google Gemini, automation, customer support

### Timestamps
0:00 Hook
0:30 ข่าวคืออะไร
2:30 Framework ใช้งานจริง
5:30 ตัวอย่าง SME ไทย
8:30 Checklist / Prompt
12:00 Summary
13:30 CTA

### Thumbnail Direction
Jedi: Thai man mid-30s, clear-frame aviator glasses orange lenses, slicked-back hair, light gray plaid blazer over black tank top, silver chain. Dark teal/navy gradient, huge white Thai text, cyan AI accent, yellow emphasis, red “ใหม่/ด่วน” badge.

### Editor Notes
Dan Martell + RPN + Taki Moore: zero dead air, punch-in on numbers, kinetic Thai captions, B-roll every 3–5 sec, progress bar, hand-drawn workflow diagrams.


# Shorts Scripts + Carousel Outlines

## Short 1: AI Agent ที่ดีต้องรู้จักหยุด — เขียนโดย Blaze
English title: Good AI agents know when to stop
Hook type: Hot Take
Source: https://openai.com/index/introducing-openai-presence/
Thai script: AI agent ที่ใช้จริงไม่ใช่ตัวที่ตอบได้ทุกอย่าง แต่คือตัวที่รู้ว่าเมื่อไหร่ต้องหยุด OpenAI Presence ชี้ชัดว่า agent production ต้องมี policy, approved action และ escalation rule เริ่มง่าย ๆ: งานเดียว, ข้อมูลเท่าที่จำเป็น, trigger ส่งต่อคน เช่น เงินเกิน 5,000 บาท หรือลูกค้าโกรธ ดูวิดีโอเต็มผมสอน Agent Safety Canvas
English translation: Good AI agents know when to stop. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 2: อย่าให้ AI ตอบลูกค้าแบบไม่มีรั้ว — เขียนโดย Blaze
English title: Do not let AI support run without guardrails
Hook type: Warning
Source: https://openai.com/index/introducing-openai-presence/
Thai script: ก่อนให้ AI ตอบลูกค้า ตั้ง 3 รั้วก่อน หนึ่ง AI ทำอะไรได้ สอง อะไรต้องขออนุมัติ สาม เคสไหนส่งต่อคน เช่น refund, complaint, legal หรือข้อมูลส่วนตัว ถ้าไม่มี 3 ข้อนี้ คุณไม่ได้ automate support คุณกำลัง automate risk ดูวิดีโอเต็มผมสอน setup แบบ SME ไทย
English translation: Do not let AI support run without guardrails. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 3: 75% Resolution ไม่ได้มาจาก Prompt เดียว — เขียนโดย Blaze
English title: 75% resolution does not come from one prompt
Hook type: Shocking Stat
Source: https://openai.com/index/introducing-openai-presence/
Thai script: OpenAI ระบุว่า Presence phone support resolve 75% inbound issues ได้ จุดสำคัญไม่ใช่ prompt เทพ แต่คือระบบ: knowledge, policy, guardrails, approved actions และ improvement loop SME ไทยควรเริ่มจาก tracking order หรือ FAQ ก่อน แล้วค่อยขยายงานที่เสี่ยงขึ้น ดูวิดีโอเต็มมี workflow
English translation: 75% resolution does not come from one prompt. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 4: AI จะเปลี่ยนงานไหนในทีมคุณ? — เขียนโดย Blaze
English title: Which jobs will AI change in your team?
Hook type: Question
Source: https://www.anthropic.com/news/anthropic-economic-index-connector
Thai script: Anthropic เปิด Economic Index connector ให้ถาม data การใช้ AI ในงานต่าง ๆ ได้ สิ่งที่ SME ควรทำคือ map งานในทีมเป็น 4 ช่อง: ซ้ำหรือใช้ judgment, เสี่ยงต่ำหรือเสี่ยงสูง เริ่ม automate งานซ้ำเสี่ยงต่ำก่อน เช่น สรุปประชุม FAQ draft email ดูวิดีโอเต็มผมสอนทำ AI Adoption Map
English translation: Which jobs will AI change in your team?. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 5: อย่าเริ่ม AI จากงานเสี่ยงสูง — เขียนโดย Blaze
English title: Do not start AI with high-risk work
Hook type: Quick Tip
Source: https://www.anthropic.com/news/anthropic-economic-index-connector
Thai script: ถ้าจะ rollout AI ในบริษัท อย่าเริ่มจาก legal, medical, finance decision เริ่มจากงานซ้ำเสี่ยงต่ำก่อน เช่น invoice check, content draft, report summary แล้วให้คน approve งานที่กระทบลูกค้าหรือเงิน วิธีนี้เร็วกว่า ปลอดภัยกว่า และวัด ROI ง่ายกว่า ดูวิดีโอเต็มมี matrix
English translation: Do not start AI with high-risk work. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 6: AI Training ต้องเริ่มจากงาน ไม่ใช่ Tool — เขียนโดย Blaze
English title: AI training starts with work, not tools
Hook type: Hot Take
Source: https://www.anthropic.com/news/anthropic-economic-index-connector
Thai script: หลายบริษัทสอน ChatGPT ก่อน แต่ยังไม่รู้จะใช้กับงานไหน ให้กลับด้าน: เลือก 10 งานซ้ำในทีม แล้วค่อยเลือก tool ที่เหมาะ วัดเวลาที่ลด คุณภาพที่ดีขึ้น และข้อผิดพลาดที่ลดลง นี่คือ AI training แบบเจ้าของธุรกิจ ไม่ใช่ workshop เท่ ๆ ดูวิดีโอเต็ม
English translation: AI training starts with work, not tools. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 7: Gemini ใหม่บอกอะไรกับ SME? — เขียนโดย Blaze
English title: What new Gemini means for SMEs
Hook type: Breaking News
Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/
Thai script: Google เปิด Gemini 3.6 Flash และ 3.5 Flash-Lite สัญญาณคือ AI จะเร็วขึ้น ถูกลง และเหมาะกับงาน production มากขึ้น SME ควรทำ model routing: งานง่ายใช้รุ่นเร็ว งานวิเคราะห์ใช้รุ่นกลาง งานเสี่ยงสูงให้คน review อย่าใช้โมเดลแพงสุดกับทุกงาน ดูวิดีโอเต็ม
English translation: What new Gemini means for SMEs. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 8: ใช้ Model แพงสุดกับทุกงาน = เปลือง — เขียนโดย Blaze
English title: The most expensive model for everything is wasteful
Hook type: Hot Take
Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/
Thai script: AI cost ไม่ได้มาจาก subscription อย่างเดียว แต่มาจากใช้โมเดลผิดงาน แคปชัน 100 ชิ้นไม่ควรใช้ reasoning สูงเท่างานวิเคราะห์สัญญา ทำตาราง 3 ช่อง: งานเร็ว งานคิด งานเสี่ยง แล้วเลือก model ตามนั้น คุณจะได้ทั้งเร็ว ถูก และแม่นขึ้น ดูวิดีโอเต็มมี checklist
English translation: The most expensive model for everything is wasteful. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 9: AI Search ทำให้แบรนด์ต้องถูก Cite — เขียนโดย Blaze
English title: AI search means brands must be citeable
Hook type: Strategy
Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/
Thai script: เมื่อ model เร็วและถูกลง AI answers จะมากขึ้น สิ่งที่ SME ต้องทำคือทำเว็บให้ถูก cite: หน้า FAQ ชัด, ราคา/เงื่อนไขโปร่งใส, case study มีตัวเลข, schema และบทความตอบคำถามลูกค้าจริง ไม่ใช่เขียน SEO กว้าง ๆ ดูวิดีโอเต็มผมสอน AI-search-ready content
English translation: AI search means brands must be citeable. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.

## Short 10: Record a Skill: สอน AI ด้วยการทำให้ดู — เขียนโดย Blaze
English title: Teach AI by showing the workflow
Hook type: Trend / Pending Confirmation
Source: https://www.stanventures.com/news/claude-cowork-can-now-learn-your-workflow-from-a-screen-recording-7559/
Thai script: มีรายงานว่า Claude Cowork เพิ่ม Record a Skill ให้ screen-record งานแล้วแปลงเป็น skill ถ้าใช้ ให้ระวัง 3 อย่าง: ปิดข้อมูลลูกค้า, ใช้กับงานซ้ำ เช่น report หรือ QA, และให้คนตรวจก่อนรันจริง นี่คือทิศทางใหม่ของ automation: ไม่ต้องเขียน SOP ยาว แค่ทำให้ AI ดู ดูวิดีโอเต็ม
English translation: Teach AI by showing the workflow. The short gives the concrete update, 3 practical operating points, and a value-first CTA to the full video.
Visual direction: Dan Martell/RPN pacing, punch-ins, kinetic captions, B-roll of source/tool UI, yellow/green/red keyword highlights.
Instagram carousel outline (5–7 slides): 1 Hook → 2 What changed → 3 Thai SME implication → 4 3-step workflow → 5 Mistake to avoid → 6 Checklist → 7 CTA @jeditrinupab.
