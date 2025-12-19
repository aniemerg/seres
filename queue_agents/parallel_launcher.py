#!/usr/bin/env python3
"""
Parallel launcher for queue agents.

Spawns multiple worker processes and displays a live progress dashboard.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import signal
import sys
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from subprocess import Popen, PIPE
from typing import Optional

REPO_ROOT = Path(__file__).parent.parent
VENV_PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
QUEUE_TOOL = REPO_ROOT / "kbtool" / "queue.py"


@dataclass
class WorkerState:
    """State for a single worker."""
    process: Popen
    worker_id: int
    agent_name: str
    current_item: Optional[str] = None
    status: str = "starting"  # starting, working, idle, done
    output_file: Optional[Path] = None
    last_file_position: int = 0  # Track how much we've read


@dataclass
class Event:
    """A worker event to display."""
    timestamp: datetime
    worker_id: int
    item_id: str
    event_type: str  # success, failure
    message: str


class ProgressDashboard:
    """Live progress dashboard for parallel workers."""

    def __init__(self, total_items: int, update_interval: float = 3.5):
        self.total_items = total_items
        self.initial_items = total_items  # Track starting size
        self.update_interval = update_interval

        self.completed = 0
        self.successes = 0
        self.failures = 0
        self.active = 0

        self.start_time = time.time()
        self.events: deque[Event] = deque(maxlen=50)  # Keep last 50 events
        self.current_event_idx = 0

        self.running = True

    def add_event(self, event: Event):
        """Add an event to the queue."""
        self.events.append(event)

    def get_current_event(self) -> Optional[Event]:
        """Get the current event to display."""
        if not self.events:
            return None
        # Rotate through recent events
        if self.current_event_idx >= len(self.events):
            self.current_event_idx = 0
        event = list(self.events)[self.current_event_idx]
        self.current_event_idx += 1
        return event

    def calculate_rate(self) -> float:
        """Calculate items per minute."""
        elapsed = time.time() - self.start_time
        if elapsed < 1:
            return 0.0
        return (self.completed / elapsed) * 60

    def update_total(self, new_total: int):
        """Update the total items count (queue is dynamic)."""
        self.total_items = new_total

    def render(self) -> str:
        """Render the dashboard as a string."""
        rate = self.calculate_rate()

        # Calculate net progress (completed vs remaining)
        remaining = self.total_items
        net_resolved = self.completed - (self.total_items - self.initial_items)

        # Build metrics line
        metrics = (
            f"Resolved: {self.completed} | "
            f"Queue: {remaining} (started: {self.initial_items}) | "
            f"Success: {self.successes} | "
            f"Failed: {self.failures} | "
            f"Active: {self.active} | "
            f"Rate: {rate:.1f}/min"
        )

        # Build event line
        event = self.get_current_event()
        if event:
            event_line = event.message
        else:
            event_line = "Waiting for events..."

        return f"\r\033[K{metrics}\n\033[K{event_line}\033[F"

    def clear(self):
        """Clear the dashboard lines."""
        print("\r\033[K\n\033[K\033[F", end="", flush=True)


class ParallelLauncher:
    """Manages parallel worker processes."""

    def __init__(self, num_workers: int, limit: Optional[int] = None):
        self.num_workers = num_workers
        self.limit = limit

        self.workers: list[WorkerState] = []
        self.dashboard: Optional[ProgressDashboard] = None
        self.shutdown_requested = False

        # Setup signal handler
        signal.signal(signal.SIGINT, self._handle_shutdown)
        signal.signal(signal.SIGTERM, self._handle_shutdown)

    def _handle_shutdown(self, signum, frame):
        """Handle shutdown signals."""
        if not self.shutdown_requested:
            print("\n\n[SHUTDOWN] Received signal, stopping workers and releasing items...")
            self.shutdown_requested = True
        else:
            print("\n[SHUTDOWN] Force quit requested, exiting immediately.")
            sys.exit(1)

    def _spawn_worker(self, worker_id: int) -> Optional[WorkerState]:
        """Spawn a single worker process."""
        agent_name = f"worker-{worker_id}"

        # Create output file
        output_file = Path(f"/tmp/claude/tasks/{agent_name}-{int(time.time())}.output")
        output_file.parent.mkdir(parents=True, exist_ok=True)

        cmd = [
            str(VENV_PYTHON),
            "-m",
            "queue_agents.worker",
            "--agent",
            agent_name,
            "--max-items",
            "999999",  # Let the worker run until queue is empty
            "--quiet",  # Suppress verbose output, logs go to file
        ]

        try:
            with output_file.open("w") as f:
                process = Popen(
                    cmd,
                    stdout=f,
                    stderr=f,
                    cwd=str(REPO_ROOT),
                )

            return WorkerState(
                process=process,
                worker_id=worker_id,
                agent_name=agent_name,
                output_file=output_file,
            )
        except Exception as e:
            print(f"[ERROR] Failed to spawn worker {worker_id}: {e}")
            return None

    def _parse_worker_output(self, worker: WorkerState) -> list[Event]:
        """Parse worker output file for new events (only new content since last read)."""
        if not worker.output_file or not worker.output_file.exists():
            return []

        events = []
        try:
            # Read only new content since last position
            with worker.output_file.open('r') as f:
                f.seek(worker.last_file_position)
                new_content = f.read()
                worker.last_file_position = f.tell()

            if not new_content:
                return []

            # Look for success/failure markers in new content
            for line in new_content.splitlines():
                # Success: [SUCCESS] Gap X resolved!
                if "[SUCCESS]" in line and "Gap " in line and " resolved!" in line:
                    item_id = line.split("Gap ")[1].split(" resolved!")[0].strip()

                    # Look for what was created (scan recent content)
                    created_items = self._extract_created_items(new_content, item_id)
                    if created_items:
                        msg = f"Worker {worker.worker_id}: {item_id} succeeded. Created {created_items}"
                    else:
                        msg = f"Worker {worker.worker_id}: {item_id} succeeded."

                    events.append(Event(
                        timestamp=datetime.now(timezone.utc),
                        worker_id=worker.worker_id,
                        item_id=item_id,
                        event_type="success",
                        message=msg,
                    ))

                # Failure: [FAILED] or [ERROR]
                elif "[FAILED]" in line or ("[ERROR]" in line and "Failed to" in line):
                    item_id = worker.current_item or "unknown"
                    # Extract error message
                    if "]" in line:
                        error_msg = line.split("]", 1)[1].strip()
                    else:
                        error_msg = "Unknown error"

                    msg = f"Worker {worker.worker_id}: {item_id} failed. Error: {error_msg[:60]}"

                    events.append(Event(
                        timestamp=datetime.now(timezone.utc),
                        worker_id=worker.worker_id,
                        item_id=item_id,
                        event_type="failure",
                        message=msg,
                    ))

                # Track current item
                elif "[LEASED]" in line:
                    parts = line.split("[LEASED]")
                    if len(parts) > 1:
                        item_id = parts[1].strip().split()[0]
                        worker.current_item = item_id
                        worker.status = "working"

        except Exception as e:
            pass  # Ignore parse errors

        return events

    def _extract_created_items(self, content: str, item_id: str) -> str:
        """Extract what items were created from worker output."""
        # Look for write_file calls: ● TOOL: write_file(path='kb/...', ...)
        created = []

        for line in content.splitlines():
            if "write_file" in line and "kb/" in line:
                # Extract path - handle both path=' and path=" formats
                path = None
                if "path='" in line:
                    path = line.split("path='")[1].split("'")[0]
                elif 'path="' in line:
                    path = line.split('path="')[1].split('"')[0]

                if path:
                    # Determine type from path
                    if "/materials/" in path:
                        created.append("material")
                    elif "/parts/" in path:
                        created.append("part")
                    elif "/machines/" in path:
                        created.append("machine")
                    elif "/processes/" in path:
                        created.append("process")
                    elif "/recipes/" in path:
                        created.append("recipe")
                    elif "/boms/" in path:
                        created.append("BOM")

        if created:
            # Count each type
            from collections import Counter
            counts = Counter(created)
            parts = [f"{count} {typ}{'s' if count > 1 else ''}" for typ, count in counts.items()]
            return ", ".join(parts)
        return ""

    def _update_metrics(self):
        """Update dashboard metrics by scanning worker states and outputs."""
        if not self.dashboard:
            return

        # Parse new events from all workers (including done ones - they might have final events)
        for worker in self.workers:
            events = self._parse_worker_output(worker)
            for event in events:
                self.dashboard.add_event(event)
                if event.event_type == "success":
                    self.dashboard.successes += 1
                    self.dashboard.completed += 1
                elif event.event_type == "failure":
                    self.dashboard.failures += 1
                    self.dashboard.completed += 1

        # Update active count
        self.dashboard.active = sum(
            1 for w in self.workers
            if w.status in ("working", "starting")
        )

        # Update total queue size (queue is dynamic - items added and removed)
        current_queue_size = self._get_queue_size()
        self.dashboard.update_total(current_queue_size)

    def _check_workers(self):
        """Check worker process status."""
        for worker in self.workers:
            if worker.process.poll() is not None:
                # Process has exited
                if worker.status != "done":
                    worker.status = "done"

    def _release_all_items(self):
        """Release all items leased by workers."""
        print("\n[CLEANUP] Releasing leased items...")

        for worker in self.workers:
            if worker.current_item:
                try:
                    # Release the item
                    cmd = [
                        str(VENV_PYTHON),
                        str(QUEUE_TOOL),
                        "release",
                        "--agent",
                        worker.agent_name,
                        worker.current_item,
                    ]
                    result = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=str(REPO_ROOT))
                    result.wait(timeout=5)
                    print(f"  ✓ Released {worker.current_item} (worker {worker.worker_id})")
                except Exception as e:
                    print(f"  ✗ Failed to release {worker.current_item}: {e}")

    def run(self):
        """Run the parallel launcher."""
        # Get queue size for progress tracking
        total_items = self._get_queue_size()
        if self.limit:
            total_items = min(total_items, self.limit)

        print(f"[PARALLEL LAUNCHER] Starting {self.num_workers} workers")
        print(f"[QUEUE] {total_items} items to process")
        print("=" * 60)
        print()

        # Initialize dashboard
        self.dashboard = ProgressDashboard(total_items)

        # Spawn workers
        for i in range(self.num_workers):
            worker = self._spawn_worker(i + 1)
            if worker:
                self.workers.append(worker)

        if not self.workers:
            print("[ERROR] Failed to spawn any workers")
            return

        print(f"[STARTED] {len(self.workers)} workers\n")

        # Main loop
        last_update = time.time()

        try:
            while not self.shutdown_requested:
                # Check worker status
                self._check_workers()

                # Update metrics
                self._update_metrics()

                # Render dashboard periodically
                now = time.time()
                if now - last_update >= self.dashboard.update_interval:
                    print(self.dashboard.render(), end="", flush=True)
                    last_update = now

                # Check if all workers are done
                if all(w.status == "done" for w in self.workers):
                    print("\n\n[COMPLETE] All workers finished")
                    break

                # Sleep briefly
                time.sleep(0.5)

        except KeyboardInterrupt:
            self.shutdown_requested = True

        finally:
            # Clear dashboard
            if self.dashboard:
                self.dashboard.clear()

            # Terminate workers
            print("\n[SHUTDOWN] Terminating workers...")
            for worker in self.workers:
                if worker.process.poll() is None:
                    worker.process.terminate()
                    try:
                        worker.process.wait(timeout=2)
                    except:
                        worker.process.kill()

            # Release items
            self._release_all_items()

            # Print final summary
            if self.dashboard:
                print("\n" + "=" * 60)
                print("FINAL SUMMARY")
                print("=" * 60)
                print(f"Completed:  {self.dashboard.completed}")
                print(f"  Success:  {self.dashboard.successes}")
                print(f"  Failed:   {self.dashboard.failures}")
                print(f"Rate:       {self.dashboard.calculate_rate():.1f} items/min")
                print("=" * 60)

    def _get_queue_size(self) -> int:
        """Get the current queue size."""
        try:
            queue_file = REPO_ROOT / "out" / "work_queue.jsonl"
            if not queue_file.exists():
                return 0
            count = 0
            with queue_file.open() as f:
                for line in f:
                    if line.strip():
                        count += 1
            return count
        except Exception as e:
            print(f"[WARNING] Failed to get queue size: {e}")
            return 0


def main():
    parser = argparse.ArgumentParser(description="Run parallel queue agents")
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum total items to process (default: unlimited)",
    )

    args = parser.parse_args()

    launcher = ParallelLauncher(
        num_workers=args.workers,
        limit=args.limit,
    )
    launcher.run()


if __name__ == "__main__":
    main()
