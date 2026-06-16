#!/usr/bin/env bash
set -euo pipefail

TASK_DIR="queue_tasks/research_pack/ream250_bom_research"
TASK_INSTRUCTIONS="$TASK_DIR/agent.md"
TASK_VALIDATOR="$TASK_DIR/research_scripts/validate_results.py"
DEFAULT_REPO_ROOT="/home/eastrolinux/seres"

repo_root="${REPO_ROOT:-$DEFAULT_REPO_ROOT}"
agent_prefix="ream250-bom-agent"
workers=1
max_items=3
max_batches=0
ttl=7200
log_dir=""
codex_bin="${CODEX_BIN:-codex}"
codex_model="${CODEX_MODEL:-}"
codex_reasoning_effort="${CODEX_REASONING_EFFORT:-}"
codex_sandbox="${CODEX_SANDBOX:-danger-full-access}"
validate_at_end=0
dry_run=0
id_prefix="research_task:ream250_bom_row_"

usage() {
  cat <<'EOF'
Usage:
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh [options]

Runs short-lived Codex exec sessions for reAM250 BOM research queue items.
Each session gets a fresh context window and processes at most --max-items.

Options:
  --repo-root PATH       Repository root. Default: /home/eastrolinux/seres
  --agent-prefix NAME    Agent name prefix. Default: ream250-bom-agent
  --workers N           Number of parallel worker loops. Default: 1
  --max-items N         Max queue items per Codex exec session. Default: 3
  --max-batches N       Max Codex exec sessions per worker. Default: 0, until queue empty
  --ttl SECONDS         Queue lease TTL passed to the agent prompt. Default: 7200
  --log-dir PATH        Log directory. Default: out/ream250_bom_runner_logs
  --codex-bin PATH      Codex executable. Default: codex or $CODEX_BIN
  --codex-model MODEL   Codex model passed to -m/--model. Default: $CODEX_MODEL or config default
  --codex-reasoning-effort EFFORT
                       Reasoning effort passed as model_reasoning_effort.
                       Values: low, medium, high, xhigh. Default: $CODEX_REASONING_EFFORT or config default
  --codex-sandbox MODE  Codex sandbox mode. Default: danger-full-access or $CODEX_SANDBOX
                       Use workspace-write only for no-network/local-only runs.
  --id-prefix PREFIX    Queue id prefix for lease filtering.
                       Default: research_task:ream250_bom_row_
  --validate-at-end     Validate research/ream250_bom after all workers exit
  --dry-run             Print the first prompt and command, then exit
  -h, --help            Show this help

Examples:
  # Conservative single-worker run.
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh

  # Two workers, each Codex session handles at most 3 rows.
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --workers 2 --max-items 3

  # Smoke test one fresh Codex session.
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --max-batches 1

  # Smoke test one fresh Codex session with an explicit model.
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --max-batches 1 --codex-model gpt-5.3-spark

  # Smoke test GPT-5.5 with medium reasoning.
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --max-batches 1 --codex-model gpt-5.5 --codex-reasoning-effort medium

  # Rerun exactly one completed row after releasing it back to pending.
  .venv/bin/python -m src.cli queue release --id research_task:ream250_bom_row_0195_6Q --agent rerun
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --id-prefix research_task:ream250_bom_row_0195_6Q --max-items 1 --max-batches 1
EOF
}

die() {
  echo "error: $*" >&2
  exit 1
}

is_positive_int() {
  [[ "${1:-}" =~ ^[1-9][0-9]*$ ]]
}

is_nonnegative_int() {
  [[ "${1:-}" =~ ^[0-9]+$ ]]
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --agent-prefix)
      agent_prefix="${2:-}"
      shift 2
      ;;
    --workers)
      workers="${2:-}"
      shift 2
      ;;
    --max-items)
      max_items="${2:-}"
      shift 2
      ;;
    --max-batches)
      max_batches="${2:-}"
      shift 2
      ;;
    --ttl)
      ttl="${2:-}"
      shift 2
      ;;
    --log-dir)
      log_dir="${2:-}"
      shift 2
      ;;
    --codex-bin)
      codex_bin="${2:-}"
      shift 2
      ;;
    --codex-model)
      codex_model="${2:-}"
      shift 2
      ;;
    --codex-reasoning-effort)
      codex_reasoning_effort="${2:-}"
      shift 2
      ;;
    --codex-sandbox)
      codex_sandbox="${2:-}"
      shift 2
      ;;
    --id-prefix)
      id_prefix="${2:-}"
      shift 2
      ;;
    --validate-at-end)
      validate_at_end=1
      shift
      ;;
    --dry-run)
      dry_run=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown option: $1"
      ;;
  esac
done

is_positive_int "$workers" || die "--workers must be a positive integer"
is_positive_int "$max_items" || die "--max-items must be a positive integer"
is_nonnegative_int "$max_batches" || die "--max-batches must be a nonnegative integer"
is_positive_int "$ttl" || die "--ttl must be a positive integer"
[[ -n "$id_prefix" ]] || die "--id-prefix must not be empty"
case "$codex_reasoning_effort" in
  ""|low|medium|high|xhigh)
    ;;
  *)
    die "--codex-reasoning-effort must be one of: low, medium, high, xhigh"
    ;;
esac
case "$codex_sandbox" in
  read-only|workspace-write|danger-full-access)
    ;;
  *)
    die "--codex-sandbox must be one of: read-only, workspace-write, danger-full-access"
    ;;
esac

repo_root="$(cd "$repo_root" && pwd)"
[[ -d "$repo_root/.git" ]] || die "repo root does not contain .git: $repo_root"
[[ -f "$repo_root/$TASK_INSTRUCTIONS" ]] || die "missing task instructions: $TASK_INSTRUCTIONS"
[[ -f "$repo_root/$TASK_VALIDATOR" ]] || die "missing task validator: $TASK_VALIDATOR"
[[ -x "$repo_root/.venv/bin/python" ]] || die "missing .venv/bin/python; run uv sync first"

if [[ -z "$log_dir" ]]; then
  log_dir="$repo_root/out/ream250_bom_runner_logs"
elif [[ "$log_dir" != /* ]]; then
  log_dir="$repo_root/$log_dir"
fi
mkdir -p "$log_dir"

queue_gc() {
  (
    cd "$repo_root"
    .venv/bin/python -m src.cli queue gc >/dev/null
  ) || true
}

pending_count() {
  (
    cd "$repo_root"
    ID_PREFIX="$id_prefix" .venv/bin/python - <<'PY'
import fcntl
import json
import os
import time
from pathlib import Path

id_prefix = os.environ["ID_PREFIX"]
queue_path = Path("out/work_queue.jsonl")
lock_path = Path("out/work_queue.lock")
lock_path.parent.mkdir(parents=True, exist_ok=True)
now = time.time()
count = 0

if not queue_path.exists():
    print(0)
    raise SystemExit

with lock_path.open("w") as lockf:
    fcntl.flock(lockf, fcntl.LOCK_EX)
    try:
        with queue_path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if obj.get("kind") != "research":
                    continue
                if (obj.get("gap_type") or obj.get("reason")) != "research_task":
                    continue
                if not str(obj.get("id", "")).startswith(id_prefix):
                    continue
                status = obj.get("status")
                if status in (None, "pending"):
                    count += 1
                elif status == "leased" and obj.get("lease_expires_at", 0) < now:
                    count += 1
    finally:
        fcntl.flock(lockf, fcntl.LOCK_UN)

print(count)
PY
  )
}

build_prompt() {
  local agent_name="$1"
  local item_limit="$2"

  cat <<EOF
Set a goal: Process only reAM250 BOM research queue items for this short batch.

You are ${agent_name}.

Read ${TASK_INSTRUCTIONS} and follow it as the authoritative workflow.

Invocation parameters:
- process at most ${item_limit} matching queue item(s), then stop successfully
- use this exact lease command for each item:

.venv/bin/python -m src.cli queue lease --agent ${agent_name} --ttl ${ttl} --kind research --gap-type research_task --id-prefix ${id_prefix}

Only process leased items that match the kind, gap type, id prefix, output path,
allowed-edit, validation, and completion rules in ${TASK_INSTRUCTIONS}. If a
leased item does not match, release it immediately and stop.
EOF
}

run_one_batch() {
  local worker_id="$1"
  local batch_no="$2"
  local agent_name
  local log_file
  local status
  local codex_cmd

  agent_name="$(printf "%s-%02d" "$agent_prefix" "$worker_id")"
  log_file="$log_dir/${agent_name}_batch_$(printf "%04d" "$batch_no")_$(date +%Y%m%d_%H%M%S).log"

  echo "[$agent_name] starting batch $batch_no; log: $log_file"
  codex_cmd=("$codex_bin" --search)
  if [[ -n "$codex_model" ]]; then
    codex_cmd+=(-m "$codex_model")
  fi
  if [[ -n "$codex_reasoning_effort" ]]; then
    codex_cmd+=(-c "model_reasoning_effort=\"$codex_reasoning_effort\"")
  fi
  codex_cmd+=(-a on-request exec -C "$repo_root" -s "$codex_sandbox" -)
  set +e
  build_prompt "$agent_name" "$max_items" | (
    cd "$repo_root" &&
    "${codex_cmd[@]}"
  ) 2>&1 | tee "$log_file"
  status=${PIPESTATUS[1]}
  set -e

  if [[ "$status" -ne 0 ]]; then
    echo "[$agent_name] codex exec failed with status $status; see $log_file" >&2
    return "$status"
  fi
}

worker_loop() {
  local worker_id="$1"
  local batch_no=1
  local pending

  while true; do
    if [[ "$max_batches" -gt 0 && "$batch_no" -gt "$max_batches" ]]; then
      echo "[$(printf "%s-%02d" "$agent_prefix" "$worker_id")] reached --max-batches $max_batches"
      return 0
    fi

    queue_gc
    pending="$(pending_count)"
    if [[ "$pending" -eq 0 ]]; then
      echo "[$(printf "%s-%02d" "$agent_prefix" "$worker_id")] no pending matching reAM250 research tasks"
      return 0
    fi

    run_one_batch "$worker_id" "$batch_no"
    batch_no=$((batch_no + 1))
  done
}

if [[ "$dry_run" -eq 1 ]]; then
  echo "Repository: $repo_root"
  if [[ -n "$codex_model" ]]; then
    command_preview="$codex_bin --search -m $codex_model"
  else
    command_preview="$codex_bin --search"
  fi
  if [[ -n "$codex_reasoning_effort" ]]; then
    command_preview="$command_preview -c model_reasoning_effort=\\\"$codex_reasoning_effort\\\""
  fi
  echo "Command: $command_preview -a on-request exec -C $repo_root -s $codex_sandbox -"
  echo
  build_prompt "$(printf "%s-%02d" "$agent_prefix" 1)" "$max_items"
  exit 0
fi

command -v "$codex_bin" >/dev/null 2>&1 || die "codex executable not found: $codex_bin"

echo "repo_root=$repo_root"
echo "workers=$workers max_items=$max_items max_batches=$max_batches ttl=$ttl"
if [[ -n "$codex_model" ]]; then
  echo "codex_model=$codex_model"
else
  echo "codex_model=(config default)"
fi
if [[ -n "$codex_reasoning_effort" ]]; then
  echo "codex_reasoning_effort=$codex_reasoning_effort"
else
  echo "codex_reasoning_effort=(config default)"
fi
echo "codex_sandbox=$codex_sandbox"
echo "log_dir=$log_dir"

if [[ "$workers" -eq 1 ]]; then
  worker_loop 1
else
  pids=()
  for worker_id in $(seq 1 "$workers"); do
    worker_loop "$worker_id" &
    pids+=("$!")
  done

  failed=0
  for pid in "${pids[@]}"; do
    if ! wait "$pid"; then
      failed=1
    fi
  done
  [[ "$failed" -eq 0 ]] || die "one or more workers failed"
fi

if [[ "$validate_at_end" -eq 1 ]]; then
  (
    cd "$repo_root"
    .venv/bin/python "$TASK_VALIDATOR" --dir research/ream250_bom
  )
fi

echo "reAM250 BOM batch runner finished"
