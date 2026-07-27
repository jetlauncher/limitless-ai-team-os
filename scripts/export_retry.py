#!/usr/bin/env python3
"""Export using cat (subprocess) to handle iCloud cloud-optimized files."""
import json, shutil, subprocess
from pathlib import Path

from sanitize_lib import harden_config, sanitize

REPO = Path(__file__).resolve().parents[1]
HOME = Path.home()

def write(rel, text, config=False):
    p = REPO / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(harden_config(text) if config else sanitize(text), encoding='utf-8')

def cat_file(path):
    """Read file using cat subprocess — works with iCloud cloud-optimized files."""
    try:
        result = subprocess.run(
            ['cat', str(path)],
            capture_output=True,
            timeout=30,
            text=True,
            errors='ignore'
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return ''
    except Exception:
        return ''

def collect(root, exts, skip_names, skip_dirs):
    results = []
    for f in sorted(root.rglob('*')):
        if not f.is_file():
            continue
        if f.suffix.lower() not in exts:
            continue
        sf = str(f)
        if any(s in sf for s in skip_dirs):
            continue
        if f.name in skip_names:
            continue
        if f.name.endswith('_state.json') or f.name == 'state.json':
            continue
        txt = cat_file(f)
        if not txt:
            continue  # Skipped unreadable
        if len(txt) > 120000:
            txt = txt[:120000] + '\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
        results.append((f, txt))
    return results

exts = {'.md', '.txt', '.yaml', '.yml', '.json'}
skip_names = {'ACCESS-TOKENS.md'}
skip_dirs = {'Content Archive', 'Generated Assets', 'node_modules'}

# Clean old outputs
for d in ['agents', 'configs']:
    p = REPO / d
    if p.exists():
        shutil.rmtree(p, ignore_errors=True)

# Root config
config_dir = HOME / '.hermes/config.yaml'
if config_dir.exists():
    write('configs/root/config.example.yaml', cat_file(config_dir), config=True)
    print(f'Exported configs/root/config.example.yaml')

agents_map = {'Hermes':'default','Blaze':'blaze','Bolt':'bolt','Kaijeaw':'kaijeaw','Protocol':'protocol','Qwen':'qwen','Signal':'signal','Zegna':'zegna'}

total_exported = 0

for agent, prof in agents_map.items():
    cfg = HOME / f'.hermes/profiles/{prof}/config.yaml'
    if prof != 'default' and cfg.exists():
        write(f'configs/profiles/{prof}/config.example.yaml', cat_file(cfg), config=True)
        print(f'Exported configs/profiles/{prof}/config.example.yaml')
    
    soul = HOME / ('.hermes/SOUL.md' if prof == 'default' else f'.hermes/profiles/{prof}/SOUL.md')
    if soul.exists():
        write(f'agents/{agent}/SOUL.md', cat_file(soul))
        total_exported += 1
        print(f'Exported {agent}/SOUL.md ({len(cat_file(soul))} bytes)')
    
    obs = HOME / f'Documents/Obsidian Vault/Agents/{agent}'
    if obs.exists():
        files = collect(obs, exts, skip_names, skip_dirs)
        for f, txt in files:
            rel = f.relative_to(obs)
            key = f'agents/{agent}/workspace/{rel}'
            write(key, txt)
            total_exported += 1
        print(f'Exported {agent}: {len(files)} workspace files')
    else:
        print(f'Skipped {agent}: obs dir not found')

shared = HOME / 'Documents/Obsidian Vault/Agents/Shared Memory'
if shared.exists():
    files = collect(shared, exts, skip_names, skip_dirs)
    for f, txt in files:
        rel = f.relative_to(shared)
        key = f'agents/Shared Memory/workspace/{rel}'
        write(key, txt)
        total_exported += 1
    print(f'Exported Shared Memory: {len(files)} workspace files')

write('agent-registry.json', json.dumps({
    'repo': 'limitless-ai-team-os',
    'agents': [{'name': a, 'profile': p} for a, p in agents_map.items()]
}, indent=2))
print(f'\nTotal files exported: {total_exported}')
print('Export complete.')
