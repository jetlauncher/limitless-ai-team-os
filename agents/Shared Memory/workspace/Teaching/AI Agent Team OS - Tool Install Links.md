# AI Agent Team OS - Tool Install Links

Use this page as the student setup checklist for the tools used in an AI Agent Team OS.

Students do **not** need every tool on day one. Start with the essentials, then add optional integrations as needed.

---

## 1. Essentials for everyone

### Hermes Agent

- Install/docs: https://hermes-agent.nousresearch.com/docs
- GitHub: https://github.com/NousResearch/hermes-agent
- Purpose: main agent framework, profiles, tools, memory, cron jobs, messaging gateway.

Mac/Linux quick install:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor
hermes setup
```

### Obsidian

- Download: https://obsidian.md/download
- Purpose: human-readable memory workspace for agents.

Recommended folder:

```text
~/Documents/Obsidian Vault/Agents/
```

### Git

- Download: https://git-scm.com/downloads
- Purpose: version control, cloning repos, saving code changes.

Mac install option:

```bash
xcode-select --install
# or
brew install git
```

### Python

- Download: https://www.python.org/downloads/
- Purpose: scripts, automations, local tools, data processing.

Mac install option:

```bash
brew install python@3.11
```

### Node.js

- Download: https://nodejs.org/en/download
- Purpose: web apps, CLIs, frontend tools, many AI coding tools.

Mac install option:

```bash
brew install node
```

### Homebrew, for macOS students

- Install: https://brew.sh/
- Purpose: easiest way to install developer tools on Mac.

Install:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Code editor

Pick one:

- VS Code: https://code.visualstudio.com/download
- Cursor: https://cursor.com/download

Purpose: editing files, reviewing agent-generated code, opening projects.

---

## 2. Local model tools

### Ollama

- Download: https://ollama.com/download
- Purpose: run local models for cheap/private memory hygiene, summarization, folder review.

Example:

```bash
ollama pull qwen3.6:35b
ollama serve
curl -s http://127.0.0.1:11434/v1/models
```

### LM Studio

- Download: https://lmstudio.ai/download
- Purpose: GUI for downloading/running local models, alternative to Ollama.

Use if students prefer a visual local-model app.

---

## 3. Messaging tools

### Telegram Desktop

- Download: https://desktop.telegram.org/
- BotFather: https://t.me/BotFather
- Purpose: chat with agents from Telegram.

Important:

- Use one bot token per public-facing agent.
- Do not reuse the same Telegram bot token across multiple polling gateways.
- Never paste bot tokens into shared chat or public docs.

### Discord

- Download: https://discord.com/download
- Developer portal: https://discord.com/developers/applications
- Purpose: connect agents to Discord servers/channels.

### Slack

- Download: https://slack.com/downloads
- App creation: https://api.slack.com/apps
- Purpose: connect agents to Slack workspaces.

---

## 4. AI model providers and accounts

Students can use one or more providers depending on budget and use case.

### OpenAI

- Platform: https://platform.openai.com/
- Purpose: GPT models, image generation, embeddings, API access.

### Anthropic / Claude

- Console: https://console.anthropic.com/
- Claude Code docs: https://docs.anthropic.com/en/docs/claude-code/overview
- Purpose: Claude models and Claude Code for coding workflows.

### Nous Research

- Portal: https://portal.nousresearch.com/
- Hermes docs: https://hermes-agent.nousresearch.com/docs
- Purpose: Hermes Agent ecosystem and Nous model access.

### OpenRouter

- Website: https://openrouter.ai/
- Purpose: access many models through one provider.

### GitHub Copilot / GitHub

- GitHub: https://github.com/
- GitHub CLI: https://cli.github.com/
- Purpose: repositories, issues, PRs, GitHub auth, Copilot-related workflows.

GitHub CLI install:

```bash
brew install gh
```

---

## 5. Coding and builder tools

### GitHub CLI

- Install: https://cli.github.com/
- Purpose: clone/create repos, open PRs, manage issues.

```bash
brew install gh
gh auth login
```

### Claude Code

- Docs: https://docs.anthropic.com/en/docs/claude-code/overview
- Purpose: advanced coding agent in the terminal.

### OpenAI Codex CLI

- GitHub: https://github.com/openai/codex
- Purpose: coding agent / CLI workflow with OpenAI models.

### Playwright

- Install docs: https://playwright.dev/docs/intro
- Purpose: browser automation, screenshots, testing web apps.

```bash
npm init playwright@latest
```

### Chrome

- Download: https://www.google.com/chrome/
- Purpose: browser testing, screenshots, local app QA.

### Vercel CLI

- Docs: https://vercel.com/docs/cli
- Purpose: deploy web apps and landing pages.

```bash
npm i -g vercel
```

### Cloudflare Wrangler

- Install docs: https://developers.cloudflare.com/workers/wrangler/install-and-update/
- Purpose: Cloudflare Workers, Pages, edge deployments.

```bash
npm install -g wrangler
```

---

## 6. Productivity and database integrations

### Notion

- Desktop app: https://www.notion.com/desktop
- Integrations: https://www.notion.so/my-integrations
- API docs: https://developers.notion.com/
- Purpose: dashboards, student pages, executive mirrors, databases.

### Google Cloud CLI

- Install: https://cloud.google.com/sdk/docs/install
- Purpose: Google APIs, Gmail, Calendar, Drive, Sheets automations.

### Airtable

- API docs: https://airtable.com/developers/web/api/introduction
- Purpose: lightweight CRM, sales tables, registration/revenue tracking.

### Todoist

- API docs: https://developer.todoist.com/rest/v2/
- Purpose: task capture, local worker queues, agent task routing.

---

## 7. Social and content tools

### X / Twitter Developer

- Developer portal: https://developer.x.com/en/portal/dashboard
- Purpose: X API workflows, posting, monitoring, handle lookup.

### Blotato

- Website: https://www.blotato.com/
- Purpose: social media posting/scheduling workflows.

### Gamma

- Website: https://gamma.app/
- Purpose: presentation generation.

### Higgsfield

- Website: https://www.higgsfield.ai/
- Purpose: AI image/video generation for marketing and creative workflows.

---

## 8. Media and visual tools

### ffmpeg

- Download: https://ffmpeg.org/download.html
- Purpose: video/audio processing, clipping, compression, transcript workflows.

Mac install:

```bash
brew install ffmpeg
```

### ImageMagick

- Download: https://imagemagick.org/script/download.php
- Purpose: image conversion, resizing, batch visual processing.

Mac install:

```bash
brew install imagemagick
```

---

## 9. Terminal apps

Students can use the default Terminal, or install one of these:

### iTerm2

- Download: https://iterm2.com/downloads.html

### Warp

- Download: https://www.warp.dev/download

Purpose: better terminal experience for running agents and scripts.

---

## 10. Recommended first-day install list

For most students, install only these first:

1. Hermes Agent: https://hermes-agent.nousresearch.com/docs
2. Obsidian: https://obsidian.md/download
3. VS Code or Cursor:
   - https://code.visualstudio.com/download
   - https://cursor.com/download
4. Git: https://git-scm.com/downloads
5. Python: https://www.python.org/downloads/
6. Node.js: https://nodejs.org/en/download
7. Ollama: https://ollama.com/download
8. Telegram Desktop, optional: https://desktop.telegram.org/

Then add provider accounts:

- OpenAI: https://platform.openai.com/
- Anthropic: https://console.anthropic.com/
- OpenRouter: https://openrouter.ai/
- GitHub: https://github.com/

---

## 11. One-command macOS starter install

Only run this after checking what it installs.

```bash
xcode-select --install || true
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git python@3.11 node jq ripgrep tmux gh ffmpeg imagemagick ollama
brew install --cask obsidian visual-studio-code cursor google-chrome telegram notion
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor
```

---

## 12. What each tool is for, in plain English

- **Hermes Agent**: the main agent operating system.
- **Obsidian**: the agents' shared notebook and memory.
- **Notion**: polished pages and student-facing dashboards.
- **Ollama/Qwen**: local low-cost worker for private tasks.
- **Telegram/Discord/Slack**: chat interface for agents.
- **Git/GitHub**: code storage and collaboration.
- **VS Code/Cursor**: editing and reviewing files.
- **Python/Node.js**: scripts and apps.
- **Playwright/Chrome**: browser automation and QA.
- **Vercel/Cloudflare**: deploying websites/apps.
- **Airtable/Todoist/Google/Notion APIs**: real-world business/task automations.
- **ffmpeg/ImageMagick**: media processing.
- **OpenAI/Anthropic/OpenRouter/Nous**: model providers.

---

## 13. Safety reminder for students

Do not put secrets in prompts or screenshots.

Secrets include:

- API keys
- Bot tokens
- OAuth tokens
- Passwords
- Private customer data
- Payment details
- Database connection strings

Ask your agent to store secrets in local `.env` files or credential files, and to print only whether the credential exists, not the credential itself.
