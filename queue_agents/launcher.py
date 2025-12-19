#!/usr/bin/env python3
"""
launcher.py

Parallel launcher for autonomous queue workers.

Spawns N worker agents in parallel, each processing queue items until the queue is empty.

Usage:
    python -m queue_agents.launcher --workers <n> [--model <model>]
"""
from __future__ import annotations

import argparse
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Tuple, Optional


REPO_ROOT = Path(__file__).parent.parent
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"


class WorkerProcess:
    """Manages a single worker subprocess."""

    def __init__(self, agent_name: str, model: str):
        self.agent_name = agent_name
        self.model = model
        self.process: Optional[subprocess.Popen] = None
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.exit_code: Optional[int] = None

    def start(self):
        """Start the worker process."""
        cmd = [
            str(VENV_PYTHON),
            "-m",
            "queue_agents.worker",
            "--agent",
            self.agent_name,
            "--model",
            self.model,
        ]

        self.process = subprocess.Popen(
            cmd,
            cwd=str(REPO_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,  # Line buffered
        )
        self.start_time = time.time()

    def poll(self) -> Optional[int]:
        """Check if process has finished. Returns exit code if done, None if running."""
        if self.process is None:
            return None

        exit_code = self.process.poll()
        if exit_code is not None and self.exit_code is None:
            self.exit_code = exit_code
            self.end_time = time.time()

        return exit_code

    def is_running(self) -> bool:
        """Check if process is still running."""
        return self.poll() is None

    def kill(self):
        """Terminate the process."""
        if self.process and self.is_running():
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()

    def get_output(self) -> str:
        """Get process output (only works after process ends)."""
        if self.process and self.process.stdout:
            return self.process.stdout.read()
        return ""

    def duration(self) -> Optional[float]:
        """Get process duration in seconds."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None


def launch_batch(
    n_workers: int,
    model: str = "gpt-5-nano",
    agent_prefix: str = "kb-worker",
) -> int:
    """
    Launch N workers in parallel.

    Returns:
        Exit code (0 = success, 1 = some failures, 2 = all failed)
    """
    print(f"{'='*60}")
    print(f"Launching {n_workers} workers with model {model}")
    print(f"{'='*60}\n")

    # Create workers
    workers: List[WorkerProcess] = []
    for i in range(1, n_workers + 1):
        agent_name = f"{agent_prefix}-{i}"
        worker = WorkerProcess(agent_name, model)
        workers.append(worker)

    # Start all workers
    for worker in workers:
        print(f"[START] {worker.agent_name}")
        worker.start()
        time.sleep(0.2)  # Slight delay to avoid race conditions

    print(f"\n[RUNNING] {n_workers} workers active\n")

    # Set up signal handler for graceful shutdown
    shutdown_requested = False

    def signal_handler(signum, frame):
        nonlocal shutdown_requested
        shutdown_requested = True
        print("\n\n[SHUTDOWN] Received interrupt, stopping workers...")

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Monitor workers
    try:
        while True:
            if shutdown_requested:
                print("[SHUTDOWN] Killing all workers...")
                for worker in workers:
                    worker.kill()
                break

            # Check worker status
            running = [w for w in workers if w.is_running()]
            finished = [w for w in workers if not w.is_running()]

            if not running:
                # All workers finished
                break

            # Print status update
            print(f"\r[STATUS] Running: {len(running)}, Finished: {len(finished)}", end="", flush=True)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Killing workers...")
        for worker in workers:
            worker.kill()

    # Wait for all to finish
    print("\n\n[WAIT] Waiting for workers to finish...")
    for worker in workers:
        if worker.is_running():
            worker.process.wait()

    # Print results
    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}\n")

    success_count = 0
    no_work_count = 0
    failure_count = 0

    for worker in workers:
        duration = worker.duration()
        duration_str = f"{duration:.1f}s" if duration else "N/A"

        if worker.exit_code == 0:
            status = "✓ SUCCESS"
            success_count += 1
        elif worker.exit_code == 2:
            status = "○ NO WORK"
            no_work_count += 1
        else:
            status = f"✗ FAILED (exit {worker.exit_code})"
            failure_count += 1

        print(f"{worker.agent_name:20s} {status:20s} {duration_str:>10s}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Success: {success_count}")
    print(f"  No work: {no_work_count}")
    print(f"  Failed:  {failure_count}")
    print(f"{'='*60}\n")

    # Determine exit code
    if failure_count == 0:
        return 0
    elif success_count > 0:
        return 1  # Some succeeded, some failed
    else:
        return 2  # All failed


def main():
    parser = argparse.ArgumentParser(
        description="Launch multiple autonomous queue workers in parallel"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=3,
        help="Number of workers to launch (default: 3)",
    )
    parser.add_argument(
        "--model",
        default="gpt-5-nano",
        help="Model to use for all workers (default: gpt-5-nano)",
    )
    parser.add_argument(
        "--prefix",
        default="kb-worker",
        help="Agent name prefix (default: kb-worker)",
    )

    args = parser.parse_args()

    try:
        exit_code = launch_batch(
            n_workers=args.workers,
            model=args.model,
            agent_prefix=args.prefix,
        )
        sys.exit(exit_code)
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
