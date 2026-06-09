import csv
import json

import yaml

from src.research_system import core


def write_yaml(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def make_mission(tmp_path):
    mission = tmp_path / "mission_bom_parts_001"
    write_yaml(
        mission / "mission_manifest.yaml",
        {
            "id": "mission_bom_parts_001",
            "mission_type": "bom_part_research",
            "input": {"primary_file": "input/bom.csv"},
            "task_generation": {"strategy": "unique_part_or_part_family"},
            "worker": {
                "output_schema": "schemas/result.schema.yaml",
                "max_attempts": 3,
            },
        },
    )
    write_csv(
        mission / "input" / "bom.csv",
        [
            {
                "row_id": "1",
                "part_number": "M3x12",
                "part_name": "M3 screw",
                "qty": "10",
            },
            {
                "row_id": "2",
                "part_number": "M3x12",
                "part_name": "M3 screw",
                "qty": "5",
            },
            {
                "row_id": "3",
                "part_number": "ABC-123",
                "part_name": "Stepper motor",
                "qty": "2",
            },
        ],
    )
    write_yaml(
        mission / "schemas" / "result.schema.yaml",
        {
            "required": ["task_id", "summary", "evidence", "confidence"],
            "fields": {
                "evidence": {"type": "list"},
                "confidence": {"type": "string", "allowed": ["high", "medium", "low"]},
                "needs_human_review": {"type": "boolean"},
            },
        },
    )
    return mission


def test_ingest_groups_unique_parts(tmp_path):
    mission = make_mission(tmp_path)

    result = core.ingest_mission(mission)

    assert result["task_count"] == 2
    assert core.status_counts(mission) == {"pending": 2}
    task_files = sorted((mission / "tasks").glob("*.json"))
    assert len(task_files) == 2

    tasks = [json.loads(path.read_text(encoding="utf-8")) for path in task_files]
    screw_task = next(task for task in tasks if task["payload"]["part_number"] == "M3x12")
    assert screw_task["payload"]["source_rows"] == ["1", "2"]
    assert screw_task["payload"]["qty_total"] == 15.0


def test_lease_complete_and_aggregate(tmp_path):
    mission = make_mission(tmp_path)
    core.ingest_mission(mission)

    leased = core.lease_task(mission, "agent-1", ttl=120)

    assert leased is not None
    assert leased["status"] == "leased"
    assert leased["lease_owner"] == "agent-1"
    assert core.status_counts(mission) == {"leased": 1, "pending": 1}

    result_path = mission / "outputs" / f"{leased['task_id']}.result.yaml"
    write_yaml(
        result_path,
        {
            "task_id": leased["task_id"],
            "summary": "Part analyzed.",
            "evidence": [{"source": "input/bom.csv", "note": "BOM row"}],
            "confidence": "medium",
            "needs_human_review": True,
        },
    )

    completed = core.complete_task(mission, leased["task_id"], "agent-1", result_path)

    assert completed["status"] == "completed"
    assert core.status_counts(mission) == {"completed": 1, "pending": 1}

    aggregate = core.aggregate_mission(mission)

    assert aggregate["completed_results"] == 1
    assert aggregate["needs_review"] == 1
    assert (mission / "aggregate" / "master_table.csv").exists()
    assert (mission / "aggregate" / "needs_review.csv").exists()
    assert (mission / "aggregate" / "summary.md").exists()


def test_complete_rejects_invalid_result(tmp_path):
    mission = make_mission(tmp_path)
    core.ingest_mission(mission)
    leased = core.lease_task(mission, "agent-1", ttl=120)
    result_path = mission / "outputs" / f"{leased['task_id']}.result.yaml"
    write_yaml(
        result_path,
        {
            "task_id": leased["task_id"],
            "summary": "Missing evidence and invalid confidence.",
            "confidence": "certain",
        },
    )

    try:
        core.complete_task(mission, leased["task_id"], "agent-1", result_path)
    except core.ResearchMissionError as exc:
        assert "Result failed schema validation" in str(exc)
    else:
        raise AssertionError("Expected invalid result to be rejected")

    assert core.status_counts(mission) == {"leased": 1, "pending": 1}

