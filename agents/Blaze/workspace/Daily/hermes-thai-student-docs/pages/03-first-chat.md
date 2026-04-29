# 03 — เริ่มคุยกับ Hermes ครั้งแรก

หลังติดตั้งแล้ว ให้ทำตามลำดับนี้

## Step 1: เลือก Provider / Model

รัน:

```bash
hermes model
```

Provider คือที่ที่ Hermes จะส่งคำถามไปให้ LLM ประมวลผล เช่น:

- Nous Portal
- OpenRouter
- OpenAI
- Anthropic
- Google/Gemini ผ่าน compatible provider
- Local model เช่น Ollama / vLLM / llama.cpp

## คำแนะนำสำหรับผู้เริ่มต้น

ถ้ายังไม่รู้จะเลือกอะไร:

- อยากง่าย: ใช้ Nous Portal หรือ OpenRouter
- มี API key ของ OpenAI/Anthropic อยู่แล้ว: ใช้ provider นั้น
- อยากใช้ local/private: ใช้ Ollama หรือ custom OpenAI-compatible endpoint

## Step 2: เริ่ม chat

```bash
hermes
```

แล้วลองพิมพ์:

```text
สวัสดี ช่วยอธิบายว่า Hermes Agent ทำอะไรได้บ้างแบบง่ายๆ
```

## Step 3: ทดสอบว่า tools ใช้งานได้ไหม

ลองถาม:

```text
ช่วยเช็กเวลาปัจจุบันของเครื่องนี้ให้หน่อย
```

ถ้าเปิด terminal tool อยู่ Hermes ควรใช้ command เช็กเวลา ไม่ใช่เดาเอง

## Step 4: อย่าเพิ่ม feature เยอะเกินไปเร็วเกินไป

หลักสำคัญ:

> ทำให้ chat ปกติใช้งานได้ก่อน  
> แล้วค่อยเพิ่ม Telegram, cron, skills, voice, routing

ถ้าพื้นฐานยังไม่ผ่าน อย่าเพิ่งตั้ง bot หรือ automation

## รูปแบบ prompt ที่ดี

ไม่ดี:

```text
ช่วยทำ project ให้หน่อย
```

ดีกว่า:

```text
ช่วยสร้าง landing page ง่ายๆ สำหรับคอร์ส AI ภาษาไทย
กลุ่มเป้าหมายคือเจ้าของธุรกิจ SME
อยากได้ tone เรียบง่าย premium
ขอเป็นไฟล์ HTML/CSS ในโฟลเดอร์นี้
```

## สูตรสั่งงานง่ายๆ

ใช้โครงนี้:

```text
เป้าหมาย:
บริบท:
ข้อจำกัด:
ผลลัพธ์ที่ต้องการ:
รูปแบบไฟล์/format:
```
