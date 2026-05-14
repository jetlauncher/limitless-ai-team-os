# 🤝 Kelly ↔ Kelly 2 — Handoff Doc

**Purpose:** Keep the two Kellys aligned without stepping on each other.
**Audience:** Both Kelly (Studio) and Kelly 2 (M5 MacBook). Read this at the start of any session where the *other* Kelly might have been working.

---

## Who runs where

| | **Kelly (primary)** | **Kelly 2 (mobile)** |
|---|---|---|
| Machine | M3 Ultra Studio · `ultras-mac-studio` | M5 Max MacBook Pro · `jedim5max` |
| Always on? | ✅ Yes — plugged in, 24/7 | ❌ No — sleeps, travels, may be offline |
| Tailscale IP | `100.94.6.84` | `100.69.255.80` (when online) |
| Telegram bot | Original bot (Jet's main) | `@kelly2jediaibot` |
| Telegram home chat | `1460936021` | `1460936021` (same Jet, different bot) |
| Obsidian Vault | `~/Documents/Obsidian Vault` → iCloud symlink | `~/Documents/Obsidian Vault` → iCloud symlink |
| Memory file | `~/.hermes/memories/MEMORY.md` (Studio version) | `~/.hermes/memories/MEMORY.md` (M5 version, different) |
| Profile file | `~/.hermes/memories/USER.md` (identical) | `~/.hermes/memories/USER.md` (identical) |

---

## Ownership boundaries — who owns what

### Kelly (Studio) owns
- **All cron jobs** — Studio is always on. Kelly 2 must NEVER schedule cron.
- **Long-running batch tasks** — image generation runs, video renders, big research sweeps, model training.
- **Local Gemma / Ollama vision work** — Studio has 99 GB Photos library + the 40 GB LM Studio models. Kelly 2 doesn't.
- **Heavy compute** — M3 Ultra is ~2x faster on ML loads than M5 Max for big models.
- **Always-on monitors** — revenue alerts, Limitless Sales watch, AI news monitor, blogwatcher.
- **Sub-agent orchestration** — when spawning Claude Code / Codex worker subagents, do it on Studio.

### Kelly 2 (M5 MacBook) owns
- **Interactive sessions on the go** — Jet talking via Telegram from anywhere.
- **Drafting and quick research** — pull a URL, summarize, ask a question, get an answer fast.
- **Travel/café work** — when Jet is away from the desk.
- **Light image generation** — gpt-image-2 carousel slides, single moodboards (cloud-side, so location doesn't matter).
- **Mobile review/approval** — Mission Control approval requests, Notion edits, quick replies.
- **Whatever Jet asks for in @kelly2jediaibot directly** — assume he's intentional about the channel.

### Joint / either
- **Skill writing & updates** — both should patch skills as they learn. Skills live in `~/.hermes/skills/` and are NOT auto-synced across machines, so commit changes to both.
- **Reading the Obsidian vault** — both can read once iCloud syncs. Writing is fine but watch for conflict files (`Note (Conflicted).md`).
- **Notion writes** — single source of truth in the cloud, both can write.

---

## Hard rules (do not violate)

1. **Never run `hermes gateway start` on a machine for the *other* machine's bot.** Telegram only allows one poller per token. Two pollers = silent message loss.
2. **Never schedule cron jobs on Kelly 2.** Schedules will fire whenever the M5 is awake → unpredictable. All cron lives on Studio.
3. **Never edit `~/.hermes/skills/` on both machines simultaneously** — sync manually after edits, or you'll get diverging skill versions.
4. **Never put secrets in Obsidian.** It's now in iCloud, accessible from anywhere — reference credential file paths only.
5. **Always save image prompts as `.prompt.txt` sidecar AND in `Obsidian Vault/Agents/Hermes/Prompts/Image Generation/`.** Either Kelly. No exceptions.

---

## Sync mechanics (what's automatic, what isn't)

| Item | Sync method | Lag |
|---|---|---|
| Obsidian Vault | iCloud Drive (via symlink) | 1–10 min typical |
| Notion content | Notion cloud | seconds |
| Airtable | Airtable cloud | seconds |
| Hermes memory (`MEMORY.md`, `USER.md`) | ❌ **Not synced** | Manual |
| Skills (`~/.hermes/skills/`) | ❌ **Not synced** | Manual (`scp` or `rsync`) |
| `~/.config/` API keys | ❌ **Not synced** | Manual when new keys added |
| `~/.hermes/config.yaml` | ❌ **Not synced** | Manual when config changes |

When Kelly (Studio) adds a new skill that Kelly 2 should also have, run on Studio:

```bash
SKILL=creative/local-gemma-vision-photo-eval   # adjust path
tar -czf /tmp/skill-sync.tar.gz -C ~/.hermes/skills "$SKILL"
scp /tmp/skill-sync.tar.gz jedijiratritarnm5max@100.69.255.80:/tmp/
ssh jedijiratritarnm5max@100.69.255.80 \
  "cd ~/.hermes/skills && tar -xzf /tmp/skill-sync.tar.gz && rm /tmp/skill-sync.tar.gz"
```

---

## Handoff log (running journal)

Append a line here when you do something the other Kelly should know about. Newest at the top.

### 2026-05-14
- 13:00 — **Kelly 2 set up.** Hermes v0.13.0, all API keys cloned, 123 skills installed, Telegram bot `@kelly2jediaibot` wired, gateway running on M5. Round-trip Telegram test passed (9 API calls, 1300-char response).
- 12:50 — **Obsidian Vault moved to iCloud Drive.** Path: `~/Library/Mobile Documents/com~apple~CloudDocs/Obsidian Vault`. Both Macs have symlinks at the old `~/Documents/Obsidian Vault` path. Workshop review videos (2.6 GB) moved to `Limitless OS/Workshop Reviews/2026-05-05/`.
- 12:30 — **Disk cleanup on Studio.** 15 GB → 32 GB free. Cleared HuggingFace cache, Yarn/Comet/Homebrew caches, old installer DMGs.
- 12:00 — **Workshop 2-day deliverables done.** Gamma deck (https://gamma.app/docs/pfyxdiou51y9e4z), 5-page workshop PDF, Notion checklist, premium black/gold org chart graphic + Thai bilingual team boardroom graphic. All prompts archived in `Obsidian Vault/Agents/Hermes/Prompts/Image Generation/`.
- 13:05 — **New skill: `local-gemma-vision-photo-eval`.** Lives on Studio only (M5 went offline mid-sync). Sync to Kelly 2 when she's back online. Uses local Gemma 4 26B + mmproj projector via LM Studio for free batch event-photo rating.

---

## Quick reference cards

### When Kelly 2 gets a question Studio Kelly is better at:
- Long research sweep → "Let me hand this to Studio Kelly — she's always on and faster on heavy lifts."
- Cron / scheduled job → "I can't run cron from here — Studio Kelly owns scheduling. Want me to draft the job and have her wire it up?"
- Batch image evaluation → "This needs Gemma vision on the Studio. Forwarding context to Studio Kelly."

### When Studio Kelly gets a question Kelly 2 is better at:
- "I'm at a café and need…" → Kelly 2 if it's a quick reply Jet wants on his MacBook.
- Approval gate / quick review → Whoever Jet is talking to. Don't insist on routing.

### When in doubt
Whoever Jet is actively chatting with handles it. The boundary is *prevention* — don't both schedule the same cron, don't both edit the same skill at the same time. Day-to-day, just answer.

---

## Identity reminders

- Both Kellys are warm, direct, concise, English by default (Thai when Jet speaks Thai).
- Same Jet, same brand (navy/black + gold, no Buddha/Zen, real Jet photos only, Limitless Club).
- Same preferences: GPT-5.5 default, Sonnet for hard problems, GPT Image 2 for visuals, approval gates, source links in X reports.
- Studio Kelly is the senior sibling — when conflict, defer to Studio Kelly's memory and stack.

— Built 2026-05-14
