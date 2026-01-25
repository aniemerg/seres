#!/usr/bin/env python3
"""
RunbookPlan: internal representation of a simulation plan that can be executed
directly (no markdown runbook required).
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


@dataclass
class PlanImport:
    item_id: str
    qty: float
    unit: str
    reason: Optional[str] = None


@dataclass
class PlanRecipe:
    recipe_id: str
    quantity: int
    reason: Optional[str] = None


@dataclass
class PlanNote:
    message: str
    style: str = "info"


@dataclass
class RunbookPlan:
    sim_id: str
    target_machine_id: str
    target_recipe_id: Optional[str] = None
    imports: Dict[str, PlanImport] = field(default_factory=dict)
    recipes: List[PlanRecipe] = field(default_factory=list)
    notes: List[PlanNote] = field(default_factory=list)
    build_machine: bool = True
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_import(self, item_id: str, qty: float, unit: str, reason: Optional[str] = None) -> None:
        existing = self.imports.get(item_id)
        if existing:
            if existing.unit == unit:
                existing.qty += qty
                if reason and existing.reason != reason:
                    existing.reason = f"{existing.reason}; {reason}" if existing.reason else reason
            else:
                # Unit mismatch; keep the larger one and note conflict.
                if reason:
                    existing.reason = f"{existing.reason}; {reason}" if existing.reason else reason
        else:
            self.imports[item_id] = PlanImport(item_id=item_id, qty=qty, unit=unit, reason=reason)

    def remove_import(self, item_id: str) -> None:
        if item_id in self.imports:
            del self.imports[item_id]

    def add_recipe(self, recipe_id: str, quantity: int, reason: Optional[str] = None) -> None:
        for entry in self.recipes:
            if entry.recipe_id == recipe_id:
                entry.quantity += quantity
                if reason and entry.reason != reason:
                    entry.reason = f"{entry.reason}; {reason}" if entry.reason else reason
                return
        self.recipes.append(PlanRecipe(recipe_id=recipe_id, quantity=quantity, reason=reason))

    def add_note(self, message: str, style: str = "info") -> None:
        self.notes.append(PlanNote(message=message, style=style))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sim_id": self.sim_id,
            "target_machine_id": self.target_machine_id,
            "target_recipe_id": self.target_recipe_id,
            "imports": {k: asdict(v) for k, v in self.imports.items()},
            "recipes": [asdict(r) for r in self.recipes],
            "notes": [asdict(n) for n in self.notes],
            "build_machine": self.build_machine,
            "metadata": self.metadata,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "RunbookPlan":
        plan = RunbookPlan(
            sim_id=data["sim_id"],
            target_machine_id=data["target_machine_id"],
            target_recipe_id=data.get("target_recipe_id"),
            build_machine=data.get("build_machine", True),
            metadata=data.get("metadata", {}),
        )
        for item_id, entry in data.get("imports", {}).items():
            plan.imports[item_id] = PlanImport(**entry)
        for recipe in data.get("recipes", []):
            plan.recipes.append(PlanRecipe(**recipe))
        for note in data.get("notes", []):
            plan.notes.append(PlanNote(**note))
        return plan

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @staticmethod
    def load(path: Path) -> "RunbookPlan":
        data = json.loads(path.read_text(encoding="utf-8"))
        return RunbookPlan.from_dict(data)
