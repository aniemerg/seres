import json
from pathlib import Path

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


def _write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _build_minimal_kb(kb_dir: Path) -> None:
    _write_file(
        kb_dir / "items" / "machines" / "test_machine.yaml",
        """id: test_machine
kind: machine
name: Test Machine
mass: 100.0
unit: count
""",
    )
    _write_file(
        kb_dir / "items" / "materials" / "item_a.yaml",
        """id: item_a
kind: material
name: Item A
mass: 1.0
unit: kg
""",
    )
    _write_file(
        kb_dir / "items" / "materials" / "item_b.yaml",
        """id: item_b
kind: material
name: Item B
mass: 1.0
unit: kg
""",
    )
    _write_file(
        kb_dir / "items" / "materials" / "ore.yaml",
        """id: ore
kind: material
name: Ore
mass: 1.0
unit: kg
""",
    )
    _write_file(
        kb_dir / "processes" / "step_a_v0.yaml",
        """id: step_a_v0
kind: process
name: Step A
process_type: batch
inputs: []
outputs:
  - item_id: item_a
    qty: 1.0
    unit: kg
resource_requirements:
  - machine_id: test_machine
    qty: 1
    unit: count
time_model:
  type: batch
  hr_per_batch: 1.0
""",
    )
    _write_file(
        kb_dir / "processes" / "step_b_v0.yaml",
        """id: step_b_v0
kind: process
name: Step B
process_type: batch
inputs:
  - item_id: item_a
    qty: 1.0
    unit: kg
outputs:
  - item_id: item_b
    qty: 1.0
    unit: kg
resource_requirements:
  - machine_id: test_machine
    qty: 1
    unit: count
time_model:
  type: batch
  hr_per_batch: 1.0
""",
    )
    _write_file(
        kb_dir / "recipes" / "recipe_two_step_v0.yaml",
        """id: recipe_two_step_v0
kind: recipe
target_item_id: item_b
steps:
  - process_id: step_a_v0
  - process_id: step_b_v0
""",
    )


def test_snapshot_roundtrip_preserves_imports(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    _build_minimal_kb(kb_dir)

    kb = KBLoader(kb_dir, use_validated_models=False)
    kb.load_all()

    sim_dir = tmp_path / "simulations"
    sim_id = "snapshot_imports"
    engine = SimulationEngine(sim_id, kb, sim_dir / sim_id)
    engine.load()

    engine.import_item("ore", 2.0, "kg")
    engine.save()

    engine2 = SimulationEngine(sim_id, kb, sim_dir / sim_id)
    assert engine2.load()
    assert "ore" in engine2.state.total_imports
    assert engine2.state.total_imports["ore"].quantity == 2.0


def test_recipe_resume_from_snapshot(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    _build_minimal_kb(kb_dir)

    kb = KBLoader(kb_dir, use_validated_models=False)
    kb.load_all()

    sim_dir = tmp_path / "simulations"
    sim_id = "snapshot_recipe"
    engine = SimulationEngine(sim_id, kb, sim_dir / sim_id)
    engine.load()

    engine.import_item("test_machine", 1.0, "count")

    process_def = kb.get_process("step_a_v0")
    assert process_def is not None
    process_dump = process_def.model_dump() if hasattr(process_def, "model_dump") else process_def
    assert process_dump.get("outputs"), "step_a_v0 should have outputs"

    resolved = engine.resolve_step({"process_id": "step_a_v0"})
    assert resolved.get("outputs"), "resolve_step should keep outputs"

    result = engine.run_recipe("recipe_two_step_v0", 1)
    assert result["success"]
    engine.save()

    snapshot_data = json.loads((sim_dir / sim_id / "snapshot.json").read_text(encoding="utf-8"))
    events = snapshot_data["scheduler"]["event_queue"]
    assert events, "Expected scheduled events in snapshot"
    start_events = [e for e in events if e.get("event_type") == "process_start"]
    assert start_events, "Expected process_start in snapshot queue"
    assert start_events[0]["data"].get("outputs_pending"), "Expected outputs pending in start event"

    engine2 = SimulationEngine(sim_id, kb, sim_dir / sim_id)
    assert engine2.load()
    assert engine2.orchestrator.get_active_recipe_runs()

    engine2.advance_time(1.0)
    engine2.advance_time(1.0)

    assert "item_b" in engine2.state.inventory
    assert engine2.state.inventory["item_b"].quantity == 1.0
