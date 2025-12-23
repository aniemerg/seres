"""
Queue management helpers.

NOTE: The work queue is now rebuilt from scratch on each indexer run,
so prune() is largely obsolete - gaps are automatically removed when fixed.
The pop() function can still be used for manual task-by-task workflows,
but popped items will reappear on next index if still unresolved.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Set
import hashlib

from contextlib import contextmanager
from functools import wraps
import fcntl

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
                if obj.get("status") == "leased" and obj.get("lease_id") != agent:
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
            if obj.get("status") == "leased" and obj.get("lease_expires_at", 0) < now:
                obj["status"] = "pending"
                obj.pop("lease_id", None)
                obj.pop("lease_expires_at", None)
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
            present.add(obj_id)
    return present
