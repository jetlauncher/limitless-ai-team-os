# Limitless AI Team OS

ระบบตัวอย่างสำหรับสร้าง “ทีม AI Agent” แบบหลายตัว โดยใช้ Hermes Agent, Telegram bots, Obsidian memory, scheduled jobs และ platform integrations ต่าง ๆ

Repo นี้เป็น **เวอร์ชัน sanitized** ของระบบ agent ของ Jet/Jedi Trinupab มี role ของ agent, profile template, config example, วิธีติดตั้ง และ automation script แต่ **ไม่มี API key / token / secret จริง**

> English version: [README.md](README.md)

## ระบบนี้มีอะไรบ้าง

- **Kelly / Hermes** — Chief-of-Staff agent ดูแลภาพรวมและ approval gate
- **Signal** — AI research/search agent
- **Blaze** — Content/creative agent
- **Kaijeaw** — Thai voice/content agent
- **Zegna** — Taste/gadgets/brand scout
- **Bolt** — App/site/landing page builder
- **Qwen** — Local/private model worker
- **Protocol** — Newsletter/Beehiiv agent
- Obsidian memory workspace สำหรับ handoff ระหว่าง agent
- Telegram gateway setup สำหรับ bot แต่ละตัว
- Cron/scheduled job pattern
- Config example ที่นักเรียน copy ไปใส่ API key ของตัวเองได้

## โครงสร้าง repo

```text
agents/                 SOUL files + Obsidian workspace docs ของแต่ละ agent
configs/                Hermes config templates ที่ลบ secret แล้ว
examples/               ตัวอย่าง .env และ setup templates
docs/                   architecture, API key guide, operations manual
scripts/                script สำหรับ export/update/validate
.github/workflows/      optional GitHub Actions checks
```

## เริ่มใช้งานเร็ว ๆ

```bash
git clone git@github.com:jetlauncher/limitless-ai-team-os.git
cd limitless-ai-team-os
bash scripts/install-hermes.sh
cp examples/env/root.env.example ~/.hermes/.env
# จากนั้นใส่ API keys ของตัวเอง
```

อ่านคู่มือเต็ม: [INSTALL.th.md](INSTALL.th.md)

## ความปลอดภัย

Repo นี้ตั้งใจไม่เก็บสิ่งเหล่านี้:

- `.env` จริง
- API keys และ OAuth tokens
- Telegram bot tokens
- auth/session database
- logs
- chat/session transcripts
- ข้อมูลลูกค้า/นักเรียน
- ข้อมูลรายได้/payment

Config ทุกไฟล์ที่ commit จะเป็น example หรือ sanitized แล้วเท่านั้น

## Daily update automation

เครื่องจริงของ Jet มี scheduled job ที่ update repo นี้ทุกวัน โดยใช้:

```bash
scripts/export_sanitized_agent_system.py
scripts/validate_no_secrets.py
git commit && git push
```

นักเรียนไม่ควรรัน daily mirror job ถ้ายังไม่เข้าใจว่ามันอ่าน path ไหนและ sanitize อย่างไร
