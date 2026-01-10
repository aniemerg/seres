"""
Integration tests for energy tracking persistence.
"""
from pathlib import Path
import json

import pytest
import yaml

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


@pytest.fixture
def kb_root(tmp_path):
    kb = tmp_path / "kb"
    (kb / "processes").mkdir(parents=True)
    (kb / "items" / "materials").mkdir(parents=True)
    (kb / "items" / "machines").mkdir(parents=True)

    with open(kb / "processes" / "energy_proc_v0.yaml", "w") as f:
        yaml.dump({
            "id": "energy_proc_v0",
            "kind": "process",
            "process_type": "batch",
            "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
            "outputs": [{"item_id": "metal", "qty": 2.0, "unit": "kg"}],
            "time_model": {"type": "batch", "hr_per_batch": 1.0},
            "energy_model": {
                "type": "per_unit",
                "value": 1.5,
                "unit": "kWh/kg",
                "scaling_basis": "metal",
            },
            "resource_requirements": [
                {"machine_id": "furnace", "qty": 1.0, "unit": "count"}
            ],
        }, f)

    with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
        yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "materials" / "metal.yaml", "w") as f:
        yaml.dump({"id": "metal", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
        yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)

    return kb


@pytest.fixture
def sim_dir(tmp_path):
    return tmp_path / "simulations"


def test_energy_persisted_in_events_and_load(kb_root, sim_dir):
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_id = "energy_persist"
    full_sim_dir = sim_dir / sim_id
    engine = SimulationEngine(sim_id, kb, full_sim_dir)

    engine.import_item("ore", 1.0, "kg")
    engine.import_item("furnace", 1.0, "count")

    result = engine.start_process(
        process_id="energy_proc_v0",
        scale=1.0,
        duration_hours=1.0,
    )
    assert result["success"]

    engine.advance_time(1.0)
    engine.save()

    log_file = full_sim_dir / "simulation.jsonl"
    assert log_file.exists()

    events = []
    with open(log_file, "r") as f:
        for line in f:
            events.append(json.loads(line))

    scheduled_events = [e for e in events if e.get("type") == "process_scheduled"]
    assert len(scheduled_events) == 1
    assert scheduled_events[0].get("energy_kwh") is not None
    assert scheduled_events[0].get("energy_kwh") > 0.0

    complete_events = [e for e in events if e.get("type") == "process_complete"]
    assert len(complete_events) == 1
    assert complete_events[0].get("energy_kwh") > 0.0

    total_before = engine.state.total_energy_kwh

    engine2 = SimulationEngine(sim_id, kb, full_sim_dir)
    assert engine2.load()
    assert engine2.state.total_energy_kwh == total_before
