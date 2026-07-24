#!/usr/bin/env python3
"""Refresh this repo from a live Hermes/Obsidian agent setup, with secret redaction."""
from pathlib import Path
import shutil, json, os

from sanitize_lib import harden_config, sanitize

REPO = Path(__file__).resolve().parents[1]
HOME = Path.home()

def write(rel, text, config=False):
    p=REPO/rel; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(harden_config(text) if config else sanitize(text), encoding='utf-8')

def safe_read(p):
    """Read text from path, returning None on iCloud/simulated file errors."""
    try:
        return p.read_text(errors='ignore')
    except OSError:
        return None

def copy_text(src, rel, config=False):
    if src.exists(): write(rel, src.read_text(errors='ignore'), config=config)


def rglob_safe(base_dir: Path):
    """Walk directory tree, catching OSError on individual dirs (iCloud Content Drops, etc.)."""
    results = []
    for root, dirs, files in os.walk(base_dir):
        # Skip problematic dirs silently
        for d in dirs[:]:
            dp = os.path.join(root, d)
            try:
                os.scandir(dp)
            except OSError:
                dirs.remove(d)
        for fn in files:
            fp = os.path.join(root, fn)
            try:
                p = Path(fp)
                if p.is_file():
                    results.append(p)
            except OSError:
                pass
    return results


AGENTS={'Hermes':'default','Blaze':'blaze','Bolt':'bolt','Kaijeaw':'kaijeaw','Protocol':'protocol','Qwen':'qwen','Signal':'signal','Zegna':'zegna'}
for d in ['agents','configs']:
    p=REPO/d
    if p.exists(): shutil.rmtree(p)
# configs
copy_text(HOME/'.hermes/config.yaml','configs/root/config.example.yaml', config=True)
for agent, prof in AGENTS.items():
    cfg=HOME/f'.hermes/profiles/{prof}/config.yaml'
    if prof!='default': copy_text(cfg, f'configs/profiles/{prof}/config.example.yaml', config=True)
    soul=HOME/('.hermes/SOUL.md' if prof=='default' else f'.hermes/profiles/{prof}/SOUL.md')
    copy_text(soul, f'agents/{agent}/SOUL.md')
    obs=HOME/f'Documents/Obsidian Vault/Agents/{agent}'
    if obs.exists():
        for f in rglob_safe(obs):
            if f.is_file() and f.suffix.lower() in ['.md','.txt','.yaml','.yml','.json'] and not any(skip in str(f) for skip in ['Content Archive','Content Drops','Generated Assets','node_modules','ACCESS-TOKENS.md']) and not f.name.endswith('_state.json') and f.name != 'state.json':
                rel=f.relative_to(obs)
                txt=safe_read(f)
                if txt is None: continue
                if len(txt)>120000: txt=txt[:120000]+'\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
                write(f'agents/{agent}/workspace/{rel}', txt)
shared=HOME/'Documents/Obsidian Vault/Agents/Shared Memory'
if shared.exists():
    for f in rglob_safe(shared):
        if f.is_file() and f.suffix.lower() in ['.md','.txt','.yaml','.yml','.json'] and not any(skip in str(f) for skip in ['ACCESS-TOKENS.md','node_modules','Generated Assets']):
            rel=f.relative_to(shared)
            txt=safe_read(f)
            if txt is None: continue
            if len(txt)>120000: txt=txt[:120000]+'\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
            write(f'agents/Shared Memory/workspace/{rel}', txt)
write('agent-registry.json', json.dumps({'repo':'limitless-ai-team-os','agents':[{'name':a,'profile':p} for a,p in AGENTS.items()]}, indent=2))
print('Export complete:', REPO)
