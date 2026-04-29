# คู่มือติดตั้ง — Limitless AI Team OS

คู่มือนี้ช่วยให้นักเรียน clone ระบบ แล้วเปลี่ยน credential ทั้งหมดเป็นของตัวเอง

## 1. สิ่งที่ต้องมี

- macOS หรือ Linux
- Git
- Python 3.11+
- Telegram account
- GitHub account
- Optional: Ollama สำหรับ local model

## 2. ติดตั้ง Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor
```

## 3. Clone repo

```bash
git clone git@github.com:jetlauncher/limitless-ai-team-os.git
cd limitless-ai-team-os
```

ถ้ายังไม่ได้ตั้ง SSH ให้ใช้ HTTPS ได้

## 4. สร้าง root config

```bash
mkdir -p ~/.hermes
cp examples/env/root.env.example ~/.hermes/.env
cp configs/root/config.example.yaml ~/.hermes/config.yaml
chmod 600 ~/.hermes/.env
```

แล้วแก้ไฟล์:

```bash
nano ~/.hermes/.env
```

## 5. API keys ที่ต้องใช้

ขั้นต่ำเพื่อให้ระบบเริ่มทำงาน:

| Platform | ใช้ทำอะไร | Env var / file |
|---|---|---|
| OpenRouter หรือ OpenAI/Anthropic | model หลักของ agent | `OPENROUTER_API_KEY`, `OPENAI_API_KEY`, หรือ `ANTHROPIC_API_KEY` |
| Telegram BotFather | bot chat สำหรับแต่ละ agent | `TELEGRAM_BOT_TOKEN` ของแต่ละ profile |
| GitHub | sync repo และงาน code | `GITHUB_TOKEN` หรือ `gh auth login` |

แนะนำสำหรับระบบเต็ม:

| Platform | ใช้ทำอะไร | ที่เก็บที่แนะนำ |
|---|---|---|
| Notion | archive content / control room | `~/.config/notion/api_key` |
| Beehiiv | newsletter drafts | `~/.config/beehiiv/api_key` |
| Airtable | sales/revenue reporting | `~/.config/airtable/api_key` |
| Google Workspace | Gmail/Calendar/Drive | OAuth token path จาก setup ของคุณ |
| OpenAI Images | carousel generation | `~/.config/openai/api_key` |
| Higgsfield | image/video MCP | `HIGGSFIELD_MCP_TOKEN` |
| Blotato | social posting approval | `~/.config/blotato/api_key` |
| Ollama | local model worker | local server `127.0.0.1:11434` |

## 6. สร้าง Telegram bots

เปิด `@BotFather` ใน Telegram แล้วสร้าง bot แยกตาม agent:

- Kelly / Hermes
- Signal
- Blaze
- Kaijeaw
- Zegna
- Bolt
- Qwen
- Protocol

ตัวอย่างการสร้าง profile:

```bash
hermes profile create signal --clone-all
hermes profile alias signal --name signal
mkdir -p ~/.hermes/profiles/signal
cp examples/env/profile.env.example ~/.hermes/profiles/signal/.env
nano ~/.hermes/profiles/signal/.env
signal gateway start
signal gateway status
```

ใช้ SOUL file จาก `agents/<AgentName>/SOUL.md`

## 7. ตั้ง Obsidian memory

```bash
mkdir -p "$HOME/Documents/Obsidian Vault/Agents"
cp -R agents/* "$HOME/Documents/Obsidian Vault/Agents/"
```

## 8. Start gateways

```bash
hermes gateway start
signal gateway start
blaze gateway start
kaijeaw gateway start
zegna gateway start
bolt gateway start
protocol gateway start
```

Qwen ควร start หลังจากติดตั้ง Ollama และมี local model แล้ว

## 9. ตรวจสอบ

```bash
hermes profile list
hermes gateway status
signal gateway status
protocol gateway status
```

จากนั้นเปิด Telegram bot แต่ละตัว แล้วส่ง `/start` และ `/status`

## 10. Daily repo update job

ระบบของ Jet มี Hermes cron job ที่รัน `scripts/export_sanitized_agent_system.py` แล้ว push repo ทุกวัน ถ้าจะใช้เหมือนกัน ให้แก้ path ใน script ก่อน แล้วค่อยสร้าง cron job ของตัวเอง
