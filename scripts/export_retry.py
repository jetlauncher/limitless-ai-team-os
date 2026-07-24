#!/usr/bin/env python3
"""Export using cat (subprocess) to handle iCloud cloud-optimized files."""
import subprocess
from pathlib import Path

from agent_export_lib import (
    AGENT_PROFILES,
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


def cat_file(path: Path) -> str:
    """Read file using cat subprocess — works with iCloud cloud-optimized files."""
    try:
        result = subprocess.run(
            ['cat', str(path)],
            capture_output=True,
            timeout=30,
            text=True,
            errors='ignore',
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return ''
    except Exception:
        return ''


def main() -> None:
    reset_export_dirs()

    root_config = root_config_path()
    if root_config.exists():
        write_sanitized('configs/root/config.example.yaml', cat_file(root_config))
        print('Exported configs/root/config.example.yaml')

    total_exported = 0
    for agent, profile in AGENT_PROFILES.items():
        cfg = profile_config_path(profile)
        if profile != 'default' and cfg.exists():
            write_sanitized(f'configs/profiles/{profile}/config.example.yaml', cat_file(cfg))
            print(f'Exported configs/profiles/{profile}/config.example.yaml')

        soul = soul_path(profile)
        if soul.exists():
            text = cat_file(soul)
            write_sanitized(f'agents/{agent}/SOUL.md', text)
            total_exported += 1
            print(f'Exported {agent}/SOUL.md ({len(text)} bytes)')

        workspace = workspace_path(agent)
        if workspace.exists():
            count = export_workspace(workspace, f'agents/{agent}/workspace', cat_file)
            total_exported += count
            print(f'Exported {agent}: {count} workspace files')
        else:
            print(f'Skipped {agent}: obs dir not found')

    if SHARED_MEMORY_DIR.exists():
        count = export_workspace(SHARED_MEMORY_DIR, 'agents/Shared Memory/workspace', cat_file)
        total_exported += count
        print(f'Exported Shared Memory: {count} workspace files')

    write_agent_registry()
    print(f'\nTotal files exported: {total_exported}')
    print('Export complete.')


if __name__ == '__main__':
    main()
