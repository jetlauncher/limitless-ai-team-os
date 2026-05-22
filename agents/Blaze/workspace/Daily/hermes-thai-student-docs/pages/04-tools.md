# 04 — Tools & Toolsets คืออะไร

Tools คือ “มือและตา” ของ Hermes

ถ้าไม่มี tools, Hermes จะตอบได้เหมือน chatbot ทั่วไป  
ถ้ามี tools, Hermes จะลงมือทำงานจริงได้

## ตัวอย่าง Tools

| หมวด | ใช้ทำอะไร |
|---|---|
| Web | ค้นเว็บ / อ่านหน้าเว็บ |
| Browser | เปิดเว็บแบบ interactive / คลิก / ดูภาพหน้าเว็บ |
| Terminal | รัน command ในเครื่องหรือ server |
| File | อ่านไฟล์ / เขียนไฟล์ / patch ไฟล์ |
| Memory | จำข้อมูลสำคัญระยะยาว |
| Session Search | ค้นบทสนทนาเก่า |
| Cron | ตั้งงานอัตโนมัติ |
| Image / Vision | วิเคราะห์ภาพ / สร้างภาพ |
| Delegation | แบ่งงานให้ sub-agent ช่วยคิดหรือทำ |

## Toolset คืออะไร

Toolset = กลุ่มของ tools

เช่น:

```bash
hermes chat --toolsets "web,terminal,file"
```

แปลว่าให้ session นี้ใช้เฉพาะ web + terminal + file

## ดู/ตั้งค่า tools

```bash
hermes tools
```

## ทำไมต้องจำกัด tools บางครั้ง

เพราะ tools เยอะเกินไปอาจทำให้:

- context หนัก
- agent สับสนว่าควรใช้อะไร
- มีความเสี่ยงด้าน security มากขึ้น

สำหรับนักเรียน แนะนำเริ่มจาก:

```text
web, terminal, file, memory, skills
```

แล้วค่อยเปิด browser / image / cron เมื่อจำเป็น

## กฎความปลอดภัย

อย่าให้ Hermes ทำคำสั่งที่อันตรายโดยไม่เข้าใจ เช่น:

```bash
rm -rf /
```

หรือ command ที่ลบไฟล์จำนวนมาก / ส่ง secret / deploy production

จำไว้:

> Agent เก่งขึ้นเมื่อมี tools  
> แต่ความรับผิดชอบของคนสั่งก็สูงขึ้นด้วย
