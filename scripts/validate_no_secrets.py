#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
patterns=[
 ('telegram bot token', r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'),
 ('github token', r'\bgh[opsru]_[A-Za-z0-9_]{20,}\b'),
 ('openai key', r'\bsk-[A-Za-z0-9_-]{20,}\b'),
 ('openrouter key', r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'),
 ('notion token', r'\bntn_[A-Za-z0-9_-]{20,}|\bsecret_[A-Za-z0-9_-]{20,}'),
 ('airtable pat', r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'),
]
found=[]
for p in ROOT.rglob('*'):
    if p.is_dir() or '.git' in p.parts: continue
    if p.name == 'validate_no_secrets.py': continue
    txt=p.read_text(errors='ignore')
    for name,pat in patterns:
        if re.search(pat, txt): found.append((str(p.relative_to(ROOT)), name))
if found:
    print('Potential secrets found:')
    for f,n in found: print(f' - {f}: {n}')
    sys.exit(1)
print('No obvious secrets found.')
