"""
KB Loader - Load and index knowledge base data

Consolidates loading logic from base_builder and kbtool with:
- Lazy loading with caching (for simulation)
- Eager loading (for indexer)
- Raw model parsing (permissive)
- Optional validated model conversion (strict)
"""
from __future__ import annotations

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any, Literal

from .schema import (
    RAW_MODEL_MAP,
    VALIDATED_MODEL_MAP,
    RawProcess,
    RawRecipe,
    RawItem,
    Process,
    Recipe,
    Item,
)


class KBLoader:
    """
    Loads and indexes KB data for simulation and indexing.

    Two usage modes:
    1. Lazy loading (default) - Load items on-demand with caching
    2. Eager loading (load_all()) - Load everything upfront for indexing

    Uses two-layer model architecture:
    - Raw models for permissive parsing
    - Validated models for strict simulation (optional)
    """

    def __init__(
        self,
        kb_root: Path,
        use_validated_models: bool = False,
        cache_enabled: bool = True
    ):
        """
        Initialize KB loader.

        Args:
            kb_root: Path to KB root directory (containing processes/, recipes/, etc.)
            use_validated_models: If True, parse and validate using strict models
            cache_enabled: If True, cache loaded items (recommended)
        """
        self.kb_root = kb_root
        self.use_validated_models = use_validated_models
        self.cache_enabled = cache_enabled

        # Lazy-loaded caches (populated on-demand)
        self._processes: Optional[Dict[str, Any]] = {} if cache_enabled else None
        self._recipes: Optional[Dict[str, Any]] = {} if cache_enabled else None
        self._items: Optional[Dict[str, Any]] = {} if cache_enabled else None
        self._recipe_index: Optional[Dict[str, Path]] = None

        # Eager-loaded indexes (populated by load_all())
        self.processes: Dict[str, Any] = {}
        self.recipes: Dict[str, Any] = {}
        self.items: Dict[str, Any] = {}
        self.boms: Dict[str, Any] = {}
        self.units: Dict[str, Any] = {}
        self.materials: Dict[str, Any] = {}
        self._boms_loaded = False
        self._units_loaded = False
        self._materials_loaded = False

        # Error tracking
        self.load_errors: List[str] = []

    # =========================================================================
    # Eager Loading (for indexer)
    # =========================================================================

    def load_all(self) -> None:
        """
        Load all KB data eagerly and build indexes.

        Used by indexer for complete KB scan.
        Populates: processes, recipes, items, boms, units, materials
        """
        self.load_processes()
        self.load_recipes()
        self.load_items()
        self.load_boms()
        self.load_units()
        self.load_material_properties()

    def load_processes(self) -> None:
        """Load all processes from kb/processes/*.yaml"""
        processes_dir = self.kb_root / "processes"
        if not processes_dir.exists():
            self.load_errors.append(f"Processes directory not found: {processes_dir}")
            return

        for process_file in processes_dir.glob("*.yaml"):
            try:
                data = self._load_yaml_file(process_file)
                if data:
                    # Add defined_in metadata
                    data['defined_in'] = str(process_file.relative_to(self.kb_root.parent))
                    process_id = data.get("id", process_file.stem)
                    self.processes[process_id] = self._parse_model(data, "process")
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
                data = self._load_yaml_file(recipe_file)
                if data:
                    # Add defined_in metadata
                    data['defined_in'] = str(recipe_file.relative_to(self.kb_root.parent))
                    recipe_id = data.get("id", recipe_file.stem)
                    self.recipes[recipe_id] = self._parse_model(data, "recipe")
            except Exception as e:
                self.load_errors.append(f"Failed to load recipe {recipe_file.name}: {e}")

    def load_items(self) -> None:
        """Load all items from kb/items/**/*.yaml and kb/imports/**/*.yaml"""
        # Load from kb/items/
        items_dir = self.kb_root / "items"
        if items_dir.exists():
            for item_file in items_dir.rglob("*.yaml"):
                try:
                    data = self._load_yaml_file(item_file)
                    if data:
                        # Add defined_in metadata for raw material detection
                        data['defined_in'] = str(item_file.relative_to(self.kb_root.parent))
                        item_id = data.get("id", item_file.stem)
                        self.items[item_id] = self._parse_model(data, data.get("kind", "material"))
                except Exception as e:
                    self.load_errors.append(f"Failed to load item {item_file.name}: {e}")

        # Load from kb/imports/ (ADR-007 architecture)
        imports_dir = self.kb_root / "imports"
        if imports_dir.exists():
            for item_file in imports_dir.rglob("*.yaml"):
                try:
                    data = self._load_yaml_file(item_file)
                    if data:
                        # Add defined_in metadata for import detection
                        data['defined_in'] = str(item_file.relative_to(self.kb_root.parent))
                        item_id = data.get("id", item_file.stem)
                        self.items[item_id] = self._parse_model(data, data.get("kind", "material"))
                except Exception as e:
                    self.load_errors.append(f"Failed to load import item {item_file.name}: {e}")

    def load_boms(self) -> None:
        """Load all BOMs from kb/boms/*.yaml"""
        boms_dir = self.kb_root / "boms"
        if not boms_dir.exists():
            self._boms_loaded = True
            return

        for bom_file in boms_dir.glob("*.yaml"):
            try:
                data = self._load_yaml_file(bom_file)
                if data:
                    bom_id = data.get("id", bom_file.stem)
                    owner_item_id = data.get("owner_item_id")
                    # Prefer explicit owner_item_id when provided; fallback to bom_<machine_id> convention.
                    if owner_item_id:
                        machine_id = owner_item_id
                    elif bom_id.startswith("bom_"):
                        machine_id = bom_id[4:]
                    else:
                        machine_id = bom_id
                    self.boms[machine_id] = data
            except Exception as e:
                self.load_errors.append(f"Failed to load BOM {bom_file.name}: {e}")
        self._boms_loaded = True

    def load_units(self) -> None:
        """Load unit definitions from kb/units/units.yaml"""
        units_file = self.kb_root / "units" / "units.yaml"
        if not units_file.exists():
            # Set defaults per ADR-016
            self.units = {
                "units": {
                    "mass": ["kg", "g", "tonne"],
                    "volume": ["m3", "L", "liter"],
                    "count": ["unit", "each", "count"],
                    "time": ["hr", "min", "s", "day"],
                    "energy": ["kWh", "MJ", "GJ"]
                },
                "conversions": [
                    # Mass
                    {"from": "kg", "to": "g", "factor": 1000.0},
                    {"from": "kg", "to": "tonne", "factor": 0.001},
                    # Volume
                    {"from": "L", "to": "mL", "factor": 1000.0},
                    {"from": "m3", "to": "L", "factor": 1000.0},
                    # Time
                    {"from": "hr", "to": "min", "factor": 60.0},
                    {"from": "hr", "to": "s", "factor": 3600.0},
                    {"from": "day", "to": "hr", "factor": 24.0},
                    # Energy
                    {"from": "kWh", "to": "MJ", "factor": 3.6},
                    # Count synonyms
                    {"from": "unit", "to": "each", "factor": 1.0},
                    {"from": "unit", "to": "count", "factor": 1.0},
                ]
            }
            self._units_loaded = True
            return

        try:
            self.units = self._load_yaml_file(units_file) or {}
        except Exception as e:
            self.load_errors.append(f"Failed to load units: {e}")
            self.units = {}
        self._units_loaded = True

    def load_material_properties(self) -> None:
        """Load material properties from kb/materials/properties.yaml"""
        props_file = self.kb_root / "materials" / "properties.yaml"
        if not props_file.exists():
            # Set defaults
            self.materials = {
                "material_properties": {
                    "steel": {"density_kg_per_m3": 7850},
                    "aluminum": {"density_kg_per_m3": 2700},
                    "water": {"density_kg_per_m3": 1000},
                }
            }
            self._materials_loaded = True
            return

        try:
            self.materials = self._load_yaml_file(props_file) or {}
        except Exception as e:
            self.load_errors.append(f"Failed to load material properties: {e}")
            self.materials = {}
        self._materials_loaded = True

    # =========================================================================
    # Lazy Loading (for simulation)
    # =========================================================================

    def get_process(self, process_id: str) -> Optional[Any]:
        """
        Get process definition (lazy-loaded with caching).

        Returns:
            RawProcess or Process (depending on use_validated_models)
            None if not found
        """
        # Check eager-loaded index first
        if process_id in self.processes:
            return self.processes[process_id]

        # Check cache
        if self.cache_enabled and self._processes is not None:
            if process_id in self._processes:
                return self._processes[process_id]

        # Lazy load from file
        process_file = self.kb_root / "processes" / f"{process_id}.yaml"
        if not process_file.exists():
            return None

        try:
            data = self._load_yaml_file(process_file)
            if data:
                model = self._parse_model(data, "process")
                # Cache it
                if self.cache_enabled and self._processes is not None:
                    self._processes[process_id] = model
                return model
        except Exception as e:
            self.load_errors.append(f"Failed to lazy-load process {process_id}: {e}")
            return None

    def get_recipe(self, recipe_id: str) -> Optional[Any]:
        """
        Get recipe definition (lazy-loaded with caching).

        Returns:
            RawRecipe or Recipe (depending on use_validated_models)
            None if not found
        """
        # Check eager-loaded index first
        if recipe_id in self.recipes:
            return self.recipes[recipe_id]

        # Check cache
        if self.cache_enabled and self._recipes is not None:
            if recipe_id in self._recipes:
                return self._recipes[recipe_id]

        # Lazy load from file
        recipe_file = self.kb_root / "recipes" / f"{recipe_id}.yaml"
        if not recipe_file.exists():
            recipe_file = self._find_recipe_file(recipe_id)
            if recipe_file is None:
                return None

        try:
            data = self._load_yaml_file(recipe_file)
            if data:
                model = self._parse_model(data, "recipe")
                # Cache it
                if self.cache_enabled and self._recipes is not None:
                    self._recipes[recipe_id] = model
                return model
        except Exception as e:
            self.load_errors.append(f"Failed to lazy-load recipe {recipe_id}: {e}")
            return None

    def _find_recipe_file(self, recipe_id: str) -> Optional[Path]:
        """
        Find recipe file by scanning recipe IDs (fallback for mismatched filenames).
        """
        if self._recipe_index is None:
            self._recipe_index = {}
            recipes_dir = self.kb_root / "recipes"
            if not recipes_dir.exists():
                return None
            for recipe_file in recipes_dir.glob("*.yaml"):
                try:
                    data = self._load_yaml_file(recipe_file)
                    if not data:
                        continue
                    rid = data.get("id", recipe_file.stem)
                    if isinstance(rid, str):
                        self._recipe_index[rid] = recipe_file
                except Exception as e:
                    self.load_errors.append(f"Failed to index recipe {recipe_file.name}: {e}")
        return self._recipe_index.get(recipe_id)

    def get_item(self, item_id: str) -> Optional[Any]:
        """
        Get item definition (lazy-loaded with caching).

        Returns:
            RawItem or Item (depending on use_validated_models)
            None if not found
        """
        # Check eager-loaded index first
        if item_id in self.items:
            return self.items[item_id]

        # Check cache
        if self.cache_enabled and self._items is not None:
            if item_id in self._items:
                return self._items[item_id]

        # Lazy load from file (try multiple locations)
        # Try kb/items/<kind>/<item_id>.yaml
        for kind in ["materials", "raw_materials", "parts", "machines"]:
            item_file = self.kb_root / "items" / kind / f"{item_id}.yaml"
            if item_file.exists():
                try:
                    data = self._load_yaml_file(item_file)
                    if data:
                        parse_kind = data.get("kind", "material")
                        model = self._parse_model(data, parse_kind)
                        # Cache it
                        if self.cache_enabled and self._items is not None:
                            self._items[item_id] = model
                        return model
                except Exception as e:
                    self.load_errors.append(f"Failed to lazy-load item {item_id}: {e}")
                    return None

        # Try kb/imports/**/<item_id>.yaml
        imports_dir = self.kb_root / "imports"
        if imports_dir.exists():
            for item_file in imports_dir.rglob(f"{item_id}.yaml"):
                try:
                    data = self._load_yaml_file(item_file)
                    if data:
                        model = self._parse_model(data, data.get("kind", "material"))
                        # Cache it
                        if self.cache_enabled and self._items is not None:
                            self._items[item_id] = model
                        return model
                except Exception as e:
                    self.load_errors.append(f"Failed to lazy-load item {item_id}: {e}")
                    return None

        return None

    def get_bom(self, machine_id: str) -> Optional[dict]:
        """Get BOM definition or None if not found."""
        if not self._boms_loaded:
            self.load_boms()
        return self.boms.get(machine_id)

    # =========================================================================
    # Unit Conversion Support (for UnitConverter)
    # =========================================================================

    def get_material_density(self, material_name: str) -> Optional[float]:
        """Get material density in kg/m³ or None if not found."""
        if not self._materials_loaded:
            self.load_material_properties()
        props = self.materials.get("material_properties", {})
        material_data = props.get(material_name, {})
        return material_data.get("density_kg_per_m3")

    def get_unit_conversion(self, from_unit: str, to_unit: str) -> Optional[float]:
        """Get conversion factor from_unit -> to_unit, or None if not found."""
        if not self._units_loaded:
            self.load_units()
        conversions = self.units.get("conversions", [])
        for conv in conversions:
            if conv.get("from") == from_unit and conv.get("to") == to_unit:
                return conv.get("factor")
        return None

    # =========================================================================
    # Internal Helpers
    # =========================================================================

    def _load_yaml_file(self, path: Path) -> Optional[dict]:
        """Load YAML file and return data."""
        try:
            with path.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if not isinstance(data, dict):
                self.load_errors.append(f"{path}: expected dict, got {type(data).__name__}")
                return None
            return data
        except Exception as e:
            self.load_errors.append(f"{path}: failed to parse - {e}")
            return None

    def _parse_model(self, data: dict, kind: str) -> Any:
        """
        Parse data into raw or validated model.

        Args:
            data: YAML data dict
            kind: Model kind (process, recipe, material, part, machine)

        Returns:
            Raw model or validated model instance (depending on use_validated_models)
        """
        if self.use_validated_models:
            # Use validated models (strict)
            model_class = VALIDATED_MODEL_MAP.get(kind)
            if model_class:
                # First parse as raw to handle deprecated fields
                raw_class = RAW_MODEL_MAP.get(kind)
                if raw_class:
                    raw_model = raw_class.model_validate(data)
                    # Convert to validated (excluding None deprecated fields)
                    payload = raw_model.model_dump(exclude_none=True)
                    payload.pop("defined_in", None)
                    return model_class.model_validate(payload)
                else:
                    # Fallback: direct validation
                    return model_class.model_validate(data)
            else:
                # No model class, return raw dict
                return data
        else:
            # Use raw models (permissive)
            model_class = RAW_MODEL_MAP.get(kind)
            if model_class:
                return model_class.model_validate(data)
            else:
                # No model class, return raw dict
                return data
