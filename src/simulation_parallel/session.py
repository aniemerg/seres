"""
Session loader/persistence for sim2 concurrent DES runner.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine
from src.simulation_parallel.intent_queue import DeferredIntentQueue

REPO_ROOT = Path(__file__).resolve().parents[2]
SIM2_DIR = REPO_ROOT / "simulations_parallel"


@dataclass
class Sim2Session:
    engine: SimulationEngine
    queue: DeferredIntentQueue
    queue_file: Path

    def save(self) -> None:
        self.engine.save()
        self.queue_file.write_text(json.dumps(self.queue.to_dict(), indent=2), encoding="utf-8")


def load_session(sim_id: str, kb_loader: KBLoader, create: bool = False) -> Sim2Session:
    sim_dir = SIM2_DIR / sim_id
    sim_dir.mkdir(parents=True, exist_ok=True)
    queue_file = sim_dir / "deferred_intents.json"
    snapshot_file = sim_dir / "snapshot.json"

    if create and snapshot_file.exists():
        raise ValueError(f"Simulation '{sim_id}' already exists")
    if not create and not snapshot_file.exists():
        raise ValueError(f"Simulation '{sim_id}' not found")

    engine = SimulationEngine(sim_id=sim_id, kb_loader=kb_loader, sim_dir=sim_dir)
    if not create:
        ok = engine.load()
        if not ok:
            raise ValueError(f"Failed to load simulation '{sim_id}'")

    if queue_file.exists():
        queue = DeferredIntentQueue.from_dict(json.loads(queue_file.read_text(encoding="utf-8")))
    else:
        queue = DeferredIntentQueue()

    return Sim2Session(engine=engine, queue=queue, queue_file=queue_file)
