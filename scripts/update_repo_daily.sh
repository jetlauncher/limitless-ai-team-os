#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/export_sanitized_agent_system.py
python3 scripts/validate_no_secrets.py
git add .
if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi
git commit -m "chore: daily sanitized agent system refresh"
git push
