# Source Ingestion Protocol

Use this when a video, transcript, article, note, or voice memo arrives.

## Source classes

| Type | Destination | Promote to memory? |
|---|---|---|
| YouTube/podcast | `Sources/YouTube Videos/` | yes, if relevant |
| Plaud transcript | `Sources/Plaud Transcripts/` | yes |
| Brain dump | `Sources/Brain Dumps/` | yes |
| Apple Note | `Sources/Apple Notes/` | yes if durable |
| External article about Jet | `Sources/References/` or press folder | yes if about Jet |
| 3rd-party tool/reference | `Sources/References/` | no by default |

## Required outputs

Every important source gets:

1. Raw file or transcript.
2. Processed summary/extraction.
3. Source metadata.
4. Links to relevant People/Projects/Concepts.
5. Handoff line in `Shared Memory/Daily/YYYY-MM-DD.md`.

## Promotion rules

Promote only durable facts:

- stable preferences
- repeated frameworks
- important people/projects
- decisions with future relevance
- reusable teaching ideas
- business strategy insights

Do not promote:

- one-off task progress
- raw transcripts
- secrets
- short-term todo state
- claims that need verification

## Verification checklist

- [ ] Raw file exists and size > 0.
- [ ] Processed summary exists and has frontmatter.
- [ ] No secrets included.
- [ ] Relevant MOC/concept linked.
- [ ] Daily handoff written.
- [ ] User-facing report includes paths.
