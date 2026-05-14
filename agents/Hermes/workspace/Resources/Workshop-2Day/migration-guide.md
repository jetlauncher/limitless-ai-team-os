# 🚚 Migrate Your AI Team to a New Machine
### Student Guide — Limitless AI Team OS Workshop

You built your agent with me in class. This guide gets you moved to your own machine — or any future machine — without losing your work.

---

## What you're moving (the 5 things that matter)

Your Hermes agent is **just files**. Move these and you're done:

| # | What | Where it lives | Why it matters |
|---|---|---|---|
| 1 | **Core config** | `~/.hermes/` | Models, providers, tools, settings |
| 2 | **Skills** | `~/.hermes/skills/` | Your custom workflows |
| 3 | **Memory** | `~/.hermes/memory/` | What the agent remembers about you |
| 4 | **Credentials** | `~/.config/<service>/api_key` | API keys for OpenAI, Notion, Gamma, etc. |
| 5 | **Obsidian vault** | wherever you chose | Your notes + agent workspace |

That's it. No databases. No cloud lock-in. Just files.

---

## Part 1 — Back up the workshop machine (do this before you leave)

Run these commands in Terminal on the machine you used in class:

```bash
# 1. Pick a backup location (USB stick or iCloud Drive folder)
BACKUP=~/Desktop/hermes-backup-$(date +%Y%m%d)
mkdir -p "$BACKUP"

# 2. Copy your Hermes config + skills + memory
cp -R ~/.hermes "$BACKUP/hermes"

# 3. Copy your credentials folder
cp -R ~/.config "$BACKUP/config"

# 4. Copy your Obsidian vault (adjust path to yours)
cp -R "$HOME/Documents/Obsidian Vault" "$BACKUP/Obsidian-Vault"

# 5. Verify
ls -lh "$BACKUP"
du -sh "$BACKUP"
```

✅ You should see four folders and a total size between 50 MB and a few GB.

**Then zip it and put it somewhere safe:**

```bash
cd ~/Desktop
zip -r "hermes-backup-$(date +%Y%m%d).zip" "$(basename $BACKUP)"
```

Move the `.zip` to: iCloud Drive, Google Drive, a USB stick, or all three.

---

## Part 2 — Save your secrets separately (critical)

Your API keys are inside `~/.config/`. **Do not** post that folder to Slack, GitHub, or anywhere public.

Write down (in a password manager — 1Password, Apple Keychain, Bitwarden):

- [ ] OpenAI API key
- [ ] Anthropic API key (if you have one)
- [ ] OpenRouter API key (if you have one)
- [ ] Telegram bot token
- [ ] Notion integration token
- [ ] Any other connector keys (Gamma, Blotato, Airtable, Google, etc.)

If you ever lose the backup, you can re-paste these into `~/.config/<service>/api_key` on the new machine.

---

## Part 3 — Restore on your new machine

### Step 1 — Install Hermes first (clean install)

```bash
# macOS
brew install python node
curl -fsSL https://get.hermes.ai | bash    # or whatever install command we used in class

# Verify
hermes --version
```

### Step 2 — Restore your files

```bash
# Move your zip onto the new machine, then:
cd ~/Desktop
unzip hermes-backup-YYYYMMDD.zip

# Put everything back where it lives
cp -R hermes-backup-YYYYMMDD/hermes ~/.hermes
cp -R hermes-backup-YYYYMMDD/config/* ~/.config/
cp -R "hermes-backup-YYYYMMDD/Obsidian-Vault" ~/Documents/
```

### Step 3 — Test

```bash
hermes config       # should show your models and providers
hermes              # opens your agent — say hi
```

✅ Your agent should remember you and respond exactly like it did in class.

---

## Part 4 — Reconnect Telegram (if it stopped working)

Telegram bots are tied to a **token**, not a machine. Your bot moves with you. But if messages aren't arriving:

1. Open Hermes config: `hermes config`
2. Confirm the Telegram token is loaded
3. Send a message from your phone to your bot
4. If silent, regenerate the webhook:
   ```bash
   hermes telegram reset
   ```

If you want a *fresh* bot on the new machine (separate from class):
1. Talk to **@BotFather** → `/newbot`
2. Get the new token
3. Paste into `hermes config set telegram.token <new-token>`

---

## Part 5 — Verify the full team is alive

Run this checklist on the new machine:

- [ ] `hermes` opens and your agent replies in chat
- [ ] Your agent's **name and persona** match what you built in class
- [ ] Telegram receives a message from your phone
- [ ] At least one of your **skills** runs (`/skills` or ask the agent to use it)
- [ ] Your **cron job** is listed: `hermes cron list`
- [ ] Your **Obsidian vault** opens and contains your notes
- [ ] Each connector you set up still works (try one: Notion, Airtable, etc.)

If any item fails, see Troubleshooting below.

---

## Troubleshooting

**"Command not found: hermes"**
→ Hermes isn't installed yet. Run the install command (Part 3, Step 1).

**"Invalid API key" errors**
→ Your `~/.config/<service>/api_key` file might have an extra newline. Check it with:
```bash
cat -A ~/.config/openai/api_key
```
If you see `$` at the end on its own line, re-save the key without the trailing newline.

**Telegram silent on new machine**
→ Two machines polling the same bot fight each other. **Shut down Hermes on the old machine** (or revoke the old token in BotFather).

**Skills missing**
→ Make sure you copied `~/.hermes/skills/` and not just `~/.hermes/config/`. Re-run the restore step.

**Cron jobs not firing**
→ Cron schedules persist, but the new machine has to be on and awake. Confirm with `hermes cron list` and trigger one manually: `hermes cron run <job_id>`.

**Memory feels reset**
→ You only copied config, not memory. Make sure `~/.hermes/memory/` made it across.

---

## Best practices going forward

1. **Back up monthly.** Same commands as Part 1. Keep the last 3 backups.
2. **Use a password manager** for API keys — not text files on your desktop.
3. **Keep your Obsidian vault in iCloud or Dropbox** — automatic sync, no manual backup needed.
4. **When you add a new skill or connector, note it down** in `Daily/` so future-you knows what's wired up.
5. **Test your backup once.** Restore it to a different folder and run `hermes` from there — if it works, you're safe.

---

## TL;DR

> Four folders are your entire agent: `~/.hermes`, `~/.config`, your Obsidian vault, and your password manager. Copy those, install Hermes on the new machine, paste them back. Done.

---

*Built with you in the 2-Day Limitless AI Team OS Workshop.*
*— Jedi Trinupab · limitlessclub.co · @jeditrinupab*
