"""
DEPRECATED: This file is deprecated and should be migrated to src/

Queue management helpers.

NOTE: The work queue is now rebuilt from scratch on each indexer run,
so prune() is largely obsolete - gaps are automatically removed when fixed.
The pop() function can still be used for manual task-by-task workflows,
but popped items will reappear on next index if still unresolved.

TODO: Migrate to src/kb_core/queue_manager.py
"""
from __future__ import annotations

import json
import os
import time
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Set
import hashlib

from contextlib import contextmanager
from functools import wraps
import fcntl

warnings.warn(
    "kbtool.queue_tool is deprecated; use src.kb_core.queue_manager instead.",
    DeprecationWarning,
    stacklevel=2,
)

WORK_QUEUE = Path("out/work_queue.jsonl")
INDEX_PATH = Path("out/index.json")

LOCK_PATH = Path("out/work_queue.lock")


@contextmanager
def _locked_queue() -> None:
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOCK_PATH, "w") as lockf:
        fcntl.flock(lockf, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lockf, fcntl.LOCK_UN)


def _load_queue() -> List[dict]:
    if not WORK_QUEUE.exists():
        return []
    items: List[dict] = []
    with WORK_QUEUE.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                items.append(json.loads(line))
            except Exception:
                continue
    return items


def _save_queue(items: List[dict]) -> None:
    WORK_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    with WORK_QUEUE.open("w", encoding="utf-8") as f:
        for obj in items:
            f.write(json.dumps(obj) + "\n")


def _load_index_map() -> Dict[str, str]:
    if not INDEX_PATH.exists():
        return {}
    try:
        with INDEX_PATH.open("r", encoding="utf-8") as f:
            data = json.load(f)
        entries = data.get("entries", {})
        return {k: v.get("status", "unknown") for k, v in entries.items()}
    except Exception:
        return {}


def _load_import_stub_targets() -> Set[str]:
    path = Path("out/import_stubs.jsonl")
    targets: Set[str] = set()
    if not path.exists():
        return targets
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
                tid = obj.get("target_item_id") or obj.get("recipe_id")
                if tid:
                    targets.add(str(tid))
            except Exception:
                continue
    return targets


def prune_queue() -> int:
    """
    Prune only items explicitly marked resolved/superseded.
    Retain gaps even if the corresponding id is already defined (e.g., no_recipe, missing_field).
    """
    with _locked_queue():
        items = _load_queue()
        if not items:
            return 0
        kept: List[dict] = []
        removed = 0
        for obj in items:
            reason = obj.get("reason", "")
            if reason in ("resolved", "superseded"):
                removed += 1
            else:
                kept.append(obj)
        _save_queue(kept)
        return removed


def pop_queue() -> Optional[dict]:
    """
    Pop and return the first item in the queue.
    """
    with _locked_queue():
        items = _load_queue()
        if not items:
            return None
        head = items.pop(0)
        _save_queue(items)
        return head


def lease_next(agent: str, ttl: int = 900, priorities: Optional[List[str]] = None) -> Optional[dict]:
    now = time.time()
    expires = now + ttl
    with _locked_queue():
        items = _load_queue()
        # revert expired leases
        for obj in items:
            if obj.get("status") == "leased" and obj.get("lease_expires_at", 0) < now:
                obj["status"] = "pending"
                obj.pop("lease_id", None)
                obj.pop("lease_expires_at", None)

        def item_key(obj: dict) -> tuple:
            prio_map = {p: i for i, p in enumerate(priorities)} if priorities else {}
            return (prio_map.get(obj.get("reason"), 9999),)

        pending = [i for i in items if i.get("status") in (None, "pending")]
        if not pending:
            return None

        # Block lease if another entry with the same item_id is already leased
        leased_ids = {
            (obj.get("item_id") or obj.get("id"))
            for obj in items
            if obj.get("status") == "leased"
        }
        pending = [
            obj for obj in pending
            if (obj.get("item_id") or obj.get("id")) not in leased_ids
        ]
        if not pending:
            return None
        pending.sort(key=item_key)

        # Use hash-based entry point to distribute agents across queue
        # This reduces collisions when multiple agents lease simultaneously
        if len(pending) > 1:
            agent_hash = int(hashlib.sha256(agent.encode()).hexdigest(), 16)
            start_idx = agent_hash % len(pending)
            # Rotate the list so different agents start at different positions
            pending = pending[start_idx:] + pending[:start_idx]

        target = pending[0]
        target["status"] = "leased"
        target["lease_id"] = agent
        target["lease_expires_at"] = expires
        _save_queue(items)
        return target


def complete(id_value: str, agent: str) -> bool:
    with _locked_queue():
        items = _load_queue()
        updated = False
        for obj in items:
            if obj.get("id") == id_value:
                # Check lease ownership for leased and resolved items
                status = obj.get("status")
                if status in ("leased", "resolved") and obj.get("lease_id") != agent:
                    continue
                obj["status"] = "done"
                obj["completed_at"] = time.time()
                updated = True
                break
        if updated:
            _save_queue(items)
        return updated


def release(id_value: str, agent: str) -> bool:
    with _locked_queue():
        items = _load_queue()
        updated = False
        for obj in items:
            if obj.get("id") == id_value:
                if obj.get("status") == "leased" and obj.get("lease_id") != agent:
                    continue
                obj["status"] = "pending"
                obj.pop("lease_id", None)
                obj.pop("lease_expires_at", None)
                updated = True
                break
        if updated:
            _save_queue(items)
        return updated


def gc(expire_ttl: int = 0, prune_done_older_than: Optional[int] = None) -> int:
    now = time.time()
    removed = 0
    with _locked_queue():
        items = _load_queue()
        kept: List[dict] = []
        for obj in items:
            # Expire leased items with expired leases
            if obj.get("status") == "leased" and obj.get("lease_expires_at", 0) < now:
                obj["status"] = "pending"
                obj.pop("lease_id", None)
                obj.pop("lease_expires_at", None)
            # Expire resolved items with expired leases (agent failed to complete)
            if obj.get("status") == "resolved" and obj.get("lease_expires_at", 0) < now:
                obj["status"] = "pending"
                obj.pop("lease_id", None)
                obj.pop("lease_expires_at", None)
            # Prune old done items
            if prune_done_older_than and obj.get("status") == "done":
                if obj.get("completed_at", 0) < now - prune_done_older_than:
                    removed += 1
                    continue
            kept.append(obj)
        _save_queue(kept)
    return removed


def list_queue() -> Dict[str, int]:
    items = _load_queue()
    counts: Dict[str, int] = {}
    for obj in items:
        st = obj.get("status") or "pending"
        counts[st] = counts.get(st, 0) + 1
    return counts


def gap_ids_present(ids: List[str]) -> Set[str]:
    wanted = set(ids)
    if not wanted:
        return set()
    items = _load_queue()
    present: Set[str] = set()
    for obj in items:
        obj_id = obj.get("id")
        if obj_id in wanted:
            status = obj.get("status") or "pending"
            if status not in ("resolved", "done", "superseded"):
                present.add(obj_id)
    return present


def gap_id_exists(id_value: str) -> bool:
    if not id_value:
        return False
    items = _load_queue()
    for obj in items:
        if obj.get("id") == id_value:
            return True
    return False


def _register_gap_type(gap_type: str, created_by: str = "unknown") -> None:
    """
    Auto-register new gap types in the registry.

    Creates queue/gap_type_registry.json if it doesn't exist.
    Updates usage_count if gap_type already registered.
    """
    import json
    from pathlib import Path

    registry_path = Path("queue/gap_type_registry.json")
    registry_path.parent.mkdir(exist_ok=True)

    # Load existing registry
    if registry_path.exists():
        try:
            registry = json.loads(registry_path.read_text(encoding="utf-8"))
        except Exception:
            registry = {}
    else:
        registry = {}

    # Add or update gap type
    if gap_type in registry:
        registry[gap_type]["usage_count"] += 1
    else:
        registry[gap_type] = {
            "description": "",  # Can be filled in manually later
            "created_by": created_by,
            "created_at": time.time(),
            "usage_count": 1,
            "source": "manual" if created_by != "indexer" else "indexer"
        }

    registry_path.write_text(json.dumps(registry, indent=2), encoding="utf-8")


def list_gap_types() -> Dict[str, dict]:
    """
    List all registered gap types from the registry.

    Returns:
        Dict mapping gap_type -> metadata dict
    """
    import json
    from pathlib import Path

    registry_path = Path("queue/gap_type_registry.json")
    if not registry_path.exists():
        return {}

    try:
        return json.loads(registry_path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def add_gap(
    gap_type: str,
    item_id: str,
    description: str = None,
    context: dict = None,
    kind: str = "gap",
    source: str = "manual"
) -> str:
    """
    Add a manual gap to the work queue.

    Args:
        gap_type: Type of issue (existing or new type)
        item_id: The item/recipe/process ID this relates to
        description: Clear description for fixing agent (added to context)
        context: Optional dict with additional metadata
        kind: Item kind (default "gap")
        source: Source of gap (default "manual", can use "agent")

    Returns:
        The generated gap ID (format: "gap_type:item_id")

    Example:
        gap_id = add_gap(
            gap_type="quality_concern",
            item_id="steel_process_v0",
            description="Energy model doesn't match paper",
            context={"paper_ref": "ellery_2023.pdf"}
        )
    """
    gap_id = f"{gap_type}:{item_id}"

    # Build context with description
    ctx = context.copy() if context else {}
    if description:
        ctx["description"] = description
    ctx["added_at"] = time.time()

    item = {
        "id": gap_id,
        "kind": kind,
        "reason": gap_type,
        "gap_type": gap_type,
        "item_id": item_id,
        "source": source,
        "context": ctx,
        "status": "pending"
    }

    # Add to queue
    with _locked_queue():
        items = _load_queue()
        items.append(item)
        _save_queue(items)

    # Register gap type
    _register_gap_type(gap_type, source)

    return gap_id


def add_from_file(file_path: Path) -> int:
    """
    Add multiple gaps from a JSONL or JSON array file.

    Each entry should have at minimum:
        - gap_type: str
        - item_id: str
        - description: str (optional but recommended)
        - context: dict (optional)

    Args:
        file_path: Path to JSONL or JSON file

    Returns:
        Number of items added

    Example file content (JSONL):
        {"gap_type": "quality_concern", "item_id": "foo_v0", "description": "..."}
        {"gap_type": "needs_review", "item_id": "bar_v0", "description": "..."}
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    new_items: List[dict] = []
    content = file_path.read_text(encoding="utf-8").strip()

    if not content:
        return 0

    try:
        # Try JSON array first
        obj = json.loads(content)
        if isinstance(obj, list):
            new_items.extend(obj)
        else:
            new_items.append(obj)
    except Exception:
        # Fallback to JSONL
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                new_items.append(json.loads(line))
            except Exception:
                continue

    if not new_items:
        return 0

    # Convert each item to proper queue format
    queue_items = []
    for item in new_items:
        gap_type = item.get("gap_type")
        item_id = item.get("item_id")

        if not gap_type or not item_id:
            continue  # Skip invalid items

        gap_id = f"{gap_type}:{item_id}"
        description = item.get("description")
        context = item.get("context", {})

        if description and "description" not in context:
            context["description"] = description

        context["added_at"] = time.time()

        queue_item = {
            "id": gap_id,
            "kind": item.get("kind", "gap"),
            "reason": gap_type,
            "gap_type": gap_type,
            "item_id": item_id,
            "source": item.get("source", "manual"),
            "context": context,
            "status": "pending"
        }
        queue_items.append(queue_item)

        # Register gap type
        _register_gap_type(gap_type, item.get("source", "manual"))

    # Add all items to queue
    with _locked_queue():
        items = _load_queue()
        items.extend(queue_items)
        _save_queue(items)

    return len(queue_items)
