"""
Cost tracking for agent usage.

Tracks token usage and costs to out/agent_usage.jsonl with file locking
for safe concurrent writes.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from filelock import FileLock


REPO_ROOT = Path(__file__).parent.parent
USAGE_FILE = REPO_ROOT / "out" / "agent_usage.jsonl"
LOCK_FILE = REPO_ROOT / "out" / "agent_usage.lock"

# Pricing for gpt-5-nano (per 1M tokens)
PRICING = {
    "input": 0.05,         # $0.05 per 1M input tokens
    "cached": 0.005,       # $0.005 per 1M cached input tokens
    "output": 0.40,        # $0.40 per 1M output tokens
}


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    cached_tokens: int = 0,
) -> float:
    """
    Calculate cost in USD for token usage.

    Args:
        input_tokens: Total number of input tokens (includes cached)
        output_tokens: Number of output tokens
        cached_tokens: Number of cached input tokens (subset of input_tokens)

    Returns:
        Cost in USD
    """
    # Cached tokens are part of input tokens, not additional
    uncached_input_tokens = input_tokens - cached_tokens

    uncached_input_cost = (uncached_input_tokens * PRICING["input"]) / 1_000_000
    cached_cost = (cached_tokens * PRICING["cached"]) / 1_000_000
    output_cost = (output_tokens * PRICING["output"]) / 1_000_000

    return uncached_input_cost + cached_cost + output_cost


def log_usage(
    agent_name: str,
    item_id: str,
    gap_type: str,
    model: str,
    input_tokens: int,
    output_tokens: int,
    cached_tokens: int = 0,
    status: str = "completed",
) -> None:
    """
    Log agent usage to the usage file with file locking.

    Args:
        agent_name: Name of the agent
        item_id: Queue item ID processed
        gap_type: Type of gap (referenced_only, import_stub, etc.)
        model: Model used (e.g., gpt-5-nano)
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        cached_tokens: Number of cached input tokens
        status: Status (completed, failed, released)
    """
    # Ensure output directory exists
    USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Calculate cost
    cost_usd = calculate_cost(input_tokens, output_tokens, cached_tokens)

    # Create usage record
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent_name": agent_name,
        "item_id": item_id,
        "gap_type": gap_type,
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cached_tokens": cached_tokens,
        "cost_usd": round(cost_usd, 6),
        "status": status,
    }

    # Write with file locking for concurrent safety
    lock = FileLock(str(LOCK_FILE), timeout=10)
    try:
        with lock:
            with USAGE_FILE.open("a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
    except Exception as e:
        print(f"Warning: Failed to log usage: {e}")


def get_total_cost() -> float:
    """
    Calculate total cost from all usage records.

    Returns:
        Total cost in USD
    """
    if not USAGE_FILE.exists():
        return 0.0

    total = 0.0
    try:
        with USAGE_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    total += record.get("cost_usd", 0.0)
    except Exception as e:
        print(f"Warning: Failed to read usage file: {e}")

    return total


def print_usage_summary() -> None:
    """Print a summary of agent usage."""
    if not USAGE_FILE.exists():
        print("No usage data yet.")
        return

    records = []
    try:
        with USAGE_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
    except Exception as e:
        print(f"Error reading usage file: {e}")
        return

    if not records:
        print("No usage data yet.")
        return

    # Calculate totals
    total_cost = sum(r.get("cost_usd", 0.0) for r in records)
    total_input = sum(r.get("input_tokens", 0) for r in records)
    total_output = sum(r.get("output_tokens", 0) for r in records)
    total_cached = sum(r.get("cached_tokens", 0) for r in records)

    completed = sum(1 for r in records if r.get("status") == "completed")
    failed = sum(1 for r in records if r.get("status") == "failed")
    released = sum(1 for r in records if r.get("status") == "released")

    print("\n" + "=" * 60)
    print("AGENT USAGE SUMMARY")
    print("=" * 60)
    print(f"Total runs:       {len(records)}")
    print(f"  Completed:      {completed}")
    print(f"  Failed:         {failed}")
    print(f"  Released:       {released}")
    print()
    print(f"Total tokens:")
    print(f"  Input:          {total_input:,}")
    print(f"  Cached:         {total_cached:,}")
    print(f"  Output:         {total_output:,}")
    print()
    print(f"Total cost:       ${total_cost:.4f} USD")
    print("=" * 60 + "\n")
