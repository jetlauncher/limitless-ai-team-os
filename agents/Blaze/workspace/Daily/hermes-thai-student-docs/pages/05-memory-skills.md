# 05 — Memory และ Skills

สองอย่างนี้คือสิ่งที่ทำให้ Hermes แตกต่างจาก chatbot ธรรมดา

## Memory คืออะไร

Memory คือความจำระยะยาวของ agent

Hermes เก็บ memory หลักไว้ใน:

```text
~/.hermes/memories/
```

โดยมี 2 ส่วนสำคัญ:

| ไฟล์ | ใช้จำอะไร |
|---|---|
| MEMORY.md | สิ่งที่ agent เรียนรู้เกี่ยวกับ environment / workflow |
| USER.md | preference ของผู้ใช้ เช่น ชอบคำตอบสั้น ชอบภาษาไทย |

## ตัวอย่าง memory ที่ดี

```text
User prefers Thai explanations for student-facing materials.
```

```text
Project X uses Next.js and deploys through Vercel.
```

## ตัวอย่าง memory ที่ไม่ควรเก็บ

- API key
- password
- token
- task ชั่วคราวที่ใช้ครั้งเดียว
- ข้อมูล private ที่ไม่จำเป็น

## Skills คืออะไร

Skill คือคู่มือเล็กๆ ที่ Hermes โหลดมาใช้เมื่อเจองานเฉพาะ

ตัวอย่าง:

- skill สำหรับ review code
- skill สำหรับเขียน content
- skill สำหรับใช้ GitHub
- skill สำหรับสร้าง slide
- skill สำหรับ debug แบบเป็นระบบ

## ใช้ skill ยังไง

ใน CLI หรือ chat platform:

```text
/plan ช่วยวางแผนสร้าง MVP สำหรับระบบ booking
```

หรือ:

```text
/github-pr-workflow ช่วยสร้าง PR จาก branch นี้
```

## ทำไม Skills สำคัญ

เพราะ skills ทำให้ agent ไม่ต้องเริ่มจากศูนย์ทุกครั้ง

ถ้ามี workflow ที่ใช้ซ้ำบ่อย เช่น “สรุปข่าว AI เป็นภาษาไทยทุกเช้า” เราควรทำเป็น skill ได้

## สรุปสั้นๆ

- Memory = จำข้อมูลระยะยาว
- Skills = จำวิธีทำงาน
- Session history = จำบทสนทนาเก่า

ถ้านักเรียนเข้าใจ 3 อย่างนี้ จะเข้าใจ AI Agent ลึกกว่าแค่ prompt engineering
