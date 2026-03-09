from pathlib import Path

import yaml

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine
from src.simulation_parallel.intent_queue import DeferredIntentQueue
from src.simulation_parallel.runner import ConcurrentDESRunner
from src.simulation_parallel.session import Sim2Session


def _build_kb(tmp_path: Path) -> Path:
    kb = tmp_path / "kb"
    (kb / "processes").mkdir(parents=True)
    (kb / "items" / "materials").mkdir(parents=True)
    (kb / "items" / "machines").mkdir(parents=True)
    (kb / "units").mkdir(parents=True)

    with open(kb / "units" / "units.yaml", "w") as f:
        yaml.dump(
            {
                "id": "unit_definitions_test_v0",
                "name": "Unit Definitions (test)",
                "units": {
                    "mass": ["kg", "g"],
                    "count": ["count", "unit"],
                    "time": ["hour"],
                },
                "conversions": [
                    {"from": "g", "to": "kg", "factor": 0.001},
                    {"from": "hour", "to": "hour", "factor": 1.0},
                ],
            },
            f,
        )

    with open(kb / "processes" / "smelt.yaml", "w") as f:
        yaml.dump(
            {
                "id": "smelt",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [{"machine_id": "furnace", "qty": 1.0, "unit": "count"}],
            },
            f,
        )

    with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
        yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "materials" / "metal.yaml", "w") as f:
        yaml.dump({"id": "metal", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
        yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)
    return kb


def test_deferred_process_promotes_on_completion(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    sim_dir = tmp_path / "sim"
    engine = SimulationEngine("sim2_test", kb, sim_dir=sim_dir)
    queue = DeferredIntentQueue()
    session = Sim2Session(engine=engine, queue=queue, queue_file=sim_dir / "deferred_intents.json")
    runner = ConcurrentDESRunner(session)

    engine.import_item("ore", 10.0, "kg")
    engine.import_item("furnace", 1.0, "count")

    first = runner.submit_process_intent(process_id="smelt")
    assert first["status"] == "accepted"

    second = runner.submit_process_intent(process_id="smelt")
    assert second["status"] == "deferred"
    assert len(queue) == 1

    result = runner.run_to_completion()
    assert result["status"] == "completed"
    assert len(queue) == 0
    assert engine.has_item("metal", 2.0, "kg")
