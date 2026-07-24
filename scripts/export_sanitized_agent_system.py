#!/usr/bin/env python3
"""Refresh this repo from a live Hermes/Obsidian agent setup, with secret redaction."""
from pathlib import Path
from typing import Optional

from agent_export_lib import (
    AGENT_PROFILES,
    REPO_ROOT,
    SHARED_MEMORY_DIR,
    export_workspace,
    profile_config_path,
    reset_export_dirs,
    root_config_path,
    soul_path,
    workspace_path,
    write_agent_registry,
    write_sanitized,
)


def safe_read(path: Path) -> Optional[str]:
    """Read text from path, returning None on iCloud/simulated file errors."""
    try:
        return path.read_text(errors='ignore')
    except OSError:
        return None


def copy_text(src: Path, rel: str) -> None:
    text = safe_read(src) if src.exists() else None
    if text is not None:
        write_sanitized(rel, text)


def main() -> None:
    reset_export_dirs()
    copy_text(root_config_path(), 'configs/root/config.example.yaml')

    for agent, profile in AGENT_PROFILES.items():
        if profile != 'default':
            copy_text(profile_config_path(profile), f'configs/profiles/{profile}/config.example.yaml')
        copy_text(soul_path(profile), f'agents/{agent}/SOUL.md')

        workspace = workspace_path(agent)
        if workspace.exists():
            export_workspace(workspace, f'agents/{agent}/workspace', safe_read)

    if SHARED_MEMORY_DIR.exists():
        export_workspace(SHARED_MEMORY_DIR, 'agents/Shared Memory/workspace', safe_read)

    write_agent_registry()
    print('Export complete:', REPO_ROOT)


if __name__ == '__main__':
    main()
