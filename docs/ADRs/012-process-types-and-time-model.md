# 012: Process Types and Time Model Redesign

**Status:** Proposed
**Date:** 2024-12-28
**Decision Makers:** Project team
**Related ADRs:** 014 (Energy Model), 013 (Recipe Overrides), 016 (Unit Conversion), 018 (Recipe Validation)

## Context

The knowledge base has ~891 processes with `time_model` definitions, but the simulation engine doesn't use them. Instead, simulations rely on agent-provided durations, creating fundamental problems:

### Problems Identified

1. **Disconnected modeling** - Rich `time_model` data exists but isn't used by simulation
2. **Hard-coded units** - `rate_kg_per_hr` only works for kg-based processes, fails for L (liters), unit (count), etc.
3. **No scaling basis** - When multiple inputs exist, unclear which drives the time calculation
4. **Type ambiguity** - `fixed_time` vs batch semantics unclear, relationship to process physics undefined
5. **Unit heterogeneity** - Processes use kg rates but inputs may be in liters or units
6. **Missing validation** - Invalid schemas exist in production (e.g., `total_time_hr` field doesn't exist)

### Investigation Summary

**Documents:**
- `design/process-time-energy-models-current-state.md` - Current state analysis
- `design/time-calculation-real-world-examples.md` - 10 processes analyzed, 50% fail calculation
- `design/batch-vs-continuous-process-types.md` - Process type definitions
- `design/time-model-schema-redesign.md` - New schema proposal

**Key Findings:**
- 50% of analyzed processes fail time calculation (unit mismatches, missing data, schema errors)
- Found processes with invalid time_model fields (`total_time_hr` instead of valid schema)
- Found recipe with 15× discrepancy (2hr vs 30hr calculated) - no validation caught it
- Count-based and volume-based processes can't use current kg-only schema

## Decision

We will implement a **new time_model schema** with the following changes:

### 1. Explicit Process Types

Add **required** `process_type` field to all processes:

```yaml
process_type: batch | continuous | boundary
```

**Semantics:**
- **Continuous:** Rate-based production (kg/hr, unit/hr), linear scaling, steady-state operation
- **Batch:** Discrete batches, setup per batch, batch size from outputs
- **Boundary:** Terminal nodes that extract from environment with no material inputs (mining, collection)

**Examples:**
- Continuous: Crushing, electrolysis, distillation, machining (one after another)
- Batch: Assembly, firing, heat treatment, discrete manufacturing
- Boundary: Regolith mining, environmental resource collection, sample gathering

**Note:** Boundary processes have special validation rules - see 018 for recipe input/output validation with boundary processes.

### 2. New Time Model Schema

#### For Continuous Processes

```yaml
process_type: continuous
time_model:
  type: linear_rate
  rate: <numeric_value>
  rate_unit: <unit>/<time_unit>  # e.g., "kg/hr", "unit/hr", "L/hr"
  scaling_basis: <item_id>  # Which input/output drives time (REQUIRED)
  notes: <optional_string>
```

**Key changes:**
- **Flexible units:** Supports any unit (kg, L, unit, count, m, etc.), not just kg
- **Required scaling_basis:** Explicitly specifies which input/output drives time
- **Structured rate:** Separate `rate` (value) and `rate_unit` (unit string)
- **Natural count rates:** 12 unit/hr (not 0.1 hr/unit)

#### For Batch Processes

```yaml
process_type: batch
time_model:
  type: batch
  setup_hr: <float>  # Optional, defaults to 0
  hr_per_batch: <float>  # Required
  notes: <optional_string>
```

**Key changes:**
- Type renamed from `fixed_time` to `batch` for clarity
- `setup_hr` optional (defaults to 0 if not specified)
- Batch size implicit from process `outputs` (not duplicated in time_model)
- No `scaling_basis` - batch size defined by outputs

### 3. Validation Rules

#### Schema Validation

1. **process_type required** - Every process must specify batch, continuous, or boundary
2. **Type consistency** - `process_type: continuous` requires `time_model.type: linear_rate`
3. **Type consistency** - `process_type: batch` requires `time_model.type: batch`
4. **Type consistency** - `process_type: boundary` allows `time_model.type: batch` or `linear_rate` (see 018)
5. **No invalid fields** - Reject deprecated fields (`rate_kg_per_hr`, `hr_per_kg`, `fixed_time`)
6. **Required fields** - For linear_rate: `rate`, `rate_unit`, `scaling_basis`. For batch: `hr_per_batch`
7. **Boundary process inputs** - Boundary processes must have empty or no inputs (validated in 018)

#### Semantic Validation

1. **No setup_hr in continuous** - Validation error if `process_type: continuous` has `setup_hr`
2. **scaling_basis exists** - Must refer to actual input or output `item_id`
3. **Unit consistency** - `scaling_basis` item unit must match `rate_unit` numerator (or be convertible)
4. **Positive values** - `rate`, `hr_per_batch`, `setup_hr` must be > 0

#### Calculation Validation

1. **Can calculate duration** - Validation ensures time_model can be evaluated with process inputs/outputs
2. **Unit conversion possible** - If `scaling_basis` unit differs from `rate_unit`, conversion must exist

### 4. Rate Unit Specification

**Format:** `<numerator_unit>/<denominator_unit>`

**Examples:**
- `kg/hr` - Kilograms per hour
- `unit/hr` - Units per hour (natural count format)
- `L/hr` - Liters per hour
- `m/hr` - Meters per hour
- `L/min` - Liters per minute (converted to /hr internally)

**Time normalization:** All rates normalized to hours internally (min → hr, day → hr)

### 5. Scaling Basis

**Purpose:** Explicitly specify which input or output drives the time calculation.

**Examples:**

```yaml
# Single input - clear
inputs:
  - item_id: regolith_coarse
    qty: 1.0
    unit: kg
time_model:
  scaling_basis: regolith_coarse  # Unambiguous
```

```yaml
# Multiple inputs - must specify
inputs:
  - item_id: steel_sheet
    qty: 10.0
    unit: kg
  - item_id: lubricant
    qty: 0.5
    unit: L
time_model:
  scaling_basis: steel_sheet  # Explicitly steel, not lubricant
```

```yaml
# Output scaling (less common)
time_model:
  scaling_basis: aluminum_pure  # Output drives time
```

## Consequences

### Positive

1. **Unit flexibility** - Supports any unit type (kg, L, unit, count, etc.)
2. **Clear semantics** - `scaling_basis` eliminates "per kg of what?" ambiguity
3. **Validation power** - Can catch errors automatically (unit mismatches, missing data)
4. **Calculation reliability** - Unambiguous time calculations for simulation
5. **Batch clarity** - Explicit batch vs continuous distinction removes confusion
6. **Natural rates** - Count-based uses natural format (12 unit/hr) improving readability
7. **Test foundation** - Real-world examples become test cases

### Negative

1. **Migration required** - All ~891 processes need updating
2. **Breaking change** - Old schema will not work (validation errors)
3. **Complexity** - More fields to specify (`process_type`, `scaling_basis`)
4. **Inference needed** - Migration script must infer `scaling_basis` for existing processes

### Neutral

1. **Parallel energy changes** - Energy model will follow same pattern (014)
2. **Recipe impacts** - Recipe override mechanics need specification (013)
3. **Unit conversion** - Requires implicit conversion system (016)

## Migration Strategy

### Phase 1: Schema Update

1. **Update `kbtool/models.py`** with new TimeModel schema
2. **Add validation** to reject old schema
3. **Implement parsing** for `rate_unit` strings

### Phase 2: Process Updates

**Automated migration where possible:**

```python
# Continuous with rate_kg_per_hr
OLD:
  time_model:
    type: linear_rate
    rate_kg_per_hr: 10.0

NEW:
  process_type: continuous
  time_model:
    type: linear_rate
    rate: 10.0
    rate_unit: kg/hr
    scaling_basis: <inferred_from_single_kg_input>
```

```python
# Continuous with hr_per_kg (invert)
OLD:
  time_model:
    type: linear_rate
    hr_per_kg: 0.1  # 0.1 hr/kg = 10 kg/hr

NEW:
  process_type: continuous
  time_model:
    type: linear_rate
    rate: 10.0  # Inverted
    rate_unit: kg/hr
    scaling_basis: <inferred>
```

```python
# Batch with fixed_time
OLD:
  time_model:
    type: fixed_time
    hr_per_batch: 1.0

NEW:
  process_type: batch
  time_model:
    type: batch
    setup_hr: 0.0
    hr_per_batch: 1.0
```

**Manual fixes required:**
- Processes with multiple inputs (ambiguous `scaling_basis`)
- Processes with `setup_hr` in continuous (split or convert to batch)
- Invalid schemas (e.g., `total_time_hr`)

### Phase 3: Validation Rollout

1. **Indexer integration** - Validate all processes
2. **Generate work queue** - Enqueue issues for agent fixing
3. **Incremental fixes** - Agents fix processes one by one

### Phase 4: Simulation Integration

1. **Implement calculation functions** - Use time_model to calculate duration
2. **Agent integration** - Agent can specify duration OR quantity (time_model calculates other)
3. **Validation during execution** - Simulation validates time_model can be evaluated

## Implementation Details

### Time Calculation Algorithm

```python
def calculate_duration(process: Process, inputs: dict) -> float:
    """Calculate process duration from time_model."""

    if process.time_model.type == "linear_rate":
        # Get scaling basis item quantity
        scaling_item = inputs.get(process.time_model.scaling_basis)
        if scaling_item is None:
            raise ValueError(f"scaling_basis '{process.time_model.scaling_basis}' not in inputs")

        # Get quantity in correct unit
        quantity = scaling_item.qty
        unit = scaling_item.unit

        # Parse rate unit
        rate_numerator, rate_denominator = parse_rate_unit(process.time_model.rate_unit)

        # Convert if needed
        if unit != rate_numerator:
            quantity = convert_unit(quantity, unit, rate_numerator, scaling_item.item_id)

        # Calculate time
        duration_hr = quantity / process.time_model.rate

        return duration_hr

    elif process.time_model.type == "batch":
        # Determine number of batches needed
        batch_output_qty = sum(output.qty for output in process.outputs)
        desired_output_qty = sum(outputs.values())  # Total desired

        num_batches = math.ceil(desired_output_qty / batch_output_qty)

        # Time = batches × (setup + batch_time)
        duration_hr = num_batches * (
            process.time_model.setup_hr + process.time_model.hr_per_batch
        )

        return duration_hr
```

### Validation Implementation

```python
def validate_time_model(process: Process) -> list[ValidationError]:
    """Validate time_model against new schema."""
    errors = []

    # 1. process_type required
    if not hasattr(process, 'process_type'):
        errors.append(ValidationError(
            f"Process '{process.id}' missing required field 'process_type'"
        ))
        return errors

    # 2. Type consistency
    if process.process_type == "continuous":
        if process.time_model.type != "linear_rate":
            errors.append(ValidationError(
                f"Process '{process.id}' has process_type: continuous "
                f"but time_model.type: {process.time_model.type}. "
                f"Must be 'linear_rate'."
            ))

    elif process.process_type == "batch":
        if process.time_model.type != "batch":
            errors.append(ValidationError(
                f"Process '{process.id}' has process_type: batch "
                f"but time_model.type: {process.time_model.type}. "
                f"Must be 'batch'."
            ))

    # 3. No setup_hr in continuous
    if process.process_type == "continuous":
        if hasattr(process.time_model, 'setup_hr') and process.time_model.setup_hr is not None:
            errors.append(ValidationError(
                f"Process '{process.id}' has process_type: continuous "
                f"but specifies setup_hr. Setup not allowed in continuous processes."
            ))

    # 4. scaling_basis exists (for continuous)
    if process.time_model.type == "linear_rate":
        if not hasattr(process.time_model, 'scaling_basis'):
            errors.append(ValidationError(
                f"Process '{process.id}' missing required field 'scaling_basis'"
            ))
        else:
            # Check scaling_basis refers to actual input/output
            all_items = [i.item_id for i in process.inputs] + [o.item_id for o in process.outputs]
            if process.time_model.scaling_basis not in all_items:
                errors.append(ValidationError(
                    f"Process '{process.id}' scaling_basis '{process.time_model.scaling_basis}' "
                    f"not found in inputs or outputs"
                ))

    # 5. Unit consistency
    if process.time_model.type == "linear_rate":
        scaling_item = next(
            (i for i in process.inputs + process.outputs
             if i.item_id == process.time_model.scaling_basis),
            None
        )
        if scaling_item:
            rate_numerator, _ = parse_rate_unit(process.time_model.rate_unit)
            if scaling_item.unit != rate_numerator:
                # Check if conversion exists
                if not can_convert(scaling_item.unit, rate_numerator, scaling_item.item_id):
                    errors.append(ValidationError(
                        f"Process '{process.id}' scaling_basis unit mismatch: "
                        f"'{scaling_item.unit}' vs rate_unit '{rate_numerator}'. "
                        f"No conversion available."
                    ))

    return errors
```

## Examples

### Example 1: Continuous Crushing (kg-based)

```yaml
process_id: regolith_crushing_grinding_v0
process_type: continuous

inputs:
  - item_id: regolith_coarse_fraction
    qty: 1.0
    unit: kg

outputs:
  - item_id: regolith_powder
    qty: 1.0
    unit: kg

time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: regolith_coarse_fraction
  notes: "Continuous crushing at 10 kg/hr throughput"
```

**Calculation (100 kg input):**
- Duration: 100 kg / 10 kg/hr = **10 hours**

### Example 2: Continuous Machining (count-based)

```yaml
process_id: pump_housing_machining_v0
process_type: continuous

inputs:
  - item_id: machined_part_raw
    qty: 25.0
    unit: unit
  - item_id: cutting_fluid
    qty: 1.8
    unit: L  # Consumable, doesn't drive time

outputs:
  - item_id: pump_housing_machined
    qty: 25.0
    unit: unit

time_model:
  type: linear_rate
  rate: 12.0
  rate_unit: unit/hr  # Natural count format
  scaling_basis: machined_part_raw  # Explicit: parts drive time, not fluid
  notes: "Machining rate based on part count"
```

**Calculation (25 parts):**
- Duration: 25 unit / 12 unit/hr = **2.08 hours**

### Example 3: Batch Assembly

```yaml
process_id: motor_final_assembly_v0
process_type: batch

inputs:
  - item_id: stator_rotor_lamination_set
    qty: 5.0
    unit: kg
  - item_id: motor_coil_wound
    qty: 2.0
    unit: kg
  # ... more inputs

outputs:
  - item_id: motor_electric_small
    qty: 1.0  # 1 batch = 1 motor
    unit: unit

time_model:
  type: batch
  setup_hr: 0.1  # Tool setup
  hr_per_batch: 0.9  # Assembly time
  notes: "Assembly of 1 motor per batch"
```

**Calculation (10 motors needed):**
- Batches: 10 motors / 1 motor per batch = 10 batches
- Duration: 10 × (0.1 + 0.9) = **10 hours**

### Example 4: Water Electrolysis (multi-output, explicit scaling)

```yaml
process_id: water_electrolysis_v0
process_type: continuous

inputs:
  - item_id: water
    qty: 1.0
    unit: kg

outputs:
  - item_id: hydrogen_gas
    qty: 0.111
    unit: kg
  - item_id: oxygen_gas
    qty: 0.889
    unit: kg

time_model:
  type: linear_rate
  rate: 0.5
  rate_unit: kg/hr
  scaling_basis: water  # Explicit: per kg water input
  notes: "Continuous electrolysis, rate based on water throughput"
```

**Calculation (100 kg water):**
- Duration: 100 kg / 0.5 kg/hr = **200 hours**
- H2 output: 11.1 kg
- O2 output: 88.9 kg

## References

- Investigation documents in `design/` directory
- Current schema: `kbtool/models.py:64-78`
- Real-world examples: `design/time-calculation-real-world-examples.md`
- Batch semantics: `design/batch-vs-continuous-process-types.md`
- Schema proposal: `design/time-model-schema-redesign.md`

## Related Decisions

- **014:** Energy model will follow same structure (type, value, unit, scaling_basis)
- **013:** Recipe override mechanics (est_time_hr → time_model overrides)
- **016:** Implicit unit conversion system
- **017:** Validation and error detection strategy

## Approval

- [ ] Architecture review
- [ ] Implementation team review
- [ ] Migration strategy approved
- [ ] Test plan approved
