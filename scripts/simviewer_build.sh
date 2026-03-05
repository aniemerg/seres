#!/usr/bin/env bash
set -euo pipefail

# Build the simviewer from repo root:
#   scripts/simviewer_build.sh [sim_id] [--install] [--preview|--no-preview]
#
# Examples:
#   scripts/simviewer_build.sh
#   scripts/simviewer_build.sh runbook_queue_sequential
#   scripts/simviewer_build.sh runbook_queue_sequential --install --preview
#   scripts/simviewer_build.sh runbook_queue_sequential --no-preview

SIM_ID="runbook_queue_sequential"
DO_INSTALL=false
DO_PREVIEW=true

for arg in "$@"; do
  case "$arg" in
    --install)
      DO_INSTALL=true
      ;;
    --preview)
      DO_PREVIEW=true
      ;;
    --no-preview)
      DO_PREVIEW=false
      ;;
    *)
      SIM_ID="$arg"
      ;;
  esac
done

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_DIR="$REPO_ROOT/apps/simviewer"
PYTHON_BIN="$REPO_ROOT/.venv/bin/python"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Error: $PYTHON_BIN not found or not executable." >&2
  echo "Run 'uv sync' from repo root first." >&2
  exit 1
fi

if [[ ! -d "$APP_DIR" ]]; then
  echo "Error: simviewer app directory not found: $APP_DIR" >&2
  exit 1
fi

echo "==> Exporting simviewer data for sim: $SIM_ID"
"$PYTHON_BIN" -m src.cli sim export-view \
  --sim-id "$SIM_ID" \
  --out "$APP_DIR/public"

pushd "$APP_DIR" >/dev/null

if [[ -f "$HOME/.nvm/nvm.sh" ]]; then
  # shellcheck source=/dev/null
  source "$HOME/.nvm/nvm.sh"
  if command -v nvm >/dev/null 2>&1; then
    nvm use 24 >/dev/null
  fi
fi

if [[ "$DO_INSTALL" == true || ! -d node_modules ]]; then
  echo "==> Installing npm dependencies"
  npm install
fi

echo "==> Building simviewer"
npm run build

popd >/dev/null

echo "==> Done"
echo "Built viewer: $APP_DIR/dist/index.html"
echo "Data files:   $APP_DIR/dist/data/"

if [[ "$DO_PREVIEW" == true ]]; then
  echo "==> Starting preview server"
  cd "$APP_DIR"
  npm run preview
fi
