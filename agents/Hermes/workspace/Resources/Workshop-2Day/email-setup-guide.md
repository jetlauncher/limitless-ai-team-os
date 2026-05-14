# 📧 Email Setup for Your Hermes Agent
### Student Guide — Limitless AI Team OS Workshop

This guide shows you how to connect your email to your Hermes agent so it can read, search, draft, and send mail for you.

There are **two paths** depending on your email provider. Pick yours:

| If your email is… | Use this path | Time |
|---|---|---|
| **Gmail / Google Workspace** | Path A — Google OAuth | 10 min one-time |
| **Outlook / Office 365 / Yahoo / iCloud / IMAP** | Path B — Himalaya CLI | 5 min |
| **Both** | Do both — they coexist | 15 min |

---

# PATH A — Gmail / Google Workspace (OAuth)

This connects Gmail, Calendar, Drive, Sheets, Docs, and Contacts all at once. One-time setup, then your agent has full access until you revoke it.

## Step 1 — Decide what your agent should access

Before clicking anything, decide:

- 📧 Just **email**? → You can skip OAuth entirely and use Path B (Himalaya). It's simpler.
- 📧 + 📅 **Email + Calendar**? → Continue here.
- 📅 📁 **Calendar + Drive + Sheets + Docs**? → Continue here.
- 🌐 **Everything (full Workspace)**? → Continue here.

## Step 2 — Create a Google Cloud project (one-time, free)

You only do this once per Google account. After this, the agent reuses the same project forever.

1. Open: **https://console.cloud.google.com/projectselector2/home/dashboard**
2. Click **"Create Project"** at the top right
3. Name it anything — `Hermes Agent` is a clean default
4. Click **Create** and wait ~30 seconds for it to be ready
5. Make sure that project is **selected** in the top bar (it'll show the project name)

## Step 3 — Enable the APIs

Open this URL — it's the API Library:
**https://console.cloud.google.com/apis/library**

Search and **enable** each of these APIs (click the API → Enable):

- **Gmail API**
- **Google Calendar API**
- **Google Drive API**
- **Google Sheets API**
- **Google Docs API**
- **People API** (for Contacts)

Each one takes 10 seconds. Enable only what you'll actually use to keep the consent screen short.

## Step 4 — Configure the OAuth consent screen

1. Open: **https://console.cloud.google.com/auth/overview**
2. If it asks, choose **External** user type → Create
3. Fill in:
   - **App name:** `Hermes Agent` (or whatever)
   - **User support email:** your email
   - **Developer contact:** your email
4. Click **Save and Continue** through the next screens (you don't need to add scopes here — Hermes asks for them at login time)
5. On the **Test users** screen, click **Add Users** → enter your own Google email
6. Save

⚠️ **Critical:** If you skip the test user step, you'll get `Error 403: access_denied` later.

## Step 5 — Create the OAuth client (the credentials file)

1. Open: **https://console.cloud.google.com/apis/credentials**
2. Click **+ Create Credentials** → **OAuth client ID**
3. Application type: **Desktop app**
4. Name: `Hermes Desktop Client`
5. Click **Create**
6. A popup shows your Client ID — click **Download JSON** and save the file
7. Note where it saved (usually `~/Downloads/client_secret_xxxxx.json`)

## Step 6 — Hand the JSON to Hermes

In your Hermes chat (Telegram or CLI), tell your agent:

> *"I just downloaded my Google OAuth client_secret JSON. The file is at: /Users/yourname/Downloads/client_secret_xxxxx.json. Please run the Google Workspace setup."*

Your agent will run:

```bash
python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py \
  --client-secret /path/to/your/client_secret.json
```

Then it'll generate an **authorization URL** and send it back to you.

## Step 7 — Authorize in the browser

1. Click the URL the agent sent
2. Pick your Google account
3. If you see a "Google hasn't verified this app" screen → click **Advanced** → **Go to Hermes Agent (unsafe)**. This is normal for personal projects.
4. Click **Allow** on every permission screen
5. The browser will redirect to a page that says **"This site can't be reached"** or `localhost refused to connect` — **this is expected and correct**
6. **Copy the entire URL from your browser's address bar** — it'll look like:
   `http://localhost:1/?code=4/0A...&scope=...`

## Step 8 — Paste the URL back to Hermes

Send the full URL back to your agent. It'll finish the exchange and confirm:

> ✅ AUTHENTICATED — Gmail, Calendar, Drive, Sheets, Docs ready

That's it. Token is saved at `~/.hermes/google_token.json` and **auto-refreshes forever**. You never need to repeat this.

## Test it

Ask your agent:

> *"Check my unread Gmail from the last 24 hours."*

If it returns a list, you're done.

---

# PATH B — Outlook, Office 365, Yahoo, iCloud, any IMAP

Use this for any non-Google email. Works with **app passwords** or OAuth depending on provider.

## Step 1 — Install Himalaya (one-time)

In Terminal:

```bash
# macOS
brew install himalaya

# Or universal (Linux/macOS)
curl -sSL https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh | PREFIX=~/.local sh
```

Verify:
```bash
himalaya --version
```

## Step 2 — Get an app password (don't use your regular password)

Modern email providers won't accept your normal password for third-party apps. You need an **app password** — a special password just for Hermes.

### For Outlook / Office 365 / Hotmail

1. Open: **https://account.microsoft.com/security**
2. Sign in → click **Advanced security options**
3. Under **App passwords**, click **Create a new app password**
4. Copy the 16-character password (no spaces) and save it somewhere safe (password manager!)

⚠️ Microsoft app passwords require **2-step verification** to be on. Enable it first if you haven't.

### For Yahoo

1. Open: **https://login.yahoo.com/account/security**
2. Click **Generate app password**
3. Name it `Hermes` → Generate
4. Copy and save the 16-character password

### For iCloud Mail

1. Open: **https://account.apple.com/account/manage** → Sign in
2. **Sign-In and Security** → **App-Specific Passwords**
3. Click **Generate Password** → label it `Hermes`
4. Copy and save the password

### For any other IMAP provider

Check their docs for "app password" or "application-specific password." Almost all major providers (FastMail, ProtonMail Bridge, Zoho, GMX, etc.) support them.

## Step 3 — Find your IMAP / SMTP server settings

Common ones:

| Provider | IMAP host | IMAP port | SMTP host | SMTP port |
|---|---|---|---|---|
| Outlook / Hotmail | `outlook.office365.com` | 993 | `smtp.office365.com` | 587 |
| Office 365 (work) | `outlook.office365.com` | 993 | `smtp.office365.com` | 587 |
| Yahoo | `imap.mail.yahoo.com` | 993 | `smtp.mail.yahoo.com` | 587 |
| iCloud | `imap.mail.me.com` | 993 | `smtp.mail.me.com` | 587 |
| FastMail | `imap.fastmail.com` | 993 | `smtp.fastmail.com` | 587 |
| Zoho | `imap.zoho.com` | 993 | `smtp.zoho.com` | 587 |

For other providers, search **"<provider name> IMAP settings"**.

## Step 4 — Tell Hermes to set up Himalaya

In your Hermes chat, give it everything in one message:

> *"Set up Himalaya for my Outlook email.*
> *Email: yourname@outlook.com*
> *App password: [REDACTED]
> *IMAP host: outlook.office365.com*
> *SMTP host: smtp.office365.com"*

Your agent will create `~/.config/himalaya/config.toml` with the right structure. You can also do it manually — see the template below.

## Step 5 — Manual config (if you prefer)

Create `~/.config/himalaya/config.toml`:

```toml
[accounts.personal]
email = "you@outlook.com"
display-name = "Your Name"
default = true

backend.type = "imap"
backend.host = "outlook.office365.com"
backend.port = 993
backend.encryption.type = "tls"
backend.login = "you@outlook.com"
backend.auth.type = "password"
backend.auth.raw = "your-16-char-app-password"

message.send.backend.type = "smtp"
message.send.backend.host = "smtp.office365.com"
message.send.backend.port = 587
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "you@outlook.com"
message.send.backend.auth.type = "password"
message.send.backend.auth.raw = "your-16-char-app-password"

folder.aliases.inbox = "INBOX"
folder.aliases.sent = "Sent"
folder.aliases.drafts = "Drafts"
folder.aliases.trash = "Deleted"
```

🔒 **Better security:** instead of `auth.raw` (plain text password in the file), use a password manager:

```toml
backend.auth.cmd = "security find-generic-password -a outlook-app -w"  # macOS Keychain
```

Or use `pass`, `1Password CLI`, etc. Ask your agent — they'll help you set it up.

## Step 6 — Test it

In your Hermes chat:

> *"List my latest 5 Outlook emails."*

Your agent will run `himalaya envelope list` and show you the list. Done.

---

# Multiple email accounts (advanced)

You can have **Gmail + Outlook + iCloud all at once**. Each in its own configuration:

- Gmail OAuth → `~/.hermes/google_token.json` (or scoped under `~/.hermes/google-accounts/<label>/` for multiple Google accounts)
- Himalaya accounts → add more `[accounts.work]`, `[accounts.personal]` blocks to the config

To use a specific Himalaya account:
```bash
himalaya --account work envelope list
```

Tell your agent the account name when you ask, e.g. *"Search my work Outlook inbox for invoices."*

---

# Common problems & fixes

| Problem | Fix |
|---|---|
| Google: `Error 403: access_denied` | You forgot to add yourself as a test user in Step 4. Go back to the OAuth consent screen and add your email. |
| Google: `Google hasn't verified this app` warning | Normal — click **Advanced → Go to (unsafe)**. You're the developer of the app. |
| Google: `redirect_uri_mismatch` | You picked the wrong app type. Re-do Step 5 and pick **Desktop app**, not Web. |
| Google: `localhost refused to connect` after Allow | Expected. Copy the URL from the address bar anyway and paste back to Hermes. |
| Outlook: `Authentication failed` | You used your real password. Outlook requires an **app password** — go back to Step 2. |
| Outlook: app password option missing | Turn on **2-step verification** first at account.microsoft.com/security. App passwords require it. |
| Yahoo: `Less secure apps` error | Yahoo now requires app passwords too — same fix as Outlook. |
| iCloud: `Authentication failed` | iCloud app passwords look like `abcd-efgh-ijkl-mnop`. Include the dashes when pasting. |
| Himalaya: `missing field accounts` | Your config uses old `[[account]]` syntax. New version wants `[accounts.NAME]` (singular `s`, dot, name). |
| Himalaya: duplicates sent | Folder alias is wrong. Make sure you use `folder.aliases.sent = "..."` (plural, dotted), not the old `[accounts.NAME.folder.alias]` block. |

---

# Security checklist (read before sending OAuth/passwords anywhere)

- ✅ **Never** paste your real Google password to anyone, ever.
- ✅ **Never** paste an app password in a public chat. Use a password manager.
- ✅ The `client_secret.json` from Google is **not actually secret** for desktop apps — but treat it carefully anyway.
- ✅ Don't commit `~/.hermes/google_token.json`, `~/.config/himalaya/config.toml`, or any `.env` files to git.
- ✅ When you stop using Hermes on a machine, **revoke**:
  - Google: `python ~/.hermes/skills/productivity/google-workspace/scripts/setup.py --revoke`
  - Outlook/Yahoo/iCloud: delete the app password from your account security settings

---

# Quick reference — once setup is done, your agent can:

**Gmail (via Path A):**
- "Show me unread email from this week"
- "Search Gmail for invoices in the last 30 days"
- "Reply to the last email from Sarah saying I'll be there Thursday at 3pm"
- "Star all customer emails from May"

**Outlook / IMAP (via Path B):**
- "List my Outlook inbox"
- "Search work email for messages from my CFO last month"
- "Send an email to client@example.com with subject Quarterly Review and body…"
- "Move all newsletter emails from this week to the Archive folder"

---

*From the 2-Day Limitless AI Team OS Workshop.*
*— Jedi Trinupab · limitlessclub.co · @jeditrinupab*
