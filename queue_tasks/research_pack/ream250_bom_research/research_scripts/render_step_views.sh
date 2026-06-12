#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

exec "$REPO_ROOT/.tools/freecad/freecadcmd" -c \
  "import sys; sys.path.insert(0, '$SCRIPT_DIR'); import render_step_views; args = sys.argv[sys.argv.index('--pass') + 1:] if '--pass' in sys.argv else []; render_step_views.main(args)" \
  --pass "$@"
