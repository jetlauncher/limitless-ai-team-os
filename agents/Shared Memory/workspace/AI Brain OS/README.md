# Limitless AI Brain OS v1

A practical operating system for building an AI brain that works for Jet, the Limitless agent fleet, and students.

This package turns the Dan Martell AI-brain idea into a Limitless OS implementation: persistent markdown memory, agent identity files, source ingestion, nightly compounding, and human review gates.

## Start here

1. Read `Folder-Structure.md`.
2. Copy `Templates/USER-template.md`, `Templates/SOUL-template.md`, and `Templates/IDENTITY-template.md` into a student vault or agent workspace.
3. Use `Prompts/Identity-Setup-Prompt.md` to interview the human and draft the identity files.
4. Use `Protocols/Source-Ingestion-Protocol.md` when a video, transcript, note, or meeting arrives.
5. Use `Prompts/Nightly-Compounding-Prompt.md` for safe daily cleanup.
6. Use `Student Materials/Student-Setup-Guide.md` as the classroom handout source.

## Core loop

```text
Capture source
→ save raw source
→ extract structured summary
→ promote durable facts
→ link concepts/MOCs
→ nightly cleanup
→ human review
```

## Existing Limitless OS mapping

| AI Brain OS layer | Existing Limitless OS location |
|---|---|
| Shared brain | `~/Documents/Limitless OS/Agents/Shared Memory/` |
| Source archive | `Shared Memory/Sources/` |
| Kelly memory | `Agents/Hermes/Memory/MEMORY.md` |
| Agent daily logs | `Agents/<Agent>/Daily/YYYY-MM-DD.md` |
| Shared handoffs | `Agents/Shared Memory/Daily/YYYY-MM-DD.md` |
| Local worker | Qwen profile + `Agents/Qwen/` |

## Safety rule

No secrets, tokens, passwords, customer PII, private session cookies, payment details, or raw revenue-sensitive records belong in teaching templates or public examples.
