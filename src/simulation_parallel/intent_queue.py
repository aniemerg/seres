"""
Deferred process-intent queue for concurrent DES runner.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set


@dataclass
class ProcessIntent:
    intent_id: str
    sequence: int
    process_id: str
    scale: float
    duration_hours: Optional[float]
    output_quantity: Optional[float]
    output_unit: Optional[str]
    required_machines: List[str]
    submitted_at: float
    last_error: Optional[str] = None


class DeferredIntentQueue:
    """Global deferred intent registry with machine-based index."""

    def __init__(self) -> None:
        self._intents: Dict[str, ProcessIntent] = {}
        self._machine_index: Dict[str, Set[str]] = {}
        self._next_sequence = 1

    def next_sequence(self) -> int:
        seq = self._next_sequence
        self._next_sequence += 1
        return seq

    def add(self, intent: ProcessIntent) -> None:
        self._intents[intent.intent_id] = intent
        for machine_id in intent.required_machines:
            bucket = self._machine_index.setdefault(machine_id, set())
            bucket.add(intent.intent_id)

    def remove(self, intent_id: str) -> None:
        intent = self._intents.get(intent_id)
        if intent is None:
            return
        for machine_id in intent.required_machines:
            bucket = self._machine_index.get(machine_id)
            if not bucket:
                continue
            bucket.discard(intent_id)
            if not bucket:
                del self._machine_index[machine_id]
        del self._intents[intent_id]

    def get(self, intent_id: str) -> Optional[ProcessIntent]:
        return self._intents.get(intent_id)

    def all_intents(self) -> List[ProcessIntent]:
        return sorted(self._intents.values(), key=lambda x: x.sequence)

    def candidate_intents(self, changed_machines: Optional[Set[str]]) -> List[ProcessIntent]:
        if not changed_machines:
            return self.all_intents()

        seen: Set[str] = set()
        out: List[ProcessIntent] = []
        for machine_id in changed_machines:
            for intent_id in self._machine_index.get(machine_id, set()):
                if intent_id in seen:
                    continue
                seen.add(intent_id)
                intent = self._intents.get(intent_id)
                if intent is not None:
                    out.append(intent)
        out.sort(key=lambda x: x.sequence)
        return out

    def __len__(self) -> int:
        return len(self._intents)

    def to_dict(self) -> Dict:
        return {
            "next_sequence": self._next_sequence,
            "intents": [
                {
                    "intent_id": i.intent_id,
                    "sequence": i.sequence,
                    "process_id": i.process_id,
                    "scale": i.scale,
                    "duration_hours": i.duration_hours,
                    "output_quantity": i.output_quantity,
                    "output_unit": i.output_unit,
                    "required_machines": i.required_machines,
                    "submitted_at": i.submitted_at,
                    "last_error": i.last_error,
                }
                for i in self.all_intents()
            ],
        }

    @staticmethod
    def from_dict(data: Dict) -> "DeferredIntentQueue":
        q = DeferredIntentQueue()
        q._next_sequence = int(data.get("next_sequence", 1))
        for row in data.get("intents", []):
            intent = ProcessIntent(
                intent_id=str(row["intent_id"]),
                sequence=int(row["sequence"]),
                process_id=str(row["process_id"]),
                scale=float(row.get("scale", 1.0)),
                duration_hours=row.get("duration_hours"),
                output_quantity=row.get("output_quantity"),
                output_unit=row.get("output_unit"),
                required_machines=list(row.get("required_machines", [])),
                submitted_at=float(row.get("submitted_at", 0.0)),
                last_error=row.get("last_error"),
            )
            q.add(intent)
        if q._intents:
            q._next_sequence = max(q._next_sequence, max(i.sequence for i in q._intents.values()) + 1)
        return q
