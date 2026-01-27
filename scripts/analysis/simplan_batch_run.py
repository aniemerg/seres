#!/usr/bin/env python3
"""
Batch runner for SimPlan optimizer across a machine queue list.

Reads machine IDs from a Markdown table and runs:
  scripts/analysis/simplan_optimizer_greedy.py

Captures failures to JSONL + Markdown summary and optionally enqueues gaps.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]


def _parse_machine_ids(md_path: Path) -> List[str]:
    text = md_path.read_text(encoding="utf-8")
    machine_ids: List[str] = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0].lower() == "machine":
            continue
        if cells[0].startswith("---"):
            continue
        machine_id = cells[0]
        if machine_id:
            machine_ids.append(machine_id)
    return machine_ids


def _parse_machine_list(path: Path) -> List[str]:
    text = path.read_text(encoding="utf-8")
    machine_ids: List[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        machine_ids.append(line)
    return machine_ids


def _classify_error(err: str) -> str:
    low = err.lower()
    if "timeout" in low:
        return "timeout"
    if "no recipe" in low or "recipe not found" in low or "missing recipe" in low:
        return "missing_recipe"
    if "process not found" in low or "missing process" in low:
        return "missing_process"
    if "item not found" in low or "missing item" in low:
        return "missing_item"
    if "insufficient" in low or "not enough" in low:
        return "insufficient_input"
    if "validation" in low:
        return "validation_error"
    return "optimizer_error"


def _extract_context(err: str) -> Optional[str]:
    patterns = [
        re.compile(r"process[_\s-]?id[:=\s]+([\w\-]+)", re.IGNORECASE),
        re.compile(r"recipe[_\s-]?id[:=\s]+([\w\-]+)", re.IGNORECASE),
        re.compile(r"process\s+([\w\-]+)", re.IGNORECASE),
        re.compile(r"recipe\s+([\w\-]+)", re.IGNORECASE),
    ]
    last_context = None
    for line in err.splitlines():
        for pat in patterns:
            match = pat.search(line)
            if match:
                last_context = match.group(1)
    return last_context


def _run_optimizer(
    python_exe: str,
    machine_id: str,
    out_path: Optional[str],
    iterations: int,
    max_depth: int,
    timeout_sec: int,
    verbose: bool,
) -> Optional[Dict[str, str]]:
    cmd = [
        python_exe,
        "scripts/analysis/simplan_optimizer_greedy.py",
        "--machine-id",
        machine_id,
        "--sim-id",
        "simplan_{0}".format(machine_id),
        "--iterations",
        str(iterations),
        "--max-depth",
        str(max_depth),
    ]
    if out_path:
        cmd += ["--out", out_path]
    if verbose:
        print("Running optimizer for {0}".format(machine_id))
    try:
        result = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )
    except subprocess.TimeoutExpired:
        return {
            "error": "Timeout after {0}s while optimizing machine_id={1}".format(
                timeout_sec, machine_id
            ),
        }

    if result.returncode == 0:
        return None

    err_text = (result.stderr or "") + ("\n" + result.stdout if result.stdout else "")
    err_text = err_text.strip()
    if not err_text:
        err_text = "Optimizer failed with exit code {0} (no stderr/stdout)".format(
            result.returncode
        )
    return {"error": err_text}


def _write_markdown_summary(path: Path, failures: List[Dict[str, str]]) -> None:
    lines = [
        "# SimPlan Optimizer Failures",
        "",
        "Total failures: {0}".format(len(failures)),
        "",
        "## Checklist",
    ]
    for item in failures:
        ctx = " (context: {0})".format(item["context"]) if item.get("context") else ""
        lines.append(
            "- [ ] {0} — {1}{2}".format(item["machine_id"], item["category"], ctx)
        )

    lines.append("")
    lines.append("## Details")
    for item in failures:
        lines.append("### {0}".format(item["machine_id"]))
        lines.append("- category: {0}".format(item["category"]))
        if item.get("context"):
            lines.append("- context: {0}".format(item["context"]))
        lines.append("- timestamp: {0}".format(item["timestamp"]))
        lines.append("```")
        lines.append(item["error"])
        lines.append("```")
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def _append_jsonl(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True) + "\n")


def _clear_file(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Batch SimPlan optimizer runner.")
    parser.add_argument(
        "--queue-file",
        default="runbooks/machine_runbook_queue_sequential.md",
        help="Markdown queue file with machine IDs in first column.",
    )
    parser.add_argument(
        "--machine-list",
        help="Plaintext file with one machine ID per line.",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Start index (0-based) for machine subset.",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=-1,
        help="End index (exclusive) for machine subset; -1 means all.",
    )
    parser.add_argument(
        "--iterations", type=int, default=3, help="Optimizer iterations."
    )
    parser.add_argument("--max-depth", type=int, default=6, help="Optimizer depth.")
    parser.add_argument(
        "--timeout-sec",
        type=int,
        default=120,
        help="Per-machine timeout in seconds.",
    )
    parser.add_argument(
        "--out-dir",
        default="out/simplans",
        help="Output directory for per-machine optimized plans.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip machines that already have an optimized plan in out-dir.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress for each machine.",
    )
    parser.add_argument(
        "--python",
        default=str(REPO_ROOT / ".venv/bin/python"),
        help="Python executable to run optimizer with.",
    )
    parser.add_argument(
        "--out-jsonl",
        default="out/simplan_failures.jsonl",
        help="Failure detail JSONL output.",
    )
    parser.add_argument(
        "--out-md",
        default="out/simplan_failures.md",
        help="Markdown summary output.",
    )
    parser.add_argument(
        "--out-queue",
        default="out/simplan_failures_queue.jsonl",
        help="Queue JSONL output for manual enqueue.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite outputs instead of appending.",
    )
    parser.add_argument(
        "--enqueue",
        action="store_true",
        help="Call queue add --file on the generated queue JSONL.",
    )
    parser.add_argument(
        "--gap-type",
        default="simplan_failure",
        help="Gap type to use if enqueuing failures.",
    )
    args = parser.parse_args()

    if args.machine_list:
        list_path = (REPO_ROOT / args.machine_list).resolve()
        machine_ids = _parse_machine_list(list_path)
    else:
        queue_path = (REPO_ROOT / args.queue_file).resolve()
        machine_ids = _parse_machine_ids(queue_path)
    if not machine_ids:
        print("No machine IDs found in {0}".format(queue_path), file=sys.stderr)
        return 1

    start = max(0, args.start)
    end = args.end if args.end >= 0 else len(machine_ids)
    subset = machine_ids[start:end]

    out_jsonl = REPO_ROOT / args.out_jsonl
    out_md = REPO_ROOT / args.out_md
    out_queue = REPO_ROOT / args.out_queue

    if args.overwrite:
        _clear_file(out_jsonl)
        _clear_file(out_queue)

    out_dir = (REPO_ROOT / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    failures: List[Dict[str, str]] = []
    total = len(subset)
    for offset, machine_id in enumerate(subset, start=1):
        if args.verbose:
            print(
                "Starting {0}/{1}: {2}".format(start + offset, start + total, machine_id)
            )
        out_path = out_dir / f"{machine_id}_optimized.json"
        if args.skip_existing and out_path.exists():
            if args.verbose:
                print("SKIP (exists): {0}".format(machine_id))
            continue
        result = _run_optimizer(
            args.python,
            machine_id,
            str(out_path),
            args.iterations,
            args.max_depth,
            args.timeout_sec,
            args.verbose,
        )
        if result is None:
            if args.verbose:
                print("OK: {0}".format(machine_id))
            continue
        err_text = result["error"]
        failures.append(
            {
                "machine_id": machine_id,
                "error": err_text,
                "context": _extract_context(err_text),
                "category": _classify_error(err_text),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        )
        if args.verbose:
            print("FAIL: {0} ({1})".format(machine_id, failures[-1]["category"]))

    if failures:
        _append_jsonl(out_jsonl, failures)
        queue_rows = []
        for item in failures:
            queue_rows.append(
                {
                    "gap_type": args.gap_type,
                    "item_id": item["machine_id"],
                    "description": "SimPlan optimizer failed ({0})".format(
                        item["category"]
                    ),
                    "context": {
                        "error": item["error"],
                        "context": item["context"],
                        "timestamp": item["timestamp"],
                    },
                }
            )
        _append_jsonl(out_queue, queue_rows)

    _write_markdown_summary(out_md, failures)

    if args.enqueue and failures:
        cmd = [
            args.python,
            "-m",
            "src.cli",
            "queue",
            "add",
            "--file",
            str(out_queue),
            "--gap-type",
            args.gap_type,
        ]
        subprocess.run(cmd, cwd=str(REPO_ROOT), check=False)

    print(
        "Processed {0} machines, failures {1}".format(len(subset), len(failures))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
