# ใช้ AI ยังไงให้ไม่ชนลิมิตอีก

## Cheat Sheet 1 หน้า สำหรับ Founder ที่อยากใช้ Claude, ChatGPT และทีม AI ให้คุ้มกว่าเดิม

**ปัญหาจริงไม่ใช่ “ลิมิตน้อย” แต่คือ “workflow ยังไม่เป็นระบบ”**  
คนส่วนใหญ่ใช้โควต้า AI หมดเร็ว เพราะใช้โมเดลแพงเร็วเกินไป, คุยในแชทยาว ๆ อันเดียว, อธิบายบริบทซ้ำ, และพยายามให้ AI ตัวเดียวทำทุกอย่าง

### 1. วางแผนด้วยโมเดลถูก แล้วค่อย execute ด้วยโมเดลแพง
ใช้โมเดลเร็ว/ถูกเพื่อเคลียร์โจทย์ก่อน แล้วค่อยส่ง brief ที่ชัดให้โมเดลที่เก่งที่สุดทำงานจริง

**Prompt:** “ช่วยสัมภาษณ์ฉันเรื่องเป้าหมาย กลุ่มเป้าหมาย ข้อจำกัด ตัวอย่าง และ output ที่ต้องการ แล้วสรุปเป็น brief 1 หน้า”

### 2. อย่าใช้แชทยักษ์อันเดียวตลอดชีวิต
แชทยาวทำให้ AI ต้องอ่านบริบทเก่า ๆ ซ้ำ ใช้ token มากขึ้น และคุณภาพตกลง ใช้ Project/Folder และเปิดแชทใหม่สำหรับงานใหม่

**Prompt:** “สรุปบทสนทนานี้เป็น handoff prompt สั้น ๆ เพื่อเอาไปเริ่มแชทใหม่โดยไม่เสีย context”

### 3. ให้ AI มี memory นอกแชท
สร้างไฟล์ง่าย ๆ 3 ไฟล์:
- Founder Profile — คุณคือใคร โทนเสียง ความชอบ
- Business Context — สินค้า offer ลูกค้า proof เป้าหมาย
- AI Operating Rules — รูปแบบคำตอบ โทน approval gates สิ่งที่ไม่ชอบ

### 4. เลือกโมเดลเหมือนผู้จัดการเลือกคนทำงาน
- Cheap/local model: brainstorm, summarize, clean notes
- Strong model: draft, analyze, create options
- Best model: final strategy, high-stakes writing, complex reasoning

ถามตัวเองเสมอ: **“ขั้นตอนนี้ใช้โมเดลที่ถูกที่สุดตัวไหนแล้วงานยังดีพอ?”**

### 5. แยกเครื่องมือตามงาน
Gamma สำหรับสไลด์, Notion/Obsidian สำหรับ memory, web agents สำหรับ research, Claude Code/Codex/Bolt สำหรับ build, Qwen/local models สำหรับงาน private draft

### 6. ใช้ low-effort / concise mode เป็นค่า default
งานสรุป จัด format ดึง action items หรือทำให้สั้น ไม่จำเป็นต้องใช้ deep reasoning ทุกครั้ง

**Prompt:** “ตอบให้กระชับ ฉันกำลัง optimize การใช้ token ถ้าแชทนี้เริ่มยาวเกินไป ให้บอกฉันให้เปิดแชทใหม่”

### 7. เปลี่ยน prompt ที่ใช้ซ้ำให้เป็นระบบ
ถ้าใช้ prompt เดิมเกิน 3 ครั้ง ให้ทำเป็น template, project instruction, skill หรือ automation

## Checklist 5 ข้อก่อนสั่ง AI ทุกครั้ง
1. ฉันต้องการ output อะไร?  
2. AI ต้องรู้อะไรบ้างถึงจะทำงานได้ดี?  
3. โมเดล/เครื่องมือไหนถูกที่สุดแต่ดีพอ?  
4. งานนี้ควรเปิดแชทใหม่ไหม?  
5. workflow นี้ควรเก็บเป็น template ไหม?

**สรุป:** อย่าใช้ AI เหมือนกล่องข้อความวิเศษ ให้ใช้เหมือน Operating System: วางแผนด้วยของถูก, execute ด้วยของแพง, เก็บ memory ให้ดี, ส่งงานให้ specialist ที่ถูกตัว, และทำ workflow ซ้ำให้เป็นระบบ
