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
    resource_type: Optional[str] = Field(default=None, alias="resource")
    amount: Optional[float] = None
    unit: Optional[str] = None
    notes: Optional[str] = None


class Process(_BaseModel):
    id: str
    name: Optional[str] = None
    kind: str = "process"
    inputs: List[Quantity] = Field(default_factory=list)
    outputs: List[Quantity] = Field(default_factory=list)
    byproducts: List[Quantity] = Field(default_factory=list)
    requires_ids: List[str] = Field(default_factory=list)
    requires_text: List[str] = Field(default_factory=list)
    resource_requirements: List[Requirement] = Field(default_factory=list)
    layer_tags: List[str] = Field(default_factory=list)
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
    notes: Optional[str] = None
    capabilities: List[str] = Field(default_factory=list)


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
    steps: List[str] = Field(default_factory=list)
    assumptions: Optional[str] = None
    notes: Optional[str] = None


MODEL_KINDS = {
    "process": Process,
    "recipe": Recipe,
    "resource_type": ResourceType,
    "material": Item,
    "part": Item,
    "machine": Item,
}
