"""
Minimal Pydantic models for the KB v0. These are intentionally permissive:
- Missing numeric fields are allowed.
- Dangling references are allowed and captured during indexing.
"""
from __future__ import annotations

from typing import List, Optional

try:
    from pydantic import BaseModel, Field  # type: ignore
    try:
        # Pydantic v2
        from pydantic import ConfigDict  # type: ignore

        class _BaseModel(BaseModel):
            model_config = ConfigDict(extra="allow", validate_assignment=False)

    except ImportError:

        class _BaseModel(BaseModel):
            class Config:
                extra = "allow"
                validate_assignment = False

except ImportError as exc:  # pragma: no cover
    raise SystemExit("pydantic is required for kbtool") from exc


class Quantity(_BaseModel):
    item_id: Optional[str] = None
    qty: Optional[float] = None
    unit: Optional[str] = None
    notes: Optional[str] = None


class Requirement(_BaseModel):
    """
    Resource requirement for a process.

    ADR 003: Migrated from abstract resource_type to concrete machine_id.
    """
    machine_id: Optional[str] = Field(default=None, alias="resource_type")  # ADR 003: was resource_type
    qty: Optional[float] = None  # ADR 003: standardized (was amount/qty)
    unit: Optional[str] = None
    notes: Optional[str] = None
    # Deprecated: amount field removed in favor of qty (ADR 003)


class EnergyModel(_BaseModel):
    """
    Energy consumption model for a process.

    Types:
    - kWh_per_kg: energy scales linearly with input mass
    - fixed_kWh: constant energy per batch/cycle
    - boundary: terminal node (no energy consumption modeled)
    """
    type: str  # kWh_per_kg, fixed_kWh, boundary
    value: Optional[float] = None  # numeric value (kWh/kg or kWh/batch)
    notes: Optional[str] = None


class TimeModel(_BaseModel):
    """
    Time/duration model for a process.

    Types:
    - linear_rate: time = setup_hr + (mass / rate_kg_per_hr)
    - fixed_time: constant time per batch/cycle
    - boundary: terminal node (no time modeled)
    """
    type: str  # linear_rate, fixed_time, boundary
    hr_per_kg: Optional[float] = None  # for linear_rate
    rate_kg_per_hr: Optional[float] = None  # alternative: throughput rate
    setup_hr: Optional[float] = None  # setup time before processing
    hr_per_batch: Optional[float] = None  # for fixed_time
    notes: Optional[str] = None


class Process(_BaseModel):
    id: str
    name: Optional[str] = None
    kind: str = "process"
    est_time_hr: Optional[float] = None
    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None
    inputs: List[Quantity] = Field(default_factory=list)
    outputs: List[Quantity] = Field(default_factory=list)
    byproducts: List[Quantity] = Field(default_factory=list)
    requires_ids: List[str] = Field(default_factory=list)
    requires_text: List[str] = Field(default_factory=list)
    resource_requirements: List[Requirement] = Field(default_factory=list)
    layer_tags: List[str] = Field(default_factory=list)
    energy_model: Optional[EnergyModel] = None
    time_model: Optional[TimeModel] = None
    notes: Optional[str] = None


class Item(_BaseModel):
    id: str
    name: Optional[str] = None
    kind: str
    mass: Optional[float] = None
    unit: Optional[str] = None
    bom: Optional[str] = None
    material_class: Optional[str] = None
    density: Optional[float] = None
    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None
    preferred_variant: Optional[str] = None  # default recipe variant hint
    notes: Optional[str] = None
    # ADR 003: capabilities deprecated in favor of processes_supported
    capabilities: List[str] = Field(default_factory=list)  # DEPRECATED: use processes_supported
    processes_supported: List[str] = Field(default_factory=list)  # ADR 003: which processes this machine can perform


class ResourceType(_BaseModel):
    id: str
    kind: str = "resource_type"
    type: Optional[str] = None
    count: Optional[int] = None
    capacity: Optional[float] = None
    capacity_unit: Optional[str] = None
    notes: Optional[str] = None
    aliases: List[str] = Field(default_factory=list)


class Recipe(_BaseModel):
    id: str
    target_item_id: str
    variant_id: Optional[str] = None
    alternatives: List[str] = Field(default_factory=list)
    dedupe_candidate: Optional[bool] = None
    steps: List["RecipeStep"] = Field(default_factory=list)
    assumptions: Optional[str] = None
    notes: Optional[str] = None


class RecipeStep(_BaseModel):
    process_id: str  # required: reference to a process
    est_time_hr: Optional[float] = None  # optional: estimated wall-clock time
    labor_hours: Optional[float] = None  # optional: labor bot hours
    machine_hours: Optional[float] = None  # optional: machine occupancy
    notes: Optional[str] = None  # optional: freeform context


MODEL_KINDS = {
    "process": Process,
    "recipe": Recipe,
    "resource_type": ResourceType,
    "material": Item,
    "part": Item,
    "machine": Item,
}
