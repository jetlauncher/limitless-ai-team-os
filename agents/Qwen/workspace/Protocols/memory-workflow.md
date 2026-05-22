# Memory Workflow — Qwen

## Storage routing

Every note belongs in exactly one place:

| Decision          | Destination                                              |
| ----------------- | -------------------------------------------------------- |
| Temporary         | `Scratchpad/inbox.md`                                    |
| Today only        | `Daily/YYYY-MM-DD.md`                                    |
| Repeatable        | `Protocols/`                                             |
| Shared durable    | `../Shared Memory/MEMORY.md` (if agent-wide rule)       |
| Shared daily coor | `../Shared Memory/Daily/YYYY-MM-DD.md`                  |
| Agent-durable     | `Memory/MEMORY.md`                                       |

## Rules

1. Write daily notes for every operational run.
2. Promote repeatable procedures to `Protocols/` with frontmatter `type: protocol`.
3. Update `Memory/MEMORY.md` when a durable fact survives the day.
4. Never store raw secrets in Obsidian.
5. Use wikilinks for related Obsidian notes.

## Durable memory pattern

When a stable preference, routing rule, or protocol fact is discovered:

```
## Decision: <title>
- **When:** <trigger condition>
- **What:** <action>
- **Where:** <Obsidian path>
- **Created:** YYYY-MM-DD
```
