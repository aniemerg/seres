"""
KB Loader - Load and index knowledge base data.

Loads processes, recipes, items, BOMs, units, and material properties.
"""
from __future__ import annotations

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any


class KBLoader:
    """
    Loads and indexes KB data for the simulation.

    Indexes:
    - processes: Dict[process_id, process_definition]
    - recipes: Dict[recipe_id, recipe_definition]
    - items: Dict[item_id, item_definition]
    - boms: Dict[machine_id, bom_definition]
    - units: Dict with unit conversion data
    - materials: Dict with material properties (densities, etc.)
    """

    def __init__(self, kb_root: Path):
        self.kb_root = kb_root

        # Indexes
        self.processes: Dict[str, dict] = {}
        self.recipes: Dict[str, dict] = {}
        self.items: Dict[str, dict] = {}
        self.boms: Dict[str, dict] = {}
        self.units: Dict[str, Any] = {}
        self.materials: Dict[str, Any] = {}

        # Counters
        self.load_errors: List[str] = []

    def load_all(self) -> None:
        """Load all KB data and build indexes."""
        print("Loading KB data...")

        self.load_processes()
        self.load_recipes()
        self.load_items()
        self.load_boms()
        self.load_units()
        self.load_material_properties()

        print(f"Loaded: {len(self.processes)} processes, {len(self.recipes)} recipes, "
              f"{len(self.items)} items, {len(self.boms)} BOMs")

        if self.load_errors:
            print(f"Load errors: {len(self.load_errors)}")
            for err in self.load_errors[:5]:
                print(f"  - {err}")
            if len(self.load_errors) > 5:
                print(f"  ... and {len(self.load_errors) - 5} more")

    def load_processes(self) -> None:
        """Load all processes from kb/processes/*.yaml"""
        processes_dir = self.kb_root / "processes"
        if not processes_dir.exists():
            self.load_errors.append(f"Processes directory not found: {processes_dir}")
            return

        for process_file in processes_dir.glob("*.yaml"):
            try:
                with process_file.open() as f:
                    data = yaml.safe_load(f)

                if data and isinstance(data, dict):
                    process_id = data.get("id", process_file.stem)
                    self.processes[process_id] = data
            except Exception as e:
                self.load_errors.append(f"Failed to load process {process_file.name}: {e}")

    def load_recipes(self) -> None:
        """Load all recipes from kb/recipes/*.yaml"""
        recipes_dir = self.kb_root / "recipes"
        if not recipes_dir.exists():
            self.load_errors.append(f"Recipes directory not found: {recipes_dir}")
            return

        for recipe_file in recipes_dir.glob("*.yaml"):
            try:
                with recipe_file.open() as f:
                    data = yaml.safe_load(f)

                if data and isinstance(data, dict):
                    recipe_id = data.get("id", recipe_file.stem)
                    self.recipes[recipe_id] = data
            except Exception as e:
                self.load_errors.append(f"Failed to load recipe {recipe_file.name}: {e}")

    def load_items(self) -> None:
        """Load all items from kb/items/**/*.yaml and kb/imports/**/*.yaml"""
        # Load from kb/items/
        items_dir = self.kb_root / "items"
        if items_dir.exists():
            for item_file in items_dir.rglob("*.yaml"):
                try:
                    with item_file.open() as f:
                        data = yaml.safe_load(f)

                    if data and isinstance(data, dict):
                        item_id = data.get("id", item_file.stem)
                        # Add the file path for reference (relative to kb_root)
                        data['defined_in'] = str(item_file.relative_to(self.kb_root.parent))
                        self.items[item_id] = data
                except Exception as e:
                    self.load_errors.append(f"Failed to load item {item_file.name}: {e}")
        else:
            self.load_errors.append(f"Items directory not found: {items_dir}")

        # Load from kb/imports/ (ADR-007 architecture)
        imports_dir = self.kb_root / "imports"
        if imports_dir.exists():
            for item_file in imports_dir.rglob("*.yaml"):
                try:
                    with item_file.open() as f:
                        data = yaml.safe_load(f)

                    if data and isinstance(data, dict):
                        item_id = data.get("id", item_file.stem)
                        # Add the file path for reference (relative to kb_root)
                        data['defined_in'] = str(item_file.relative_to(self.kb_root.parent))
                        self.items[item_id] = data
                except Exception as e:
                    self.load_errors.append(f"Failed to load import item {item_file.name}: {e}")

    def load_boms(self) -> None:
        """Load all BOMs from kb/boms/*.yaml"""
        boms_dir = self.kb_root / "boms"
        if not boms_dir.exists():
            self.load_errors.append(f"BOMs directory not found: {boms_dir}")
            return

        for bom_file in boms_dir.glob("*.yaml"):
            try:
                with bom_file.open() as f:
                    data = yaml.safe_load(f)

                if data and isinstance(data, dict):
                    # BOM id is typically "bom_<machine_id>"
                    # Extract machine_id
                    bom_id = data.get("id", bom_file.stem)
                    if bom_id.startswith("bom_"):
                        machine_id = bom_id[4:]  # Remove "bom_" prefix
                    else:
                        machine_id = bom_id

                    self.boms[machine_id] = data
            except Exception as e:
                self.load_errors.append(f"Failed to load BOM {bom_file.name}: {e}")

    def load_units(self) -> None:
        """Load unit definitions from kb/units/units.yaml"""
        units_file = self.kb_root / "units" / "units.yaml"
        if not units_file.exists():
            self.load_errors.append(f"Units file not found: {units_file}")
            # Set defaults
            self.units = {
                "units": {
                    "mass": ["kg", "g", "tonne"],
                    "volume": ["m3", "liter"],
                    "count": ["count", "unit"],
                    "time": ["minute", "hour", "day"]
                },
                "conversions": []
            }
            return

        try:
            with units_file.open() as f:
                self.units = yaml.safe_load(f) or {}
        except Exception as e:
            self.load_errors.append(f"Failed to load units: {e}")
            self.units = {}

    def load_material_properties(self) -> None:
        """Load material properties from kb/materials/properties.yaml"""
        props_file = self.kb_root / "materials" / "properties.yaml"
        if not props_file.exists():
            self.load_errors.append(f"Material properties file not found: {props_file}")
            # Set defaults
            self.materials = {
                "material_properties": {
                    "steel": {"density_kg_per_m3": 7850},
                    "aluminum": {"density_kg_per_m3": 2700},
                    "regolith_lunar": {"density_kg_per_m3": 1500}
                }
            }
            return

        try:
            with props_file.open() as f:
                self.materials = yaml.safe_load(f) or {}
        except Exception as e:
            self.load_errors.append(f"Failed to load material properties: {e}")
            self.materials = {}

    # ========================================================================
    # Query methods
    # ========================================================================

    def get_process(self, process_id: str) -> Optional[dict]:
        """Get process definition or None if not found."""
        return self.processes.get(process_id)

    def get_recipe(self, recipe_id: str) -> Optional[dict]:
        """Get recipe definition or None if not found."""
        return self.recipes.get(recipe_id)

    def get_item(self, item_id: str) -> Optional[dict]:
        """Get item definition or None if not found."""
        return self.items.get(item_id)

    def get_bom(self, machine_id: str) -> Optional[dict]:
        """Get BOM definition or None if not found."""
        return self.boms.get(machine_id)

    def get_material_density(self, material_name: str) -> Optional[float]:
        """Get material density in kg/m3 or None if not found."""
        props = self.materials.get("material_properties", {})
        material_data = props.get(material_name, {})
        return material_data.get("density_kg_per_m3")

    def get_unit_conversion(self, from_unit: str, to_unit: str) -> Optional[float]:
        """Get conversion factor from_unit -> to_unit, or None if not found."""
        conversions = self.units.get("conversions", [])
        for conv in conversions:
            if conv.get("from") == from_unit and conv.get("to") == to_unit:
                return conv.get("factor")
        return None
