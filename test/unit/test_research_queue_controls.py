import json
import time

import pytest

from src.cli import _check_queue_output_artifact
from src.indexer import indexer
from src.kb_core import queue_manager


def write_queue(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def read_queue(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def configure_queue_paths(monkeypatch, tmp_path):
    work_queue = tmp_path / "out" / "work_queue.jsonl"
    lock_path = tmp_path / "out" / "work_queue.lock"
    monkeypatch.setattr(queue_manager, "WORK_QUEUE", work_queue)
    monkeypatch.setattr(queue_manager, "LOCK_PATH", lock_path)
    return work_queue


def test_lease_next_hard_filters_by_kind_gap_type_and_id_prefix(monkeypatch, tmp_path):
    work_queue = configure_queue_paths(monkeypatch, tmp_path)
    write_queue(
        work_queue,
        [
            {
                "id": "validation:error:machine:foo",
                "kind": "machine",
                "gap_type": "validation_error",
                "reason": "validation_error",
                "item_id": "foo",
                "status": "pending",
            },
            {
                "id": "research_task:other_project_001",
                "kind": "research",
                "gap_type": "research_task",
                "reason": "research_task",
                "item_id": "other_project_001",
                "status": "pending",
            },
            {
                "id": "research_task:ream250_bom_row_0001_11",
                "kind": "research",
                "gap_type": "research_task",
                "reason": "research_task",
                "item_id": "ream250_bom_row_0001_11",
                "status": "pending",
            },
        ],
    )

    leased = queue_manager.lease_next(
        "agent-1",
        kind="research",
        gap_type="research_task",
        id_prefix="research_task:ream250_bom_row_",
    )

    assert leased is not None
    assert leased["id"] == "research_task:ream250_bom_row_0001_11"
    assert leased["lease_id"] == "agent-1"


def test_lease_next_returns_empty_when_hard_filters_do_not_match(monkeypatch, tmp_path):
    work_queue = configure_queue_paths(monkeypatch, tmp_path)
    write_queue(
        work_queue,
        [
            {
                "id": "validation:error:machine:foo",
                "kind": "machine",
                "gap_type": "validation_error",
                "reason": "validation_error",
                "item_id": "foo",
                "status": "pending",
            }
        ],
    )

    assert queue_manager.lease_next("agent-1", kind="research") is None


def test_index_rebuild_preserves_research_task_status_without_duplicate(monkeypatch, tmp_path):
    work_queue = configure_queue_paths(monkeypatch, tmp_path)
    monkeypatch.setattr(indexer, "WORK_QUEUE", work_queue)
    monkeypatch.setattr(indexer, "_detect_circular_dependencies", lambda entries, kb_loader: [])
    now = time.time()
    write_queue(
        work_queue,
        [
            {
                "id": "research_task:ream250_bom_row_0001_11",
                "kind": "research",
                "gap_type": "research_task",
                "reason": "research_task",
                "item_id": "ream250_bom_row_0001_11",
                "source": "manual",
                "status": "leased",
                "lease_id": "agent-1",
                "lease_expires_at": now + 3600,
            }
        ],
    )

    indexer._update_work_queue(
        unresolved_refs=[],
        referenced_only=set(),
        import_stubs=[],
        items_without_recipes=[],
        missing_fields=[],
        orphan_resources=[],
        invalid_recipes=[],
        missing_recipe_items=[],
        recipes_no_inputs=[],
        seed_references={},
        item_metadata={},
        entries={},
        kb_loader=None,
    )

    rows = read_queue(work_queue)
    assert len(rows) == 1
    assert rows[0]["id"] == "research_task:ream250_bom_row_0001_11"
    assert rows[0]["status"] == "leased"
    assert rows[0]["lease_id"] == "agent-1"


def test_index_rebuild_does_not_restore_done_research_task(monkeypatch, tmp_path):
    work_queue = configure_queue_paths(monkeypatch, tmp_path)
    monkeypatch.setattr(indexer, "WORK_QUEUE", work_queue)
    monkeypatch.setattr(indexer, "_detect_circular_dependencies", lambda entries, kb_loader: [])
    write_queue(
        work_queue,
        [
            {
                "id": "research_task:ream250_bom_row_0001_11",
                "kind": "research",
                "gap_type": "research_task",
                "reason": "research_task",
                "item_id": "ream250_bom_row_0001_11",
                "source": "manual",
                "status": "done",
            }
        ],
    )

    indexer._update_work_queue(
        unresolved_refs=[],
        referenced_only=set(),
        import_stubs=[],
        items_without_recipes=[],
        missing_fields=[],
        orphan_resources=[],
        invalid_recipes=[],
        missing_recipe_items=[],
        recipes_no_inputs=[],
        seed_references={},
        item_metadata={},
        entries={},
        kb_loader=None,
    )

    assert read_queue(work_queue) == []


def test_complete_output_guard_rejects_missing_result_file(monkeypatch, tmp_path):
    work_queue = configure_queue_paths(monkeypatch, tmp_path)
    missing_result = tmp_path / "research" / "missing.md"
    validator = tmp_path / "validator.py"
    validator.write_text("raise SystemExit(0)\n", encoding="utf-8")
    write_queue(
        work_queue,
        [
            {
                "id": "research_task:ream250_bom_row_0002_1A1",
                "kind": "research",
                "gap_type": "research_task",
                "reason": "research_task",
                "item_id": "ream250_bom_row_0002_1A1",
                "status": "leased",
                "lease_id": "agent-1",
                "context": {
                    "output_path": str(missing_result),
                    "output_validator": str(validator),
                },
            }
        ],
    )

    with pytest.raises(SystemExit):
        _check_queue_output_artifact(
            queue_manager,
            "research_task:ream250_bom_row_0002_1A1",
            validate_output=True,
        )


def test_complete_output_guard_accepts_validated_result_file(monkeypatch, tmp_path):
    work_queue = configure_queue_paths(monkeypatch, tmp_path)
    result = tmp_path / "research" / "result.md"
    result.parent.mkdir(parents=True)
    result.write_text("---\nok: true\n---\n", encoding="utf-8")
    validator = tmp_path / "validator.py"
    validator.write_text("raise SystemExit(0)\n", encoding="utf-8")
    write_queue(
        work_queue,
        [
            {
                "id": "research_task:ream250_bom_row_0002_1A1",
                "kind": "research",
                "gap_type": "research_task",
                "reason": "research_task",
                "item_id": "ream250_bom_row_0002_1A1",
                "status": "leased",
                "lease_id": "agent-1",
                "context": {
                    "output_path": str(result),
                    "output_validator": str(validator),
                },
            }
        ],
    )

    _check_queue_output_artifact(
        queue_manager,
        "research_task:ream250_bom_row_0002_1A1",
        validate_output=True,
    )
