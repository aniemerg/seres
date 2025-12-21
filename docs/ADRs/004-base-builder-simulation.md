# ADR 004 — Base Builder Simulation

**Status:** ✅ IMPLEMENTED
**Date:** 2024-12-19 (Proposed) → 2025-12-20 (Implemented)
**Owner:** kb/validation

## Context / Problem

The knowledge base aims to model a self-replicating lunar base, but we lack validation that:
1. The KB is complete enough to support actual base building
2. We understand the supply chain dependencies
3. We know what must be imported from Earth vs made in situ
4. The processes and recipes form coherent production chains

**Current issues:**
- KB completeness is uncertain (many gaps may remain undetected)
- No way to test if processes/recipes can support end-to-end production
- Mission planning (what to bring from Earth) is guesswork
- Self-sufficiency goals are unvalidated

We need a simulation mode where an agent attempts to build a base from scratch, using the KB as the "tech tree". This will:
- Surface KB gaps through actual usage
- Validate process/recipe chains
- Quantify Earth import requirements
- Test self-replication feasibility

## Decision / Direction

Build a **Base Builder Simulation** where agents start with nothing and build up a lunar base by:
1. Mining local regolith (multiple types available freely)
2. Running processes to refine materials
3. Running recipes to create parts
4. Building machines from BOMs
5. Importing from Earth only when necessary (tracked as failure mode)

The simulation validates KB completeness and generates mission planning data.

### Core Design Principles

1. **Single JSONL file per simulation** - All events, state changes, actions logged chronologically
2. **Agent uses standard file tools** - No special KB query tools, just rg_search/read_file/write_file
3. **Duration-based time model** - Agent specifies duration for all processes (hours/days)
4. **Empty initial state** - Agent bootstraps everything, decides what to import
5. **KB gap detection via errors** - Preview/execute returns clear errors when KB incomplete
6. **Indefinite runtime** - No fixed win condition, runs until user stops
7. **Import tracking** - All Earth imports logged separately from ISRU production

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│ Base Builder Agent                                       │
│  - Standard: rg_search, read_file, write_file           │
│  - Simulation: view_state, start_process, run_recipe,   │
│    build_machine, import_item, preview_step,            │
│    advance_time                                         │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│ Simulation Engine                                        │
│  - KB Loader: Index processes, recipes, items, BOMs     │
│  - State Manager: Track inventory, active processes     │
│  - Process Executor: Validate, execute, advance time    │
│  - Unit Converter: Handle mass/volume/count conversions │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│ Storage: simulations/{sim_id}/simulation.jsonl          │
│  Events: state_snapshot, action, process_start/complete,│
│          import, build, error, kb_gap, agent_delegate   │
└─────────────────────────────────────────────────────────┘
```

### Time Model

- **Granularity:** Minutes, hours, days (not seconds)
- **Process duration:** Agent specifies when starting process
- **Parallel execution:** Multiple processes run simultaneously
- **Time advancement:** Agent commits to time step, processes complete, state updates

Example:
```python
# Agent starts mining for 8 hours
start_process("regolith_mining_v0", scale=1, duration_hours=8)

# Agent previews what would happen
preview_step(duration_hours=8)  # Shows: mining completes, produces 800kg regolith

# Agent commits
advance_time(duration_hours=8)  # Actually executes, updates inventory
```

### Resource Model

**Local Resources (Free, Infinite):**
- `regolith_lunar_mare` (iron-rich)
- `regolith_lunar_highlands` (aluminum-rich)
- `regolith_carbonaceous` (carbon from meteorites)
- `regolith_silicate` (silicon-rich)

Mining just requires a process + machine (e.g., labor_bot). No consumables.

**Processed Materials:**
Tracked in inventory with units (kg, count, m³, etc.). Consumed by processes/recipes.

**Machines:**
Built from BOMs. Not consumed by processes, but required (like catalysts).

**Imports:**
Anything can be imported from Earth. Tracked separately. Agent instructed to minimize.

### Unit Handling

Items can have multiple unit types (mass, volume, count). System handles conversions:

1. **Direct conversions:** kg ↔ g ↔ tonne (via conversion factors)
2. **Material properties:** mass ↔ volume (via density)
3. **Item definitions:** count ↔ mass (e.g., "1 steel_ingot = 10kg")

Agent can specify units when importing/using items. Engine validates and converts as needed.

### KB Gap Handling

When engine detects KB gaps (missing recipe, undefined item, invalid reference), it:
1. Returns error to agent with clear description
2. Logs `kb_gap` event with details
3. Agent can:
   - Delegate to kb_fixer subagent (same as queue_agents)
   - Import missing item from Earth (if no local alternative)
   - Retry after fix

This creates a feedback loop: simulation → gaps → fixes → simulation.

## Implementation Components

### 1. Data Models (`base_builder/models.py`)

Pydantic models for type safety and validation:

```python
class InventoryItem(BaseModel):
    quantity: float
    unit: str  # kg, count, m3, etc.

class ActiveProcess(BaseModel):
    process_id: str
    scale: float
    started_at: float  # hours
    ends_at: float     # hours
    inputs_consumed: Dict[str, InventoryItem]
    outputs_pending: Dict[str, InventoryItem]

class SimulationState(BaseModel):
    sim_id: str
    current_time_hours: float
    inventory: Dict[str, InventoryItem]
    active_processes: List[ActiveProcess]
    machines_built: List[str]
    total_imports: Dict[str, InventoryItem]

# Event types
class Event(BaseModel):
    type: str
    timestamp: str

class ActionEvent(Event):
    action: str
    args: Dict[str, Any]
    agent_reasoning: Optional[str]

class ProcessCompleteEvent(Event):
    process_id: str
    outputs: Dict[str, InventoryItem]

class KBGapEvent(Event):
    gap_type: str
    details: str

# ... etc
```

### 2. KB Loader (`base_builder/kb_loader.py`)

Loads and indexes KB data on startup:

```python
class KBLoader:
    def __init__(self, kb_root: Path):
        self.processes = {}      # id -> process definition
        self.recipes = {}        # id -> recipe definition
        self.items = {}          # id -> item definition
        self.boms = {}           # id -> BOM definition
        self.units = {}          # unit conversions
        self.materials = {}      # material properties (density, etc.)

    def load_all(self):
        """Load all KB files and build indexes."""
        self.load_processes()
        self.load_recipes()
        self.load_items()
        self.load_boms()
        self.load_units()
        self.load_material_properties()

    def get_process(self, process_id: str) -> Optional[dict]:
        """Get process definition or None if missing."""
        return self.processes.get(process_id)
```

### 3. Unit Converter (`base_builder/unit_converter.py`)

Handles all unit conversions:

```python
class UnitConverter:
    def __init__(self, units: dict, materials: dict):
        self.conversion_factors = units['conversions']
        self.material_densities = materials

    def convert(self, quantity: float, from_unit: str, to_unit: str,
                item_id: Optional[str] = None) -> float:
        """
        Convert quantity from one unit to another.

        Uses:
        - Direct conversion factors (kg -> g)
        - Material densities (kg -> m3 if item_id provided)
        - Item definitions (count -> kg if item defines mass_per_unit)
        """
        # ... implementation ...
```

### 4. Simulation Engine (`base_builder/sim_engine.py`)

Core simulation logic:

```python
class SimulationEngine:
    def __init__(self, sim_id: str, kb_loader: KBLoader):
        self.sim_id = sim_id
        self.kb = kb_loader
        self.state = SimulationState(sim_id=sim_id, ...)
        self.event_log = []
        self.converter = UnitConverter(kb.units, kb.materials)

    def start_process(self, process_id: str, scale: float,
                     duration_hours: float) -> dict:
        """
        Start a process.

        1. Validate process exists in KB
        2. Check required machines exist
        3. Calculate inputs needed (base × scale)
        4. Validate inputs available in inventory
        5. Reserve inputs (mark as consumed)
        6. Schedule completion at current_time + duration
        7. Log process_start event

        Returns: {"success": bool, "message": str, ...}
        """

    def advance_time(self, duration_hours: float) -> dict:
        """
        Advance simulation time.

        1. Calculate new_time = current_time + duration
        2. Find all processes that end <= new_time
        3. For each completed process:
           - Add outputs to inventory
           - Remove from active_processes
           - Log process_complete event
        4. Update current_time
        5. Log state_snapshot event

        Returns: {"new_time": float, "completed": [...], ...}
        """

    def run_recipe(self, recipe_id: str, quantity: int) -> dict:
        """Run a recipe to produce items."""

    def build_machine(self, machine_id: str) -> dict:
        """Build machine from BOM if components available."""

    def import_item(self, item_id: str, quantity: float, unit: str) -> dict:
        """Import item from Earth, add to inventory and imports log."""

    def preview_step(self, duration_hours: float) -> dict:
        """Preview what would happen without committing changes."""

    def save(self):
        """Append current events to simulation.jsonl."""
```

### 5. Agent Tools (`base_builder/sim_tools.py`)

Tool functions for agent:

```python
from agents import function_tool

# Global engine instance (initialized by agent runner)
_engine: Optional[SimulationEngine] = None

@function_tool
def view_state() -> dict:
    """
    Get current simulation state.

    Returns:
        {
            "current_time_hours": float,
            "inventory": {item_id: {quantity, unit}, ...},
            "active_processes": [{process_id, ends_at, ...}, ...],
            "machines_built": [machine_id, ...],
            "total_imports_mass_kg": float
        }
    """
    return _engine.state.dict()

@function_tool
def start_process(process_id: str, scale: float, duration_hours: float) -> dict:
    """
    Start a process.

    Args:
        process_id: Process to run (e.g., "regolith_mining_v0")
        scale: Scale factor for inputs/outputs (1.0 = base rate)
        duration_hours: How long to run the process

    Returns:
        {"success": bool, "message": str, ...}
    """
    return _engine.start_process(process_id, scale, duration_hours)

@function_tool
def run_recipe(recipe_id: str, quantity: int) -> dict:
    """
    Run a recipe to produce items.

    Args:
        recipe_id: Recipe to run (e.g., "recipe_steel_ingot_v0")
        quantity: Number of batches to produce

    Returns:
        {"success": bool, "message": str, "duration_hours": float, ...}
    """
    return _engine.run_recipe(recipe_id, quantity)

@function_tool
def build_machine(machine_id: str) -> dict:
    """
    Build a machine from its BOM.

    Consumes all BOM components from inventory.

    Args:
        machine_id: Machine to build (e.g., "labor_bot_general_v0")

    Returns:
        {"success": bool, "message": str, ...}
    """
    return _engine.build_machine(machine_id)

@function_tool
def import_item(item_id: str, quantity: float, unit: str) -> dict:
    """
    Import an item from Earth.

    WARNING: Imports are a failure mode. Only use when:
    - No local alternative exists
    - KB is incomplete (delegate to kb_fixer first)

    Args:
        item_id: Item to import (e.g., "labor_bot_general_v0")
        quantity: Amount to import
        unit: Unit of quantity (e.g., "count", "kg")

    Returns:
        {"success": bool, "imported": {item_id, quantity, unit, mass_kg}, ...}
    """
    return _engine.import_item(item_id, quantity, unit)

@function_tool
def preview_step(duration_hours: float) -> dict:
    """
    Preview what would happen if time advanced.

    Does NOT commit changes. Use this before advance_time() to check.

    Args:
        duration_hours: How much time to preview

    Returns:
        {
            "new_time": float,
            "processes_completing": [{process_id, outputs}, ...],
            "errors": [str, ...] if any processes would fail
        }
    """
    return _engine.preview_step(duration_hours)

@function_tool
def advance_time(duration_hours: float) -> dict:
    """
    Advance simulation time.

    COMMITS changes. Processes complete, inventory updates.

    Args:
        duration_hours: How much time to advance

    Returns:
        {
            "new_time": float,
            "completed": [{process_id, outputs}, ...],
            "new_inventory": {...}
        }
    """
    return _engine.advance_time(duration_hours)
```

### 6. Agent Runner (`base_builder/agent.py`)

Sets up and runs the agent:

```python
from agents import Agent
import base_builder.sim_tools as sim_tools

AGENT_INSTRUCTIONS = """
You are a Lunar Base Builder agent.

Your goal is to build up a self-sustaining base on the Moon, starting from nothing.

## Your Resources

1. **Local Resources (Free):**
   - regolith_lunar_mare (iron-rich)
   - regolith_lunar_highlands (aluminum-rich)
   - regolith_carbonaceous (carbon-rich, from meteorites)
   - regolith_silicate (silicon-rich)

   Mining is simple: start_process("regolith_mining_v0", scale, duration_hours)

2. **Imported Resources (Track):**
   - You CAN import anything using import_item()
   - HOWEVER: Imports are a FAILURE MODE
   - Your goal is to use IN SITU resources as much as possible
   - Only import when:
     a) No local alternative exists
     b) KB is missing info (delegate to kb_fixer first)

## Your Process

1. **Explore the KB:**
   - Use rg_search() to find processes, recipes, items
   - Use read_file() to understand definitions
   - Build mental model of production chains

2. **Plan Your Build:**
   - What machines do you need?
   - What materials do they require?
   - What's the dependency tree?

3. **Bootstrap:**
   - Import minimal bootstrap items (e.g., 1-2 robots)
   - Start mining regolith
   - Begin refining local materials

4. **Execute:**
   - Use start_process() to mine/refine materials
   - Use run_recipe() to produce parts
   - Use build_machine() when you have BOM components
   - Always preview_step() before advance_time()

5. **Handle KB Gaps:**
   - If you get errors about missing recipes/processes
   - Analyze what's needed
   - Delegate to kb_fixer subagent
   - Retry after fix

6. **Iterate:**
   - Build more capable machines
   - Expand production capacity
   - Work toward self-sufficiency

## Important Notes

- There is NO time limit - build deliberately
- preview_step() before every advance_time()
- Explain your reasoning before each action
- When stuck, search KB for similar items
- Imports are tracked but unlimited (scenario planning)
- Focus on ONE goal at a time

Begin by exploring what processes exist for refining regolith.
"""

def build_agent(model: str, kb_loader: KBLoader) -> Agent:
    """Build the base builder agent."""

    # Initialize engine
    sim_tools._engine = SimulationEngine(sim_id, kb_loader)

    # Create agent with tools
    agent = Agent(
        name="BaseBuilderAgent",
        instructions=AGENT_INSTRUCTIONS,
        tools=[
            sim_tools.view_state,
            sim_tools.start_process,
            sim_tools.run_recipe,
            sim_tools.build_machine,
            sim_tools.import_item,
            sim_tools.preview_step,
            sim_tools.advance_time,
            # Also include KB tools
            rg_search,
            read_file,
            write_file,
        ],
        model=model,
    )

    return agent

def run_simulation(sim_id: str, model: str = "gpt-4"):
    """Run a base builder simulation."""
    # Load KB
    kb_loader = KBLoader(REPO_ROOT / "kb")
    kb_loader.load_all()

    # Build agent
    agent = build_agent(model, kb_loader)

    # Run agent loop
    runner = Runner(agent)
    result = runner.run("Begin building the lunar base.")

    # Save final state
    sim_tools._engine.save()
```

### 7. Event Log Format

Each simulation has a `simulation.jsonl` file with one event per line:

```jsonl
{"type": "sim_start", "timestamp": "2024-01-15T10:00:00Z", "sim_id": "lunar_base_001"}
{"type": "action", "timestamp": "2024-01-15T10:01:23Z", "action": "import_item", "args": {"item_id": "labor_bot_general_v0", "quantity": 1, "unit": "count"}, "agent_reasoning": "Need robot to start mining operations"}
{"type": "import", "timestamp": "2024-01-15T10:01:23Z", "item_id": "labor_bot_general_v0", "quantity": 1, "unit": "count", "mass_kg": 200}
{"type": "action", "timestamp": "2024-01-15T10:02:15Z", "action": "start_process", "args": {"process_id": "regolith_mining_v0", "scale": 1, "duration_hours": 8}}
{"type": "process_start", "timestamp": "2024-01-15T10:02:15Z", "process_id": "regolith_mining_v0", "scale": 1, "ends_at": 8}
{"type": "action", "timestamp": "2024-01-15T10:05:00Z", "action": "preview_step", "args": {"duration_hours": 8}}
{"type": "preview", "timestamp": "2024-01-15T10:05:00Z", "new_time": 8, "processes_completing": [{"process_id": "regolith_mining_v0", "outputs": {"regolith_lunar_mare": {"quantity": 800, "unit": "kg"}}}]}
{"type": "action", "timestamp": "2024-01-15T10:05:30Z", "action": "advance_time", "args": {"duration_hours": 8}}
{"type": "process_complete", "timestamp": "2024-01-15T10:05:30Z", "process_id": "regolith_mining_v0", "outputs": {"regolith_lunar_mare": {"quantity": 800, "unit": "kg"}}}
{"type": "state_snapshot", "timestamp": "2024-01-15T10:05:30Z", "time_hours": 8, "inventory": {"regolith_lunar_mare": {"quantity": 800, "unit": "kg"}}, "active_processes": []}
{"type": "kb_gap", "timestamp": "2024-01-15T10:10:00Z", "gap_type": "missing_recipe", "details": "No recipe found for steel_ingot production from regolith"}
{"type": "agent_delegate", "timestamp": "2024-01-15T10:10:30Z", "subagent": "kb_fixer", "task": "Create recipe for steel_ingot_from_regolith"}
{"type": "kb_fix_complete", "timestamp": "2024-01-15T10:15:00Z", "created_files": ["kb/recipes/recipe_steel_from_regolith_v0.yaml"]}
```

## KB Requirements & Updates

### New KB Files

1. **kb/units/units.yaml** - Unit definitions and conversions
2. **kb/materials/properties.yaml** - Material properties (densities, etc.)

### Process Updates

All processes should include:
```yaml
id: process_id_v0
name: Process Name
base_rate: "100 kg/hour"  # Or "per batch"
inputs:
  - item_id: input_item
    quantity: 10
    unit: kg
outputs:
  - item_id: output_item
    quantity: 5
    unit: kg
required_machines:
  - labor_bot_basic_v0: 1
scalable: true/false
```

### Recipe Updates

All recipes should include:
```yaml
id: recipe_id_v0
name: Recipe Name
inputs:
  - item_id: input_item
    quantity: 10
    unit: kg
outputs:
  - item_id: output_item
    quantity: 1
    unit: count
    mass_kg: 10  # Optional, for count->mass conversion
processes:
  - process_a_v0
  - process_b_v0
duration: 2
duration_unit: hours
required_machines:
  - machine_id: 1
```

## CLI Interface

```bash
# Start new simulation
python -m base_builder.cli start --sim-id lunar_base_001 --model gpt-4

# Continue existing simulation
python -m base_builder.cli continue --sim-id lunar_base_001

# Analyze simulation
python -m base_builder.cli analyze --sim-id lunar_base_001

# List all simulations
python -m base_builder.cli list

# Export report
python -m base_builder.cli report --sim-id lunar_base_001 --output report.md
```

## Implementation Phases

### Phase 1: Core Engine (Priority: Critical)
- [ ] Data models (Pydantic)
- [ ] KB loader
- [ ] Unit converter
- [ ] State manager
- [ ] Process executor (start, preview, advance)

### Phase 2: Agent Integration (Priority: Critical)
- [ ] Agent tools (@function_tool)
- [ ] Agent instructions
- [ ] Runner setup
- [ ] Event logging

### Phase 3: KB Updates (Priority: High)
- [ ] Create kb/units/units.yaml
- [ ] Create kb/materials/properties.yaml
- [ ] Update processes with rates and scalability
- [ ] Update recipes with durations
- [ ] Define regolith types and mining processes

### Phase 4: Machine Building (Priority: High)
- [ ] BOM loader
- [ ] build_machine() implementation
- [ ] Component validation

### Phase 5: KB Gap Handling (Priority: Medium)
- [ ] Gap detection and reporting
- [ ] Subagent delegation
- [ ] Retry logic

### Phase 6: Analysis Tools (Priority: Low)
- [ ] Simulation analyzer
- [ ] Import summary
- [ ] Timeline visualization
- [ ] Mission planning report

## Success Metrics

1. **KB Validation:** Agent discovers and reports KB gaps during simulation
2. **End-to-end Production:** Agent can build at least one machine entirely from ISRU
3. **Import Quantification:** Clear tracking of what must come from Earth
4. **Self-Sufficiency:** Agent can build labor_bot from local materials (ultimate test)

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| KB too incomplete to start | High | Bootstrap with imports, find gaps iteratively |
| Unit conversions too complex | Medium | Start with simple units, add complexity gradually |
| Agent gets stuck in loops | Medium | Add iteration limits, delegation prompts |
| Simulation runs too long | Low | No issue - user can stop anytime |
| JSONL gets too large | Low | Compress old events, keep recent in memory |

## Open Questions

None - all clarified during planning:
- ✅ Single file per simulation
- ✅ Agent specifies duration
- ✅ KB has conversion factors + material properties
- ✅ Mining is rate-based
- ✅ Errors reveal KB gaps → delegate to kb_fixer
- ✅ Empty initial inventory, agent bootstraps
- ✅ Tools via @function_tool from openai-agents

## Related ADRs

- ADR-002: Autonomous Queue Agent (similar agent architecture, KB tools)
- ADR-003: Process-Machine Refactor (process definitions this builds on)

## Approvals

- [ ] Technical review
- [ ] KB structure review
- [ ] Implementation plan approval
