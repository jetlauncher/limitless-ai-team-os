# 09 — Hermes Cheat Sheet สำหรับนักเรียน

## คำสั่งติดตั้ง

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

## เริ่มใช้งาน

```bash
hermes
```

## เลือก model/provider

```bash
hermes model
```

## ตั้งค่า tools

```bash
hermes tools
```

## ดู config

```bash
hermes config
```

## แก้ config

```bash
hermes config edit
```

## ตั้งค่า gateway เช่น Telegram

```bash
hermes gateway setup
```

## ตั้ง cron job

```bash
hermes cron create "every 2h" "Check server status"
```

## คุยครั้งเดียวแบบไม่เปิด interactive

```bash
hermes chat -q "อธิบาย Hermes Agent แบบง่าย"
```

## ระบุ toolsets

```bash
hermes chat --toolsets "web,terminal,file" -q "ช่วยดูโฟลเดอร์นี้และสรุป project"
```

## เรียกใช้ skill

```text
/plan ช่วยวางแผนสร้าง AI assistant สำหรับร้านอาหาร
```

## Prompt template

```text
เป้าหมาย:
บริบท:
ข้อมูลที่มี:
ข้อจำกัด:
รูปแบบผลลัพธ์:
ภาษาที่ต้องการ:
```

## สิ่งที่ควรจำ

- ทำให้ chat ปกติใช้งานได้ก่อน ค่อยเพิ่ม feature
- อย่าใส่ secret ลง memory หรือ prompt โดยไม่จำเป็น
- ถ้าจะตั้ง cron ให้เขียน prompt แบบ self-contained
- ถ้างานซ้ำบ่อย ให้ทำเป็น skill
- ถ้าใช้ Telegram group ให้ระวัง privacy mode
