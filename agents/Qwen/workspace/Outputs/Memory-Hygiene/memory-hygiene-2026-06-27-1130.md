
# Memory Hygiene Audit — 2026-06-27 11:15 UTC+07:00

## Executive summary
Vault underwent recent restructuring. All Daily dirs were destroyed across agents (except Shared Memory), while MEMORY.md files were destroyed across most agents (only Qwen's survived, but its content is near-empty). The vault partially recovered via cron resuscitation that restored 5 of 6 agent directories. Two unexpected "nova" and "team" directories appeared — need review.

## Check 1: Today's daily note (2026-06-27)

| Agent          | Daily Note Status     |
|----------------|----------------------|
| Blaze          | MISSING              |
| Hermes/Kelly   | MISSING              |
| Nova           | MISSING (new dir)    |
| Qwen           | MISSING              |
| Shared Memory  | ACTIVE               |
| Signal         | ACTIVE (cron-created)|
| Team           | MISSING (new dir)    |

**Result:** Only **Shared Memory** (previous daily note exists, not today) has surviving files. All agents lack today's Daily/YYYY-MM-27.md.

## Check 2: MEMORY.md staleness

| Agent          | FILE STATUS            | Age (days) |
|----------------|------------------------|------------|
| Blaze          | DESTROYED              | —          |
| Hermes/Kelly   | DESTROYED              | —          |
| Nova           | MISSING                | —          |
| Qwen           | EXISTS but near-empty  | N/A        |
| Shared Memory  | MISSING                | —          |
| Signal         | MISSING                | —          |
| Team           | MISSING                | —          |

**Result:** **No durable context preserved** across the vault. Only Qwen/MEMORY.md survives but contains no useful content (538 bytes of "## Memory System" header only). This is **CRITICAL** — all agents have lost their persistent memory surface.

## Check 3: Recent daily activity (last 48h)
- Signal Daily dir survived + had recent cron output at 01:27 and 06:23 today (both "cron ran" messages).
- Blaze Content From Intel dir exists with files through 2026-06-26 (content production was active yesterday).
- Qwen Memory dir survived but is empty.
- All other agent Daily dirs were deleted during restructuring.

## Check 4: Agent directory status vs expected roster

| Expected Agent | On Disk?      | Notes                        |
|---------------|---------------|------------------------------|
| Blaze         | ✅ Blaze      | surviving, lost Memory/      |
| Hermes/Kelly  | ✅ Hermes     | surviving, lost Memory/      |
| Nova          | ❓ Nova       | NEW — needs context (not in roster) |
| Qwen          | ✅ Qwen       | survived but empty           |
| Shared Memory | ✅ Shared Memory | partially surviving    |
| Signal        | ✅ Signal     | surviving, lost Memory/      |
| Team          | ❓ Team       | NEW — needs context (not in roster) |
| Bolt          | MISSING       | —                            |
| Kaijeaw       | MISSING       | —                            |
| Pixel         | MISSING       | —                            |
| Protocol      | MISSING       | —                            |
| Zegna         | MISSING       | —                            |

**Result:** 7 dirs present vs expected ~12 (6 standard agents + Nova/Team). **5 folders vanished**: Bolt, Kaijeaw, Pixel, Protocol, Zegna. Two new directories appeared: "Nova" and "Team". Needs Kelly review to understand if this is intentional restructuring or a crash.

## Todoist selection — NO tasks
- No tasks matched Qwen's label/prefix selection rule. 579 total open tasks across the account but none are assigned/visible for the qwen/agent/delegate ai labels or Qwen:/AI: prefixes.
- Status: **NO WORK AVAILABLE** for this run.

## Priority action items — needs Kelly review
1. **Rebuild MEMORY.md files** for all 6 standard agents (Blaze, Hermes, Nova, Qwen, Signal, Team) — currently only Qwen has a surviving file and it's near-empty.
2. **Review "Nova" and "Team" directories** — need to understand if these replace or supplement existing agents per the new structure.
3. **Restore missing agent dirs** (Bolt, Kaijeaw, Pixel, Protocol, Zegna) — determine if they still need independent memory folders or were absorbed into "Team"/"Nova".
4. **Rebuild Daily dir structures** for all agents so tomorrow's scheduled jobs don't fail on missing directories.

## Diagnostic notes
- Vault restructuring confirmed: simultaneous deletion of Daily dirs + loss of MEMORY.md files across multiple agent dirs points to vault restructuring, not individual agent failure.
- Signal's Memory dir was also destroyed but its Daily dir survived (cron resuscitated it).
- Qwen's Memory dir survived but is near-empty — likely from the resuscitation phase which created blank structure without populating content.
