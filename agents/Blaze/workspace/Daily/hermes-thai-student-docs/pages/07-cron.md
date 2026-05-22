# 07 — ตั้งงานอัตโนมัติด้วย Cron

Cron คือระบบตั้งเวลาให้ Hermes ทำงานเอง

ตัวอย่าง:

- ทุกเช้า 9 โมง สรุปข่าว AI ให้ฉัน
- ทุก 2 ชั่วโมง เช็ก status server
- ทุกวันศุกร์ สรุปงานที่ค้าง
- อีก 30 นาที เตือนให้ดู build

## วิธีสั่งผ่าน chat

ใน Hermes chat หรือ platform ที่รองรับ:

```text
Every morning at 9am, check AI news and send me a short Thai summary on Telegram.
```

หรือใช้ slash command:

```bash
/cron add 30m "Remind me to check the build"
/cron add "every 2h" "Check server status"
```

## ใช้ผ่าน CLI

```bash
hermes cron create "every 2h" "Check server status"
```

## Cron + Skills

ถ้างานซ้ำต้องใช้วิธีเฉพาะ สามารถแนบ skill ได้

```bash
hermes cron create "every 1h" "Summarize new feed items" --skill blogwatcher
```

## ข้อควรระวัง

Cron job จะรันใน session ใหม่

ดังนั้น prompt ต้องเขียนให้ครบ ไม่ใช่อ้างอิงว่า “ทำเหมือนเมื่อกี้” เพราะ session ใหม่อาจไม่มี context เดิม

ไม่ดี:

```text
ทำอันเดิมทุกวัน
```

ดี:

```text
ทุกวันเวลา 9:00 ให้ค้นข่าว AI สำคัญ 5 ข่าวล่าสุดจากแหล่งที่น่าเชื่อถือ สรุปเป็นภาษาไทยแบบ bullet และส่งกลับมาที่ Telegram นี้
```

## หลักการเขียน cron prompt

ใส่ให้ครบ:

- ต้องทำอะไร
- แหล่งข้อมูลมาจากไหน
- format ผลลัพธ์
- ภาษาอะไร
- ส่งผลลัพธ์ไปที่ไหน
- ต้องหลีกเลี่ยงอะไร

## สำคัญ

Cron-run session ไม่ควรสร้าง cron job ซ้อนเอง เพื่อป้องกัน loop งานอัตโนมัติที่ควบคุมยาก
