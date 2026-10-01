# Hermes vs Claude Code vs ChatGPT/Codex — Desktop Comparison

**Audit date:** 2026-08-20  
**Scope:** Current official product documentation plus live verification on Jet's Mac.

## Executive verdict

These are overlapping but differently optimized desktop systems.

- **Hermes is the operating-system layer.** Its desktop app shares the same sessions, config, skills, memory, profiles, tools, and state as its CLI and messaging gateway. The desktop adds artifacts, terminals, Git review, worktrees, memory graph, bots, voice, quick entry, and management surfaces.[1]
- **Claude Code is the deep software-engineering specialist.** Claude Desktop's Code tab supports local, cloud, and SSH sessions; visual diff review; browser/app preview; terminal/editor panes; external tools; computer control; parallel sessions; and scheduled work.[2][3]
- **ChatGPT/Codex is the parallel mixed-work command center.** The ChatGPT desktop app combines Chat and Codex, projects, files, artifacts, browser/computer access, plugins, scheduling, worktrees, cloud agents, and parallel work; OpenAI positions Codex as the same coding agent across ChatGPT, editor, and terminal.[4][5][6]

## Capability matrix

| Criterion | Hermes | Claude Code | ChatGPT / Codex |
|---|---|---|---|
| Broad business operations | **Lead** | Good | Strong |
| Deep codebase work | Strong | **Lead** | **Lead** |
| Parallel agents/worktrees | **Lead** | Strong | **Lead** |
| Persistent memory & skills | **Lead** | Strong | Strong |
| Scheduling / always-on work | **Lead** | Strong | Strong |
| Messaging / remote channels | **Lead** | Good | Good |
| Model & provider freedom | **Lead** | Narrow | Narrow |
| Finished docs / artifacts | Strong | Strong | **Lead** |
| Native coding review UX | Strong | **Lead** | **Lead** |
| Best role for Jet | **HQ / orchestration** | Deep implementation | Parallel build & review |

## Live state on this Mac

### Hermes
- Desktop UI running.
- Hermes Agent `v0.20.4` and current.
- Ten Hermes gateways running across the active fleet.
- Default profile has 42 cron definitions, 22 active.
- Desktop visibly exposes profiles/bots, sessions, cron jobs, voice, and agent activity.

### Claude
- Claude Desktop `1.32885.1` running.
- Claude Code `2.1.161` installed and authenticated via Claude Max.
- Playwright MCP connected; GitHub and Firecrawl MCP endpoints currently failed in the local health check.
- Desktop visibly supports Code sessions and permissions.

### ChatGPT / Codex
- ChatGPT Desktop `26.814.41407` running with bundle ID `com.openai.codex`.
- Embedded Codex CLI `0.148.0-alpha.15` is healthy inside the app bundle.
- Desktop visibly runs commands, reads files, exposes Outputs, Computer Use, and Web Search.
- The separate global npm `codex` wrapper is locally broken because its expected native binary is missing (`ENOENT`); this does not block the running desktop app.

## Recommended operating stack

1. **Jet** — purpose, taste, relationships, and approval.
2. **Hermes / Kelly** — memory, routing, scheduling, business operations, cross-agent coordination, delivery, and verification.
3. **Claude Code** — deep debugging, large codebase reasoning, implementation, and visual diff review.
4. **ChatGPT / Codex** — parallel coding agents, worktrees/cloud execution, mixed documents/artifacts, and second-opinion review.

**Recommended principle:** do not choose one winner. Keep Hermes as the headquarters and route specialist engineering work to Claude Code and Codex based on the job.

## Sources

[1] https://hermes-agent.nousresearch.com/docs/user-guide/desktop — Hermes Desktop App
[2] https://code.claude.com/docs/en/overview — Claude Code Overview
[3] https://code.claude.com/docs/en/desktop — Claude Code Desktop
[4] https://openai.com/codex — OpenAI Codex
[5] https://openai.com/chatgpt/desktop — ChatGPT Desktop
[6] https://developers.openai.com/codex/app — Codex App Docs
