# AI Creative Director Daily Package — 2026-07-29
Prepared by: Blaze — AI Creative Director


---

## Fresh-news curation gate — PASSED
Checked 9 candidate sources/items in the last 24–48h mix of official/company and reputable trend/news sources. Selected 5 source-backed angles for Thai SME relevance.


---

- OpenAI News — https://openai.com/news/ — official; Jul 28 scientific computing, Jul 27 work

---

- Anthropic Claude Opus 5 — https://www.anthropic.com/news/claude-opus-5 — official; Jul 24, still fresh but outside 48h

---

- Anthropic cryptography research — https://www.anthropic.com/research/discovering-cryptographic-weaknesses — official; Jul 28

---

- MCP 2026-07-28 spec — https://blog.modelcontextprotocol.io/posts/2026-07-28/ — official; Jul 28

---

- JFrog/OpenAI zero-day remediation — https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/ — vendor official; posted after OpenAI/HF disclosure

---

- Perplexity Personal Computer for Windows — https://www.theverge.com/ai-artificial-intelligence/971750/perplexity-personal-computer-windows-ai-agents — reputable secondary; Jul 28; direct Perplexity PC page not found in scan

---

- Meta + BlackRock AI data center — https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/ — official; Jul 28/27

---

- NVIDIA Open Secure AI Alliance — https://blogs.nvidia.com/blog/open-secure-ai-alliance/ — official; recent; date visible via AI Weekly recency

---

- AI Weekly live index — https://aiweekly.co/ai-news-today — reputable trend aggregator; Jul 28 live

---


## Selected source-backed stories


---

- **Claude Mythos finds cryptographic weaknesses** (Jul 28, 2026 — official Anthropic research)
  - URL: https://www.anthropic.com/research/discovering-cryptographic-weaknesses
  - What changed: Claude Mythos Preview helped discover an improved HAWK post-quantum signature attack and a 200–800x faster attack on reduced-round AES; Anthropic says no production systems are affected and disclosures were coordinated.
  - Thai SME/founder implication: AI is becoming a research-grade security analyst. Thai SMEs should not panic about cryptography, but must realize both attackers and defenders will find weaknesses faster; vendor patch speed and security process now matter more.
  - Urgency: 9/10
  - Content-worthy: Fresh, official, surprising; perfect for an AI-security education angle with practical guardrails.


---

- **MCP 2026-07-28 goes stateless** (Jul 28, 2026 — official MCP blog)
  - URL: https://blog.modelcontextprotocol.io/posts/2026-07-28/
  - What changed: MCP removed initialize/initialized and session IDs, shifted to stateless request/response, added MRTR for mid-call user input, header-based routing, cache hints, auth hardening, and 12-month deprecation windows.
  - Thai SME/founder implication: Agent integrations are maturing from demos to enterprise infrastructure. Thai founders building automations should demand scalable, auditable, permissioned agent connections instead of brittle Zapier-style chains.
  - Urgency: 8/10
  - Content-worthy: Fresh builder news with clear workflow value for operators and AI agencies.


---

- **Perplexity Personal Computer reaches Windows** (Jul 28, 2026 — The Verge; secondary coverage)
  - URL: https://www.theverge.com/ai-artificial-intelligence/971750/perplexity-personal-computer-windows-ai-agents
  - What changed: Perplexity expanded its Personal Computer agent to Windows for Max and Enterprise Max users from $200/month, allowing AI to work across local files, Office 365 and web; user confirmation for sensitive actions is noted.
  - Thai SME/founder implication: The next interface is not chat; it is a desktop worker. Thai SMEs running Windows/Office can start redesigning admin, finance, and sales ops around supervised computer-use agents.
  - Urgency: 8/10
  - Content-worthy: Practical, tool-focused, highly relevant for Thai offices; label as secondary-source-backed.


---

- **JFrog/OpenAI zero-day remediation model** (Jul 2026 — vendor official, refers to last week OpenAI/HF disclosure)
  - URL: https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/
  - What changed: JFrog says OpenAI models found unknown Artifactory vulnerabilities during cyber evaluation; JFrog released fixes including Artifactory 7.161 and framed rapid remediation as the new trust model.
  - Thai SME/founder implication: SMEs using cloud tools/plugins need patch discipline, vendor inventory, and incident workflows because AI agents can find exploit chains at machine speed.
  - Urgency: 8/10
  - Content-worthy: Great practical security checklist companion to the Anthropic story.


---

- **Meta + BlackRock $14B / 1GW AI data center** (Jul 28/27, 2026 — official Meta newsroom)
  - URL: https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/
  - What changed: Meta and BlackRock announced a venture for a 1GW El Paso AI data center campus, about $14B development cost, expected online in 2028; Meta initial sole occupant.
  - Thai SME/founder implication: AI cost and compute supply will shape tool pricing. Thai founders should diversify AI tools and track usage economics instead of assuming prices only go down.
  - Urgency: 7/10
  - Content-worthy: Macro angle, useful for founder strategy and budget planning.


---

# LF1 — AI หา ‘ช่องโหว่’ ได้เองแล้ว SME ต้องทำยังไง by Blaze
เขียนโดย Blaze / Written by: Blaze

Thai title: AI หา ‘ช่องโหว่’ ได้เองแล้ว SME ต้องทำยังไง
English: AI Can Find Weaknesses Now — What SMEs Must Do
Category: Breaking News / Security
Urgency: 9/10
Sources: https://www.anthropic.com/research/discovering-cryptographic-weaknesses, https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/

## Word-for-word Thai script

### HOOK
วันนี้มีข่าว AI ที่เจ้าของธุรกิจควรฟังแบบจริงจังครับ Anthropic เปิดเผยว่า Claude Mythos Preview ช่วยค้นพบวิธีโจมตี cryptography ที่มนุษย์ตรวจมาหลายปีแล้วยังไม่เจอ หนึ่งคือ HAWK ระบบลายเซ็นดิจิทัลสำหรับโลกหลัง quantum สองคือ reduced-round AES ที่ AI ทำให้โจมตีเร็วขึ้น 200 ถึง 800 เท่า Anthropic ย้ำว่า production system ยังไม่กระทบ แต่สัญญาณสำคัญคือ AI ไม่ได้แค่เขียนคอนเทนต์แล้ว มันเริ่มเป็นนักวิจัย security ระดับสูงได้

English translation: วันนี้มีข่าว AI ที่เจ้าของธุรกิจควรฟังแบบจริงจังครับ Anthropic เปิดเผยว่า Claude Mythos Preview ช่วยค้นพบวิธีโจมตี cryptography ที่มนุษย์ตรวจมาหลายปีแล้วยังไม่เจอ หนึ่งคือ HAWK ระบบลายเซ็นดิจิทัลสำหรับโลกหลัง quantum สองคือ reduced-round AES ที่ AI ทำให้โจมตีเร็วขึ้น 200 ถึง 800 เท่า Anthropic ย้ำว่า production system ...

### CONTEXT
สำหรับ SME ไทย ข่าวนี้ไม่ใช่ให้คุณไปเรียน cryptography วันนี้ แต่ให้เข้าใจว่าเกมความปลอดภัยเปลี่ยนจากมนุษย์หา bug เป็น AI หา bug ด้วยความเร็วเครื่องจักร อีกข่าวจาก JFrog บอกว่า OpenAI model เคยพบ zero-day ใน Artifactory ระหว่าง evaluation แล้ว JFrog ต้อง patch ให้เร็ว นี่คือ trust model ใหม่: ไม่ใช่ vendor ที่ไม่มีช่องโหว่ แต่คือ vendor ที่รู้เร็ว แก้เร็ว แจ้งชัด และลูกค้าปรับตามได้เร็ว

English translation: สำหรับ SME ไทย ข่าวนี้ไม่ใช่ให้คุณไปเรียน cryptography วันนี้ แต่ให้เข้าใจว่าเกมความปลอดภัยเปลี่ยนจากมนุษย์หา bug เป็น AI หา bug ด้วยความเร็วเครื่องจักร อีกข่าวจาก JFrog บอกว่า OpenAI model เคยพบ zero-day ใน Artifactory ระหว่าง evaluation แล้ว JFrog ต้อง patch ให้เร็ว นี่คือ trust model ใหม่: ไม่ใช่ vendor ที่ไม่มีช่อง...

### DEMO
ผมแนะนำ AI Security OS 7 วันสำหรับ SME วันแรก ทำ asset inventory: เว็บ, โดเมน, LINE OA, Facebook, Shopify, CRM, Google Workspace, payment gateway วันที่สอง เช็กบัญชี admin เก่าและเปิด 2FA ทุกบัญชี วันที่สาม ทำ vendor/plugin inventory แล้วถามว่า plugin ไหนเข้าถึงข้อมูลลูกค้า วันสี่ ตั้ง patch routine: ทุกวันศุกร์ 30 นาทีตรวจ update และ advisory วันห้า ทำ backup และ restore test ไม่ใช่แค่มี backup แต่ต้องลองกู้ วันหก ทำ incident playbook ถ้าเพจโดนยึด ถ้าข้อมูลลูกค้ารั่ว ถ้าเว็บ redirect แปลก ใครตัดสินใจอะไร วันเจ็ด ใช้ AI ช่วยเขียน checklist ด้วย prompt นี้: ‘คุณคือ cybersecurity advisor สำหรับ SME ไทย สร้าง checklist 7 วันสำหรับธุรกิจที่ใช้ Google Workspace, LINE OA, Facebook Ads และเว็บไซต์ WordPress แบ่ง critical/high/medium บอกวิธีตรวจที่ไม่ต้องใช้ password จริง’ ข้อห้ามคืออย่า paste password, token, private key, หรือข้อมูลลูกค้าลับให้ AI ตรวจ

English translation: ผมแนะนำ AI Security OS 7 วันสำหรับ SME วันแรก ทำ asset inventory: เว็บ, โดเมน, LINE OA, Facebook, Shopify, CRM, Google Workspace, payment gateway วันที่สอง เช็กบัญชี admin เก่าและเปิด 2FA ทุกบัญชี วันที่สาม ทำ vendor/plugin inventory แล้วถามว่า plugin ไหนเข้าถึงข้อมูลลูกค้า วันสี่ ตั้ง patch routine: ทุกวันศุกร์ 30 นาท...

### SUMMARY
บทเรียนคือ AI ทำให้การค้นหาช่องโหว่เร็วขึ้นมาก ธุรกิจเล็กไม่ต้องกลัวจนหยุดใช้ AI แต่ต้องมี inventory, 2FA, patch rhythm, backup, vendor review และ incident playbook

English translation: บทเรียนคือ AI ทำให้การค้นหาช่องโหว่เร็วขึ้นมาก ธุรกิจเล็กไม่ต้องกลัวจนหยุดใช้ AI แต่ต้องมี inventory, 2FA, patch rhythm, backup, vendor review และ incident playbook

### CTA
ถ้าคุณมีทีมเล็กและไม่มี IT เต็มเวลา ดูวิดีโอเต็มนี้แล้วทำ checklist 7 วันก่อนครับ กดติดตามไว้ ผมจะทำ template security sprint ให้เอาไปใช้กับทีมจริง

English translation: ถ้าคุณมีทีมเล็กและไม่มี IT เต็มเวลา ดูวิดีโอเต็มนี้แล้วทำ checklist 7 วันก่อนครับ กดติดตามไว้ ผมจะทำ template security sprint ให้เอาไปใช้กับทีมจริง

## Description and SEO
Claude Mythos ช่วยค้นพบ weakness ใน HAWK และ reduced-round AES ส่วน JFrog เผย workflow patch zero-day ที่ OpenAI model พบ
นี่ไม่ใช่ข่าวให้กลัว แต่เป็นสัญญาณว่า security ต้องเร็วขึ้นมาก
วิดีโอนี้สอน AI Security Operating System 7 วันสำหรับ SME ไทย

Tags: AI Security, Claude Mythos, Anthropic, JFrog, OpenAI, Cybersecurity, SME Thailand, AI Agents, Business Security, Jedi Trinupab

## Timestamps
0:00 Hook
0:30 Context
2:30 Demo / Workflow
8:30 Thai SME examples
12:00 Summary
13:30 CTA

## Thumbnail direction
Jet สีหน้าจริงจัง + โล่แตก + text ‘AI หา BUG เอง’; red ด่วน, cyan AI

## Editor notes
Dan Martell jump cuts, RPN kinetic captions, Taki Moore diagrams/whiteboard. B-roll every 3–5 sec. Use Jedi visual identity: Thai man mid-30s, clear aviator glasses orange lenses, slicked-back dark hair, light gray plaid blazer over black tank, silver accessories.

---

# LF2 — MCP ใหม่: Agent AI กำลังเข้าองค์กรจริง by Blaze
เขียนโดย Blaze / Written by: Blaze

Thai title: MCP ใหม่: Agent AI กำลังเข้าองค์กรจริง
English: New MCP: AI Agents Are Becoming Enterprise Infrastructure
Category: Builder / Workflow
Urgency: 8/10
Sources: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Word-for-word Thai script

### HOOK
ถ้าคุณทำ AI automation แล้วเจอปัญหาเชื่อม tool แล้วพังง่าย ข่าว MCP วันนี้สำคัญมากครับ Model Context Protocol ออก spec ใหม่วันที่ 28 กรกฎาคม 2026 และเปลี่ยนแกนหลักเป็น stateless request-response แปลภาษาคนคือ agent ไม่จำเป็นต้องผูก session แปลก ๆ กับ server เดิมอีกต่อไป request ใด ๆ ไปลง instance ไหนก็ได้หลัง load balancer นี่คือสัญญาณว่า AI agent กำลังออกจากโลก demo เข้าโลก infrastructure

English translation: ถ้าคุณทำ AI automation แล้วเจอปัญหาเชื่อม tool แล้วพังง่าย ข่าว MCP วันนี้สำคัญมากครับ Model Context Protocol ออก spec ใหม่วันที่ 28 กรกฎาคม 2026 และเปลี่ยนแกนหลักเป็น stateless request-response แปลภาษาคนคือ agent ไม่จำเป็นต้องผูก session แปลก ๆ กับ server เดิมอีกต่อไป request ใด ๆ ไปลง instance ไหนก็ได้หลัง load balan...

### CONTEXT
MCP เพิ่มหลายอย่างที่ธุรกิจควรรู้ หนึ่ง ไม่มี initialize handshake และ session id แบบเดิม สเกล server ง่ายขึ้น สอง MRTR ทำให้ tool ขอข้อมูลหรือ confirmation จากคนกลางคันได้ สาม header-based routing ให้ gateway, rate limiter, WAF จัดการ request ได้ง่าย สี่ list result cacheable ลดการเรียกซ้ำ ห้า auth hardening ด้วย issuer validation และ client metadata document พูดง่าย ๆ คือระบบ agent เริ่มมีภาษามาตรฐานสำหรับ reliability, permission และ governance

English translation: MCP เพิ่มหลายอย่างที่ธุรกิจควรรู้ หนึ่ง ไม่มี initialize handshake และ session id แบบเดิม สเกล server ง่ายขึ้น สอง MRTR ทำให้ tool ขอข้อมูลหรือ confirmation จากคนกลางคันได้ สาม header-based routing ให้ gateway, rate limiter, WAF จัดการ request ได้ง่าย สี่ list result cacheable ลดการเรียกซ้ำ ห้า auth hardening ด้วย issu...

### DEMO
สำหรับ SME หรือ AI agency ในไทย ให้ใช้ MCP news นี้เป็น checklist เวลาสร้าง workflow หนึ่ง ทุก tool ต้องมี permission ชัด เช่น read-only, draft-only, approve-required สอง ทุก action เสี่ยงต้องมี human confirmation เช่น ส่งอีเมล ลบไฟล์ สร้าง invoice สาม ต้องมี audit log ว่า agent เรียก tool ไหนด้วย input อะไร สี่ ต้องแยก environment ทดลองกับ production ห้า ต้องมี fallback ถ้า tool ล่ม prompt สำหรับ founder: ‘ออกแบบ AI agent workflow สำหรับบริษัท SME ของฉัน โดยแบ่ง tools เป็น read, write draft, write with approval และ forbidden พร้อม risk control และ KPI’ ตัวอย่างฝ่ายขาย: agent อ่าน CRM ได้ สรุป lead ได้ draft follow-up ได้ แต่ส่ง email ต้องให้ salesperson กด approve

English translation: สำหรับ SME หรือ AI agency ในไทย ให้ใช้ MCP news นี้เป็น checklist เวลาสร้าง workflow หนึ่ง ทุก tool ต้องมี permission ชัด เช่น read-only, draft-only, approve-required สอง ทุก action เสี่ยงต้องมี human confirmation เช่น ส่งอีเมล ลบไฟล์ สร้าง invoice สาม ต้องมี audit log ว่า agent เรียก tool ไหนด้วย input อะไร สี่ ต้องแย...

### SUMMARY
MCP ใหม่คือสัญญาณว่า AI agent จะไม่ใช่แค่ chat window แต่เป็นชั้นเชื่อมต่อข้อมูลและ tool ขององค์กร ใครทำระบบตั้งแต่วันนี้ด้วย permission, audit, approval จะได้เปรียบมาก

English translation: MCP ใหม่คือสัญญาณว่า AI agent จะไม่ใช่แค่ chat window แต่เป็นชั้นเชื่อมต่อข้อมูลและ tool ขององค์กร ใครทำระบบตั้งแต่วันนี้ด้วย permission, audit, approval จะได้เปรียบมาก

### CTA
ถ้าคุณกำลังทำ automation ให้ทีม ดูวิดีโอเต็มนี้ก่อนต่อ tool เพิ่มครับ กดติดตามไว้ ผมจะสอนออกแบบ Agent Stack สำหรับ SME แบบปลอดภัย

English translation: ถ้าคุณกำลังทำ automation ให้ทีม ดูวิดีโอเต็มนี้ก่อนต่อ tool เพิ่มครับ กดติดตามไว้ ผมจะสอนออกแบบ Agent Stack สำหรับ SME แบบปลอดภัย

## Description and SEO
MCP 2026-07-28 เปลี่ยนเป็น stateless core เพิ่ม MRTR, header routing, cache hints และ auth hardening
นี่คือข่าวสำคัญสำหรับคนทำ AI workflow เพราะ agent connection กำลังโตเป็น infrastructure
วิดีโอนี้แปลงข่าวเทคนิคให้เป็น checklist สำหรับ founder/operator

Tags: MCP, Model Context Protocol, AI Agents, Automation, AI Workflow, Thai SME, Claude, Agentic AI, Operations, Jedi Trinupab

## Timestamps
0:00 Hook
0:30 Context
2:30 Demo / Workflow
8:30 Thai SME examples
12:00 Summary
13:30 CTA

## Thumbnail direction
Jet ชี้ diagram Agent → Tool → Data; text ‘Agent ไม่ใช่ demo แล้ว’; navy/cyan

## Editor notes
Dan Martell jump cuts, RPN kinetic captions, Taki Moore diagrams/whiteboard. B-roll every 3–5 sec. Use Jedi visual identity: Thai man mid-30s, clear aviator glasses orange lenses, slicked-back dark hair, light gray plaid blazer over black tank, silver accessories.

---

# LF3 — Perplexity ทำให้ Windows เป็นพนักงาน AI by Blaze
เขียนโดย Blaze / Written by: Blaze

Thai title: Perplexity ทำให้ Windows เป็นพนักงาน AI
English: Perplexity Turns Windows Into an AI Worker
Category: Tool Update / Workflow
Urgency: 8/10
Sources: https://www.theverge.com/ai-artificial-intelligence/971750/perplexity-personal-computer-windows-ai-agents, https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/

## Word-for-word Thai script

### HOOK
AI กำลังจะออกจากช่องแชตไปอยู่ในคอมคุณครับ The Verge รายงานว่า Perplexity ขยาย Personal Computer ไป Windows แล้ว สำหรับผู้ใช้ Max และ Enterprise Max เริ่มต้นประมาณ 200 ดอลลาร์ต่อเดือน หรือราว 7,200 บาทต่อเดือน สิ่งที่น่าสนใจคือมันทำงานข้าม local files, Microsoft Office 365 และ web ได้ในที่เดียว นี่คือภาพอนาคตของพนักงาน AI บนเครื่องทำงานจริง

English translation: AI กำลังจะออกจากช่องแชตไปอยู่ในคอมคุณครับ The Verge รายงานว่า Perplexity ขยาย Personal Computer ไป Windows แล้ว สำหรับผู้ใช้ Max และ Enterprise Max เริ่มต้นประมาณ 200 ดอลลาร์ต่อเดือน หรือราว 7,200 บาทต่อเดือน สิ่งที่น่าสนใจคือมันทำงานข้าม local files, Microsoft Office 365 และ web ได้ในที่เดียว นี่คือภาพอนาคตของพนักงาน ...

### CONTEXT
ทำไมข่าวนี้สำคัญกับ SME ไทย เพราะออฟฟิศส่วนใหญ่ยังทำงานบน Windows, Excel, Word, PowerPoint, Outlook และไฟล์ที่กระจัดกระจาย AI chat แบบเดิมตอบได้ แต่ไม่เห็น context ในเครื่อง Perplexity กำลังผลักแนวคิด general-purpose digital worker ที่ช่วยสร้างเอกสาร update spreadsheet และทำงานจากข้อมูล local ได้ แต่ข่าวก็ย้ำว่าต้องมี notification ก่อน action เสี่ยง เช่น ส่งอีเมลหรือลบไฟล์ นี่คือ keyword สำคัญ: supervised automation

English translation: ทำไมข่าวนี้สำคัญกับ SME ไทย เพราะออฟฟิศส่วนใหญ่ยังทำงานบน Windows, Excel, Word, PowerPoint, Outlook และไฟล์ที่กระจัดกระจาย AI chat แบบเดิมตอบได้ แต่ไม่เห็น context ในเครื่อง Perplexity กำลังผลักแนวคิด general-purpose digital worker ที่ช่วยสร้างเอกสาร update spreadsheet และทำงานจากข้อมูล local ได้ แต่ข่าวก็ย้ำว่าต้องมี ...

### DEMO
5 workflow ที่ SME ควรทดลองเมื่อเครื่องมือแนวนี้พร้อม หนึ่ง Sales ops: อ่านไฟล์ proposal เก่า สรุป pattern ที่ปิดดี แล้ว draft proposal ใหม่ สอง Finance admin: รวมใบแจ้งหนี้จาก folder ทำตารางครบ/ขาด แต่ห้ามจ่ายเงินเอง สาม Customer support: อ่าน FAQ และ ticket เก่า draft คำตอบที่สอดคล้องกับ tone ของแบรนด์ สี่ Marketing: เปิด report, website, competitor page แล้วทำ weekly insight ห้า Founder assistant: สรุปเอกสารประชุมและสร้าง action list ข้อควรระวัง: เริ่มด้วยไฟล์ sample, สร้าง folder เฉพาะ AI, ห้ามให้เข้าทั้ง drive ตั้งชื่อไฟล์มาตรฐาน และ action เสี่ยงต้อง approve prompt: ‘คุณคือ AI operations assistant ทำงานเฉพาะใน folder นี้ สรุปไฟล์ทั้งหมดเป็น action list ห้ามลบ ส่ง หรือแก้ไฟล์ต้นฉบับ ให้สร้าง draft ใหม่เท่านั้น’

English translation: 5 workflow ที่ SME ควรทดลองเมื่อเครื่องมือแนวนี้พร้อม หนึ่ง Sales ops: อ่านไฟล์ proposal เก่า สรุป pattern ที่ปิดดี แล้ว draft proposal ใหม่ สอง Finance admin: รวมใบแจ้งหนี้จาก folder ทำตารางครบ/ขาด แต่ห้ามจ่ายเงินเอง สาม Customer support: อ่าน FAQ และ ticket เก่า draft คำตอบที่สอดคล้องกับ tone ของแบรนด์ สี่ Marketing:...

### SUMMARY
Perplexity บน Windows คือสัญญาณว่า AI จะกลายเป็น desktop worker แต่ SME ที่ได้ประโยชน์ไม่ใช่คนที่ปล่อย AI อิสระที่สุด แต่คือคนที่วาง folder, permission, naming, approval และ KPI ดีที่สุด

English translation: Perplexity บน Windows คือสัญญาณว่า AI จะกลายเป็น desktop worker แต่ SME ที่ได้ประโยชน์ไม่ใช่คนที่ปล่อย AI อิสระที่สุด แต่คือคนที่วาง folder, permission, naming, approval และ KPI ดีที่สุด

### CTA
ถ้าทีมคุณใช้ Windows และ Office ทั้งวัน วิดีโอเต็มนี้คือแผนทดลองแบบไม่เสี่ยง กดติดตามไว้ ผมจะทำ workflow ตัวอย่างสำหรับฝ่ายขาย แอดมิน และบัญชี

English translation: ถ้าทีมคุณใช้ Windows และ Office ทั้งวัน วิดีโอเต็มนี้คือแผนทดลองแบบไม่เสี่ยง กดติดตามไว้ ผมจะทำ workflow ตัวอย่างสำหรับฝ่ายขาย แอดมิน และบัญชี

## Description and SEO
Perplexity Personal Computer ขยายไป Windows ให้ AI ทำงานข้าม local files, Microsoft 365 และ web สำหรับ Max/Enterprise Max
นี่คือ practical signal ว่า interface ต่อไปของ AI คือ desktop worker ไม่ใช่ chatbot
วิดีโอนี้สอน 5 workflow ที่ SME ไทยควรทดลองแบบ supervised

Tags: Perplexity, AI Agent, Windows AI, Microsoft 365, AI Tools, SME Automation, AI Browser, Computer Use, Thai Business, Jedi Trinupab

## Timestamps
0:00 Hook
0:30 Context
2:30 Demo / Workflow
8:30 Thai SME examples
12:00 Summary
13:30 CTA

## Thumbnail direction
Jet + หน้าจอ Windows + text ‘คอมทำงานแทนคุณ’; badge $200/mo

## Editor notes
Dan Martell jump cuts, RPN kinetic captions, Taki Moore diagrams/whiteboard. B-roll every 3–5 sec. Use Jedi visual identity: Thai man mid-30s, clear aviator glasses orange lenses, slicked-back dark hair, light gray plaid blazer over black tank, silver accessories.

---

# Short01 — Claude เจอ weakness ที่คนตรวจมาหลายปี by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: Claude เจอ weakness ที่คนตรวจมาหลายปี
English title: Claude Found Crypto Weaknesses
Hook type: Shocking Stat
Source: https://www.anthropic.com/research/discovering-cryptographic-weaknesses

## Script
Claude Mythos ช่วยพบ weakness ใน HAWK และ reduced-round AES โดย AES เร็วขึ้น 200–800 เท่าในการโจมตีเวอร์ชันทดลอง Anthropic บอก production ยังไม่กระทบ แต่บทเรียนสำหรับ SME คือ patch เร็วขึ้น vendor inventory ต้องชัด และห้ามรอ audit ปีละครั้ง ดูวิดีโอเต็มผมสอน Security OS 7 วัน

English translation: Claude Mythos ช่วยพบ weakness ใน HAWK และ reduced-round AES โดย AES เร็วขึ้น 200–800 เท่าในการโจมตีเวอร์ชันทดลอง Anthropic บอก production ยังไม่กระทบ แต่บทเรียนสำหรับ SME คือ patch เร็วขึ้น vendor inventory ต้องชัด และห้ามรอ audit ปีละครั้ง ดูวิดีโอเต็มผมสอน Security OS 7 วัน

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. Claude เจอ weakness ที่คนตรวจมาหลายปี →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short02 — AI Security ไม่ใช่เรื่องบริษัทใหญ่แล้ว by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: AI Security ไม่ใช่เรื่องบริษัทใหญ่แล้ว
English title: AI Security Is Now SME Work
Hook type: Hot Take
Source: https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/

## Script
JFrog บอก OpenAI model พบ zero-day ใน Artifactory แล้วทีมต้อง patch ถึงเวอร์ชัน 7.161 สิ่งที่ SME ต้องทำคือรู้ว่าใช้ vendor/plugin อะไร ใครเป็น admin มี backup ไหม และ update เมื่อไร อย่าให้ระบบสำคัญไม่มีเจ้าของ ดูวิดีโอเต็มสำหรับ checklist

English translation: JFrog บอก OpenAI model พบ zero-day ใน Artifactory แล้วทีมต้อง patch ถึงเวอร์ชัน 7.161 สิ่งที่ SME ต้องทำคือรู้ว่าใช้ vendor/plugin อะไร ใครเป็น admin มี backup ไหม และ update เมื่อไร อย่าให้ระบบสำคัญไม่มีเจ้าของ ดูวิดีโอเต็มสำหรับ checklist

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. AI Security ไม่ใช่เรื่องบริษัทใหญ่แล้ว →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short03 — ห้ามเอา password ให้ AI ตรวจ by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: ห้ามเอา password ให้ AI ตรวจ
English title: Never Give AI Passwords
Hook type: Quick Tip
Source: https://www.anthropic.com/research/discovering-cryptographic-weaknesses

## Script
ถ้าจะให้ AI ช่วยทำ security checklist ให้ใส่ชื่อ tool และ process ได้ แต่อย่า paste password, token, private key หรือข้อมูลลูกค้า ใช้ prompt ให้ AI บอกวิธีตรวจแบบปลอดภัยแทน: ‘ห้ามขอ credential จริง ให้แนะนำ checklist เท่านั้น’ ดูวิดีโอเต็มผมสอนวิธีใช้ AI แบบไม่เสี่ยง

English translation: ถ้าจะให้ AI ช่วยทำ security checklist ให้ใส่ชื่อ tool และ process ได้ แต่อย่า paste password, token, private key หรือข้อมูลลูกค้า ใช้ prompt ให้ AI บอกวิธีตรวจแบบปลอดภัยแทน: ‘ห้ามขอ credential จริง ให้แนะนำ checklist เท่านั้น’ ดูวิดีโอเต็มผมสอนวิธีใช้ AI แบบไม่เสี่ยง

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. ห้ามเอา password ให้ AI ตรวจ →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short04 — MCP ใหม่ทำให้ Agent สเกลได้จริง by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: MCP ใหม่ทำให้ Agent สเกลได้จริง
English title: MCP Goes Stateless
Hook type: Breaking News
Source: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Script
MCP spec ใหม่วันที่ 28 ก.ค. เปลี่ยนเป็น stateless core ตัด session id และ handshake เดิม แปลว่า agent tool server สเกลง่ายขึ้น หลัง load balancer ได้ดีขึ้น สำหรับ founder นี่คือสัญญาณว่า agent integration กำลังเป็น infrastructure ไม่ใช่ของเล่น ดูวิดีโอเต็มสำหรับ checklist

English translation: MCP spec ใหม่วันที่ 28 ก.ค. เปลี่ยนเป็น stateless core ตัด session id และ handshake เดิม แปลว่า agent tool server สเกลง่ายขึ้น หลัง load balancer ได้ดีขึ้น สำหรับ founder นี่คือสัญญาณว่า agent integration กำลังเป็น infrastructure ไม่ใช่ของเล่น ดูวิดีโอเต็มสำหรับ checklist

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. MCP ใหม่ทำให้ Agent สเกลได้จริง →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short05 — Agent ต้องถามคนก่อน action เสี่ยง by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: Agent ต้องถามคนก่อน action เสี่ยง
English title: Agents Need Human Confirmation
Hook type: Quick Tip
Source: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Script
MCP เพิ่ม MRTR ให้ tool ขอข้อมูลหรือ confirmation ระหว่างทำงานได้ นี่สำคัญมากสำหรับธุรกิจ: AI อ่านข้อมูลได้ draft ได้ แต่ส่งอีเมล ลบไฟล์ สร้าง invoice หรือแตะเงิน ต้องให้คน approve ดูวิดีโอเต็มผมสอน permission model 4 ชั้น

English translation: MCP เพิ่ม MRTR ให้ tool ขอข้อมูลหรือ confirmation ระหว่างทำงานได้ นี่สำคัญมากสำหรับธุรกิจ: AI อ่านข้อมูลได้ draft ได้ แต่ส่งอีเมล ลบไฟล์ สร้าง invoice หรือแตะเงิน ต้องให้คน approve ดูวิดีโอเต็มผมสอน permission model 4 ชั้น

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. Agent ต้องถามคนก่อน action เสี่ยง →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short06 — Perplexity ทำให้ Windows เป็น AI Worker by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: Perplexity ทำให้ Windows เป็น AI Worker
English title: Windows Becomes an AI Worker
Hook type: Breaking News
Source: https://www.theverge.com/ai-artificial-intelligence/971750/perplexity-personal-computer-windows-ai-agents

## Script
Perplexity Personal Computer มาถึง Windows แล้ว รายงานว่าทำงานข้าม local files, Microsoft 365 และ web ได้ ราคา Max เริ่มราว $200/เดือน หรือประมาณ 7,200 บาท จุดเริ่มที่ปลอดภัยคือให้ทำ draft ใน folder เฉพาะ ไม่ให้แก้ไฟล์จริง ดูวิดีโอเต็มสำหรับ 5 workflow SME

English translation: Perplexity Personal Computer มาถึง Windows แล้ว รายงานว่าทำงานข้าม local files, Microsoft 365 และ web ได้ ราคา Max เริ่มราว $200/เดือน หรือประมาณ 7,200 บาท จุดเริ่มที่ปลอดภัยคือให้ทำ draft ใน folder เฉพาะ ไม่ให้แก้ไฟล์จริง ดูวิดีโอเต็มสำหรับ 5 workflow SME

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. Perplexity ทำให้ Windows เป็น AI Worker →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short07 — AI Chat กำลังแพ้ Desktop Worker by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: AI Chat กำลังแพ้ Desktop Worker
English title: Chatbots vs Desktop Workers
Hook type: Hot Take
Source: https://www.theverge.com/ai-artificial-intelligence/971750/perplexity-personal-computer-windows-ai-agents

## Script
Chatbot ตอบคำถามได้ แต่ desktop AI worker ทำงานกับไฟล์จริงได้ เช่น proposal, spreadsheet, email draft สิ่งที่ SME ต้องเตรียมคือ naming convention, folder แยก, permission และ approval ไม่ใช่แค่ซื้อ tool ใหม่ ดูวิดีโอเต็มผมสอน setup ทดลอง

English translation: Chatbot ตอบคำถามได้ แต่ desktop AI worker ทำงานกับไฟล์จริงได้ เช่น proposal, spreadsheet, email draft สิ่งที่ SME ต้องเตรียมคือ naming convention, folder แยก, permission และ approval ไม่ใช่แค่ซื้อ tool ใหม่ ดูวิดีโอเต็มผมสอน setup ทดลอง

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. AI Chat กำลังแพ้ Desktop Worker →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short08 — Meta ลง $14B เพราะ AI กิน Compute by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: Meta ลง $14B เพราะ AI กิน Compute
English title: AI Compute Is the New Oil
Hook type: Shocking Stat
Source: https://about.fb.com/news/2026/07/meta-announces-new-venture-with-blackrock-to-develop-data-center-in-el-paso/

## Script
Meta กับ BlackRock ประกาศ data center 1GW มูลค่าพัฒนาเกือบ $14B เพื่อ AI นี่บอกว่า compute ยังแพงและสำคัญมาก SME ต้องคิดเรื่อง cost ต่อ workflow เลือก model ตามงาน และ track token/seat cost ทุกเดือน ดูวิดีโอเต็มสำหรับ AI budget strategy

English translation: Meta กับ BlackRock ประกาศ data center 1GW มูลค่าพัฒนาเกือบ $14B เพื่อ AI นี่บอกว่า compute ยังแพงและสำคัญมาก SME ต้องคิดเรื่อง cost ต่อ workflow เลือก model ตามงาน และ track token/seat cost ทุกเดือน ดูวิดีโอเต็มสำหรับ AI budget strategy

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. Meta ลง $14B เพราะ AI กิน Compute →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short09 — ใช้ AI ต้องมี Vendor Inventory by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: ใช้ AI ต้องมี Vendor Inventory
English title: Build a Vendor Inventory
Hook type: Quick Tip
Source: https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/

## Script
ถ้าธุรกิจคุณใช้ plugin, chatbot, CRM, payment, ad account ให้ทำ vendor inventory วันนี้: ชื่อ tool, ข้อมูลที่เข้าถึง, admin คือใคร, update ล่าสุด, วิธีปิดฉุกเฉิน ข่าว AI zero-day ทำให้เรื่องนี้ไม่ใช่งาน IT เสริมอีกต่อไป ดูวิดีโอเต็มสำหรับ template

English translation: ถ้าธุรกิจคุณใช้ plugin, chatbot, CRM, payment, ad account ให้ทำ vendor inventory วันนี้: ชื่อ tool, ข้อมูลที่เข้าถึง, admin คือใคร, update ล่าสุด, วิธีปิดฉุกเฉิน ข่าว AI zero-day ทำให้เรื่องนี้ไม่ใช่งาน IT เสริมอีกต่อไป ดูวิดีโอเต็มสำหรับ template

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. ใช้ AI ต้องมี Vendor Inventory →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab

---

# Short10 — Agent Workflow ที่ดีมี 4 สิทธิ์ by Blaze
เขียนโดย Blaze / Written by: Blaze
Thai title: Agent Workflow ที่ดีมี 4 สิทธิ์
English title: 4 Permission Levels
Hook type: Quick Tip
Source: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Script
ออกแบบ AI agent ด้วย 4 permission: read-only, draft-only, write with approval, forbidden ตัวอย่าง ฝ่ายขายให้ AI อ่าน CRM และ draft follow-up ได้ แต่ส่งอีเมลต้อง approve ส่วนการลบข้อมูลกับโอนเงินคือ forbidden ดูวิดีโอเต็มผมสอน Agent Stack สำหรับ SME

English translation: ออกแบบ AI agent ด้วย 4 permission: read-only, draft-only, write with approval, forbidden ตัวอย่าง ฝ่ายขายให้ AI อ่าน CRM และ draft follow-up ได้ แต่ส่งอีเมลต้อง approve ส่วนการลบข้อมูลกับโอนเงินคือ forbidden ดูวิดีโอเต็มผมสอน Agent Stack สำหรับ SME

## Visual direction
Dan Martell/RPN: jump cuts, punch-in on numbers, bold kinetic Thai captions, yellow highlights for stats, red for warnings.

## Instagram carousel outline
1. Agent Workflow ที่ดีมี 4 สิทธิ์ →
2. Fresh news / exact number
3. Why Thai SMEs should care
4. 3-step workflow
5. Prompt/checklist
6. Risk / guardrail
7. CTA: ดูวิดีโอเต็ม @jeditrinupab