"""
Shared override resolution helpers (ADR-013).

Keeps recipe-step override behavior consistent across simulation, validators,
and indexer tooling.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Optional


def _normalize_def(defn: Any) -> Dict[str, Any]:
    if defn is None:
        return {}
    if hasattr(defn, "model_dump"):
        return defn.model_dump()
    if isinstance(defn, dict):
        return dict(defn)
    return dict(defn)


def _get_process_def(kb: Any, process_id: str) -> Optional[Any]:
    if kb is None:
        return None
    if hasattr(kb, "get_process"):
        return kb.get_process(process_id)
    processes = getattr(kb, "processes", None)
    if isinstance(processes, dict):
        return processes.get(process_id)
    return None


def resolve_recipe_step(step_def: Dict[str, Any], process_def: Optional[Any]) -> Dict[str, Any]:
    """
    Resolve a recipe step against a process definition using ADR-013 rules.

    Args:
        step_def: Recipe step definition (dict)
        process_def: Process definition (dict or model). If None, returns step_def.

    Returns:
        Resolved process definition (dict)
    """
    step = _normalize_def(step_def)
    if process_def is None:
        return dict(step)

    base = _normalize_def(process_def)
    resolved = deepcopy(base)

    # Override direct fields (step wins)
    for key in [
        "inputs",
        "outputs",
        "byproducts",
        "requires_ids",
        "resource_requirements",
        "energy_model",
    ]:
        if key in step:
            value = step.get(key)
            if value is None:
                continue
            if isinstance(value, list) and not value:
                continue
            resolved[key] = deepcopy(value)

    # ADR-013 time_model: partial override when type is missing/None
    if "time_model" in step:
        step_time_model = step.get("time_model")
        has_type = isinstance(step_time_model, dict) and step_time_model.get("type") is not None
        if not has_type:
            base_time_model = resolved.get("time_model", {})
            if isinstance(base_time_model, dict):
                merged = dict(base_time_model)
                if isinstance(step_time_model, dict):
                    for key, value in step_time_model.items():
                        if value is not None:
                            merged[key] = value
                resolved["time_model"] = merged
            else:
                resolved["time_model"] = step_time_model
        else:
            resolved["time_model"] = step_time_model

    # Apply scale multiplier if present
    scale = step.get("scale", 1.0)
    if scale != 1.0:
        for key in ["inputs", "outputs", "byproducts"]:
            for item in resolved.get(key, []) or []:
                if "qty" in item:
                    item["qty"] *= scale
                elif "quantity" in item:
                    item["quantity"] *= scale

    # Override specific time/labor estimates and notes
    for key in ["est_time_hr", "machine_hours", "labor_hours", "notes"]:
        if key in step:
            resolved[key] = step[key]

    return resolved


def resolve_recipe_step_with_kb(step_def: Dict[str, Any], kb: Any) -> Dict[str, Any]:
    """
    Resolve a recipe step using KB lookups for base processes.

    Returns step_def when process is missing.
    """
    if "process_id" not in step_def:
        return _normalize_def(step_def)

    process_id = step_def["process_id"]
    process_def = _get_process_def(kb, process_id)
    if not process_def:
        resolved = _normalize_def(step_def)
        resolved["_warning"] = f"Process '{process_id}' not found in KB"
        return resolved

    return resolve_recipe_step(step_def, process_def)
