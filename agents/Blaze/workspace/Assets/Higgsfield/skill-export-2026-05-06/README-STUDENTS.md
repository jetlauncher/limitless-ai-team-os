# Higgsfield AI Skills

These are the Higgsfield skills Jet is sharing for class use.

Included skills:
- `higgsfield-generate` — generate images/videos with Higgsfield CLI
- `higgsfield-product-photoshoot` — product photoshoot workflows
- `higgsfield-marketplace-cards` — marketplace product image cards
- `higgsfield-soul-id` — train/use Soul Character workflows

## Install options

### Easiest: install from the official repo
```bash
npx --yes skills add https://github.com/higgsfield-ai/skills -g --all --copy
```

### Manual install
Copy the skill folders into your agent's skills directory, for example:

- Claude Code: `~/.claude/skills/`
- Generic agents: `~/.agents/skills/`
- Hermes global: `~/.hermes/skills/`
- Hermes profile: `~/.hermes/profiles/<profile-name>/skills/`

Then restart or reload your agent's skills.

## Requirements
- Node/npm for `npx skills` install path
- Higgsfield CLI installed and authenticated for generation commands

Official repo: https://github.com/higgsfield-ai/skills
