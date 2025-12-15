"""
Queue management helpers.

NOTE: The work queue is now rebuilt from scratch on each indexer run,
so prune() is largely obsolete - gaps are automatically removed when fixed.
The pop() function can still be used for manual task-by-task workflows,
but popped items will reappear on next index if still unresolved.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Set

WORK_QUEUE = Path("out/work_queue.jsonl")
INDEX_PATH = Path("out/index.json")


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
    items = _load_queue()
    if not items:
        return None
    head = items.pop(0)
    _save_queue(items)
    return head
