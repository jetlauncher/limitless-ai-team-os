#!/usr/bin/env python3
"""Refresh this repo from a live Hermes/Obsidian agent setup, with secret redaction."""
from pathlib import Path
import re, shutil, json, os, subprocess
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
    (re.compile(r'(api[_-]?key\s*[:=]\s*)([^\s\n\"\']+)', re.I), r'\1[REDACTED]'),
    (re.compile(r'(token\s*[:=]\s*)([^\s\n\"\']+)', re.I), r'\1[REDACTED]'),
    (re.compile(r'(password\s*[:=]\s*)([^\s\n\"\']+)', re.I), r'\1[REDACTED]'),
]
def sanitize(text:str)->str:
    for pat,repl in SECRET_PATTERNS:
        text=pat.sub(repl,text)
    return text

def write(rel, text):
    p=REPO/rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(sanitize(text), encoding='utf-8')

def copy_text(src, rel):
    if src.exists(): write(rel, src.read_text(errors='ignore'))

AGENTS={'Hermes':'default','Blaze':'blaze','Bolt':'bolt','Kaijeaw':'kaijeaw','Protocol':'protocol','Qwen':'qwen','Signal':'signal','Zegna':'zegna'}
for d in ['agents','configs']:
    p=REPO/d
    if p.exists(): shutil.rmtree(p)
# configs
copy_text(HOME/'.hermes/config.yaml','configs/root/config.example.yaml')
for agent, prof in AGENTS.items():
    cfg=HOME/f'.hermes/profiles/{prof}/config.yaml'
    if prof!='default': copy_text(cfg, f'configs/profiles/{prof}/config.example.yaml')
    soul=HOME/('.hermes/SOUL.md' if prof=='default' else f'.hermes/profiles/{prof}/SOUL.md')
    copy_text(soul, f'agents/{agent}/SOUL.md')
    obs=HOME/f'Documents/Obsidian Vault/Agents/{agent}'
    if obs.exists():
        for f in obs.rglob('*'):
            if f.is_file() and f.suffix.lower() in ['.md','.txt','.yaml','.yml','.json'] and not any(skip in str(f) for skip in ['Content Archive','Generated Assets','node_modules','ACCESS-TOKENS.md']) and not f.name.endswith('_state.json') and f.name != 'state.json':
                rel=f.relative_to(obs)
                txt=f.read_text(errors='ignore')
                if len(txt)>120000: txt=txt[:120000]+'\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
                write(f'agents/{agent}/workspace/{rel}', txt)
shared=HOME/'Documents/Obsidian Vault/Agents/Shared Memory'
if shared.exists():
    for f in shared.rglob('*'):
        if f.is_file() and f.suffix.lower() in ['.md','.txt','.yaml','.yml','.json'] and not any(skip in str(f) for skip in ['ACCESS-TOKENS.md','node_modules','Generated Assets']):
            rel=f.relative_to(shared); txt=f.read_text(errors='ignore')
            if len(txt)>120000: txt=txt[:120000]+'\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
            write(f'agents/Shared Memory/workspace/{rel}', txt)
write('agent-registry.json', json.dumps({'repo':'limitless-ai-team-os','agents':[{'name':a,'profile':p} for a,p in AGENTS.items()]}, indent=2))
print('Export complete:', REPO)
