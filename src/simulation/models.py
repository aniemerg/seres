"""
Data models for base builder simulation.

All models use Pydantic for validation and serialization.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Literal
from pydantic import BaseModel, Field


class InventoryItem(BaseModel):
    """An item in inventory with quantity and unit."""
    quantity: float
    unit: str  # kg, count, m3, liter, etc.


class ProvenanceTotals(BaseModel):
    """Mass provenance totals (kg) for an inventory item."""
    in_situ_kg: float = 0.0
    imported_kg: float = 0.0
    unknown_kg: float = 0.0


class ActiveProcess(BaseModel):
    """A process currently running in the simulation."""
    process_id: str
    scale: float = 1.0
    started_at: float  # simulation time in hours
    ends_at: float     # simulation time in hours
    inputs_consumed: Dict[str, InventoryItem] = Field(default_factory=dict)
    outputs_pending: Dict[str, InventoryItem] = Field(default_factory=dict)
    machines_reserved: Dict[str, int] = Field(default_factory=dict)


class SimulationState(BaseModel):
    """Current state of the simulation."""
    sim_id: str
    current_time_hours: float = 0.0
    inventory: Dict[str, InventoryItem] = Field(default_factory=dict)
    active_processes: List[ActiveProcess] = Field(default_factory=list)
    machines_built: List[str] = Field(default_factory=list)
    machines_in_use: Dict[str, int] = Field(default_factory=dict)
    total_imports: Dict[str, InventoryItem] = Field(default_factory=dict)
    provenance: Dict[str, ProvenanceTotals] = Field(default_factory=dict)
    total_energy_kwh: float = 0.0  # Cumulative energy consumed


# ============================================================================
# Event Models
# ============================================================================

class Event(BaseModel):
    """Base event class."""
    type: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")


class SimStartEvent(Event):
    """Simulation started."""
    type: Literal["sim_start"] = "sim_start"
    sim_id: str


class ActionEvent(Event):
    """Agent performed an action."""
    type: Literal["action"] = "action"
    action: str  # start_process, run_recipe, build_machine, etc.
    args: Dict[str, Any]
    agent_reasoning: Optional[str] = None


class ProcessScheduledEvent(Event):
    """Process scheduled for execution."""
    type: Literal["process_scheduled"] = "process_scheduled"

    process_id: str
    process_run_id: str

    scheduled_start_time: float
    duration_hours: float
    scheduled_end_time: float

    scale: float

    inputs_consumed: Dict[str, Dict[str, Any]]
    outputs_pending: Dict[str, Dict[str, Any]]
    machine_reservations: List[Dict[str, Any]]

    recipe_run_id: Optional[str] = None
    step_index: Optional[int] = None
    energy_kwh: Optional[float] = None


class ProcessStartEvent(Event):
    """Process started."""
    type: Literal["process_start"] = "process_start"
    process_id: str
    process_run_id: str
    actual_start_time: float
    scale: float
    scheduled_end_time: Optional[float] = None


class ProcessCompleteEvent(Event):
    """Process completed."""
    type: Literal["process_complete"] = "process_complete"
    process_id: str
    process_run_id: Optional[str] = None  # Runtime process instance ID
    recipe_run_id: Optional[str] = None  # Recipe run ID if part of a recipe
    outputs: Dict[str, InventoryItem]
    energy_kwh: Optional[float] = None  # Energy consumed by this process
    time_hours: float
    start_time: Optional[float] = None


class RecipeStartEvent(Event):
    """Recipe started."""
    type: Literal["recipe_start"] = "recipe_start"
    recipe_id: str
    quantity: int
    duration_hours: float


class RecipeCompleteEvent(Event):
    """Recipe completed."""
    type: Literal["recipe_complete"] = "recipe_complete"
    recipe_id: str
    quantity: int
    outputs: Dict[str, InventoryItem]
    energy_kwh: Optional[float] = None  # Energy consumed by this recipe


class BuildEvent(Event):
    """Machine built."""
    type: Literal["build"] = "build"
    machine_id: str
    components_consumed: Dict[str, InventoryItem]


class ImportEvent(Event):
    """Item imported from Earth."""
    type: Literal["import"] = "import"
    item_id: str
    quantity: float
    unit: str
    mass_kg: Optional[float] = None  # Estimated mass for tracking


class PreviewEvent(Event):
    """Preview of what would happen."""
    type: Literal["preview"] = "preview"
    new_time: float
    processes_completing: List[Dict[str, Any]]
    errors: List[str] = Field(default_factory=list)


class StateSnapshotEvent(Event):
    """Snapshot of simulation state."""
    type: Literal["state_snapshot"] = "state_snapshot"
    time_hours: float
    inventory: Dict[str, InventoryItem]
    active_processes: List[ActiveProcess]
    machines_built: List[str]
    machines_in_use: Dict[str, int] = Field(default_factory=dict)
    total_imports: Dict[str, InventoryItem] = Field(default_factory=dict)
    total_energy_kwh: Optional[float] = None  # Cumulative energy at snapshot time


class ErrorEvent(Event):
    """Error occurred."""
    type: Literal["error"] = "error"
    error_type: str
    message: str
    details: Optional[Dict[str, Any]] = None


class KBGapEvent(Event):
    """KB gap detected."""
    type: Literal["kb_gap"] = "kb_gap"
    gap_type: str  # missing_recipe, missing_process, missing_item, etc.
    details: str


class AgentDelegateEvent(Event):
    """Agent delegated to subagent."""
    type: Literal["agent_delegate"] = "agent_delegate"
    subagent: str
    task: str


class KBFixCompleteEvent(Event):
    """KB fix completed by subagent."""
    type: Literal["kb_fix_complete"] = "kb_fix_complete"
    created_files: List[str] = Field(default_factory=list)
    modified_files: List[str] = Field(default_factory=list)
