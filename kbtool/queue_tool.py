"""
Queue management helpers: prune completed items and pop next item.
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
    Remove items that are already defined (status == defined) in the index.
    Keep unresolved refs.
    Keep import_stub entries only if they still appear in out/import_stubs.jsonl.
    Keep referenced_only/status!=defined items in the queue.
    """
    items = _load_queue()
    if not items:
        return 0
    index_status = _load_index_map()
    active_import_stubs = _load_import_stub_targets()
    kept: List[dict] = []
    removed = 0
    for obj in items:
        reason = obj.get("reason", "")
        if reason == "unresolved_ref":
            kept.append(obj)
            continue
        if reason == "import_stub":
            if obj.get("id") in active_import_stubs:
                kept.append(obj)
                continue
            removed += 1
            continue
        status = index_status.get(obj.get("id"))
        if status == "defined":
            removed += 1
            continue
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
