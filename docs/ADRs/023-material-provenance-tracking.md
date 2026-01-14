# 023: Material Provenance Tracking

**Status:** Implemented
**Date:** 2026-01-14
**Decision Makers:** Project team
**Related ADRs:** ADR-004 (Base Builder Simulation), ADR-007 (Explicit Import Items), ADR-021 (State Persistence)

---

## Context

### Problem

When simulating lunar base construction, a critical metric is **ISRU (In-Situ Resource Utilization)** - the percentage of materials sourced from local resources versus imported from Earth. Without provenance tracking, we cannot:

1. **Measure ISRU effectiveness**: "Is this electrolysis cell 80% local materials or 20%?"
2. **Optimize runbooks**: "Which imports should I replace with local production?"
3. **Track material flow**: "Where did this iron come from - mined regolith or imported?"
4. **Verify design goals**: "Did we achieve our 90% ISRU target?"

### Current State (Before ADR-023)

The simulation tracks:
- ✅ Inventory quantities (`iron_metal: 50 kg`)
- ✅ Import history (`total_imports: {labor_bot: 2 unit}`)
- ❌ Material origin (imported vs mined)
- ❌ Provenance through processing (regolith → iron → steel → component)
- ❌ Blended provenance (50% imported, 50% in-situ)

### Use Case Example

**Scenario:** Building an electrolysis cell unit

**Without provenance:**
```bash
$ python -m src.cli sim view-state --sim-id cell_build
Inventory:
  electrolysis_cell_unit_v0: 1.00 unit

# Question: How much is ISRU?
# Answer: Unknown
```

**With provenance:**
```bash
$ python -m src.cli sim provenance --sim-id cell_build --item electrolysis_cell_unit_v0
=== Item: electrolysis_cell_unit_v0 ===
Total mass: 25.00 kg
  In-situ:     20.00 kg ( 80.0%) ████████████████████████████████░░░░░░░░
  Imported:     5.00 kg ( 20.0%)

# Answer: 80% ISRU achieved!
```

---

## Decision

We will implement **comprehensive material provenance tracking** that follows materials through the entire supply chain from origin to final product.

### Core Principles

1. **Origin Tagging**: Every material has provenance tags (in-situ, imported, unknown)
2. **Flow Through Processing**: Provenance flows through recipes and processes
3. **Proportional Blending**: When materials combine, provenance blends proportionally by mass
4. **Mass-Based Tracking**: Track provenance in kilograms (canonical unit)
5. **Persistent State**: Provenance persists in simulation state

### Provenance Categories

Materials are classified into three categories:

1. **`in_situ_kg`**: Extracted/produced locally from environmental resources
   - Mined regolith
   - Captured water/volatiles
   - Materials produced from boundary processes

2. **`imported_kg`**: Brought from Earth
   - Items added via `sim.import` command
   - Bootstrap equipment and materials

3. **`unknown_kg`**: Provenance untracked (legacy/error cases)
   - Items created without provenance information
   - Used as fallback for robustness

---

## Architecture

### 1. State Model

**Add to `SimulationState` (src/simulation/models.py):**

```python
class ProvenanceTotals(BaseModel):
    """Mass provenance totals (kg) for an inventory item."""
    in_situ_kg: float = 0.0
    imported_kg: float = 0.0
    unknown_kg: float = 0.0

class SimulationState(BaseModel):
    # ... existing fields ...
    provenance: Dict[str, ProvenanceTotals] = Field(default_factory=dict)
```

**Storage:**
- Provenance stored per `item_id` in `state.provenance` dictionary
- Separate from `inventory` (which tracks quantities/units)
- Persisted in `snapshot.json`

### 2. Provenance Flow

#### A. Material Origins

**Boundary processes create in-situ materials:**

```python
# Process: regolith_mining_simple_v0
# Input: [] (no inputs - boundary process)
# Output: regolith_lunar_mare: 100 kg

# Provenance assigned at output:
provenance["regolith_lunar_mare"] = {
    "in_situ_kg": 100.0,
    "imported_kg": 0.0,
    "unknown_kg": 0.0
}
```

**Import command creates imported materials:**

```python
# Command: sim.import --item nickel_metal --quantity 2 --unit kg

# Provenance assigned:
provenance["nickel_metal"] = {
    "in_situ_kg": 0.0,
    "imported_kg": 2.0,
    "unknown_kg": 0.0
}
```

#### B. Processing Flow

**When a process consumes inputs, provenance is tracked:**

```python
# Process: iron_smelting_reduction_v0
# Inputs: iron_ore: 2 kg, carbon: 0.5 kg
# Outputs: iron_pig: 1 kg, slag: 0.24 kg

# Step 1: Consume inputs (in _validate_process_inputs event handler)
iron_ore_prov = _consume_provenance("iron_ore", 2.0, "kg")
  # Returns: {"in_situ_kg": 2.0, "imported_kg": 0.0, "unknown_kg": 0.0}
carbon_prov = _consume_provenance("carbon", 0.5, "kg")
  # Returns: {"in_situ_kg": 0.0, "imported_kg": 0.5, "unknown_kg": 0.0}

# Step 2: Aggregate consumed provenance
total_consumed = {
    "in_situ_kg": 2.0,
    "imported_kg": 0.5,
    "unknown_kg": 0.0
}
# Stored on ProcessRun.provenance_consumed_kg

# Step 3: Distribute to outputs (in _add_process_outputs event handler)
# Calculate output masses
iron_pig_mass = 1.0 kg
slag_mass = 0.24 kg
total_output_mass = 1.24 kg

# Distribute proportionally
iron_pig_share = 1.0 / 1.24 = 0.806
slag_share = 0.24 / 1.24 = 0.194

provenance["iron_pig"] += {
    "in_situ_kg": 2.0 * 0.806 = 1.61,
    "imported_kg": 0.5 * 0.806 = 0.40,
    "unknown_kg": 0.0
}

provenance["slag"] += {
    "in_situ_kg": 2.0 * 0.194 = 0.39,
    "imported_kg": 0.5 * 0.194 = 0.10,
    "unknown_kg": 0.0
}
```

**Key insight:** Provenance flows proportionally to output mass ratios.

#### C. Multi-Step Recipes

**Provenance flows through recipe steps automatically:**

```python
# Recipe: recipe_steel_ingot_v0
# Step 0: steel_refining_basic_v0
#   Input: iron_pig (1.61 in-situ, 0.40 imported)
#   Output: steel_billet (inherits blended provenance)

# Step 1: steel_ingot_cast_v0
#   Input: steel_billet (1.61 in-situ, 0.40 imported)
#   Output: steel_ingot (inherits blended provenance)

# Final provenance:
provenance["steel_ingot"] = {
    "in_situ_kg": 1.61,  # ~80% ISRU
    "imported_kg": 0.40,  # ~20% imported
    "unknown_kg": 0.0
}
```

No special handling needed - provenance naturally flows through steps.

### 3. Implementation Details

#### Event Handlers (src/simulation/engine.py)

**Two event handlers manage provenance:**

1. **`_validate_process_inputs`** (PROCESS_START event)
   - Consumes inventory
   - Tracks provenance consumed
   - Stores on `ProcessRun.provenance_consumed_kg`
   - Rolls back on failure

2. **`_add_process_outputs`** (PROCESS_COMPLETE event)
   - Retrieves `ProcessRun.provenance_consumed_kg`
   - Distributes proportionally to outputs by mass
   - Adds provenance to output items

**Key Methods:**

```python
def _consume_provenance(item_id: str, qty: float, unit: str, context: str) -> Dict[str, float]:
    """Remove provenance from inventory, return consumed amounts."""
    # Convert qty to kg
    # Remove from state.provenance[item_id]
    # Return consumed totals

def _add_provenance(item_id: str, totals: Dict[str, float]) -> None:
    """Add provenance to inventory."""
    # Add to state.provenance[item_id]
    # Create entry if doesn't exist

def _require_kg(item_id: str, qty: float, unit: str, context: str) -> float:
    """Convert quantity to kg for mass tracking."""
    # Uses UnitConverter
    # Returns mass in kg
```

**Boundary Process Handling:**

```python
# Boundary processes have no inputs
if not process.inputs or len(process.inputs) == 0:
    # Mark outputs as 100% in-situ
    self._add_provenance(item_id, {"in_situ_kg": mass_kg})
```

**Import Handling:**

```python
# In import_item()
self._add_provenance(item_id, {"imported_kg": mass_kg})
```

### 4. CLI Command

**New command: `sim provenance`**

```bash
python -m src.cli sim provenance --sim-id <sim_id> [--item <item_id>] [--json]
```

**Features:**
- Overall ISRU percentage
- Top items by mass with bar charts
- Mixed provenance items (opportunities for improvement)
- Detailed per-item breakdown
- JSON output for scripting
- Runbook integration (`sim.provenance` command)

---

## Examples

### Example 1: Fully In-Situ Production

```bash
# Mine regolith (boundary process)
$ sim.run-recipe --recipe recipe_regolith_lunar_mare_v0 --quantity 50
# Provenance: 100% in-situ (5000 kg)

# Extract iron
$ sim.run-recipe --recipe recipe_iron_pig_or_ingot_v0 --quantity 30
# Provenance: 100% in-situ (30 kg)
# (Consumes 60 kg regolith, 15 kg carbon_reducing_agent imported)

# Check result
$ sim provenance --item iron_pig_or_ingot
In-situ:    24.00 kg ( 80.0%)  # From regolith
Imported:    6.00 kg ( 20.0%)  # From carbon
```

### Example 2: Blended Materials

```bash
# Start with mixed inventory
regolith: 50 kg (100% in-situ)
regolith: 50 kg (100% imported)

# Process combined batch
$ sim.run-recipe --recipe recipe_ilmenite_from_regolith_v0 --quantity 100

# Output has blended provenance
ilmenite: 60 kg (50% in-situ, 50% imported)
```

### Example 3: Complex Assembly

```bash
# Electrolysis cell unit from mixed sources:
# - Steel sheet: 20 kg (80% in-situ from regolith)
# - Nickel wire: 2 kg (0% in-situ - imported)
# - Tungsten cathode: 2 kg (0% in-situ - imported)
# - Other parts: 1 kg (100% imported)

$ sim provenance --item electrolysis_cell_unit_v0
Total: 25.00 kg
In-situ:   16.00 kg (64.0%)
Imported:   9.00 kg (36.0%)

# ISRU opportunity: Extract nickel from regolith → 72% ISRU
```

---

## Runbook Integration

Provenance commands work in runbooks:

```markdown
## Check Initial State

\`\`\`sim-runbook
- cmd: sim.provenance
  args: {}
\`\`\`

## Mine Regolith

\`\`\`sim-runbook
- cmd: sim.run-recipe
  args:
    recipe: recipe_regolith_lunar_mare_v0
    quantity: 100
- cmd: sim.advance-time
  args:
    hours: 1
\`\`\`

## Verify ISRU Improvement

\`\`\`sim-runbook
- cmd: sim.provenance
  args: {}
\`\`\`

## Check Final Product

\`\`\`sim-runbook
- cmd: sim.provenance
  args:
    item: steel_ingot
\`\`\`
```

---

## Testing

### Unit Tests

**File:** `test/integration/test_provenance.py`

```python
def test_boundary_process_creates_in_situ():
    """Boundary processes mark outputs as 100% in-situ."""
    engine.run_recipe("recipe_regolith_lunar_mare_v0", quantity=1)
    engine.advance_time(1.0)

    prov = engine.state.provenance["regolith_lunar_mare"]
    assert prov.in_situ_kg == 100.0
    assert prov.imported_kg == 0.0

def test_import_creates_imported():
    """Import command marks items as 100% imported."""
    engine.import_item("nickel_metal", 2.0, "kg")

    prov = engine.state.provenance["nickel_metal"]
    assert prov.in_situ_kg == 0.0
    assert prov.imported_kg == 2.0

def test_provenance_flows_through_processing():
    """Provenance flows proportionally through processes."""
    # Set up: 60 kg regolith (in-situ), 15 kg carbon (imported)
    engine.run_recipe("recipe_regolith_lunar_mare_v0", quantity=60)
    engine.import_item("carbon_reducing_agent", 15.0, "kg")

    # Process: iron smelting
    engine.run_recipe("recipe_iron_pig_or_ingot_v0", quantity=30)
    engine.advance_time(120.0)

    # Check blended provenance
    prov = engine.state.provenance["iron_pig_or_ingot"]
    total = prov.in_situ_kg + prov.imported_kg
    isru_pct = prov.in_situ_kg / total * 100

    assert isru_pct > 70  # Mostly in-situ
    assert prov.imported_kg > 0  # Some imported carbon

def test_multi_step_recipe_provenance():
    """Provenance flows through multi-step recipes."""
    # Already tested by runbook integration tests
    # See: test_nickel_extraction.md → 80% ISRU result
```

### Integration Tests

**Runbook:** `runbooks/electrolysis_cell_unit_v0_runbook.md`

```bash
$ python -m src.cli sim runbook --file runbooks/electrolysis_cell_unit_v0_runbook.md
# ... builds electrolysis cell ...

$ python -m src.cli sim provenance --sim-id electrolysis_cell_v0_build_v2 \
  --item electrolysis_cell_unit_v0

=== Item: electrolysis_cell_unit_v0 ===
Total mass: 25.00 kg
  In-situ:     20.00 kg ( 80.0%)
  Imported:     5.00 kg ( 20.0%)
```

**Result:** ✅ 80% ISRU achieved (iron/steel from local regolith)

---

## Limitations and Future Work

### Current Limitations

1. **Volume/Count Tracking**: Only mass-based provenance (kg)
   - Items measured in `unit` or `m3` use mass lookups
   - Items without mass definitions show warnings

2. **Assembly Provenance**: Assemblies don't track component provenance
   - E.g., `labor_bot` assembly doesn't show steel (60%) + electronics (40%)
   - Only tracks total blended provenance

3. **Energy Provenance**: Energy (kWh) provenance not tracked
   - Solar = in-situ, imported fuel = imported
   - Future: Track energy origin separately

4. **Provenance History**: No timeline view
   - Can't see "ISRU improved from 20% to 80% over time"
   - Future: Add `provenance_history` events

### Future Enhancements

1. **Provenance Visualization** (ADR-024?)
   - Sankey diagrams showing material flow
   - Timeline charts of ISRU improvement
   - Component breakdowns (steel 60%, electronics 40%)

2. **Provenance Goals**
   - Set target ISRU percentages
   - Runbook validation: "Must achieve ≥75% ISRU"
   - Alerts when falling below target

3. **Provenance Optimization**
   - Auto-suggest recipe swaps to improve ISRU
   - "Replace imported nickel with recipe_nickel_from_regolith_v0 → +8% ISRU"

4. **Energy Provenance**
   - Track energy origin (solar/nuclear/imported)
   - Separate energy ISRU from material ISRU

---

## Files Modified

1. **src/simulation/models.py** (~20 lines)
   - Add `ProvenanceTotals` model
   - Add `provenance: Dict[str, ProvenanceTotals]` to `SimulationState`
   - Add `provenance_consumed_kg: Dict[str, float]` to `ProcessRun`

2. **src/simulation/engine.py** (~150 lines)
   - Add `_consume_provenance()` method
   - Add `_add_provenance()` method
   - Add `_get_provenance_entry()` method
   - Modify `_validate_process_inputs()` handler to track provenance
   - Modify `_add_process_outputs()` handler to distribute provenance
   - Modify `import_item()` to mark as imported

3. **src/simulation/cli.py** (~200 lines)
   - Add `cmd_provenance()` function
   - Add `sim provenance` subcommand parser
   - Add `sim.provenance` to runbook command map
   - Add provenance display helpers

4. **docs/CLI_COMMANDS_GUIDE.md** (~100 lines)
   - Add `sim provenance` command documentation

5. **docs/CLI_USAGE_FOR_CLAUDE.md** (~20 lines)
   - Add provenance to available commands
   - Add to workflow examples

6. **docs/ADRs/023-material-provenance-tracking.md** (this file)
   - Complete ADR documentation

---

## Decision Rationale

### Why Mass-Based Tracking?

**Alternative:** Track provenance as percentages per item

**Problems:**
- Percentages don't compose (40% + 60% ≠ 100% when masses differ)
- Can't blend provenance when combining materials
- Loses information during processing

**Solution:** Track absolute masses (kg)
- Composes correctly: 80 kg + 20 kg = 100 kg
- Blends proportionally: (80 kg in-situ + 20 kg imported) / 100 kg = 80% ISRU
- Preserves information through supply chain

### Why Three Categories?

**in_situ + imported + unknown**

**Rationale:**
1. **in_situ**: Clear ISRU metric
2. **imported**: Clear Earth-dependence metric
3. **unknown**: Robustness for legacy data, missing information

**Alternative:** Just two categories (in_situ + imported)

**Problem:** Breaks when provenance unknown (old simulations, errors)

**Solution:** Three categories with `unknown` fallback

### Why Event Handlers?

**Alternative:** Track provenance in `advance_time()` loop

**Problem:**
- Duplicates process logic
- Misses timing (consumes before start vs after complete)
- Doesn't work with ADR-020 event-driven architecture

**Solution:** Use existing PROCESS_START and PROCESS_COMPLETE handlers
- Provenance consumed at PROCESS_START (with input validation)
- Provenance distributed at PROCESS_COMPLETE (with output addition)
- Aligns with ADR-020 event lifecycle

---

## Consequences

### Positive

1. **ISRU Measurement**: Quantifiable metric for design decisions
2. **Runbook Optimization**: Identify high-value ISRU opportunities
3. **Design Validation**: Verify ISRU targets achieved
4. **Supply Chain Visibility**: Track material origins through processing
5. **Automation Ready**: JSON output enables scripted optimization

### Negative

1. **State Size**: Adds ~10-20% to snapshot.json size
2. **Processing Overhead**: Extra calculations during process completion
3. **Memory Usage**: Additional dictionaries in state
4. **Complexity**: More state to manage and test

### Neutral

1. **Backward Compatibility**: Old simulations work (provenance starts as unknown)
2. **Optional Feature**: Provenance tracking passive - doesn't affect functionality
3. **Granularity Trade-offs**: Mass-based tracking simpler than full component tracking

---

## Status

**Status:** IMPLEMENTED

**Implementation Date:** 2026-01-14

**Next Steps:**
1. ✅ Add ProvenanceTotals model
2. ✅ Implement provenance flow in event handlers
3. ✅ Add `sim provenance` CLI command
4. ✅ Test with electrolysis cell runbook
5. ✅ Document in CLI guides
6. 🔄 Future: Visualization and optimization features (ADR-024?)

---

## References

- **ADR-004 (Base Builder Simulation)**: Original simulation architecture
- **ADR-007 (Explicit Import Items)**: Import tracking foundation
- **ADR-020 (Recipe Orchestration)**: Event-driven processing
- **ADR-021 (State Persistence)**: Provenance persists in snapshots
- **ADR-022 (Simulation Runbooks)**: Runbook integration
- **Runbook Example**: `runbooks/electrolysis_cell_unit_v0_runbook.md`
- **Implementation**: `src/simulation/engine.py` (provenance methods)
- **CLI Command**: `src/simulation/cli.py:cmd_provenance()`
