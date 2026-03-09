from pathlib import Path

import yaml

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


def _build_kb(tmp_path: Path) -> Path:
    kb = tmp_path / "kb"
    (kb / "processes").mkdir(parents=True)
    (kb / "recipes").mkdir(parents=True)
    (kb / "items" / "materials").mkdir(parents=True)
    (kb / "items" / "parts").mkdir(parents=True)
    (kb / "items" / "machines").mkdir(parents=True)
    (kb / "units").mkdir(parents=True)

    with open(kb / "units" / "units.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "unit_definitions_test_v0",
                "name": "Unit Definitions (test)",
                "units": {"mass": ["kg"], "count": ["count", "unit"], "time": ["hour"]},
                "conversions": [{"from": "hour", "to": "hour", "factor": 1.0}],
            },
            f,
        )

    with open(kb / "processes" / "long_batch_bulk_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "long_batch_bulk_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1000.0, "unit": "kg"}],
                "outputs": [{"item_id": "bulk_output", "qty": 1000.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 2000.0},
                "resource_requirements": [{"machine_id": "press", "qty": 1.0, "unit": "count"}],
            },
            f,
        )

    with open(kb / "processes" / "long_batch_discrete_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "long_batch_discrete_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 2.0, "unit": "kg"}],
                "outputs": [{"item_id": "widget", "qty": 1.0, "unit": "unit"}],
                "time_model": {"type": "batch", "hr_per_batch": 2000.0},
                "resource_requirements": [{"machine_id": "press", "qty": 1.0, "unit": "count"}],
            },
            f,
        )

    with open(kb / "recipes" / "recipe_bulk_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "recipe_bulk_v0",
                "target_item_id": "bulk_output",
                "variant_id": "v0",
                "steps": [{"process_id": "long_batch_bulk_v0", "dependencies": []}],
            },
            f,
        )

    with open(kb / "recipes" / "recipe_widget_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "recipe_widget_v0",
                "target_item_id": "widget",
                "variant_id": "v0",
                "steps": [{"process_id": "long_batch_discrete_v0", "dependencies": []}],
            },
            f,
        )

    with open(kb / "items" / "materials" / "ore.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "unit_kind": "bulk", "mass": 1.0}, f)
    with open(kb / "items" / "materials" / "bulk_output.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "bulk_output", "kind": "material", "unit": "kg", "unit_kind": "bulk", "mass": 1.0}, f)
    with open(kb / "items" / "parts" / "widget.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "widget", "kind": "part", "unit": "unit", "unit_kind": "discrete", "mass": 1.0}, f)
    with open(kb / "items" / "machines" / "press.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "press", "kind": "machine", "unit": "count", "unit_kind": "discrete", "mass": 100.0}, f)

    return kb


def _advance_until_idle(engine: SimulationEngine) -> None:
    while engine.scheduler.event_queue:
        next_event = engine.scheduler.event_queue.peek()
        if not next_event:
            break
        delta = max(0.0, next_event.time - engine.scheduler.current_time)
        engine.advance_time(delta)


def test_long_batch_bulk_step_is_chunked(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    engine = SimulationEngine("batch_chunk_bulk", kb, sim_dir=tmp_path / "sim_bulk")

    engine.import_item("ore", 1000.0, "kg")
    engine.import_item("press", 1.0, "count")

    result = engine.run_recipe("recipe_bulk_v0", 1)
    assert result["success"]
    _advance_until_idle(engine)

    assert len(engine.scheduler.completed_processes) == 2
    assert engine.has_item("bulk_output", 1000.0, "kg")


def test_long_batch_discrete_step_is_not_fractionalized(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    engine = SimulationEngine("batch_chunk_discrete", kb, sim_dir=tmp_path / "sim_discrete")

    engine.import_item("ore", 2.0, "kg")
    engine.import_item("press", 1.0, "count")

    result = engine.run_recipe("recipe_widget_v0", 1)
    assert result["success"]
    _advance_until_idle(engine)

    assert len(engine.scheduler.completed_processes) == 1
    assert engine.has_item("widget", 1.0, "unit")


def test_long_batch_bulk_chunks_run_in_parallel_when_capacity_allows(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    engine = SimulationEngine("batch_chunk_parallel", kb, sim_dir=tmp_path / "sim_parallel")

    engine.import_item("ore", 1000.0, "kg")
    engine.import_item("press", 2.0, "count")

    result = engine.run_recipe("recipe_bulk_v0", 1)
    assert result["success"]
    _advance_until_idle(engine)

    assert len(engine.scheduler.completed_processes) == 2
    assert engine.has_item("bulk_output", 1000.0, "kg")
    assert engine.scheduler.current_time == 1000.0
