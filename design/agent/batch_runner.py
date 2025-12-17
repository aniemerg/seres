#!/usr/bin/env python3
"""
batch_runner.py

Batch processing for dependency usage analysis.

Processes multiple (repo, dependency) pairs in parallel with:
- Resume support (skip already-completed reports)
- Circuit breaker (stop on repeated failures)
- Progress display with sampled worker activity
- Graceful shutdown on SIGINT/SIGTERM

See docs/ADR/002-batch-processing.md for design details.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import signal
import subprocess
import sys
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from multiprocessing import Pool, Queue, Value, Manager
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from src.output import is_report_completed, REPORTS_BASE_PATH


# -----------------------------
# Data structures
# -----------------------------


@dataclass
class WorkItem:
    """A single (seed_repo, dependency) pair to process."""
    seed_repo: str           # e.g., "ethereum/go-ethereum"
    dependency_url: str      # e.g., "https://github.com/google/uuid"
    search_name: str         # e.g., "github.com/google/uuid"
    package_manager: str     # e.g., "GO", "NPM", "CARGO"


# -----------------------------
# Data loading
# -----------------------------

DATA_DIR = Path("data")
SEED_REPOS_FULL = DATA_DIR / "seedReposWithDependencies.json"
SEED_REPOS_PRUNED = DATA_DIR / "seedReposWithDependencies_pruned.json"
DEPENDENCIES_CSV = DATA_DIR / "dependencies.csv"

TMP_DIR = Path("tmp")


def load_seed_repos(use_pruned: bool = True) -> Dict[str, List[str]]:
    """Load seed repos with their dependencies from JSON file."""
    path = SEED_REPOS_PRUNED if use_pruned else SEED_REPOS_FULL
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_oso_lookup() -> Dict[Tuple[str, str], List[Tuple[str, str]]]:
    """
    Build (seed_repo, dependency_github) -> [(package_manager, package_name)] lookup.

    Uses the OSO dependencies.csv to map GitHub URLs to searchable package names.
    """
    lookup: Dict[Tuple[str, str], List[Tuple[str, str]]] = {}

    if not DEPENDENCIES_CSV.exists():
        print(f"[WARN] {DEPENDENCIES_CSV} not found, OSO lookup disabled")
        return lookup

    with DEPENDENCIES_CSV.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            seed = row.get("repo_name", "").lower()  # e.g., 'ethereum/go-ethereum'
            pkg_name = row.get("package_name", "")
            pkg_mgr = row.get("package_manager", "")

            # Skip GitHub Actions (not code dependencies)
            if pkg_mgr == "ACTIONS":
                continue

            # For Go packages, extract owner/repo from package name
            if pkg_mgr == "GO" and pkg_name.startswith("github.com/"):
                parts = pkg_name.replace("github.com/", "").split("/")
                if len(parts) >= 2:
                    dep_github = f"{parts[0]}/{parts[1]}".lower()
                    key = (seed, dep_github)
                    if key not in lookup:
                        lookup[key] = []
                    lookup[key].append((pkg_mgr, pkg_name))

            # For other package managers, we'd need reverse resolution
            # This is a simplified implementation - expand as needed

    return lookup


def github_url_to_repo(url: str) -> str:
    """Convert GitHub URL to owner/repo format."""
    # https://github.com/google/uuid -> google/uuid
    return url.replace("https://github.com/", "").lower().rstrip("/")


def resolve_search_name(
    seed_repo: str,
    dep_url: str,
    oso_lookup: Dict[Tuple[str, str], List[Tuple[str, str]]],
) -> Tuple[str, str]:
    """
    Resolve a dependency GitHub URL to a searchable package name.

    Returns (package_manager, search_name).
    """
    seed_normalized = seed_repo.lower()
    dep_repo = github_url_to_repo(dep_url)

    # Check OSO lookup
    key = (seed_normalized, dep_repo)
    if key in oso_lookup:
        # Return the first match (could be smarter about picking)
        return oso_lookup[key][0]

    # Fall back to GitHub URL as search name (works for Go)
    return ("GO", f"github.com/{dep_repo}")


def generate_work_items(
    seed_repos: Dict[str, List[str]],
    oso_lookup: Dict[Tuple[str, str], List[Tuple[str, str]]],
    repo_filter: Optional[List[str]] = None,
    top_n: Optional[int] = None,
) -> List[WorkItem]:
    """
    Generate work items from seed repos.

    Args:
        seed_repos: Dict of seed_repo_url -> [dependency_urls]
        oso_lookup: OSO lookup table for package name resolution
        repo_filter: If provided, only include these repos
        top_n: If provided, only include top N repos by dependency count
    """
    items: List[WorkItem] = []

    # Sort by dependency count for top_n
    sorted_repos = sorted(
        seed_repos.items(),
        key=lambda x: len(x[1]),
        reverse=True,
    )

    # Apply filters
    if repo_filter:
        filter_set = {r.lower() for r in repo_filter}
        sorted_repos = [
            (url, deps) for url, deps in sorted_repos
            if github_url_to_repo(url) in filter_set
        ]

    if top_n:
        sorted_repos = sorted_repos[:top_n]

    for seed_url, dep_urls in sorted_repos:
        seed_repo = github_url_to_repo(seed_url)

        for dep_url in dep_urls:
            pkg_mgr, search_name = resolve_search_name(seed_repo, dep_url, oso_lookup)
            items.append(WorkItem(
                seed_repo=seed_repo,
                dependency_url=dep_url,
                search_name=search_name,
                package_manager=pkg_mgr,
            ))

    return items


# -----------------------------
# Repo cloning
# -----------------------------


def ensure_repo_cloned(repo: str, quiet: bool = False) -> Path:
    """
    Ensure the repo is cloned to tmp/{org}_{repo}/.

    Returns the path to the cloned repo.
    """
    org_repo = repo.replace("/", "_")
    clone_path = TMP_DIR / org_repo

    if clone_path.exists():
        return clone_path

    TMP_DIR.mkdir(parents=True, exist_ok=True)

    url = f"https://github.com/{repo}.git"
    if not quiet:
        print(f"Cloning {repo}...")

    result = subprocess.run(
        ["git", "clone", "--depth", "1", url, str(clone_path)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Failed to clone {repo}: {result.stderr}")

    return clone_path


# -----------------------------
# Circuit breaker
# -----------------------------


class CircuitBreaker:
    """Stop processing if too many recent failures."""

    def __init__(self, threshold: int = 3, window: int = 10):
        self.threshold = threshold
        self.window = window
        self.recent_results: deque = deque(maxlen=window)

    def record(self, success: bool) -> None:
        self.recent_results.append(success)

    def should_stop(self) -> bool:
        if len(self.recent_results) < self.window:
            return False
        failures = sum(1 for r in self.recent_results if not r)
        return failures >= self.threshold


# -----------------------------
# Progress display
# -----------------------------


class ProgressDisplay:
    """Progress bar with sampled worker activity."""

    def __init__(self, total: int, activity_queue: Queue):
        self.total = total
        self.completed = Value('i', 0)
        self.failed = Value('i', 0)
        self.activity_queue = activity_queue
        self.start_time = time.time()
        self.last_activity = None
        self.last_activity_time = 0
        self.activity_max_age = 3.0  # seconds before activity considered stale
        self._first_update = True

    def update(self) -> None:
        """Update the progress display."""
        # Calculate stats
        completed = self.completed.value
        failed = self.failed.value

        if self.total == 0:
            pct = 100
        else:
            pct = (completed / self.total) * 100

        elapsed = time.time() - self.start_time
        rate = completed / elapsed if elapsed > 0 else 0
        remaining = self.total - completed
        eta = remaining / rate if rate > 0 else 0

        # Drain queue and keep only the freshest activity
        now = time.time()
        while not self.activity_queue.empty():
            try:
                item = self.activity_queue.get_nowait()
                self.last_activity = item
                self.last_activity_time = now
            except:
                break

        # Check if last activity is stale
        activity = None
        if self.last_activity and (now - self.last_activity_time) < self.activity_max_age:
            activity = self.last_activity

        # Build progress bar
        bar_width = 20
        filled = int(pct / 100 * bar_width)
        bar = "=" * filled + ">" + " " * (bar_width - filled - 1)
        if filled >= bar_width:
            bar = "=" * bar_width

        # Clear previous lines (except on first update)
        if not self._first_update:
            sys.stdout.write('\033[2A\033[J')  # Move up 2 lines, clear to end
        self._first_update = False

        # Print progress line
        eta_str = f"{eta/60:.0f}m" if eta > 60 else f"{eta:.0f}s"
        print(f"[{bar}] {pct:.0f}% | {completed}/{self.total} | {failed} failed | ETA {eta_str}")

        # Print activity line
        if activity:
            dep = activity.get('dependency', '?')[:40]
            msg = activity.get('message', '')[:60]
            print(f"[{dep}] {msg}")
        else:
            print("  ...")

        sys.stdout.flush()

    def increment_completed(self) -> None:
        with self.completed.get_lock():
            self.completed.value += 1

    def increment_failed(self) -> None:
        with self.failed.get_lock():
            self.failed.value += 1


# -----------------------------
# Worker function
# -----------------------------


def process_work_item(args: Tuple[WorkItem, Queue, bool]) -> Tuple[bool, Optional[str]]:
    """
    Process a single work item.

    This runs in a worker process.

    Returns (success, error_message).
    """
    work_item, activity_queue, force = args

    try:
        # Import here to avoid issues with multiprocessing
        from src.agent import analyze_dependency
        from src.output import is_report_completed

        repo_id = f"github.com/{work_item.seed_repo}"

        # Check if already completed (resume support) - skip if force=True
        if not force and is_report_completed(repo_id, work_item.search_name):
            return (True, None)

        # Ensure repo is cloned (quietly in batch mode)
        repo_path = ensure_repo_cloned(work_item.seed_repo, quiet=True)

        # Create activity callback to push updates to the queue
        def activity_callback(message: str):
            activity_queue.put({
                'dependency': work_item.search_name,
                'message': message,
            })

        # Run the analysis in quiet mode with activity callback
        report, saved_path = analyze_dependency(
            repo_root=str(repo_path),
            repo_id=repo_id,
            dependency=work_item.search_name,
            quiet=True,
            activity_callback=activity_callback,
        )

        if report is None:
            return (False, "No report generated")

        return (True, None)

    except Exception as e:
        return (False, f"{type(e).__name__}: {e}")


# -----------------------------
# Batch state persistence
# -----------------------------

BATCH_STATE_PATH = Path("output/batch/batch_state.json")
FAILURES_LOG_PATH = Path("output/batch/failures.jsonl")


def save_batch_state(state: Dict[str, Any]) -> None:
    """Save batch state to JSON file."""
    BATCH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    state["last_updated"] = datetime.utcnow().isoformat() + "Z"
    with BATCH_STATE_PATH.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def log_failure(work_item: WorkItem, error: str) -> None:
    """Append failure to failures.jsonl."""
    FAILURES_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "seed_repo": work_item.seed_repo,
        "dependency": work_item.search_name,
        "dependency_url": work_item.dependency_url,
        "error": error,
    }
    with FAILURES_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


# -----------------------------
# Main batch runner
# -----------------------------


def run_batch(
    work_items: List[WorkItem],
    workers: int = 50,
    dry_run: bool = False,
    force: bool = False,
) -> None:
    """
    Run batch processing on work items.

    Args:
        work_items: List of work items to process
        workers: Number of parallel workers
        dry_run: If True, just print what would be processed
        force: If True, re-run even if report exists for today
    """
    if dry_run:
        print(f"Would process {len(work_items)} items with {workers} workers:")
        for item in work_items[:20]:
            print(f"  {item.seed_repo} -> {item.search_name}")
        if len(work_items) > 20:
            print(f"  ... and {len(work_items) - 20} more")
        return

    # Filter already-completed items (unless force=True)
    pending_items = []
    for item in work_items:
        repo_id = f"github.com/{item.seed_repo}"
        if force or not is_report_completed(repo_id, item.search_name):
            pending_items.append(item)

    print(f"Total items: {len(work_items)}")
    print(f"Already completed: {len(work_items) - len(pending_items)}")
    print(f"Pending: {len(pending_items)}")
    print(f"Workers: {workers}")
    print()

    if not pending_items:
        print("Nothing to do!")
        return

    # Set up shared state
    manager = Manager()
    activity_queue = manager.Queue()

    progress = ProgressDisplay(len(pending_items), activity_queue)
    # More tolerant circuit breaker for large batches
    # Stop if 10 of the last 50 fail (20% failure rate)
    circuit_breaker = CircuitBreaker(threshold=10, window=50)

    # Batch state
    batch_state = {
        "started_at": datetime.utcnow().isoformat() + "Z",
        "total_items": len(pending_items),
        "completed": 0,
        "failed": 0,
        "skipped": len(work_items) - len(pending_items),
        "stopped_reason": None,
    }
    save_batch_state(batch_state)

    # Set up graceful shutdown
    shutdown_requested = False

    def signal_handler(signum, frame):
        nonlocal shutdown_requested
        shutdown_requested = True
        print("\n\nShutdown requested, finishing in-flight workers...")

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Prepare args for workers
    worker_args = [(item, activity_queue, force) for item in pending_items]

    # Process with pool
    # Note: Using imap_unordered for better responsiveness
    try:
        with Pool(processes=workers) as pool:
            results_iter = pool.imap_unordered(process_work_item, worker_args)

            for i, (success, error) in enumerate(results_iter):
                if shutdown_requested:
                    batch_state["stopped_reason"] = "user_interrupt"
                    break

                # Update progress
                if success:
                    progress.increment_completed()
                    batch_state["completed"] += 1
                else:
                    progress.increment_failed()
                    batch_state["failed"] += 1
                    log_failure(pending_items[i], error or "Unknown error")

                # Check circuit breaker
                circuit_breaker.record(success)
                if circuit_breaker.should_stop():
                    batch_state["stopped_reason"] = "circuit_breaker"
                    print("\n\nCircuit breaker triggered - too many failures")
                    break

                # Update display
                progress.update()

                # Periodically save state
                if i % 10 == 0:
                    save_batch_state(batch_state)

    finally:
        save_batch_state(batch_state)
        print("\n\nBatch complete!")
        print(f"  Completed: {batch_state['completed']}")
        print(f"  Failed: {batch_state['failed']}")
        if batch_state["stopped_reason"]:
            print(f"  Stopped: {batch_state['stopped_reason']}")


# -----------------------------
# CLI
# -----------------------------


def cmd_run(args: argparse.Namespace) -> None:
    """Run batch processing."""
    use_pruned = args.input == "pruned"
    seed_repos = load_seed_repos(use_pruned=use_pruned)
    oso_lookup = build_oso_lookup()

    # Determine repo filter
    repo_filter = None
    if args.repo:
        repo_filter = [args.repo]
    elif args.repos:
        repo_filter = [r.strip() for r in args.repos.split(",")]

    work_items = generate_work_items(
        seed_repos,
        oso_lookup,
        repo_filter=repo_filter,
        top_n=args.top,
    )

    run_batch(
        work_items,
        workers=args.workers,
        dry_run=args.dry_run,
        force=getattr(args, 'force', False),
    )


def load_revalidation_candidates(
    summary_csv: Path,
    usage_class_filter: Optional[str] = None,
    inclusion_type_filter: Optional[str] = None,
    sample_size: Optional[int] = None,
) -> List[WorkItem]:
    """
    Load candidates for revalidation from the summary CSV.

    Args:
        summary_csv: Path to all_repos_summary.csv
        usage_class_filter: Filter by usage_class (e.g., "Unused")
        inclusion_type_filter: Filter by inclusion_type (e.g., "direct")
        sample_size: If provided, randomly sample this many items

    Returns:
        List of WorkItem objects to revalidate
    """
    import random

    candidates = []

    with summary_csv.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Apply filters
            if usage_class_filter and row.get("usage_class") != usage_class_filter:
                continue
            if inclusion_type_filter and row.get("inclusion_type") != inclusion_type_filter:
                continue

            # Extract repo and dependency
            repo = row.get("repo", "")  # e.g., "ethereum/go-ethereum"
            dependency = row.get("dependency", "")  # e.g., "github.com/google/uuid"

            if repo and dependency:
                candidates.append(WorkItem(
                    seed_repo=repo,
                    dependency_url=f"https://github.com/{dependency.replace('github.com/', '')}",
                    search_name=dependency,
                    package_manager="UNKNOWN",
                ))

    # Sample if requested
    if sample_size and len(candidates) > sample_size:
        candidates = random.sample(candidates, sample_size)

    return candidates


def load_candidates_from_csv(candidates_csv: Path) -> List[WorkItem]:
    """
    Load candidates from a custom CSV file.

    Expected columns: repo, dependency
    """
    candidates = []

    with candidates_csv.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            repo = row.get("repo", "")
            dependency = row.get("dependency", "")

            if repo and dependency:
                candidates.append(WorkItem(
                    seed_repo=repo,
                    dependency_url=f"https://github.com/{dependency.replace('github.com/', '')}",
                    search_name=dependency,
                    package_manager="UNKNOWN",
                ))

    return candidates


def cmd_revalidate(args: argparse.Namespace) -> None:
    """Revalidate a subset of existing reports."""

    # If --candidates is provided, load from that file
    if args.candidates:
        candidates_path = Path(args.candidates)
        if not candidates_path.exists():
            print(f"Error: Candidates file not found at {candidates_path}")
            return

        print(f"Loading candidates from {candidates_path}")
        work_items = load_candidates_from_csv(candidates_path)
        print(f"  Found {len(work_items)} candidates")

    else:
        # Load from summary CSV with filters
        summary_csv = REPORTS_BASE_PATH / "all_repos_summary.csv"

        if not summary_csv.exists():
            print(f"Error: Summary CSV not found at {summary_csv}")
            print("Run the initial batch first to generate reports.")
            return

        # Parse filter (e.g., "direct+Unused" -> inclusion_type=direct, usage_class=Unused)
        usage_class_filter = None
        inclusion_type_filter = None

        if args.filter:
            parts = args.filter.split("+")
            for part in parts:
                part = part.strip()
                if part in ("Unused", "SinglePoint", "Utility", "FeatureFocused", "Pervasive"):
                    usage_class_filter = part
                elif part in ("direct", "transitive", "unknown"):
                    inclusion_type_filter = part

        print(f"Loading candidates from {summary_csv}")
        print(f"  Filter: usage_class={usage_class_filter}, inclusion_type={inclusion_type_filter}")
        print(f"  Sample size: {args.sample or 'all'}")

        work_items = load_revalidation_candidates(
            summary_csv,
            usage_class_filter=usage_class_filter,
            inclusion_type_filter=inclusion_type_filter,
            sample_size=args.sample,
        )

        print(f"  Found {len(work_items)} candidates")

    if not work_items:
        print("No candidates found matching filter.")
        return

    run_batch(
        work_items,
        workers=args.workers,
        dry_run=args.dry_run,
        force=True,  # Always force for revalidation
    )


def cmd_status(args: argparse.Namespace) -> None:
    """Show batch status."""
    if not BATCH_STATE_PATH.exists():
        print("No batch state found.")
        return

    with BATCH_STATE_PATH.open("r", encoding="utf-8") as f:
        state = json.load(f)

    print("Batch Status:")
    print(f"  Started: {state.get('started_at', '?')}")
    print(f"  Last updated: {state.get('last_updated', '?')}")
    print(f"  Total items: {state.get('total_items', '?')}")
    print(f"  Completed: {state.get('completed', '?')}")
    print(f"  Failed: {state.get('failed', '?')}")
    print(f"  Skipped: {state.get('skipped', '?')}")
    if state.get("stopped_reason"):
        print(f"  Stopped: {state.get('stopped_reason')}")


def cmd_clone(args: argparse.Namespace) -> None:
    """Clone repos without processing."""
    use_pruned = args.input == "pruned"
    seed_repos = load_seed_repos(use_pruned=use_pruned)

    # Determine which repos to clone
    repos_to_clone = set()

    if args.repo:
        repos_to_clone.add(args.repo)
    elif args.all:
        for url in seed_repos.keys():
            repos_to_clone.add(github_url_to_repo(url))
    else:
        print("Specify --repo or --all")
        return

    print(f"Cloning {len(repos_to_clone)} repos...")
    for repo in sorted(repos_to_clone):
        try:
            path = ensure_repo_cloned(repo)
            print(f"  {repo} -> {path}")
        except Exception as e:
            print(f"  {repo} FAILED: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Batch processing for dependency usage analysis.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # run command
    run_parser = subparsers.add_parser("run", help="Run batch processing")
    run_parser.add_argument("--repo", help="Process single repo (e.g., ethereum/go-ethereum)")
    run_parser.add_argument("--repos", help="Comma-separated list of repos")
    run_parser.add_argument("--top", type=int, help="Process top N repos by dependency count")
    run_parser.add_argument("--all", action="store_true", help="Process all repos")
    run_parser.add_argument("--input", choices=["pruned", "full"], default="pruned",
                           help="Which seed repos file to use (default: pruned)")
    run_parser.add_argument("--workers", type=int, default=50,
                           help="Number of parallel workers (default: 50)")
    run_parser.add_argument("--dry-run", action="store_true",
                           help="Show what would be processed without running")
    run_parser.set_defaults(func=cmd_run)

    # status command
    status_parser = subparsers.add_parser("status", help="Show batch status")
    status_parser.set_defaults(func=cmd_status)

    # clone command
    clone_parser = subparsers.add_parser("clone", help="Clone repos without processing")
    clone_parser.add_argument("--repo", help="Clone single repo")
    clone_parser.add_argument("--all", action="store_true", help="Clone all repos")
    clone_parser.add_argument("--input", choices=["pruned", "full"], default="pruned",
                             help="Which seed repos file to use (default: pruned)")
    clone_parser.set_defaults(func=cmd_clone)

    # revalidate command
    revalidate_parser = subparsers.add_parser(
        "revalidate",
        help="Re-run analysis on subset of existing reports to check for false negatives"
    )
    revalidate_parser.add_argument(
        "--filter",
        help="Filter by usage_class+inclusion_type (e.g., 'direct+Unused', 'Unused', 'direct')"
    )
    revalidate_parser.add_argument(
        "--candidates",
        help="Path to CSV file with repo,dependency columns (alternative to --filter)"
    )
    revalidate_parser.add_argument(
        "--sample", type=int,
        help="Randomly sample N items from filtered set"
    )
    revalidate_parser.add_argument(
        "--workers", type=int, default=5,
        help="Number of parallel workers (default: 5)"
    )
    revalidate_parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be processed without running"
    )
    revalidate_parser.set_defaults(func=cmd_revalidate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
