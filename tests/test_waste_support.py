from pathlib import Path

from src.kb_core.kb_loader import KBLoader
from src.kb_core.unit_converter import UnitConverter
from src.kb_core.validators import validate_recipe


def _make_converter() -> UnitConverter:
    kb = KBLoader(Path("kb"))
    return UnitConverter(kb)


def test_recipe_outputs_cannot_include_waste() -> None:
    converter = _make_converter()
    recipe = {
        "id": "test_recipe_waste_output",
        "target_item_id": "separator_frame",
        "inputs": [
            {"item_id": "steel_bar_stock", "qty": 1.0, "unit": "kg"},
        ],
        "outputs": [
            {"item_id": "separator_frame", "qty": 1.0, "unit": "unit"},
            {"item_id": "waste", "qty": 0.1, "unit": "kg"},
        ],
        "steps": [
            {
                "process_id": "machining_finish_basic_v0",
                "inputs": [{"item_id": "steel_bar_stock", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "separator_frame", "qty": 1.0, "unit": "unit"}],
            }
        ],
    }
    issues = validate_recipe(recipe, converter)
    assert any(i.rule == "recipe_outputs_waste_not_allowed" for i in issues)


def test_mass_balance_counts_byproducts() -> None:
    converter = _make_converter()
    recipe = {
        "id": "test_recipe_byproduct_mass_balance",
        "target_item_id": "machined_part_raw",
        "inputs": [
            {"item_id": "steel_bar_stock", "qty": 1.0, "unit": "kg"},
        ],
        "steps": [
            {
                "process_id": "machining_finish_basic_v0",
                "inputs": [{"item_id": "steel_bar_stock", "qty": 1.0, "unit": "kg"}],
                "outputs": [{"item_id": "machined_part_raw", "qty": 1.0, "unit": "kg"}],
                "byproducts": [{"item_id": "waste", "qty": 0.1, "unit": "kg"}],
            }
        ],
    }
    issues = validate_recipe(recipe, converter)
    assert any(i.rule == "recipe_step_mass_imbalance" for i in issues)
