#!/usr/bin/env python3
"""Refresh this repo from a live Hermes/Obsidian agent setup, with secret redaction."""
from pathlib import Path
import re, shutil, json, os, sys

REPO = Path(__file__).resolve().parents[1]
HOME = Path.home()

SECRET_PATTERNS = [
    (re.compile(r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'), '[REDACTED_TELEGRAM_BOT_TOKEN]'),
    (re.compile(r'\bgh[opsru]_[A-Za-z0-9_]{20,}\b'), '[REDACTED_GITHUB_TOKEN]'),
    (re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_OPENAI_KEY]'),
    (re.compile(r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_OPENROUTER_KEY]'),
    (re.compile(r'\bntn_[A-Za-z0-9_-]{20,}\b'), '[REDACTED_NOTION_TOKEN]'),
    (re.compile(r'\bsecret_[A-Za-z0-9_-]{20,}\b'), '[REDACTED_SECRET]'),
    (re.compile(r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'), '[REDACTED_AIRTABLE_PAT]'),
    (re.compile(r'Bearer\s+[A-Za-z0-9._-]{20,}', re.I), 'Bearer [REDACTED]'),
    (re.compile(r'(api[_-]?key\s*[:=]\s*)([^\s\n\"\'\x5c]+)', re.I), r'\1[REDACTED]'),
    (re.compile(r'(token\s*[:=]\s*)([^\s\n\"\'\x5c]+)', re.I), r'\1[REDACTED]'),
    (re.compile(r'(password\s*[:=]\s*)([^\s\n\"\'\x5c]+)', re.I), r'\1[REDACTED]'),
]

def sanitize(text: str) -> str:
    for pat, repl in SECRET_PATTERNS:
        text = pat.sub(repl, text)
    return text

def write(rel, text):
    p = REPO / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(sanitize(text), encoding='utf-8')

def safe_read(p):
    try:
        return p.read_text(errors='ignore')
    except OSError:
        return None

def copy_text(src, rel):
    if src.exists():
        write(rel, src.read_text(errors='ignore'))

def rglob_safe(base_dir: Path):
    _ext = {'.md', '.txt', '.yaml', '.yml', '.json'}
    results = []
    stack = [base_dir]
    while stack:
        d = stack.pop()
        try:
            for entry in d.iterdir():
                if entry.is_symlink():
                    continue  # skip symlinks (iCloud Content Drops etc.)
                if entry.is_file() and entry.suffix.lower() in _ext:
                    results.append(entry)
                elif entry.is_dir():
                    stack.append(entry)
        except OSError:
            continue
    return results



sys.stderr.write('Exporting agents/configs from live OS...\n')
sys.stderr.flush()

AGENTS = {'Hermes': 'default', 'Blaze': 'blaze', 'Bolt': 'bolt', 
          'Kaijeaw': 'kaijeaw', 'Protocol': 'protocol', 'Qwen': 'qwen', 
          'Signal': 'signal', 'Zegna': 'zegna'}

for d in ['agents', 'configs']:
    p = REPO / d
    if p.exists():
        shutil.rmtree(p)

# configs
cfg_root = HOME / '.hermes/config.yaml'
if cfg_root.exists():
    copy_text(cfg_root, 'configs/root/config.example.yaml')
else:
    sys.stderr.write('WARN: root .hermes/config.yaml missing\n')
    sys.stderr.flush()

for agent, prof in AGENTS.items():
    if prof != 'default':
        p_cfg = HOME / f'.hermes/profiles/{prof}/config.yaml'
        if p_cfg.exists():
            copy_text(p_cfg, f'configs/profiles/{prof}/config.example.yaml')
    
    soul_path = HOME / ('.hermes/SOUL.md' if prof == 'default' 
                         else f'.hermes/profiles/{prof}/SOUL.md')
    copy_text(soul_path, f'agents/{agent}/SOUL.md')

sys.stderr.write(f'Done: configs for {len(AGENTS)} agents\n')
sys.stderr.flush()

# Agent workspace files
for agent in AGENTS:
    obs = HOME / f'Documents/Obsidian Vault/Agents/{agent}'
    if obs.exists():
        sys.stderr.write(f'  rglob({obs.name})...\n')
        sys.stderr.flush()
        found = rglob_safe(obs)
        sys.stderr.write(f'    {len(found)} files\n')
        sys.stderr.flush()
        for f in found:
            if f.suffix.lower() in ['.md', '.txt', '.yaml', '.yml', '.json']:
                rel = f.relative_to(obs)
                txt = safe_read(f)
                if txt is None:
                    continue
                if len(txt) > 100000:
                    txt = txt[:100000] + '\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
                write(f'agents/{agent}/workspace/{rel}', txt)

# Shared memory
shared = HOME / 'Documents/Obsidian Vault/Shared Memory'
if shared.exists():
    sys.stderr.write('  rglob(Shared Memory)...\n')
    found = rglob_safe(shared)
    for f in found:
        if f.suffix.lower() in ['.md', '.txt', '.yaml', '.yml', '.json']:
            rel = f.relative_to(shared)
            txt = safe_read(f)
            if txt is None:
                continue
            if len(txt) > 100000:
                txt = txt[:100000] + '\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
            write(f'agents/Shared Memory/workspace/{rel}', txt)

write('agent-registry.json', json.dumps({
    'repo': 'limitless-ai-team-os',
    'agents': [{'name': a, 'profile': p} for a, p in AGENTS.items()]
}, indent=2))

sys.stderr.write(f'Export complete: {REPO}\n')
sys.stderr.flush()
print('Export complete:', REPO)
