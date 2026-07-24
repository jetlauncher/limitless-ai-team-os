#!/usr/bin/env python3
"""Fail if any committed file looks like it contains a real credential."""
import sys

from agent_export_lib import REPO_ROOT, find_secrets

SELF_NAMES = {'validate_no_secrets.py', 'agent_export_lib.py'}


def main() -> int:
    found = []
    for path in REPO_ROOT.rglob('*'):
        if path.is_dir() or '.git' in path.parts:
            continue
        if path.name in SELF_NAMES:
            continue
        for name in find_secrets(path.read_text(errors='ignore')):
            found.append((str(path.relative_to(REPO_ROOT)), name))

    if found:
        print('Potential secrets found:')
        for rel, name in found:
            print(f' - {rel}: {name}')
        return 1
    print('No obvious secrets found.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
