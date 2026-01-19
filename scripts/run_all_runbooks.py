#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "runbooks" / "machine_runbook_queue_sequential.md"
RUNBOOKS_DIR = ROOT / "runbooks"
RUNBOOK_CMD = [
    str(ROOT / ".venv" / "bin" / "python"),
    str(ROOT / "scripts" / "debug" / "run_runbook_debug.py"),
    "sim",
    "runbook",
]


def load_queue_rows():
    rows = []
    runbook_map = {}
    with QUEUE_PATH.open(encoding="utf-8") as f:
        for i, line in enumerate(f):
            if not line.startswith("| "):
                rows.append(line)
                continue
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(parts) < 3 or parts[0] == "Machine":
                rows.append(line)
                continue
            machine, runbook, isru = parts[:3]
            m = re.search(r"\[runbook\]\(([^)]+)\)", runbook)
            if m:
                runbook_path = m.group(1)
                runbook_map[runbook_path] = (i, machine, isru)
            rows.append(line)
    return rows, runbook_map


def run_runbook(runbook_path):
    cmd = RUNBOOK_CMD + ["--file", str(RUNBOOKS_DIR / runbook_path)]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT)
    result = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, env=env)
    if result.returncode == 0:
        return True, ""
    combined = (result.stderr or "") + "\n" + (result.stdout or "")
    lines = [ln.strip() for ln in combined.splitlines() if ln.strip()]
    last_line = lines[-1] if lines else "unknown error"
    last_line = re.sub(r"\s+", " ", last_line)
    return False, last_line[:140]


def update_queue(rows, runbook_map, failures):
    updated = list(rows)
    for runbook_path, (idx, machine, isru) in runbook_map.items():
        line = updated[idx]
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 3:
            continue
        isru_clean = re.sub(r"\s*\(runbook failed:.*\)$", "", parts[2]).strip()
        if runbook_path in failures:
            isru_clean = f"{isru_clean} (runbook failed: {failures[runbook_path]})"
        parts[2] = isru_clean
        updated[idx] = "| " + " | ".join(parts) + " |\n"
    QUEUE_PATH.write_text("".join(updated), encoding="utf-8")


def main():
    rows, runbook_map = load_queue_rows()
    if not runbook_map:
        print("No runbooks found in queue.")
        return 1
    failures = {}
    for runbook_path in sorted(runbook_map.keys()):
        ok, err = run_runbook(runbook_path)
        status = "ok" if ok else "failed"
        print(f"{runbook_path}: {status}")
        if not ok:
            failures[runbook_path] = err
    update_queue(rows, runbook_map, failures)
    if failures:
        print("\nFailures:")
        for runbook_path, err in failures.items():
            print(f"- {runbook_path}: {err}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
