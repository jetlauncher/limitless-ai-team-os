# Claude Code / Claude Code on Web Project Drop-in

Use this version when the standalone `.skill` folders do not appear in Claude Code, Claude Code on the web, or a shared/cowork project.

## Install for a project/repo

Copy the `.claude` folder from this package into the root of your project or GitHub repo:

```text
your-project/
└── .claude/
    └── skills/
        ├── higgsfield-generate/
        │   └── SKILL.md
        ├── higgsfield-product-photoshoot/
        │   └── SKILL.md
        ├── higgsfield-marketplace-cards/
        │   └── SKILL.md
        └── higgsfield-soul-id/
            └── SKILL.md
```

Then restart Claude Code, or in an existing Claude Code session run:

```text
/reload-skills
```

## Use

```text
/higgsfield-generate Create a premium 1:1 image of a futuristic AI classroom
```

Other skills:

```text
/higgsfield-product-photoshoot ...
/higgsfield-marketplace-cards ...
/higgsfield-soul-id ...
```

## Required on each student's machine

```bash
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
higgsfield auth login
higgsfield account status
```

If `higgsfield account status` works, Claude can call the Higgsfield CLI through Bash.

## Common fixes

- If the slash command is missing: make sure the folder path is exactly `.claude/skills/<skill-name>/SKILL.md`.
- If using Claude Code on the web/cowork: commit or upload the `.claude/skills` folder into the repo/project, not just your local `~/.claude`.
- If generation fails: install/login to the Higgsfield CLI on the execution machine.
- If Claude asks to trust the workspace or approve Bash, approve only in a project you trust.
