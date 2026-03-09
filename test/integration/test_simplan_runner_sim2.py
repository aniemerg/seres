from pathlib import Path

import yaml

from scripts.analysis.simplan import SimPlan
from scripts.analysis.simplan_runner import execute_plan


def _build_kb(tmp_path: Path) -> Path:
    kb = tmp_path / "kb"
    (kb / "processes").mkdir(parents=True)
    (kb / "recipes").mkdir(parents=True)
    (kb / "items" / "materials").mkdir(parents=True)
    (kb / "items" / "machines").mkdir(parents=True)
    (kb / "units").mkdir(parents=True)

    with open(kb / "units" / "units.yaml", "w") as f:
        yaml.dump(
            {
                "id": "unit_definitions_test_v0",
                "name": "Unit Definitions (test)",
                "units": {"mass": ["kg"], "count": ["count", "unit"], "time": ["hour"]},
                "conversions": [{"from": "hour", "to": "hour", "factor": 1.0}],
            },
            f,
        )

    with open(kb / "processes" / "smelt_v0.yaml", "w") as f:
        yaml.dump(
            {
                "id": "smelt_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "ingot", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [{"machine_id": "furnace", "qty": 1.0, "unit": "count"}],
            },
            f,
        )
    with open(kb / "processes" / "forge_v0.yaml", "w") as f:
        yaml.dump(
            {
                "id": "forge_v0",
                "kind": "process",
                "process_type": "batch",
                "inputs": [{"item_id": "ingot", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "part", "qty": 1.0, "unit": "kg"}],
                "time_model": {"type": "batch", "hr_per_batch": 1.0},
                "resource_requirements": [{"machine_id": "forge", "qty": 1.0, "unit": "count"}],
            },
            f,
        )

    with open(kb / "recipes" / "recipe_ingot_v0.yaml", "w") as f:
        yaml.dump(
            {
                "id": "recipe_ingot_v0",
                "target_item_id": "ingot",
                "variant_id": "v0",
                "steps": [{"process_id": "smelt_v0", "dependencies": []}],
            },
            f,
        )
    with open(kb / "recipes" / "recipe_part_v0.yaml", "w") as f:
        yaml.dump(
            {
                "id": "recipe_part_v0",
                "target_item_id": "part",
                "variant_id": "v0",
                "steps": [{"process_id": "forge_v0", "dependencies": []}],
            },
            f,
        )

    with open(kb / "items" / "materials" / "ore.yaml", "w") as f:
        yaml.dump({"id": "ore", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "materials" / "ingot.yaml", "w") as f:
        yaml.dump({"id": "ingot", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "materials" / "part.yaml", "w") as f:
        yaml.dump({"id": "part", "kind": "material", "unit": "kg", "mass": 1.0}, f)
    with open(kb / "items" / "machines" / "furnace.yaml", "w") as f:
        yaml.dump({"id": "furnace", "kind": "machine", "unit": "count", "mass": 100.0}, f)
    with open(kb / "items" / "machines" / "forge.yaml", "w") as f:
        yaml.dump({"id": "forge", "kind": "machine", "unit": "count", "mass": 100.0}, f)

    return kb


def test_execute_plan_sim2_sequential(tmp_path: Path):
    kb_root = _build_kb(tmp_path)
    sim_root = tmp_path / "simulations_parallel"

    plan = SimPlan(sim_id="plan_sim2", target_machine_id="part", build_machine=False)
    plan.add_import("ore", 10.0, "kg")
    plan.add_import("furnace", 1.0, "count")
    plan.add_import("forge", 1.0, "count")
    plan.add_recipe("recipe_ingot_v0", 2)
    plan.add_recipe("recipe_part_v0", 2)

    result = execute_plan(
        plan=plan,
        kb_root=kb_root,
        sim_root=sim_root,
        reset=True,
        dry_run=False,
        trace=False,
        engine_mode="sim2",
        strategy="sequential",
    )

    assert result["success"]
    assert (sim_root / "plan_sim2" / "snapshot.json").exists()
    assert (sim_root / "plan_sim2" / "deferred_intents.json").exists()
