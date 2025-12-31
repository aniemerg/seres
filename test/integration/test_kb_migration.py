"""Integration tests against migrated KB schemas (ADR-012/014/017)."""
from pathlib import Path

import pytest
import yaml

from src.kb_core.kb_loader import KBLoader
from src.simulation.engine import SimulationEngine


@pytest.fixture
def kb_loader(kb_root):
    """Load the real KB once for integration tests."""
    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()
    return kb


@pytest.fixture
def sim_dir(tmp_path):
    return tmp_path / "simulations"


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        yaml.dump(data, handle, default_flow_style=False, sort_keys=False)


def test_process_with_linear_rate_time_model(kb_loader, sim_dir):
    """Test duration calculation for continuous process."""
    engine = SimulationEngine("linear_rate", kb_loader, sim_dir)

    # regolith_mining_highlands_v0: 100 kg output / 12.5 kg/hr = 8 hr
    result = engine.start_process(
        process_id="regolith_mining_highlands_v0",
        output_quantity=100.0,
        output_unit="kg",
    )

    assert result["success"] is True
    assert result["duration_hours"] == pytest.approx(8.0, rel=0.01)


def test_process_with_batch_time_model(kb_loader, sim_dir):
    """Test duration calculation for batch process."""
    engine = SimulationEngine("batch_time", kb_loader, sim_dir)
    # Process takes 1.0 kg input, produces 0.95 kg output
    # To get 1.0 kg output, need 1.0/0.95 = ~1.053 kg input
    engine.import_item("metal_sheet_or_plate", 2.0, "kg")

    # metal_forming_basic_v0: hr_per_batch = 1.5
    result = engine.start_process(
        process_id="metal_forming_basic_v0",
        output_quantity=1.0,
        output_unit="kg",
    )

    assert result["success"] is True
    assert result["duration_hours"] == pytest.approx(1.5, rel=0.01)


def test_energy_calculation_per_unit(kb_loader, sim_dir):
    """Test energy calculation with per_unit model."""
    engine = SimulationEngine("energy_per_unit", kb_loader, sim_dir)

    result = engine.start_process(
        process_id="regolith_mining_highlands_v0",
        duration_hours=8.0,
    )
    assert result["success"] is True

    advance = engine.advance_time(8.0)
    assert advance["completed_count"] == 1

    completed = advance["completed"][0]
    assert completed["energy_kwh"] == pytest.approx(50.0, rel=0.01)


def test_energy_calculation_fixed_per_batch(kb_loader, sim_dir):
    """Test energy calculation with fixed_per_batch model."""
    engine = SimulationEngine("energy_fixed", kb_loader, sim_dir)
    engine.import_item("metal_sheet_or_plate", 1.0, "kg")

    result = engine.start_process(
        process_id="metal_forming_basic_v0",
        duration_hours=1.5,
    )
    assert result["success"] is True

    advance = engine.advance_time(1.5)
    assert advance["completed_count"] == 1

    completed = advance["completed"][0]
    assert completed["energy_kwh"] == pytest.approx(1.5, rel=0.01)


def test_recipe_with_complete_override(tmp_path):
    """Test recipe step with complete time_model override."""
    kb_root = tmp_path / "kb"
    (kb_root / "processes").mkdir(parents=True, exist_ok=True)
    (kb_root / "recipes").mkdir(parents=True, exist_ok=True)

    write_yaml(kb_root / "processes" / "base_process.yaml", {
        "id": "base_process",
        "kind": "process",
        "process_type": "continuous",
        "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
        "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
        "time_model": {
            "type": "linear_rate",
            "rate": 10.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "ore",
        },
    })

    write_yaml(kb_root / "recipes" / "test_recipe.yaml", {
        "id": "test_recipe",
        "target_item_id": "metal",
        "variant_id": "v0",
        "steps": [
            {
                "process_id": "base_process",
                "time_model": {
                    "type": "linear_rate",
                    "rate": 5.0,
                    "rate_unit": "kg/hr",
                    "scaling_basis": "ore",
                },
            }
        ],
    })

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    engine = SimulationEngine("override_complete", kb, tmp_path / "sims")
    step = kb.get_recipe("test_recipe").model_dump()["steps"][0]
    resolved = engine.resolve_step(step)

    assert resolved["time_model"]["rate"] == 5.0
    assert resolved["time_model"]["type"] == "linear_rate"


def test_recipe_with_partial_override(tmp_path):
    """Test recipe step with partial time_model override."""
    kb_root = tmp_path / "kb"
    (kb_root / "processes").mkdir(parents=True, exist_ok=True)
    (kb_root / "recipes").mkdir(parents=True, exist_ok=True)

    write_yaml(kb_root / "processes" / "base_process.yaml", {
        "id": "base_process",
        "kind": "process",
        "process_type": "continuous",
        "inputs": [{"item_id": "ore", "qty": 1.0, "unit": "kg"}],
        "outputs": [{"item_id": "metal", "qty": 1.0, "unit": "kg"}],
        "time_model": {
            "type": "linear_rate",
            "rate": 10.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "ore",
        },
    })

    write_yaml(kb_root / "recipes" / "test_recipe.yaml", {
        "id": "test_recipe",
        "target_item_id": "metal",
        "variant_id": "v0",
        "steps": [
            {
                "process_id": "base_process",
                "time_model": {
                    "rate": 20.0,
                },
            }
        ],
    })

    kb = KBLoader(kb_root, use_validated_models=False)
    kb.load_all()

    engine = SimulationEngine("override_partial", kb, tmp_path / "sims")
    step = kb.get_recipe("test_recipe").model_dump()["steps"][0]
    resolved = engine.resolve_step(step)

    assert resolved["time_model"]["rate"] == 20.0
    assert resolved["time_model"]["type"] == "linear_rate"
    assert resolved["time_model"]["rate_unit"] == "kg/hr"
    assert resolved["time_model"]["scaling_basis"] == "ore"


def test_full_bootstrap_chain(kb_loader, sim_dir):
    """Test complete production chain from regolith to processed output."""
    engine = SimulationEngine("bootstrap_chain", kb_loader, sim_dir)

    # Bootstrap imports
    engine.import_item("labor_bot_general_v0", 2.0, "unit")
    engine.import_item("magnesium_metal_v0", 2.31, "kg")
    engine.import_item("methyl_chloride_gas", 1.0, "kg")

    # Mine regolith
    mine = engine.start_process(
        process_id="regolith_mining_highlands_v0",
        duration_hours=8.0,
    )
    assert mine["success"] is True
    engine.advance_time(8.0)
    assert engine.state.inventory["regolith_lunar_highlands"].quantity == pytest.approx(100.0, rel=0.01)

    # Extract silicon
    extract = engine.start_process(
        process_id="silicon_extraction_from_regolith_magnesiothermic_v0",
        duration_hours=0.9,
    )
    assert extract["success"] is True
    engine.advance_time(0.9)
    assert engine.state.inventory["silicon_metal_v0"].quantity == pytest.approx(1.0, rel=0.01)

    # Rochow process
    rochow = engine.start_process(
        process_id="rochow_process_reactor_v0",
        duration_hours=1.0,
    )
    assert rochow["success"] is True
    engine.advance_time(1.0)
    assert engine.state.inventory["methyl_trichlorosilane_v0"].quantity == pytest.approx(1.0, rel=0.01)
