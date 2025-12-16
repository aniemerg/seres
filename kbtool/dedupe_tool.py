"""
Dedupe queue management (parallel to work queue).
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Dict, List, Optional
import fcntl
from contextlib import contextmanager

LOCK_PATH = Path("out/dedupe_queue.lock")
QUEUE_PATH = Path("out/dedupe_queue.jsonl")


@contextmanager
def _locked_queue():
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOCK_PATH, "w") as lockf:
        fcntl.flock(lockf, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lockf, fcntl.LOCK_UN)


def _load_queue() -> List[dict]:
    if not QUEUE_PATH.exists():
        return []
    items: List[dict] = []
    with QUEUE_PATH.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                items.append(json.loads(line))
            except Exception:
                continue
    return items


def _save_queue(items: List[dict]) -> None:
    QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with QUEUE_PATH.open("w", encoding="utf-8") as f:
        for obj in items:
            f.write(json.dumps(obj) + "\n")


def lease_next(agent: str, ttl: int = 900) -> Optional[dict]:
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

        pending = [i for i in items if i.get("status") in (None, "pending")]
        if not pending:
            return None

        # prevent multiple leases for the same item_id/candidate
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


def gc(prune_done_older_than: Optional[int] = None) -> int:
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


def add_from_file(path: Path) -> int:
    """
    Append dedupe tasks from a JSONL or JSON array file.
    Each entry should already have an 'id' and optional fields:
    kind, reason, candidate_ids, notes, status (defaults to pending).
    """
    if not path.exists():
        raise FileNotFoundError(path)
    new_items: List[dict] = []
    content = path.read_text(encoding="utf-8").strip()
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
    with _locked_queue():
        items = _load_queue()
        items.extend(new_items)
        _save_queue(items)
    return len(new_items)
