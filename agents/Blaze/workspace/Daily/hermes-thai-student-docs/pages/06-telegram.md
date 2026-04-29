# 06 — ใช้ Hermes ผ่าน Telegram

Hermes สามารถทำงานเป็น Telegram bot ได้ ทำให้เราคุยกับ agent จากมือถือได้

## ภาพรวมขั้นตอน

1. สร้าง bot ผ่าน BotFather
2. เอา bot token มาใส่ Hermes
3. ระบุว่าใครมีสิทธิ์คุยกับ bot
4. เปิด gateway
5. ทดลองส่งข้อความ

## Step 1: สร้าง bot กับ BotFather

ใน Telegram:

1. ค้นหา `@BotFather`
2. ส่งคำสั่ง:

```text
/newbot
```

3. ตั้งชื่อ bot
4. ตั้ง username ที่ลงท้ายด้วย `bot`
5. BotFather จะส่ง token ให้

ตัวอย่าง token:

[REDACTED]
123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
```

> ห้ามแชร์ token นี้ เพราะคนที่มี token สามารถควบคุม bot ได้

## Step 2: ตั้งค่าใน Hermes

ใช้คำสั่ง:

```bash
hermes gateway setup
```

เลือก Telegram แล้วใส่ token ตามขั้นตอน

## Step 3: เรื่อง User ID

Telegram user ID ไม่ใช่ username

Hermes ใช้ numeric user ID เพื่อกำหนดว่าใครมีสิทธิ์ใช้ bot

ถ้าใส่ผิด bot อาจไม่ตอบ หรือคนอื่นอาจใช้งานได้โดยไม่ตั้งใจ

## Step 4: ใช้ใน group

Telegram bot มี privacy mode

ถ้า privacy mode เปิดอยู่ bot จะเห็นเฉพาะ:

- command ที่ขึ้นต้นด้วย `/`
- ข้อความที่ reply หา bot
- service messages บางอย่าง

ถ้าอยากให้ bot เห็นทุกข้อความใน group:

- ไปที่ BotFather
- `/mybots`
- เลือก bot
- Bot Settings → Group Privacy → Turn off
- remove แล้ว add bot เข้า group ใหม่

## คำสั่งที่ควรตั้งใน bot menu

```text
help - Show help
new - Start a new conversation
sethome - Set this chat as home channel
```

## ใช้ Telegram ทำอะไรดี

- สั่งงานจากมือถือ
- ส่ง voice memo ให้ agent สรุป/ทำงานต่อ
- รับผล cron job เช่น briefing ทุกเช้า
- ใช้เป็น assistant ส่วนตัวหรือทีม
