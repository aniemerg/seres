# 014: Energy Model Redesign

**Status:** Proposed
**Date:** 2024-12-28
**Decision Makers:** Project team
**Related ADRs:** 012 (Process Types and Time Model), 013 (Recipe Overrides), 016 (Unit Conversion)

## Context

The knowledge base has energy models in many processes, but the current schema has the same fundamental limitations as the time_model schema addressed in 012:

### Problems Identified

1. **Hard-coded units** - `kWh_per_kg` type only works for kg-based processes, fails for other units
2. **No scaling basis** - "Is it per kg input or per kg output? For which output?" - ambiguous
3. **Type explosion** - Encoding too much in type names (kWh_per_kg, kWh_per_batch, kWh_per_unit_output)
4. **Unclear semantics** - Cannot determine which input or output drives energy consumption
5. **Limited flexibility** - Cannot represent MJ, BTU, or other energy units
6. **No validation** - Cannot validate energy-time coupling or reasonable power levels

### Current Schema

```python
class EnergyModel:
    type: str  # kWh_per_kg, kWh_per_batch, kWh_per_unit_output
    value: float
    notes: Optional[str]
```

**Critical limitations:**
- Type encodes both unit AND scaling method
- Cannot extend to new energy units (MJ, GJ, BTU)
- Cannot specify different mass/volume/count units
- No explicit scaling basis

### Real Example Issues

**Water electrolysis ambiguity:**
```yaml
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

energy_model:
  type: kWh_per_kg
  value: 15.0
  notes: "~50 kWh per kg H2, ~4-5 kWh per kg water"
```

**Questions:**
- Is it 15 kWh per kg **water** (input)?
- Or 15 kWh per kg **hydrogen** (output)?
- Notes mention both - which is it?

**Current status:** **Undefined!** Must guess from notes or context.

## Decision

We will implement a **new energy_model schema** that parallels the time_model redesign (012):

### 1. Structured Energy Model Schema

Replace type-encoded schema with structured approach:

#### For Per-Unit Energy (Continuous or Batch)

```yaml
energy_model:
  type: per_unit
  value: <numeric_value>
  unit: <energy_unit>/<scaling_unit>  # e.g., "kWh/kg", "kWh/unit", "MJ/L"
  scaling_basis: <item_id>  # Which input/output drives energy (REQUIRED)
  notes: <optional_string>
```

**Key features:**
- **Flexible energy units:** Supports kWh, MJ, GJ, BTU, etc.
- **Flexible scaling units:** Supports any unit (kg, unit, L, m, etc.)
- **Required scaling_basis:** Explicitly specifies which input/output drives energy
- **Structured format:** Separate value and unit fields

#### For Fixed Energy Per Batch

```yaml
energy_model:
  type: fixed_per_batch
  value: <numeric_value>
  unit: <energy_unit>  # e.g., "kWh", "MJ"
  notes: <optional_string>
```

**Key features:**
- Type renamed from `kWh_per_batch` to `fixed_per_batch` for clarity
- No scaling_basis - batch size implicit from process outputs
- Energy unit flexible (kWh, MJ, etc.)

### 2. Energy Unit Specification

**Format for per-unit:** `<energy_unit>/<scaling_unit>`

**Supported energy units:**
- `kWh` - Kilowatt-hour (standard)
- `MWh` - Megawatt-hour
- `Wh` - Watt-hour
- `MJ` - Megajoule
- `GJ` - Gigajoule
- `BTU` - British Thermal Unit

**Examples:**
- `kWh/kg` - Kilowatt-hours per kilogram
- `kWh/unit` - Kilowatt-hours per unit
- `MJ/L` - Megajoules per liter
- `kWh/m` - Kilowatt-hours per meter
- `GJ/kg` - Gigajoules per kilogram

**Energy conversions** (normalized to kWh internally):
```python
ENERGY_UNIT_TO_KWH = {
    "kWh": 1.0,
    "MWh": 1000.0,
    "Wh": 0.001,
    "MJ": 0.2778,    # 1 MJ = 0.2778 kWh
    "GJ": 277.8,     # 1 GJ = 277.8 kWh
    "BTU": 0.000293, # 1 BTU = 0.000293 kWh
}
```

### 3. Validation Rules

#### Schema Validation

1. **Type required** - Must be `per_unit` or `fixed_per_batch`
2. **Value and unit required** - Both must be specified
3. **scaling_basis required for per_unit** - Must specify which input/output
4. **No scaling_basis for fixed_per_batch** - Validation error if specified
5. **No invalid types** - Reject deprecated types (kWh_per_kg, kWh_per_batch, kWh_per_unit_output)

#### Semantic Validation

1. **scaling_basis exists** - Must refer to actual input or output `item_id`
2. **Unit consistency** - `scaling_basis` item unit must match `unit` denominator (or be convertible)
3. **Positive values** - `value` must be > 0
4. **Type alignment** - `fixed_per_batch` typically used with batch processes (warning if not)

#### Energy-Time Coupling Validation

1. **Reasonable power** - Average power (energy/time) should be in reasonable range (0.001 kW to 10,000 kW)
2. **Consistency checks** - Energy and time models should use same scaling_basis (warning if different)
3. **Power sanity check** - Calculate implied power and warn if unusual

### 4. Scaling Basis

**Purpose:** Explicitly specify which input or output drives the energy calculation.

**Required for:** `type: per_unit`
**Not used for:** `type: fixed_per_batch`

**Examples:**

```yaml
# Single input - clear
inputs:
  - item_id: regolith_coarse_fraction
    qty: 1.0
    unit: kg
energy_model:
  scaling_basis: regolith_coarse_fraction  # Unambiguous
```

```yaml
# Multiple inputs - must specify
inputs:
  - item_id: alumina_powder
    qty: 1.92
    unit: kg
  - item_id: carbon_electrodes
    qty: 0.05
    unit: kg
energy_model:
  scaling_basis: alumina_powder  # Explicitly alumina, not electrodes
```

```yaml
# Output scaling
energy_model:
  scaling_basis: aluminum_pure  # Per kg aluminum output
```

### 5. Alignment with Process Types

**Continuous processes** typically use `per_unit`:
```yaml
process_type: continuous
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: input_material
```

**Batch processes** can use either:
- `per_unit` - if energy scales with batch size
- `fixed_per_batch` - if energy is fixed per cycle

```yaml
# Batch with scaling energy
process_type: batch
energy_model:
  type: per_unit
  value: 2.0
  unit: kWh/kg
  scaling_basis: material
```

```yaml
# Batch with fixed energy
process_type: batch
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
```

## Consequences

### Positive

1. **Unit flexibility** - Supports any energy unit (kWh, MJ, GJ, BTU) and any scaling unit (kg, L, unit)
2. **Clear semantics** - `scaling_basis` eliminates "per kg of what?" ambiguity
3. **Validation power** - Can validate energy-time coupling and reasonable power levels
4. **Consistency** - Parallel structure to time_model (type, value, unit, scaling_basis)
5. **Easy to learn** - Same patterns as time_model redesign
6. **Natural rates** - Count-based uses natural format (kWh/unit) improving readability
7. **Power checking** - Can validate that implied power is physically reasonable

### Negative

1. **Migration required** - All processes with energy_model need updating
2. **Breaking change** - Old schema will not work (validation errors)
3. **Complexity** - More fields to specify (`scaling_basis`, structured `unit`)
4. **Inference needed** - Migration script must infer `scaling_basis` for existing processes

### Neutral

1. **Parallel to time model** - Same migration effort and timeline as 012
2. **Recipe impacts** - Recipe override mechanics need specification (013)
3. **Unit conversion** - Requires implicit conversion system (016)

## Migration Strategy

### Phase 1: Schema Update

1. **Update `kbtool/models.py`** with new EnergyModel schema
2. **Add validation** to reject old schema types
3. **Implement parsing** for energy unit strings
4. **Add energy conversions** (MJ→kWh, etc.)

### Phase 2: Process Updates

**Automated migration where possible:**

```python
# kWh_per_kg (most common)
OLD:
  energy_model:
    type: kWh_per_kg
    value: 0.3

NEW:
  energy_model:
    type: per_unit
    value: 0.3
    unit: kWh/kg
    scaling_basis: <inferred_from_single_kg_input>
```

```python
# kWh_per_batch
OLD:
  energy_model:
    type: kWh_per_batch
    value: 120.0

NEW:
  energy_model:
    type: fixed_per_batch
    value: 120.0
    unit: kWh
```

```python
# kWh_per_unit_output
OLD:
  energy_model:
    type: kWh_per_unit_output
    value: 2.5

NEW:
  energy_model:
    type: per_unit
    value: 2.5
    unit: kWh/unit
    scaling_basis: <inferred_from_outputs>
```

**Manual fixes required:**
- Processes with multiple inputs (ambiguous `scaling_basis`)
- Processes where scaling basis differs from obvious choice
- Energy models that should use different units (MJ instead of kWh)

### Phase 3: Validation Rollout

1. **Indexer integration** - Validate all energy models
2. **Power sanity checks** - Calculate and validate implied power
3. **Generate work queue** - Enqueue issues for agent fixing
4. **Incremental fixes** - Agents fix processes one by one

### Phase 4: Simulation Integration

1. **Implement calculation functions** - Use energy_model to calculate energy consumption
2. **Energy-time coupling validation** - Check that power is reasonable
3. **Agent integration** - Agent specifies quantity, both time and energy calculated

## Implementation Details

### Energy Calculation Algorithm

```python
def calculate_energy(process: Process, inputs: dict, outputs: dict) -> float:
    """Calculate process energy consumption from energy_model."""

    if process.energy_model.type == "per_unit":
        # Get scaling basis item quantity
        scaling_item = inputs.get(process.energy_model.scaling_basis) or \
                       outputs.get(process.energy_model.scaling_basis)
        if scaling_item is None:
            raise ValueError(
                f"scaling_basis '{process.energy_model.scaling_basis}' "
                f"not in inputs or outputs"
            )

        # Get quantity in correct unit
        quantity = scaling_item.qty
        unit = scaling_item.unit

        # Parse energy unit
        energy_unit, scaling_unit = parse_energy_unit(process.energy_model.unit)

        # Convert if needed
        if unit != scaling_unit:
            quantity = convert_unit(quantity, unit, scaling_unit, scaling_item.item_id)

        # Calculate energy in specified unit
        energy = quantity * process.energy_model.value

        # Convert to kWh (standard internal unit)
        energy_kwh = energy * ENERGY_UNIT_TO_KWH[energy_unit]

        return energy_kwh

    elif process.energy_model.type == "fixed_per_batch":
        # Determine number of batches needed
        batch_output_qty = sum(output.qty for output in process.outputs)
        desired_output_qty = sum(outputs.values())  # Total desired

        num_batches = math.ceil(desired_output_qty / batch_output_qty)

        # Energy = batches × fixed energy
        energy = num_batches * process.energy_model.value

        # Convert to kWh
        energy_kwh = energy * ENERGY_UNIT_TO_KWH[process.energy_model.unit]

        return energy_kwh
```

### Validation Implementation

```python
def validate_energy_model(process: Process) -> list[ValidationError]:
    """Validate energy_model against new schema."""
    errors = []

    if not hasattr(process, 'energy_model') or process.energy_model is None:
        # Energy model is optional
        return errors

    # 1. Type required
    if not hasattr(process.energy_model, 'type'):
        errors.append(ValidationError(
            f"Process '{process.id}' energy_model missing required field 'type'"
        ))
        return errors

    # 2. Valid types only
    valid_types = ["per_unit", "fixed_per_batch"]
    if process.energy_model.type not in valid_types:
        errors.append(ValidationError(
            f"Process '{process.id}' energy_model.type '{process.energy_model.type}' "
            f"invalid. Must be one of: {valid_types}"
        ))

    # 3. scaling_basis required for per_unit
    if process.energy_model.type == "per_unit":
        if not hasattr(process.energy_model, 'scaling_basis'):
            errors.append(ValidationError(
                f"Process '{process.id}' energy_model type 'per_unit' "
                f"missing required field 'scaling_basis'"
            ))
        else:
            # Check scaling_basis refers to actual input/output
            all_items = [i.item_id for i in process.inputs] + \
                       [o.item_id for o in process.outputs]
            if process.energy_model.scaling_basis not in all_items:
                errors.append(ValidationError(
                    f"Process '{process.id}' energy_model.scaling_basis "
                    f"'{process.energy_model.scaling_basis}' "
                    f"not found in inputs or outputs"
                ))

    # 4. No scaling_basis for fixed_per_batch
    if process.energy_model.type == "fixed_per_batch":
        if hasattr(process.energy_model, 'scaling_basis') and \
           process.energy_model.scaling_basis is not None:
            errors.append(ValidationError(
                f"Process '{process.id}' energy_model type 'fixed_per_batch' "
                f"should not have scaling_basis"
            ))

    # 5. Unit consistency
    if process.energy_model.type == "per_unit":
        scaling_item = next(
            (i for i in process.inputs + process.outputs
             if i.item_id == process.energy_model.scaling_basis),
            None
        )
        if scaling_item:
            energy_unit, scaling_unit = parse_energy_unit(process.energy_model.unit)
            if scaling_item.unit != scaling_unit:
                # Check if conversion exists
                if not can_convert(scaling_item.unit, scaling_unit, scaling_item.item_id):
                    errors.append(ValidationError(
                        f"Process '{process.id}' energy_model scaling_basis unit mismatch: "
                        f"'{scaling_item.unit}' vs unit '{scaling_unit}'. "
                        f"No conversion available."
                    ))

    # 6. Positive values
    if hasattr(process.energy_model, 'value'):
        if process.energy_model.value <= 0:
            errors.append(ValidationError(
                f"Process '{process.id}' energy_model.value must be positive, "
                f"got {process.energy_model.value}"
            ))

    return errors

def validate_energy_time_coupling(process: Process) -> list[ValidationError]:
    """Validate that energy and time models are consistent (reasonable power)."""
    warnings = []

    if not hasattr(process, 'energy_model') or not hasattr(process, 'time_model'):
        return warnings

    if process.energy_model is None or process.time_model is None:
        return warnings

    try:
        # Calculate for nominal inputs
        energy_kwh = calculate_energy(process, process.inputs, process.outputs)
        time_hr = calculate_duration(process, process.inputs)

        if time_hr > 0:
            avg_power_kw = energy_kwh / time_hr

            # Sanity check: 1W to 10MW is reasonable range
            if not (0.001 < avg_power_kw < 10000):
                warnings.append(ValidationError(
                    f"Process '{process.id}' has unusual average power: "
                    f"{avg_power_kw:.2f} kW. "
                    f"(Energy: {energy_kwh:.2f} kWh, Time: {time_hr:.2f} hr). "
                    f"Check energy_model and time_model for consistency.",
                    severity="warning"
                ))
    except Exception as e:
        warnings.append(ValidationError(
            f"Process '{process.id}' could not validate energy-time coupling: {e}",
            severity="warning"
        ))

    return warnings
```

### Energy Unit Parsing

```python
def parse_energy_unit(unit: str) -> tuple[str, Optional[str]]:
    """Parse energy unit string into energy type and optional scaling unit.

    Examples:
        "kWh/kg" → ("kWh", "kg")
        "kWh" → ("kWh", None)
        "MJ/unit" → ("MJ", "unit")
    """
    if '/' in unit:
        parts = unit.split('/')
        if len(parts) != 2:
            raise ValueError(f"Invalid energy unit format: '{unit}'")
        return (parts[0].strip(), parts[1].strip())
    else:
        return (unit.strip(), None)
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

energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: regolith_coarse_fraction
  notes: "Bond work index for lunar regolith comminution"
```

**Calculation (100 kg input):**
- Time: 100 kg / 10 kg/hr = 10 hours
- Energy: 100 kg × 0.3 kWh/kg = 30 kWh
- Average power: 30 kWh / 10 hr = **3 kW** ✓ (reasonable for crusher)

### Example 2: Water Electrolysis (multi-output, explicit scaling)

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
  scaling_basis: water

energy_model:
  type: per_unit
  value: 15.0
  unit: kWh/kg
  scaling_basis: water  # ← EXPLICIT: per kg water input
  notes: "15 kWh/kg water = 135 kWh/kg H2 (stoichiometric)"
```

**Calculation (100 kg water):**
- Time: 100 kg / 0.5 kg/hr = 200 hours
- Energy: 100 kg × 15 kWh/kg = 1500 kWh
- H2 produced: 11.1 kg
- Average power: 1500 kWh / 200 hr = **7.5 kW** ✓ (reasonable for electrolyzer)

### Example 3: Ceramic Firing (fixed energy per batch)

```yaml
process_id: ceramic_firing_v0
process_type: batch

inputs:
  - item_id: green_ceramic_parts
    qty: 10.0
    unit: kg

outputs:
  - item_id: fired_ceramic_parts
    qty: 9.5
    unit: kg

time_model:
  type: batch
  setup_hr: 0.5
  hr_per_batch: 8.0

energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
  notes: "Kiln firing energy independent of load within 5-15 kg range"
```

**Calculation (100 kg green parts = 10 batches):**
- Time: 10 × (0.5 + 8.0) = 85 hours
- Energy: 10 × 120 kWh = 1200 kWh
- Average power: 1200 kWh / 85 hr = **14.1 kW** ✓ (reasonable for kiln)

### Example 4: Aluminum Smelting (MJ/kg alternative units)

```yaml
process_id: aluminum_smelting_hall_heroult_v0
process_type: continuous

inputs:
  - item_id: alumina_powder
    qty: 1.92
    unit: kg

outputs:
  - item_id: aluminum_pure
    qty: 1.0
    unit: kg

time_model:
  type: linear_rate
  rate: 50.0
  rate_unit: kg/hr
  scaling_basis: aluminum_pure

energy_model:
  type: per_unit
  value: 180.0
  unit: MJ/kg  # ← Alternative energy unit (not kWh)
  scaling_basis: aluminum_pure
  notes: "Hall-Heroult process: ~160-200 MJ/kg Al (45-55 kWh/kg)"
```

**Calculation (100 kg aluminum):**
- Time: 100 kg / 50 kg/hr = 2 hours
- Energy: 100 kg × 180 MJ/kg = 18000 MJ = 5000 kWh (converted internally)
- Average power: 5000 kWh / 2 hr = **2500 kW** ✓ (reasonable for smelter)

### Example 5: Motor Assembly (count-based, output scaling)

```yaml
process_id: motor_final_assembly_v0
process_type: batch

outputs:
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit

time_model:
  type: batch
  setup_hr: 0.1
  hr_per_batch: 0.9

energy_model:
  type: per_unit
  value: 0.2
  unit: kWh/unit  # ← Natural count format
  scaling_basis: motor_electric_small  # Output drives energy
  notes: "Testing and tool energy per motor"
```

**Calculation (10 motors = 10 batches):**
- Time: 10 × (0.1 + 0.9) = 10 hours
- Energy: 10 unit × 0.2 kWh/unit = 2 kWh
- Average power: 2 kWh / 10 hr = **0.2 kW** ✓ (reasonable for assembly tools)

## References

- Investigation documents in `design/` directory
- Design document: `design/energy-model-redesign.md`
- Current schema: `kbtool/models.py` (EnergyModel class)
- Parallel design: 012 (Process Types and Time Model Redesign)

## Related Decisions

- **012:** Time model redesign - parallel structure
- **013:** Recipe override mechanics (est_energy_kWh → energy_model overrides)
- **016:** Implicit unit conversion system
- **017:** Validation and error detection strategy

## Approval

- [ ] Architecture review
- [ ] Implementation team review
- [ ] Migration strategy approved
- [ ] Test plan approved
