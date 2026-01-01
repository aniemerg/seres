"""End-to-end integration tests for simulation and closure analysis."""
from pathlib import Path

import pytest
import yaml

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine
from src.indexer.closure_analysis import ClosureAnalyzer


@pytest.fixture
def kb_loader(kb_root):
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    return kb


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        yaml.dump(data, handle, default_flow_style=False, sort_keys=False)


def test_simulation_lifecycle(kb_loader, tmp_path):
    """Test complete simulation lifecycle."""
    sim_dir = tmp_path / "simulations" / "lifecycle"
    engine = SimulationEngine("lifecycle", kb_loader, sim_dir)

    engine.import_item("anorthite_ore", 2.0, "kg")

    start = engine.start_process(
        process_id="crushing_basic_v0",
        duration_hours=0.3,
    )
    assert start["success"] is True

    advance = engine.advance_time(0.3)
    assert advance["completed_count"] == 1
    assert "regolith_crushed" in engine.state.inventory

    # Build a machine from BOM components
    engine.import_item("steel_ingot", 8, "count")
    engine.import_item("steel_plate_or_sheet", 4, "count")
    engine.import_item("steel_sheet_1mm", 12, "count")

    build = engine.build_machine("pellet_press")
    assert build["success"] is True
    assert "pellet_press" in engine.state.machines_built

    engine.save()

    # Reload simulation and verify persistence
    reloaded = SimulationEngine("lifecycle", kb_loader, sim_dir)
    assert reloaded.load() is True
    assert "pellet_press" in reloaded.state.machines_built
    assert "regolith_crushed" in reloaded.state.inventory


def test_validation_at_runtime(tmp_path):
    """Test that runtime validation catches errors."""
    kb_root = tmp_path / "kb"
    (kb_root / "processes").mkdir(parents=True, exist_ok=True)
    (kb_root / "items" / "materials").mkdir(parents=True, exist_ok=True)

    write_yaml(kb_root / "processes" / "broken_process.yaml", {
        "id": "broken_process",
        "kind": "process",
        "process_type": "continuous",
        "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
        "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
        "time_model": {
            "type": "linear_rate",
            "rate": 10.0,
            "rate_unit": "kg/hr",
        },
    })

    write_yaml(kb_root / "items" / "materials" / "ore.yaml", {
        "id": "ore",
        "kind": "material",
        "mass": 1.0,
        "unit": "kg",
    })

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    engine = SimulationEngine("validation", kb, tmp_path / "simulations")
    engine.import_item("ore", 1.0, "kg")

    result = engine.start_process(
        process_id="broken_process",
        duration_hours=1.0,
    )

    assert result["success"] is False
    assert result["error"] == "validation_error"


def test_closure_analysis_integration(kb_loader):
    """Test closure analysis with real KB."""
    analyzer = ClosureAnalyzer(kb_loader)

    for machine_id in ["pellet_press", "3d_printer_basic_v0", "labor_bot_general_v0"]:
        result = analyzer.analyze_machine(machine_id)
        assert result["machine_id"] == machine_id
        assert 0.0 <= result["isru_percent"] <= 100.0
        assert isinstance(result["errors"], list)


def test_recipe_energy_calculation_from_steps(tmp_path):
    """Recipe energy should sum step process energy when inputs/outputs are explicit."""
    kb_root = tmp_path / "kb"
    (kb_root / "processes").mkdir(parents=True, exist_ok=True)
    (kb_root / "recipes").mkdir(parents=True, exist_ok=True)
    (kb_root / "items" / "materials").mkdir(parents=True, exist_ok=True)

    write_yaml(kb_root / "processes" / "step_process.yaml", {
        "id": "step_process",
        "kind": "process",
        "process_type": "continuous",
        "inputs": [{"item_id": "input_material", "qty": 1.0, "unit": "kg"}],
        "outputs": [{"item_id": "output_material", "qty": 1.0, "unit": "kg"}],
        "time_model": {
            "type": "linear_rate",
            "rate": 1.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "input_material",
        },
        "energy_model": {
            "type": "per_unit",
            "value": 2.0,
            "unit": "kWh/kg",
            "scaling_basis": "input_material",
        },
    })

    write_yaml(kb_root / "recipes" / "test_recipe.yaml", {
        "id": "test_recipe",
        "target_item_id": "output_material",
        "variant_id": "v0",
        "inputs": [{"item_id": "input_material", "qty": 2.0, "unit": "kg"}],
        "outputs": [{"item_id": "output_material", "qty": 2.0, "unit": "kg"}],
        "steps": [
            {
                "process_id": "step_process",
                "inputs": [{"item_id": "input_material", "qty": 2.0, "unit": "kg"}],
                "outputs": [{"item_id": "output_material", "qty": 2.0, "unit": "kg"}],
            }
        ],
    })

    write_yaml(kb_root / "items" / "materials" / "input_material.yaml", {
        "id": "input_material",
        "kind": "material",
        "mass": 1.0,
        "unit": "kg",
    })
    write_yaml(kb_root / "items" / "materials" / "output_material.yaml", {
        "id": "output_material",
        "kind": "material",
        "mass": 1.0,
        "unit": "kg",
    })

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    engine = SimulationEngine("recipe_energy", kb, tmp_path / "simulations")
    engine.import_item("input_material", 2.0, "kg")

    result = engine.run_recipe("test_recipe", 1)
    assert result["success"] is True

    advance = engine.advance_time(1.0)
    assert advance["completed_count"] == 1

    completed = advance["completed"][0]
    assert completed["process_id"] == "recipe:test_recipe"
    assert completed["energy_kwh"] == pytest.approx(4.0, rel=0.01)
