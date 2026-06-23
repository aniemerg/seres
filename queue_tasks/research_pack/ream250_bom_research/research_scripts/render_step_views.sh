#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"
ARGS_FILE="$(mktemp)"
trap 'rm -f "$ARGS_FILE"' EXIT

printf '%s\0' "$@" > "$ARGS_FILE"

RENDER_STEP_ARGS_FILE="$ARGS_FILE" exec "$REPO_ROOT/.tools/freecad/freecadcmd" -c \
  "import os, sys; sys.path.insert(0, '$SCRIPT_DIR'); import render_step_views; raw = open(os.environ['RENDER_STEP_ARGS_FILE'], 'rb').read(); args = [part.decode() for part in raw.split(b'\0') if part]; render_step_views.main(args)"
