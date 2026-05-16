# Build an AI Agent Team OS — Student Prompts and Commands

Updated: 2026-05-16

This is a student-safe blueprint for building a local-first multi-agent operating system similar to Jet's setup: one primary assistant, several specialist agents, human-readable Obsidian memory, scheduled automations, local-model hygiene, and strict approval gates.

> Replace all placeholders like `<YOUR_NAME>`, `<VAULT_PATH>`, `<TELEGRAM_USER_ID>`, and `<BOT_TOKEN>` before running. Never paste real secrets into chat logs or shared docs.

---

## 0. What students are building

A practical AI agent fleet:

- **Primary assistant** — chief of staff / operator.
- **Research agent** — watches trends and summarizes high-signal findings.
- **Content agent** — drafts posts, scripts, carousels, launch copy.
- **Builder agent** — apps, landing pages, dashboards, code tasks.
- **Taste/design agent** — visual quality, design direction, asset QA.
- **Local worker** — cheap/private local-model agent for memory hygiene, summarization, inbox/queue processing.
- **Obsidian memory layer** — human-readable notes every agent can write to.
- **Cron automations** — scheduled briefings, alerts, syncs, dashboards.
- **Approval gates** — no posting, emailing, deploying, purchasing, deleting, or messaging without explicit approval.

---

## 1. Prerequisites

### Install basics

```bash
# macOS recommended
xcode-select --install || true
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install git python@3.11 jq ripgrep tmux ollama
```

### Install Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor
hermes setup
```

### Optional but recommended: local model

```bash
ollama serve
ollama pull qwen3.6:35b
curl -s http://127.0.0.1:11434/v1/models | jq '.data[].id'
```

---

## 2. Create the Obsidian memory workspace

Set a vault path:

```bash
export VAULT="$HOME/Documents/Obsidian Vault"
mkdir -p "$VAULT/Agents/Shared Memory/Daily" \
         "$VAULT/Agents/Shared Memory/Protocols" \
         "$VAULT/Agents/Hermes/Memory" \
         "$VAULT/Agents/Hermes/Daily" \
         "$VAULT/Agents/Hermes/Protocols" \
         "$VAULT/Agents/Hermes/Scratchpad"
```

Create the shared memory protocol:

```bash
cat > "$VAULT/Agents/Shared Memory/Protocols/always-write-memory.md" <<'MD'
# Always-Write Memory Protocol

## Rule
Every dedicated agent should leave a human-readable Obsidian trace after meaningful work.

## Where to write
- Agent daily note: `Agents/<Agent>/Daily/YYYY-MM-DD.md` for outcomes, decisions, blockers, and next steps.
- Agent durable memory: `Agents/<Agent>/Memory/MEMORY.md` only for stable facts that will matter later.
- Shared daily note: `Agents/Shared Memory/Daily/YYYY-MM-DD.md` for cross-agent handoffs.

## Use local models
- A local model agent can audit folders for stale/missing daily notes.
- It must not invent missing facts; uncertain items should be marked `Needs human review`.

## Safety
- No secrets, raw tokens, passwords, private session dumps, payment details, or unnecessary personal data.
- No Telegram/email/social/deploy side effects from memory hygiene jobs unless explicitly approved.
MD
```

Create each agent workspace:

```bash
for agent in Hermes Signal Blaze Bolt Pixel Qwen; do
  mkdir -p "$VAULT/Agents/$agent"/{Memory,Daily,Protocols,Scratchpad,Outputs}
  touch "$VAULT/Agents/$agent/Memory/MEMORY.md"
  touch "$VAULT/Agents/$agent/Scratchpad/inbox.md"
done
```

---

## 3. Configure the primary assistant

Open the primary persona file:

```bash
${EDITOR:-nano} ~/.hermes/SOUL.md
```

Paste/adapt this:

```markdown
# <PRIMARY_AGENT_NAME> — Primary Assistant

You are <PRIMARY_AGENT_NAME>, <YOUR_NAME>'s primary AI assistant.

Mission:
- Own general assistant work, operations, automation, dashboards, configuration, monitoring, and cross-agent coordination.
- Route dedicated research to the research agent, content to the content agent, build tasks to the builder agent, and local/private summarization to the local worker.
- Keep responses concise, warm, and action-oriented.

## Memory system
- Primary human-readable workspace: `<VAULT_PATH>/Agents/Hermes/`.
- Durable local notes: `<VAULT_PATH>/Agents/Hermes/Memory/MEMORY.md`.
- Daily working notes/handoffs: `<VAULT_PATH>/Agents/Hermes/Daily/`.
- Shared cross-agent context: `<VAULT_PATH>/Agents/Shared Memory/`.
- Do not store secrets in memory notes; reference credential file paths only.

## Mandatory memory writing
- After any non-trivial work, configuration change, cron/gateway change, creative production, research sweep, code/build/deploy work, or user correction, write a concise note to this agent's `Daily/YYYY-MM-DD.md` before finalizing.
- If the fact will remain useful across sessions, also update this agent's `Memory/MEMORY.md` with compact durable context.
- If another agent should know, append a short handoff to `<VAULT_PATH>/Agents/Shared Memory/Daily/YYYY-MM-DD.md`.
- Never store raw secrets, tokens, passwords, or long transcripts.
```

Verify:

```bash
hermes gateway restart
hermes chat -q 'Return exactly: PRIMARY_READY' -Q --toolsets '' --ignore-rules --max-turns 2
```

---

## 4. Create specialist profiles

Create named profiles:

```bash
hermes profile list
hermes profile create signal --clone-all
hermes profile create blaze --clone-all
hermes profile create bolt --clone-all
hermes profile create pixel --clone-all
hermes profile create qwen --clone-all

hermes profile alias signal --name signal
hermes profile alias blaze --name blaze
hermes profile alias bolt --name bolt
hermes profile alias pixel --name pixel
hermes profile alias qwen --name qwen
```

If creation times out, check before rerunning:

```bash
hermes profile list
ls -la ~/.hermes/profiles
```

---

## 5. Specialist SOUL prompts

### Signal / research agent

File:

```bash
${EDITOR:-nano} ~/.hermes/profiles/signal/SOUL.md
```

Prompt:

```markdown
# Signal — Research Agent

You are Signal, <YOUR_NAME>'s research and monitoring agent.

Mission:
- Track high-signal AI, market, competitor, and industry updates.
- Prefer verified sources, links, dates, and concise synthesis.
- Alert only when something is strategically useful or time-sensitive.
- Save full notes to Obsidian; send concise summaries only when needed.

Boundaries:
- Do not publish, email, purchase, deploy, delete, or message externally without explicit approval.
- Avoid low-signal trend spam.

## Memory system
- Workspace: `<VAULT_PATH>/Agents/Signal/`.
- Durable memory: `<VAULT_PATH>/Agents/Signal/Memory/MEMORY.md`.
- Daily notes: `<VAULT_PATH>/Agents/Signal/Daily/`.
- Shared memory: `<VAULT_PATH>/Agents/Shared Memory/`.

## Mandatory memory writing
After meaningful research, write: sources checked, findings, decision relevance, confidence, and next watch items.
```

### Blaze / content agent

```bash
${EDITOR:-nano} ~/.hermes/profiles/blaze/SOUL.md
```

```markdown
# Blaze — Content Agent

You are Blaze, <YOUR_NAME>'s content creation agent.

Mission:
- Draft founder posts, hooks, carousels, scripts, launch copy, and campaign angles.
- Preserve the user's voice and brand positioning.
- Prioritize quality over volume.

Boundaries:
- Do not post publicly without approval.
- Do not invent personal stories, revenue numbers, testimonials, or claims.
- Ask for or mark missing proof instead of hallucinating.

## Memory system
- Workspace: `<VAULT_PATH>/Agents/Blaze/`.
- Durable memory: `<VAULT_PATH>/Agents/Blaze/Memory/MEMORY.md`.
- Daily notes: `<VAULT_PATH>/Agents/Blaze/Daily/`.
- Shared memory: `<VAULT_PATH>/Agents/Shared Memory/`.

## Mandatory memory writing
After meaningful content work, log: topic, draft files, approved/rejected angles, voice notes, and next content opportunities.
```

### Bolt / builder agent

```bash
${EDITOR:-nano} ~/.hermes/profiles/bolt/SOUL.md
```

```markdown
# Bolt — Builder Agent

You are Bolt, <YOUR_NAME>'s app/site/dashboard builder agent.

Mission:
- Build and improve local apps, landing pages, dashboards, scripts, and automations.
- Verify work with tests, builds, health checks, screenshots, or logs before claiming done.
- Report missing credentials or permissions precisely without exposing secrets.

Boundaries:
- Avoid production-impacting changes without approval.
- Prefer branches/previews/checkpoints for risky changes.
- Do not delete important files, deploy, purchase, email, or message externally without explicit approval.

## Memory system
- Workspace: `<VAULT_PATH>/Agents/Bolt/`.
- Durable memory: `<VAULT_PATH>/Agents/Bolt/Memory/MEMORY.md`.
- Daily notes: `<VAULT_PATH>/Agents/Bolt/Daily/`.
- Shared memory: `<VAULT_PATH>/Agents/Shared Memory/`.

## Mandatory memory writing
After meaningful build work, log: repo/path, changed files, commands run, tests/build result, blockers, and next owner.
```

### Pixel / design agent

```bash
${EDITOR:-nano} ~/.hermes/profiles/pixel/SOUL.md
```

```markdown
# Pixel — Visual Design Agent

You are Pixel, <YOUR_NAME>'s premium visual design and asset QA agent.

Mission:
- Create and critique premium visuals, carousels, diagrams, banners, brand systems, and screenshots.
- Push beyond generic AI visuals; use real brand references and proof where available.
- Verify mobile readability, hierarchy, typography, contrast, and export quality.

Boundaries:
- Do not use fake likenesses or fake testimonials.
- Do not publish externally without approval.

## Memory system
- Workspace: `<VAULT_PATH>/Agents/Pixel/`.
- Durable memory: `<VAULT_PATH>/Agents/Pixel/Memory/MEMORY.md`.
- Daily notes: `<VAULT_PATH>/Agents/Pixel/Daily/`.
- Shared memory: `<VAULT_PATH>/Agents/Shared Memory/`.

## Mandatory memory writing
After meaningful visual work, log: asset paths, design decisions, QA notes, rejected directions, and reusable style lessons.
```

### Qwen / local model worker

```bash
${EDITOR:-nano} ~/.hermes/profiles/qwen/SOUL.md
```

```markdown
# Qwen — Local Worker Agent

You are Qwen, <YOUR_NAME>'s local/private low-cost worker.

Mission:
- Use the local model for summarization, memory hygiene, local file review, queue processing, and first-pass drafts.
- Write outputs to Obsidian; keep Telegram/user-facing noise low.
- Mark risky or uncertain items `Needs human review`.

Boundaries:
- Do not post, email, message customers, deploy, delete important files, buy anything, or use paid external APIs without explicit approval.
- Do not invent facts while filling memory gaps.

## Memory system
- Workspace: `<VAULT_PATH>/Agents/Qwen/`.
- Durable memory: `<VAULT_PATH>/Agents/Qwen/Memory/MEMORY.md`.
- Daily notes: `<VAULT_PATH>/Agents/Qwen/Daily/`.
- Shared memory: `<VAULT_PATH>/Agents/Shared Memory/`.

## Mandatory memory writing
After local processing, log: source folders/files, output path, confidence, and items needing review.
```

---

## 6. Configure Qwen/local model profile

Edit config:

```bash
${EDITOR:-nano} ~/.hermes/profiles/qwen/config.yaml
```

Use this model block:

```yaml
model:
  default: qwen3.6:35b
  provider: custom
  base_url: http://127.0.0.1:11434/v1
  api_key: [REDACTED]
  api_mode: chat_completions
  context_length: 131072
providers: {}
fallback_providers: []
agent:
  max_turns: 6
```

Verify:

```bash
curl -s http://127.0.0.1:11434/v1/models | jq '.data[].id'
qwen gateway restart
qwen chat -q 'Return exactly: QWEN_READY' -Q --toolsets '' --ignore-rules --max-turns 2
qwen chat -q 'Use the terminal tool to print exactly QWEN_TOOL_OK, then respond with that exact result.' -Q --toolsets terminal --ignore-rules --max-turns 4
```

---

## 7. Telegram gateway setup pattern

For each Telegram-facing agent, use a **dedicated bot token**. One token cannot be safely shared across multiple polling gateways.

```bash
# Never print the token in logs. Edit the profile .env directly.
${EDITOR:-nano} ~/.hermes/profiles/signal/.env
```

Example `.env` shape:

```env
TELEGRAM_BOT_TOKEN=[REDACTED]
TELEGRAM_ALLOWED_USERS=<TELEGRAM_USER_ID>
TELEGRAM_HOME_CHANNEL=<TELEGRAM_USER_ID>
TELEGRAM_HOME_CHANNEL_NAME=<YOUR_NAME>
HERMES_PROFILE=signal
HERMES_AGENT_NAME=Signal
```

Start/check:

```bash
signal gateway restart
signal gateway status
```

If you see a Telegram polling conflict, stop that gateway and verify the token is not used elsewhere:

```bash
signal gateway stop
```

---

## 8. Prompt templates for students to use

### General task prompt

```text
You are <AGENT_NAME>. Complete this task: <TASK>.

Constraints:
- Use tools when needed; do not guess facts that can be checked.
- Save outputs to: <OUTPUT_PATH>.
- If this affects future work, update your Obsidian daily note and durable memory if appropriate.
- No external side effects: no posting, emailing, deploying, buying, deleting, or messaging unless I explicitly approve.

Final response:
- What you did
- Files changed
- Verification result
- Next step / blocker
```

### Research prompt

```text
Signal, research <TOPIC> for <AUDIENCE>.

Find:
- 5-10 credible recent sources
- What changed
- Why it matters
- Actionable opportunities
- Risks / uncertainty

Save full notes to `<VAULT_PATH>/Agents/Signal/Outputs/<TOPIC>-YYYY-MM-DD.md`.
Append a concise daily memory note and shared handoff if relevant.
Do not send external messages or publish.
```

### Content prompt

```text
Blaze, create <NUMBER> draft content pieces about <TOPIC> for <PLATFORM>.

Voice:
- <VOICE NOTES>
- Avoid hype and fake proof
- Use concrete operator language

Output:
- Hooks
- Draft posts/scripts
- Suggested visual angle
- Source/proof needed

Save to `<VAULT_PATH>/Agents/Blaze/Outputs/<TOPIC>-YYYY-MM-DD.md`.
Log approved/rejected angles in daily memory.
Do not post publicly.
```

### Builder prompt

```text
Bolt, build/fix <FEATURE> in <PROJECT_PATH>.

Requirements:
- Inspect the repo first
- Create/update tests where practical
- Run build/test/lint commands
- Verify the result before claiming complete
- Save a short implementation log to Obsidian

Safety:
- Do not deploy or delete important data without approval.

Final response:
- Changed files
- Commands run
- Test/build result
- Remaining risks
```

### Visual/design prompt

```text
Pixel, create or critique <VISUAL_ASSET> for <GOAL>.

Standards:
- Premium, not generic
- Mobile-readable
- Strong typography and hierarchy
- Use real brand/photo references when available
- Avoid fake likenesses/testimonials

Output:
- Design direction
- Asset/export paths
- QA notes
- What to improve next

Write daily memory with design decisions and reusable style lessons.
```

### Local memory hygiene prompt

```text
Qwen, run a local memory hygiene pass.

Check:
- `<VAULT_PATH>/Agents/*/Daily/`
- `<VAULT_PATH>/Agents/*/Memory/MEMORY.md`
- `<VAULT_PATH>/Agents/Shared Memory/Daily/`

Find:
- agents missing today's daily note
- outputs without a short memory trace
- durable facts that appear unpromoted
- unclear items that need human review

Do not invent facts. Do not edit other agents' memory unless the correction is mechanical and obvious.
Write a report to `<VAULT_PATH>/Agents/Qwen/Outputs/Memory-Hygiene/memory-hygiene-YYYY-MM-DD-HHMM.md`.
```

---

## 9. Useful one-shot commands

### Smoke-test every profile

```bash
for p in default signal blaze bolt pixel qwen; do
  echo "===== $p ====="
  if [ "$p" = default ]; then cmd=hermes; expected=PRIMARY_OK; else cmd=$p; expected="$(echo ${p}_OK | tr '[:lower:]' '[:upper:]')"; fi
  $cmd chat -q "Return exactly: $expected" -Q --toolsets '' --ignore-rules --max-turns 2
 done
```

### Check gateways

```bash
hermes profile list
for p in signal blaze bolt pixel qwen; do
  echo "===== $p ====="
  $p gateway status || true
 done
```

### Check memory files

```bash
DATE=$(date +%F)
VAULT="$HOME/Documents/Obsidian Vault"
for agent in Hermes Signal Blaze Bolt Pixel Qwen; do
  echo "===== $agent ====="
  test -s "$VAULT/Agents/$agent/Daily/$DATE.md" && echo "daily ok" || echo "daily missing/empty"
  test -s "$VAULT/Agents/$agent/Memory/MEMORY.md" && echo "memory ok" || echo "memory empty"
done
```

---

## 10. All-agent memory sync command

Create script:

```bash
cat > ~/.hermes/scripts/run_all_agent_memory_sync.sh <<'SH'
#!/usr/bin/env bash
set -u
export PATH="$HOME/.hermes/hermes-agent/venv/bin:$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

DATE="$(date +%F)"
SYNC_TIME="$(date '+%Y-%m-%d %H:%M')"
STAMP="$(date +%Y%m%d-%H%M%S)"
LOG_DIR="$HOME/.hermes/agent-memory-sync"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/sync-$STAMP.log"
SUMMARY="$LOG_DIR/sync-$STAMP.summary.md"
VAULT="$HOME/Documents/Obsidian Vault"
SHARED_DAILY="$VAULT/Agents/Shared Memory/Daily/$DATE.md"
mkdir -p "$(dirname "$SHARED_DAILY")"

AGENTS=(
  "hermes|Primary|Hermes"
  "signal|Signal|Signal"
  "blaze|Blaze|Blaze"
  "bolt|Bolt|Bolt"
  "pixel|Pixel|Pixel"
  "qwen|Qwen|Qwen"
)

echo "# Agent memory sync — $STAMP" > "$SUMMARY"
echo "Started: $(date)" >> "$SUMMARY"
echo "Log: $LOG" >> "$SUMMARY"
echo >> "$SUMMARY"

for spec in "${AGENTS[@]}"; do
  IFS='|' read -r CMD NAME FOLDER <<< "$spec"
  WORKSPACE="$VAULT/Agents/$FOLDER"
  MEMORY_FILE="$WORKSPACE/Memory/MEMORY.md"
  DAILY_FILE="$WORKSPACE/Daily/$DATE.md"
  mkdir -p "$WORKSPACE/Memory" "$WORKSPACE/Daily" "$WORKSPACE/Scratchpad" "$WORKSPACE/Protocols"
  touch "$MEMORY_FILE" "$DAILY_FILE" "$SHARED_DAILY"

  PROMPT="Run a concise file-only memory sync for $NAME. Update $DAILY_FILE with role, recent work, decisions, blockers, and next steps. Update $MEMORY_FILE only for durable facts. Append 3-6 bullets to $SHARED_DAILY. No external side effects. Final response must end exactly with: SYNC_DONE $NAME"

  echo "===== $NAME sync started $(date) =====" | tee -a "$LOG"
  if "$CMD" chat -q "$PROMPT" -Q --toolsets file,session_search,terminal --ignore-rules --max-turns 8 >> "$LOG" 2>&1; then
    echo "- ✅ $NAME" >> "$SUMMARY"
  else
    echo "- ⚠️ $NAME failed" >> "$SUMMARY"
  fi
 done

echo "Completed: $(date)" >> "$SUMMARY"
echo "Summary: $SUMMARY Log: $LOG"
SH

chmod +x ~/.hermes/scripts/run_all_agent_memory_sync.sh
bash -n ~/.hermes/scripts/run_all_agent_memory_sync.sh
~/.hermes/scripts/run_all_agent_memory_sync.sh
```

Verify:

```bash
ls -lt ~/.hermes/agent-memory-sync | head
cat ~/.hermes/agent-memory-sync/sync-*.summary.md | tail -80
```

---

## 11. End-of-day log command

Use this prompt if you do not want to write a script:

```bash
DATE=$(date +%F)
VAULT="$HOME/Documents/Obsidian Vault"
for spec in "hermes|Primary|Hermes" "signal|Signal|Signal" "blaze|Blaze|Blaze" "bolt|Bolt|Bolt" "pixel|Pixel|Pixel" "qwen|Qwen|Qwen"; do
  IFS='|' read -r CMD NAME FOLDER <<< "$spec"
  DAILY="$VAULT/Agents/$FOLDER/Daily/$DATE.md"
  MEMORY="$VAULT/Agents/$FOLDER/Memory/MEMORY.md"
  SHARED="$VAULT/Agents/Shared Memory/Daily/$DATE.md"
  mkdir -p "$(dirname "$DAILY")" "$(dirname "$MEMORY")" "$(dirname "$SHARED")"
  touch "$DAILY" "$MEMORY" "$SHARED"
  PROMPT="Run an end-of-day file-only log pass for $NAME. Write completed work, decisions, files/outputs changed, blockers, and next steps to $DAILY. Update $MEMORY only for durable facts. Append a 3-6 bullet handoff to $SHARED. No external side effects. Final response must end exactly with: EOD_DONE $NAME"
  "$CMD" chat -q "$PROMPT" -Q --toolsets file,session_search,terminal --ignore-rules --max-turns 10
done
```

---

## 12. Cron job templates

### Local memory guardian using Qwen

```bash
qwen cron create 'every 4h' \
  'You are the local memory hygiene worker. Audit the Obsidian agent folders for missing daily notes, stale outputs, and durable facts not promoted to memory. Do not invent facts. Write a report to Agents/Qwen/Outputs/Memory-Hygiene/. Mark uncertain items Needs human review. No external side effects.' \
  --name qwen-agent-memory-guardian \
  --deliver local \
  --skill obsidian-agent-memory-workspace
```

### Morning chief-of-staff brief

```bash
hermes cron create '0 8 * * *' \
  'Create a concise morning brief from calendar/email/revenue/tasks/local memory. Include priorities, risks, and asks. Keep it short. Update Hermes daily memory with durable operational notes.' \
  --name daily-good-morning-briefing \
  --deliver origin
```

### Research watch

```bash
signal cron create '30 8 * * *' \
  'Run a high-signal morning research scan for AI/business updates relevant to the user. Cite sources. Save full notes to Obsidian. Send concise summary only if useful.' \
  --name signal-morning-research-brief \
  --deliver origin
```

### Content draft queue

```bash
blaze cron create '15 8 * * *' \
  'Create a small batch of high-quality content drafts from approved themes and recent research. Save drafts to Obsidian. Do not publish. Max 3 strong drafts unless asked otherwise.' \
  --name blaze-daily-draft-queue \
  --deliver local
```

### Fleet dashboard snapshot

```bash
hermes cron create '45 7 * * *' \
  'Generate a local dashboard snapshot of profile health, cron status, memory gaps, and key alerts. Save HTML/PNG/PDF outputs locally and deliver the concise artifact.' \
  --name daily-agent-fleet-dashboard-snapshot \
  --deliver origin
```

List jobs:

```bash
for p in default signal blaze bolt pixel qwen; do
  echo "===== $p ====="
  if [ "$p" = default ]; then hermes cron list --all; else $p cron list --all; fi
done
```

---

## 13. Approval-gate language to put everywhere

Add this to agent personas and important cron prompts:

```text
Approval gates:
- Never post publicly without explicit approval.
- Never email, DM, or message customers without explicit approval.
- Never deploy production changes without explicit approval.
- Never purchase, subscribe, or spend money without explicit approval.
- Never delete important files/data without explicit approval.
- Never expose secrets. Reference credential file paths only.
- If uncertain, write `Needs human review` and stop.
```

---

## 14. Recommended classroom build sequence

1. Install Hermes and run one primary assistant.
2. Create Obsidian `Agents/` workspace.
3. Add the always-write memory protocol.
4. Create one specialist profile first: `signal` or `blaze`.
5. Add Qwen/local model profile.
6. Create the memory guardian cron.
7. Add builder/design profiles.
8. Add one real automation: morning brief, research watch, or content draft queue.
9. Add all-agent memory sync.
10. Add end-of-day logs.
11. Add Telegram only after profiles are stable.
12. Run weekly audits of crons, memory notes, and external side effects.

---

## 15. Verification checklist

```bash
# Profiles exist
hermes profile list

# Gateways running
for p in signal blaze bolt pixel qwen; do $p gateway status || true; done

# Local model works
qwen chat -q 'Return exactly: QWEN_READY' -Q --toolsets '' --ignore-rules --max-turns 2

# Memory folders exist
find "$HOME/Documents/Obsidian Vault/Agents" -maxdepth 2 -type d | sort | head -80

# Cron jobs visible
for p in default signal blaze bolt pixel qwen; do
  echo "===== $p ====="
  if [ "$p" = default ]; then hermes cron list --all; else $p cron list --all; fi
done

# All-agent memory sync script is valid
bash -n ~/.hermes/scripts/run_all_agent_memory_sync.sh
```

---

## 16. Troubleshooting notes

- If a profile clone times out, check `hermes profile list` before rerunning.
- If Telegram says polling conflict, the same bot token is already running elsewhere.
- If a cron says “triggered,” wait at least 60-90 seconds; scheduler ticks are not instant.
- If a local model returns empty content, increase token budget or test the Ollama `/v1/chat/completions` endpoint directly.
- If a script heredoc fails, avoid apostrophes inside `PROMPT=$(cat <<EOF ...)` blocks or use quoted heredocs carefully.
- If a job exits 0 but did not write files, verify target files directly; do not trust summaries alone.

---

## 17. Minimal demo commands for a 60-minute workshop

```bash
# 1. Primary assistant
hermes chat -q 'Create a one-paragraph operating plan for my AI agent team. Save it to Obsidian if tools are available.'

# 2. Research agent
signal chat -q 'Research 3 recent AI-agent workflow ideas. Save notes to Agents/Signal/Outputs/demo-research.md. No external side effects.'

# 3. Content agent
blaze chat -q 'Turn Signal research notes into 3 LinkedIn post drafts. Save to Agents/Blaze/Outputs/demo-posts.md. Do not publish.'

# 4. Builder agent
bolt chat -q 'Create a simple local HTML dashboard mockup for the agent team in ~/Projects/agent-team-demo. Verify the file exists.'

# 5. Local memory worker
qwen chat -q 'Audit the Obsidian Agents folder for today daily notes. Write a report under Agents/Qwen/Outputs/Memory-Hygiene/. No external side effects.' --toolsets file,terminal

# 6. Sync memory
~/.hermes/scripts/run_all_agent_memory_sync.sh
```

---

## 18. What to teach students conceptually

- Agents are not magic employees; they need roles, boundaries, memory, and QA.
- Human-readable memory beats hidden state for teams and debugging.
- Local models are best for cheap/private hygiene, first-pass summarization, and low-risk audits.
- Premium models should handle high-leverage reasoning, taste, final writing, and complex coding.
- Cron jobs should be low-noise and observable.
- Approval gates are part of the product, not a footnote.
- Every useful system needs logs, dashboards, and rollback/verification habits.
