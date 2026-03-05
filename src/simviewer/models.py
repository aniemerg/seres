from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class ProcessRunRecord:
    process_run_id: str
    process_id: str
    recipe_run_id: str | None
    recipe_id: str | None
    start_time: float | None
    end_time: float | None
    duration_hours: float | None
    energy_kwh: float | None
    status: str
    machine_type: str | None
    lane_id: str | None
    inputs: Dict[str, dict]
    outputs: Dict[str, dict]
    error_message: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class InventoryCheckpoint:
    idx: int
    time_hours: float
    process_complete_count: int
    inventory: Dict[str, dict]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class InventoryDelta:
    process_run_id: str
    time_hours: float | None
    delta: Dict[str, dict]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ExportWarnings:
    unresolved_wiki_links: List[dict]
    missing_kb_categories: List[str]
    undefined_references: List[str]

    def to_dict(self) -> dict:
        return asdict(self)
