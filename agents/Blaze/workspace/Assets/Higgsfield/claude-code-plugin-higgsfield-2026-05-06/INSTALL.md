# Higgsfield Claude Code Plugin

This package is made for **Claude Code / Claude Code on the web/cowork flow**.

The previous ZIP contained standalone Agent Skill folders. Claude Code can use those only when they are copied into the correct `~/.claude/skills/` or project `.claude/skills/` directory. For sharing with students, this plugin package is safer because Claude Code recognizes it as one plugin.

## What is included

- `/higgsfield:higgsfield-generate`
- `/higgsfield:higgsfield-product-photoshoot`
- `/higgsfield:higgsfield-marketplace-cards`
- `/higgsfield:higgsfield-soul-id`

Because this is a plugin, Claude Code namespaces commands as `plugin-name:skill-name`.

## Requirements

1. Claude Code installed and updated:
   ```bash
   npm install -g @anthropic-ai/claude-code
   claude update
   ```

2. Higgsfield CLI installed and logged in:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
   higgsfield auth login
   higgsfield account status
   ```

## Quick test without installing permanently

Unzip this folder, then run from the parent directory:

```bash
claude --plugin-dir ./claude-code-plugin-higgsfield-2026-05-06
```

Inside Claude Code, type:

```text
/higgsfield:higgsfield-generate Create a premium 1:1 image of a futuristic AI classroom, high-end editorial style
```

If Claude asks for Bash permission, approve it.

## Permanent install option A — user-level plugin folder

Copy this plugin folder into Claude's plugin directory and enable it in settings:

```bash
mkdir -p ~/.claude/plugins
cp -R claude-code-plugin-higgsfield-2026-05-06 ~/.claude/plugins/higgsfield
python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home()/'.claude/settings.json'
data = json.loads(p.read_text()) if p.exists() else {}
data.setdefault('enabledPlugins', {})['higgsfield'] = True
p.write_text(json.dumps(data, indent=2))
print('Enabled Higgsfield plugin in', p)
PY
```

Restart Claude Code or run `/reload-plugins`.

## Permanent install option B — standalone skills, no namespace

If you want shorter slash commands like `/higgsfield-generate`, copy the skill folders directly:

```bash
mkdir -p ~/.claude/skills
cp -R claude-code-plugin-higgsfield-2026-05-06/skills/higgsfield-* ~/.claude/skills/
```

Restart Claude Code. Then use:

```text
/higgsfield-generate Create a premium 1:1 image of a futuristic AI classroom
```

## Troubleshooting

- If `/higgsfield:...` does not appear, update Claude Code and run `/reload-plugins`.
- If generation fails with `higgsfield: command not found`, install the Higgsfield CLI and restart the terminal.
- If generation fails with auth/session errors, run `higgsfield auth login`.
- If Claude refuses to run Bash, approve Bash permissions or run in Auto Accept mode only in a trusted environment.
