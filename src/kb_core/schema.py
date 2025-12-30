"""
KB Core Schema Definitions

Two-layer model architecture:
- Raw models: Permissive parsing from YAML (allows nulls, extra fields)
- Validated models: Strict validation for simulation (requires all fields)

Implements ADR-012 (Process Types & Time Model), ADR-014 (Energy Model),
and ADR-013 (Recipe Overrides).
"""
from __future__ import annotations

from typing import List, Optional, Literal
from pydantic import BaseModel, Field, ConfigDict


# =============================================================================
# Raw Models (Permissive - for YAML parsing)
# =============================================================================

class RawQuantity(BaseModel):
    """Raw quantity specification (permissive parsing)."""
    model_config = ConfigDict(extra="allow")

    item_id: Optional[str] = None
    qty: Optional[float] = None
    unit: Optional[str] = None
    notes: Optional[str] = None


class RawRequirement(BaseModel):
    """Raw resource requirement (permissive parsing)."""
    model_config = ConfigDict(extra="allow")

    machine_id: Optional[str] = Field(default=None, alias="resource_type")
    qty: Optional[float] = None
    unit: Optional[str] = None
    notes: Optional[str] = None


class RawTimeModel(BaseModel):
    """
    Raw time model (permissive parsing).

    Supports both new schema (ADR-012) and deprecated fields for migration.

    New schema (ADR-012):
        type: "linear_rate" or "batch"

        For linear_rate:
            rate: float (e.g., 10.0)
            rate_unit: str (e.g., "kg/hr", "L/min", "unit/hr")
            scaling_basis: str (item_id from inputs/outputs)

        For batch:
            hr_per_batch: float
            setup_hr: float (optional, default 0)

    Deprecated fields (will trigger validation errors):
        rate_kg_per_hr: float
        hr_per_kg: float
    """
    model_config = ConfigDict(extra="allow")

    # New schema (ADR-012)
    type: Optional[str] = None  # "linear_rate" or "batch"
    rate: Optional[float] = None
    rate_unit: Optional[str] = None
    scaling_basis: Optional[str] = None
    hr_per_batch: Optional[float] = None
    setup_hr: Optional[float] = None

    # Deprecated fields (for parsing old data)
    rate_kg_per_hr: Optional[float] = None
    hr_per_kg: Optional[float] = None

    notes: Optional[str] = None


class RawEnergyModel(BaseModel):
    """
    Raw energy model (permissive parsing).

    Supports both new schema (ADR-014) and deprecated fields for migration.

    New schema (ADR-014):
        type: "per_unit" or "fixed_per_batch"

        For per_unit:
            value: float (e.g., 50.0)
            unit: str (e.g., "kWh/kg", "MJ/unit")
            scaling_basis: str (item_id from inputs/outputs)

        For fixed_per_batch:
            value: float (e.g., 100.0)
            unit: str (e.g., "kWh", "MJ")

    Deprecated fields:
        type: "kWh_per_kg", "fixed_kWh", etc.
    """
    model_config = ConfigDict(extra="allow")

    # New schema (ADR-014)
    type: Optional[str] = None
    value: Optional[float] = None
    unit: Optional[str] = None
    scaling_basis: Optional[str] = None

    notes: Optional[str] = None


class RawProcess(BaseModel):
    """Raw process definition (permissive parsing)."""
    model_config = ConfigDict(extra="allow")

    id: str
    kind: str = "process"
    name: Optional[str] = None

    # ADR-012: process_type required (but optional in raw for migration)
    process_type: Optional[str] = None  # "batch", "continuous", or "boundary"

    inputs: List[RawQuantity] = Field(default_factory=list)
    outputs: List[RawQuantity] = Field(default_factory=list)
    byproducts: List[RawQuantity] = Field(default_factory=list)

    time_model: Optional[RawTimeModel] = None
    energy_model: Optional[RawEnergyModel] = None

    requires_ids: List[str] = Field(default_factory=list)
    requires_text: List[str] = Field(default_factory=list)
    resource_requirements: List[RawRequirement] = Field(default_factory=list)

    layer_tags: List[str] = Field(default_factory=list)
    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None

    # Template process flag - allows undefined item references
    is_template: Optional[bool] = None

    notes: Optional[str] = None

    # Deprecated fields
    est_time_hr: Optional[float] = None


class RawRecipeStep(BaseModel):
    """
    Raw recipe step (permissive parsing).

    Supports ADR-013 override mechanics:
    - If time_model.type is present → complete override
    - If time_model.type is absent → partial override (merge with process)
    """
    model_config = ConfigDict(extra="allow")

    process_id: str

    # Override support (ADR-013)
    time_model: Optional[RawTimeModel] = None
    energy_model: Optional[RawEnergyModel] = None

    # Step-level inputs/outputs (optional, for explicit material flow)
    inputs: List[RawQuantity] = Field(default_factory=list)
    outputs: List[RawQuantity] = Field(default_factory=list)
    byproducts: List[RawQuantity] = Field(default_factory=list)

    # Deprecated fields
    est_time_hr: Optional[float] = None
    labor_hours: Optional[float] = None
    machine_hours: Optional[float] = None

    notes: Optional[str] = None


class RawRecipe(BaseModel):
    """Raw recipe definition (permissive parsing)."""
    model_config = ConfigDict(extra="allow")

    id: str
    target_item_id: str
    variant_id: Optional[str] = None

    steps: List[RawRecipeStep] = Field(default_factory=list)

    # Recipe-level inputs/outputs (optional)
    inputs: List[RawQuantity] = Field(default_factory=list)
    outputs: List[RawQuantity] = Field(default_factory=list)

    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None

    assumptions: Optional[str] = None
    notes: Optional[str] = None


class RawItem(BaseModel):
    """Raw item definition (permissive parsing)."""
    model_config = ConfigDict(extra="allow")

    id: str
    kind: str  # "material", "part", "machine"
    name: Optional[str] = None

    mass: Optional[float] = None  # Item mass (for count → mass conversion)
    mass_kg: Optional[float] = None  # Explicit mass_kg field
    unit: Optional[str] = None

    bom: Optional[str] = None
    recipe: Optional[str] = None

    material_class: Optional[str] = None
    density: Optional[float] = None  # kg/m³ (for mass ↔ volume conversion)

    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None
    preferred_variant: Optional[str] = None

    # Machine-specific fields
    capabilities: List[str] = Field(default_factory=list)
    processes_supported: List[str] = Field(default_factory=list)

    # Import flag
    is_import: Optional[bool] = None
    is_raw_material: Optional[bool] = None

    notes: Optional[str] = None


# =============================================================================
# Validated Models (Strict - for simulation)
# =============================================================================

class Quantity(BaseModel):
    """Validated quantity specification (strict)."""
    model_config = ConfigDict(extra="forbid")

    item_id: str
    qty: float
    unit: str
    notes: Optional[str] = None


class Requirement(BaseModel):
    """Validated resource requirement (strict)."""
    model_config = ConfigDict(extra="forbid")

    machine_id: str
    qty: float
    unit: str
    notes: Optional[str] = None


class TimeModel(BaseModel):
    """
    Validated time model (strict).

    Per ADR-012, two types:

    1. linear_rate (for continuous processes):
        - rate: throughput rate (e.g., 10.0)
        - rate_unit: compound unit (e.g., "kg/hr", "L/min", "unit/hr")
        - scaling_basis: which input/output item drives time

    2. batch (for batch processes):
        - hr_per_batch: time per batch
        - setup_hr: setup time (optional, default 0)

    Examples:
        # Continuous crushing
        TimeModel(
            type="linear_rate",
            rate=10.0,
            rate_unit="kg/hr",
            scaling_basis="ore_crushed"
        )

        # Batch assembly
        TimeModel(
            type="batch",
            hr_per_batch=0.5,
            setup_hr=0.1
        )
    """
    model_config = ConfigDict(extra="forbid")

    type: Literal["linear_rate", "batch"]

    # For linear_rate (all required)
    rate: Optional[float] = None
    rate_unit: Optional[str] = None
    scaling_basis: Optional[str] = None

    # For batch (hr_per_batch required)
    hr_per_batch: Optional[float] = None
    setup_hr: Optional[float] = Field(default=0.0)

    notes: Optional[str] = None


class EnergyModel(BaseModel):
    """
    Validated energy model (strict).

    Per ADR-014, two types:

    1. per_unit (scales with production):
        - value: energy per unit (e.g., 50.0)
        - unit: compound unit (e.g., "kWh/kg", "MJ/unit")
        - scaling_basis: which input/output item drives energy

    2. fixed_per_batch (constant per batch):
        - value: fixed energy (e.g., 100.0)
        - unit: energy unit (e.g., "kWh", "MJ")

    Examples:
        # Per-unit energy
        EnergyModel(
            type="per_unit",
            value=50.0,
            unit="kWh/kg",
            scaling_basis="water_processed"
        )

        # Fixed batch energy
        EnergyModel(
            type="fixed_per_batch",
            value=100.0,
            unit="kWh"
        )
    """
    model_config = ConfigDict(extra="forbid")

    type: Literal["per_unit", "fixed_per_batch"]
    value: float
    unit: str

    # For per_unit (required)
    scaling_basis: Optional[str] = None

    notes: Optional[str] = None


class Process(BaseModel):
    """
    Validated process definition (strict).

    Per ADR-012:
    - process_type required ("batch", "continuous", or "boundary")
    - process_type must align with time_model.type (boundary may use batch or linear_rate)
    - time_model required (for now, may be WARNING later)
    """
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal["process"]
    name: Optional[str] = None

    process_type: Literal["batch", "continuous", "boundary"]

    inputs: List[Quantity]
    outputs: List[Quantity]
    byproducts: List[Quantity] = Field(default_factory=list)

    time_model: TimeModel
    energy_model: Optional[EnergyModel] = None

    requires_ids: List[str] = Field(default_factory=list)
    requires_text: List[str] = Field(default_factory=list)
    resource_requirements: List[Requirement] = Field(default_factory=list)

    layer_tags: List[str] = Field(default_factory=list)
    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None

    # Template process flag - allows undefined item references
    is_template: Optional[bool] = None

    notes: Optional[str] = None


class RecipeStep(BaseModel):
    """
    Validated recipe step (strict).

    Note: Overrides stored as RawTimeModel/RawEnergyModel because they
    may be partial (missing type field). Validation happens during
    resolution with process.
    """
    model_config = ConfigDict(extra="forbid")

    process_id: str

    # Overrides (optional, validated during resolution)
    time_model: Optional[RawTimeModel] = None
    energy_model: Optional[RawEnergyModel] = None

    # Step-level inputs/outputs (optional)
    inputs: List[Quantity] = Field(default_factory=list)
    outputs: List[Quantity] = Field(default_factory=list)
    byproducts: List[Quantity] = Field(default_factory=list)

    notes: Optional[str] = None


class Recipe(BaseModel):
    """Validated recipe definition (strict)."""
    model_config = ConfigDict(extra="forbid")

    id: str
    target_item_id: str
    variant_id: Optional[str] = None

    steps: List[RecipeStep]

    # Recipe-level inputs/outputs (optional)
    inputs: List[Quantity] = Field(default_factory=list)
    outputs: List[Quantity] = Field(default_factory=list)

    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None

    assumptions: Optional[str] = None
    notes: Optional[str] = None


class Item(BaseModel):
    """Validated item definition (strict)."""
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal["material", "part", "machine"]
    name: Optional[str] = None

    mass: Optional[float] = None
    mass_kg: Optional[float] = None
    unit: Optional[str] = None

    bom: Optional[str] = None
    recipe: Optional[str] = None

    material_class: Optional[str] = None
    density: Optional[float] = None

    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None
    preferred_variant: Optional[str] = None

    capabilities: List[str] = Field(default_factory=list)
    processes_supported: List[str] = Field(default_factory=list)

    is_import: Optional[bool] = None
    is_raw_material: Optional[bool] = None

    notes: Optional[str] = None


# =============================================================================
# Helper mappings
# =============================================================================

# Map kind to raw model class (for parsing)
RAW_MODEL_MAP = {
    "process": RawProcess,
    "recipe": RawRecipe,
    "material": RawItem,
    "part": RawItem,
    "machine": RawItem,
}

# Map kind to validated model class
VALIDATED_MODEL_MAP = {
    "process": Process,
    "recipe": Recipe,
    "material": Item,
    "part": Item,
    "machine": Item,
}
