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


def scan_text(txt):
    """Return list of pattern names whose regex matches anywhere in txt."""
    return [name for name, pat in patterns if re.search(pat, txt)]


def scan_tree(root):
    """Scan every non-.git file under root, returning (relative_path, name) hits."""
    root = Path(root)
    found = []
    for p in root.rglob('*'):
        if p.is_dir() or '.git' in p.parts:
            continue
        if p.name == 'validate_no_secrets.py':
            continue
        txt = p.read_text(errors='ignore')
        for name in scan_text(txt):
            found.append((str(p.relative_to(root)), name))
    return found


def main(root=ROOT):
    found = scan_tree(root)
    if found:
        print('Potential secrets found:')
        for f, n in found:
            print(f' - {f}: {n}')
        return 1
    print('No obvious secrets found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
