#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/export_sanitized_agent_system.py
git add -A agents configs agent-registry.json
# Validate after staging so the scan covers exactly what would be pushed.
python3 scripts/validate_no_secrets.py
if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi
git commit -m "chore: daily sanitized agent system refresh"
git push
