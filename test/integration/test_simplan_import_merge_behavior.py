from pathlib import Path

import yaml

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_build_combined import _merge_plans
from scripts.analysis.simplan_runner import execute_plan
from src.kb_core.kb_loader import KBLoader


def _build_kb(tmp_path: Path) -> Path:
    kb = tmp_path / "kb"
    (kb / "processes").mkdir(parents=True)
    (kb / "recipes").mkdir(parents=True)
    (kb / "items" / "materials").mkdir(parents=True)
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

    with open(kb / "processes" / "smelt_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "smelt_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "ingot", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [{"machine_id": "labor_bot_general_v0", "qty": 1.0, "unit": "count"}],
            },
            f,
        )

    with open(kb / "recipes" / "recipe_ingot_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump(
            {
                "id": "recipe_ingot_v0",
                "target_item_id": "ingot",
                "variant_id": "v0",
                "steps": [{"process_id": "smelt_v0", "dependencies": []}],
            },
            f,
        )

    with open(kb / "items" / "materials" / "ore.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "materials" / "ingot.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "ingot", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "machines" / "labor_bot_general_v0.yaml", "w", encoding="utf-8") as f:
        yaml.dump({"id": "labor_bot_general_v0", "kind": "machine", "unit": "count", "mass": 100.0}, f)

    return kb


def test_combined_plan_uses_max_for_machine_imports_and_sum_for_materials(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    p1 = SimPlan(sim_id="s1", target_machine_id="m1", target_recipe_id="recipe_a", build_machine=False)
    p1.add_import("labor_bot_general_v0", 3.0, "count")
    p1.add_import("ore", 10.0, "kg")

    p2 = SimPlan(sim_id="s2", target_machine_id="m2", target_recipe_id="recipe_b", build_machine=False)
    p2.add_import("labor_bot_general_v0", 5.0, "count")
    p2.add_import("ore", 20.0, "kg")

    merged = _merge_plans([p1, p2], kb, sim_id="merged", allow_bom=False)

    assert merged.imports["labor_bot_general_v0"].qty == 5.0
    assert merged.imports["ore"].qty == 30.0


def test_execute_plan_imports_only_missing_delta(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    sim_root = tmp_path / "simulations"

    initial = SimPlan(sim_id="delta_topup", target_machine_id="ingot", build_machine=False)
    initial.add_import("ore", 5.0, "kg")
    result1 = execute_plan(
        plan=initial,
        kb_root=kb_root,
        sim_root=sim_root,
        reset=True,
        dry_run=False,
        trace=False,
        engine_mode="sim",
        strategy="sequential",
    )
    assert result1["success"]

    topup = SimPlan(sim_id="delta_topup", target_machine_id="ingot", build_machine=False)
    topup.add_import("ore", 7.0, "kg")
    result2 = execute_plan(
        plan=topup,
        kb_root=kb_root,
        sim_root=sim_root,
        reset=False,
        dry_run=False,
        trace=False,
        engine_mode="sim",
        strategy="sequential",
    )
    assert result2["success"]

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    from src.simulation.engine import SimulationEngine

    engine = SimulationEngine("delta_topup", kb, sim_root / "delta_topup")
    assert engine.load()
    assert engine.state.inventory["ore"].quantity == 7.0


def test_merge_plans_splits_same_recipe_by_machine_goal(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    p1 = SimPlan(sim_id="s1", target_machine_id="machine_alpha", target_recipe_id="recipe_alpha", build_machine=False)
    p1.add_recipe("recipe_ingot_v0", 3, reason="expand:ingot")

    p2 = SimPlan(sim_id="s2", target_machine_id="machine_beta", target_recipe_id="recipe_beta", build_machine=False)
    p2.add_recipe("recipe_ingot_v0", 5, reason="expand:ingot")

    merged = _merge_plans([p1, p2], kb, sim_id="merged_split", allow_bom=False)

    ingot_entries = [r for r in merged.recipes if r.recipe_id == "recipe_ingot_v0"]
    assert len(ingot_entries) == 2

    by_goal = {}
    for entry in ingot_entries:
        tags = entry.metadata.get("tags", {}) if isinstance(entry.metadata, dict) else {}
        by_goal[tags.get("goal.machine_id")] = entry.quantity

    assert by_goal["machine_alpha"] == 3
    assert by_goal["machine_beta"] == 5
