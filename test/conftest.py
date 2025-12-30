"""
Pytest configuration and shared fixtures.
"""
import pytest
from pathlib import Path


@pytest.fixture
def kb_root():
    """Return path to KB root directory."""
    return Path(__file__).parent.parent / "kb"


@pytest.fixture
def test_fixtures_dir():
    """Return path to test fixtures directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_raw_process():
    """Return a sample raw process definition for testing."""
    return {
        "id": "test_process_v0",
        "kind": "process",
        "process_type": "continuous",
        "inputs": [
            {"item_id": "input_item", "qty": 10.0, "unit": "kg"}
        ],
        "outputs": [
            {"item_id": "output_item", "qty": 9.0, "unit": "kg"}
        ],
        "time_model": {
            "type": "linear_rate",
            "rate": 5.0,
            "rate_unit": "kg/hr",
            "scaling_basis": "input_item"
        },
        "energy_model": {
            "type": "per_unit",
            "value": 2.0,
            "unit": "kWh/kg",
            "scaling_basis": "input_item"
        }
    }


@pytest.fixture
def sample_raw_recipe():
    """Return a sample raw recipe definition for testing."""
    return {
        "id": "test_recipe_v0",
        "target_item_id": "final_product",
        "variant_id": "default",
        "steps": [
            {
                "process_id": "test_process_v0",
                "notes": "Production step"
            }
        ]
    }
