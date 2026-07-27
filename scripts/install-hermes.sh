#!/usr/bin/env bash
# Download the Hermes installer, let the operator inspect it, then run it.
# Piping curl straight into bash executes whatever the server returns, unreviewed.
set -euo pipefail

INSTALLER_URL="${HERMES_INSTALLER_URL:-https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh}"
workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT
installer="$workdir/install.sh"

curl -fsSL --proto '=https' --tlsv1.2 "$INSTALLER_URL" -o "$installer"
echo "Downloaded installer: $INSTALLER_URL"
echo "sha256: $(shasum -a 256 "$installer" 2>/dev/null || sha256sum "$installer")"

if [[ "${HERMES_INSTALL_ASSUME_YES:-0}" != "1" ]]; then
  echo "Review it before running:  less $installer"
  read -r -p "Run this installer now? [y/N] " reply
  [[ "$reply" == "y" || "$reply" == "Y" ]] || { echo "Aborted."; exit 1; }
fi

bash "$installer"
hermes doctor || true
