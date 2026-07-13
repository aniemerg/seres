#!/usr/bin/env bash
set -euo pipefail

TASK_DIR="queue_tasks/research_pack/ream250_bom_to_kb_conversion"
TASK_INSTRUCTIONS="$TASK_DIR/agent.md"
DEFAULT_REPO_ROOT="/home/eastrolinux/seres"

repo_root="${REPO_ROOT:-$DEFAULT_REPO_ROOT}"
phase="row"
agent_prefix=""
max_items=1
max_batches=1
ttl=7200
codex_bin="${CODEX_BIN:-codex}"
codex_model="${CODEX_MODEL:-}"
codex_reasoning_effort="${CODEX_REASONING_EFFORT:-}"
codex_sandbox="${CODEX_SANDBOX:-workspace-write}"
dry_run=0
semantic_validate_after=0
semantic_validate_output="research/ream250_bom/kb_conversion/semantic_validate_report.md"
semantic_validate_previous_report=""
semantic_validate_fail_on_warning=0
semantic_validate_sample_size=5

usage() {
  cat <<'EOF'
Usage:
  queue_tasks/research_pack/ream250_bom_to_kb_conversion/research_scripts/run_codex_batches.sh [options]

Options:
  --phase row|merge|stage Task phase. Default: row
  --repo-root PATH        Repository root. Default: /home/eastrolinux/seres
  --agent-prefix NAME     Agent name prefix. Default depends on phase
  --max-items N           Max items per Codex exec session. Default: 1
  --max-batches N         Max Codex sessions. Default: 1
  --ttl SECONDS           Queue lease TTL. Default: 7200
  --codex-bin PATH        Codex executable. Default: codex or $CODEX_BIN
  --codex-model MODEL     Optional Codex model
  --codex-reasoning-effort low|medium|high|xhigh
  --codex-sandbox MODE    read-only|workspace-write|danger-full-access. Default: workspace-write
  --semantic-validate-after
                          Run row conversion semantic validate after all Codex sessions
  --semantic-validate-output PATH
                          Semantic validate report path. Default: research/ream250_bom/kb_conversion/semantic_validate_report.md
  --semantic-validate-previous-report PATH
                          Previous semantic validate report for new-warning comparison. Default: <semantic-validate-output>.previous.md
  --semantic-validate-sample-size N
                          Random no-warning rows to list for LLM/manual review. Default: 5
  --semantic-validate-fail-on-warning
                          Make semantic validate return non-zero when warnings are present
  --audit-*               Backward-compatible aliases for --semantic-validate-*
  --dry-run               Print prompt and command, then exit
  -h, --help              Show this help
EOF
}

die() {
  echo "error: $*" >&2
  exit 1
}

is_positive_int() {
  [[ "${1:-}" =~ ^[1-9][0-9]*$ ]]
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --phase)
      phase="${2:-}"
      shift 2
      ;;
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --agent-prefix)
      agent_prefix="${2:-}"
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
    --semantic-validate-after|--audit-after)
      semantic_validate_after=1
      shift
      ;;
    --semantic-validate-output|--audit-output)
      semantic_validate_output="${2:-}"
      shift 2
      ;;
    --semantic-validate-previous-report|--audit-previous-report)
      semantic_validate_previous_report="${2:-}"
      shift 2
      ;;
    --semantic-validate-sample-size|--audit-sample-size)
      semantic_validate_sample_size="${2:-}"
      shift 2
      ;;
    --semantic-validate-fail-on-warning|--audit-fail-on-warning)
      semantic_validate_fail_on_warning=1
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

case "$phase" in
  row)
    id_prefix="research_task:ream250_kb_row_"
    default_agent_prefix="ream250-kb-row-agent"
    ;;
  merge)
    id_prefix="research_task:ream250_kb_merge_"
    default_agent_prefix="ream250-kb-merge-agent"
    ;;
  stage)
    id_prefix="research_task:ream250_kb_stage_"
    default_agent_prefix="ream250-kb-stage-agent"
    ;;
  *)
    die "--phase must be row, merge, or stage"
    ;;
esac

is_positive_int "$max_items" || die "--max-items must be a positive integer"
is_positive_int "$max_batches" || die "--max-batches must be a positive integer"
is_positive_int "$ttl" || die "--ttl must be a positive integer"
is_positive_int "$semantic_validate_sample_size" || die "--semantic-validate-sample-size must be a positive integer"

case "$codex_reasoning_effort" in
  ""|low|medium|high|xhigh) ;;
  *) die "--codex-reasoning-effort must be one of: low, medium, high, xhigh" ;;
esac

case "$codex_sandbox" in
  read-only|workspace-write|danger-full-access) ;;
  *) die "--codex-sandbox must be read-only, workspace-write, or danger-full-access" ;;
esac

if [[ -z "$agent_prefix" ]]; then
  agent_prefix="$default_agent_prefix"
fi

repo_root="$(cd "$repo_root" && pwd)"
[[ -f "$repo_root/$TASK_INSTRUCTIONS" ]] || die "missing task instructions: $TASK_INSTRUCTIONS"
if [[ "$semantic_validate_after" -eq 1 && -z "$semantic_validate_previous_report" ]]; then
  if [[ "$semantic_validate_output" == *.md ]]; then
    semantic_validate_previous_report="${semantic_validate_output%.md}.previous.md"
  else
    semantic_validate_previous_report="${semantic_validate_output}.previous"
  fi
fi

codex_args=(exec -C "$repo_root" -s "$codex_sandbox")
if [[ -n "$codex_model" ]]; then
  codex_args+=(-m "$codex_model")
fi
if [[ -n "$codex_reasoning_effort" ]]; then
  codex_args+=(-c "model_reasoning_effort=$codex_reasoning_effort")
fi

for ((batch=1; batch<=max_batches; batch++)); do
  agent_name="$(printf "%s-%02d" "$agent_prefix" "$batch")"
  prompt="Read $TASK_INSTRUCTIONS and follow it as $agent_name. Process at most $max_items queue item(s). Use this exact lease filter: .venv/bin/python -m src.cli queue lease --agent $agent_name --ttl $ttl --kind research --gap-type research_task --id-prefix $id_prefix"

  if [[ "$dry_run" -eq 1 ]]; then
    printf 'Command: %q' "$codex_bin"
    printf ' %q' "${codex_args[@]}"
    printf ' %q\n' "$prompt"
    if [[ "$semantic_validate_after" -eq 1 ]]; then
      printf 'Semantic validate command: %q' "$repo_root/.venv/bin/python"
      printf ' %q' "$repo_root/$TASK_DIR/research_scripts/semantic_validate_row_conversions.py"
      printf ' %q' --output
      printf ' %q' "$semantic_validate_output"
      if [[ -n "$semantic_validate_previous_report" ]]; then
        printf ' %q' --previous-report
        printf ' %q' "$semantic_validate_previous_report"
      fi
      printf ' %q' --sample-size
      printf ' %q' "$semantic_validate_sample_size"
      if [[ "$semantic_validate_fail_on_warning" -eq 1 ]]; then
        printf ' %q' --fail-on-warning
      fi
      printf '\n'
    fi
    printf '\nPrompt:\n%s\n' "$prompt"
    exit 0
  fi

  "$codex_bin" "${codex_args[@]}" "$prompt"
done

if [[ "$semantic_validate_after" -eq 1 ]]; then
  semantic_validate_output_abs="$semantic_validate_output"
  if [[ "$semantic_validate_output_abs" != /* ]]; then
    semantic_validate_output_abs="$repo_root/$semantic_validate_output_abs"
  fi
  semantic_validate_previous_abs="$semantic_validate_previous_report"
  if [[ "$semantic_validate_previous_abs" != /* ]]; then
    semantic_validate_previous_abs="$repo_root/$semantic_validate_previous_abs"
  fi
  if [[ -f "$semantic_validate_output_abs" ]]; then
    mkdir -p "$(dirname "$semantic_validate_previous_abs")"
    cp "$semantic_validate_output_abs" "$semantic_validate_previous_abs"
  fi
  semantic_validate_cmd=(
    "$repo_root/.venv/bin/python"
    "$repo_root/$TASK_DIR/research_scripts/semantic_validate_row_conversions.py"
    --output
    "$semantic_validate_output"
    --previous-report
    "$semantic_validate_previous_report"
    --sample-size
    "$semantic_validate_sample_size"
  )
  if [[ "$semantic_validate_fail_on_warning" -eq 1 ]]; then
    semantic_validate_cmd+=(--fail-on-warning)
  fi
  "${semantic_validate_cmd[@]}"
fi
