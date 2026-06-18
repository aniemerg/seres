#!/usr/bin/env bash
set -euo pipefail

TASK_DIR="queue_tasks/research_pack/ream250_bom_research"
TASK_INSTRUCTIONS="$TASK_DIR/agent.md"
TASK_VALIDATOR="$TASK_DIR/research_scripts/validate_results.py"
TASK_OUTPUT_AUDIT="$TASK_DIR/research_scripts/audit_queue_outputs.py"
DEFAULT_REPO_ROOT="/home/eastrolinux/seres"
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")"
ORIGINAL_ARGS=("$@")

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
batch_timeout=0
validate_at_end=0
dry_run=0
id_prefix="research_task:ream250_bom_row_"
detach=0
no_terminal_stream=0
run_id="${REAM250_BOM_RUN_ID:-$(date +%Y%m%d_%H%M%S)_$$}"
run_log=""
run_events=""
heartbeat_file=""
status_dir=""
heartbeat_pid=""

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
  --batch-timeout SECONDS
                       Optional timeout per Codex exec batch. Default: 0, disabled
  --id-prefix PREFIX    Queue id prefix for lease filtering.
                       Default: research_task:ream250_bom_row_
  --detach             Relaunch in a background session and return immediately.
                       Use this for overnight runs or unstable terminal windows.
  --no-terminal-stream Write all runner output to the run log without streaming
                       it back to the invoking terminal.
  --validate-at-end     Audit done queue outputs after all workers exit
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
  queue_tasks/research_pack/ream250_bom_research/research_scripts/run_codex_batches.sh --max-batches 1 --codex-model gpt-5.3-codex-spark

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
    --batch-timeout)
      batch_timeout="${2:-}"
      shift 2
      ;;
    --id-prefix)
      id_prefix="${2:-}"
      shift 2
      ;;
    --detach)
      detach=1
      shift
      ;;
    --no-terminal-stream)
      no_terminal_stream=1
      shift
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
is_nonnegative_int "$batch_timeout" || die "--batch-timeout must be a nonnegative integer"
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
[[ -f "$repo_root/$TASK_OUTPUT_AUDIT" ]] || die "missing task output audit: $TASK_OUTPUT_AUDIT"
[[ -x "$repo_root/.venv/bin/python" ]] || die "missing .venv/bin/python; run uv sync first"

if [[ -z "$log_dir" ]]; then
  log_dir="$repo_root/out/ream250_bom_runner_logs"
elif [[ "$log_dir" != /* ]]; then
  log_dir="$repo_root/$log_dir"
fi
mkdir -p "$log_dir"
run_log="$log_dir/run_${run_id}.log"
run_events="$log_dir/run_${run_id}_events.tsv"
heartbeat_file="$log_dir/run_${run_id}.heartbeat"
status_dir="$log_dir/run_${run_id}_status"
pid_file="$log_dir/run_${run_id}.pid"
launcher_log="$log_dir/run_${run_id}_launcher.log"

timestamp_utc() {
  date -u +%Y-%m-%dT%H:%M:%SZ
}

log_event() {
  local event="$1"
  shift || true
  {
    printf "%s\t%s" "$(timestamp_utc)" "$event"
    for field in "$@"; do
      printf "\t%s" "$field"
    done
    printf "\n"
  } >> "$run_events"
}

snapshot_queue() {
  local label="$1"
  (
    cd "$repo_root"
    .venv/bin/python -m src.cli queue ls > "$log_dir/run_${run_id}_queue_${label}.json"
  ) || true
}

start_heartbeat() {
  (
    while true; do
      printf "%s pid=%s ppid=%s\n" "$(timestamp_utc)" "$$" "$PPID" > "$heartbeat_file"
      sleep 60
    done
  ) &
  heartbeat_pid="$!"
}

stop_heartbeat() {
  if [[ -n "${heartbeat_pid:-}" ]]; then
    kill "$heartbeat_pid" >/dev/null 2>&1 || true
    wait "$heartbeat_pid" >/dev/null 2>&1 || true
    heartbeat_pid=""
  fi
}

on_signal() {
  local sig="$1"
  trap - INT TERM HUP EXIT
  log_event "signal" "signal=$sig" "pid=$$" "ppid=$PPID"
  echo "runner received $sig; diagnostics are in $log_dir/run_${run_id}*"
  snapshot_queue "signal_${sig}"
  stop_heartbeat
  case "$sig" in
    INT) exit 130 ;;
    TERM) exit 143 ;;
    HUP) exit 129 ;;
    *) exit 1 ;;
  esac
}

on_exit() {
  local status="$1"
  log_event "runner_exit" "status=$status"
  snapshot_queue "exit"
  stop_heartbeat
}

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
  local active_file
  local status
  local codex_cmd
  local run_cmd

  agent_name="$(printf "%s-%02d" "$agent_prefix" "$worker_id")"
  log_file="$log_dir/${agent_name}_batch_$(printf "%04d" "$batch_no")_$(date +%Y%m%d_%H%M%S).log"
  active_file="$status_dir/${agent_name}_batch_$(printf "%04d" "$batch_no").active"

  echo "[$agent_name] starting batch $batch_no; log: $log_file"
  printf "started_at=%s\nagent=%s\nworker_id=%s\nbatch=%s\nlog_file=%s\n" \
    "$(timestamp_utc)" "$agent_name" "$worker_id" "$batch_no" "$log_file" > "$active_file"
  log_event "batch_start" "agent=$agent_name" "worker=$worker_id" "batch=$batch_no" "log_file=$log_file"
  codex_cmd=("$codex_bin" --search)
  if [[ -n "$codex_model" ]]; then
    codex_cmd+=(-m "$codex_model")
  fi
  if [[ -n "$codex_reasoning_effort" ]]; then
    codex_cmd+=(-c "model_reasoning_effort=\"$codex_reasoning_effort\"")
  fi
  codex_cmd+=(-a on-request exec -C "$repo_root" -s "$codex_sandbox" -)
  run_cmd=("${codex_cmd[@]}")
  if [[ "$batch_timeout" -gt 0 ]]; then
    run_cmd=(timeout --preserve-status "$batch_timeout" "${codex_cmd[@]}")
  fi
  set +e
  build_prompt "$agent_name" "$max_items" | (
    cd "$repo_root" &&
    "${run_cmd[@]}"
  ) 2>&1 | tee "$log_file"
  status=${PIPESTATUS[1]}
  set -e
  log_event "batch_exit" "agent=$agent_name" "worker=$worker_id" "batch=$batch_no" "status=$status" "log_file=$log_file"
  rm -f "$active_file"

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
if [[ "$batch_timeout" -gt 0 ]]; then
  command -v timeout >/dev/null 2>&1 || die "timeout executable not found; required by --batch-timeout"
fi
mkdir -p "$status_dir"

if [[ "$detach" -eq 1 ]]; then
  detached_args=()
  has_no_terminal_stream=0
  for arg in "${ORIGINAL_ARGS[@]}"; do
    case "$arg" in
      --detach)
        ;;
      --no-terminal-stream)
        has_no_terminal_stream=1
        detached_args+=("$arg")
        ;;
      *)
        detached_args+=("$arg")
        ;;
    esac
  done
  if [[ "$has_no_terminal_stream" -eq 0 ]]; then
    detached_args+=("--no-terminal-stream")
  fi

  echo "starting detached reAM250 BOM runner"
  echo "run_id=$run_id"
  echo "run_log=$run_log"
  echo "run_events=$run_events"
  echo "heartbeat_file=$heartbeat_file"
  echo "status_dir=$status_dir"
  echo "launcher_log=$launcher_log"
  if command -v setsid >/dev/null 2>&1; then
    (
      cd "$repo_root"
      REAM250_BOM_RUN_ID="$run_id" nohup setsid "$SCRIPT_PATH" "${detached_args[@]}" \
        > "$launcher_log" 2>&1 < /dev/null &
      printf "%s\n" "$!" > "$pid_file"
    )
  else
    (
      cd "$repo_root"
      REAM250_BOM_RUN_ID="$run_id" nohup "$SCRIPT_PATH" "${detached_args[@]}" \
        > "$launcher_log" 2>&1 < /dev/null &
      printf "%s\n" "$!" > "$pid_file"
    )
  fi
  echo "pid_file=$pid_file"
  echo "pid=$(cat "$pid_file")"
  exit 0
fi

if [[ "$no_terminal_stream" -eq 1 ]]; then
  exec >> "$run_log" 2>&1
else
  exec > >(tee -a "$run_log") 2>&1
fi
trap 'on_signal INT' INT
trap 'on_signal TERM' TERM
trap 'on_signal HUP' HUP
trap 'on_exit $?' EXIT
start_heartbeat

echo "repo_root=$repo_root"
echo "workers=$workers max_items=$max_items max_batches=$max_batches ttl=$ttl"
echo "run_id=$run_id"
echo "run_log=$run_log"
echo "run_events=$run_events"
echo "heartbeat_file=$heartbeat_file"
echo "status_dir=$status_dir"
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
echo "batch_timeout=$batch_timeout"
echo "log_dir=$log_dir"
log_event "runner_start" "pid=$$" "ppid=$PPID" "repo_root=$repo_root" "workers=$workers" "max_items=$max_items" "max_batches=$max_batches" "ttl=$ttl" "id_prefix=$id_prefix" "codex_model=${codex_model:-config_default}" "codex_reasoning_effort=${codex_reasoning_effort:-config_default}" "codex_sandbox=$codex_sandbox" "batch_timeout=$batch_timeout"
snapshot_queue "start"

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
    .venv/bin/python "$TASK_OUTPUT_AUDIT"
  )
fi

echo "reAM250 BOM batch runner finished"
