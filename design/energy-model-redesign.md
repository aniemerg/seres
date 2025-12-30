# Energy Model Redesign

**Status:** In Progress
**Date:** 2024-12-28
**Purpose:** Propose new energy_model schema parallel to time_model redesign

## Overview

The current energy_model schema has the same fundamental limitations as time_model:
1. **Hard-coded units** - `kWh_per_kg` only works for kg-based processes
2. **No scaling basis** - unclear which input/output drives energy consumption
3. **Ambiguous semantics** - is it per kg input or per kg output?
4. **Type confusion** - when to use kWh_per_kg vs kWh_per_batch

This document proposes a **new energy_model schema** that:
- Supports **any unit** (kWh/kg, kWh/unit, MJ/L, etc.)
- **Explicitly specifies scaling basis** (which input/output drives energy)
- Aligns with **batch vs continuous process types**
- Enables **validation and calculation**
- Parallels **time_model redesign** for consistency

---

## Current Schema Problems

### Problem 1: Hard-Coded Units

**Current (from kbtool/models.py):**
```python
class EnergyModel:
    type: str  # kWh_per_kg, kWh_per_batch, kWh_per_unit_output
    value: float
    notes: Optional[str]
```

**Issues:**
- Type encodes both **unit** and **scaling method**
- Can't represent:
  - MJ or other energy units
  - Different mass units (g, ton)
  - Volume-based (kWh/L)
  - Non-standard combinations

**Example failure:**
```yaml
# Want MJ/kg instead of kWh/kg
energy_model:
  type: MJ_per_kg  # ✗ Not a valid type!
  value: 1.08  # 0.3 kWh = 1.08 MJ
```

### Problem 2: No Scaling Basis

**User feedback:** "Is it input or output kg? For which output?"

**Example:**
```yaml
# Water electrolysis
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
- Notes say both (confusing!)

**Current:** **Undefined!** Must guess from notes.

### Problem 3: Type Explosion

**Current types:**
- `kWh_per_kg` - per kg of... what?
- `kWh_per_batch` - for batch processes
- `kWh_per_unit_output` - per unit output (which output?)

**Problems:**
- Encoding too much in type name
- Can't extend to new units
- Unclear semantics

---

## Proposed New Schema

### Core Principles

Same as time_model redesign:
1. **Flexible units** - support any energy and scaling unit
2. **Required scaling_basis** - specify which input/output drives energy
3. **Natural rates** - clear numerator/denominator
4. **Structured specification** - clear value and unit
5. **Alignment with process_type** - batch vs continuous

### Schema V2: Structured Approach

```python
class EnergyModelV2:
    """New energy model schema with flexible units and scaling basis."""

    # For per-unit energy (continuous or batch)
    class PerUnitEnergyModel:
        type: Literal["per_unit"]
        value: float  # Numeric value
        unit: str  # Unit string (e.g., "kWh/kg", "MJ/unit", "kWh/L")
        scaling_basis: str  # Item ID that drives energy
        notes: Optional[str]

    # For fixed energy per batch
    class FixedPerBatchEnergyModel:
        type: Literal["fixed_per_batch"]
        value: float  # Energy per batch
        unit: str  # Energy unit (e.g., "kWh", "MJ")
        notes: Optional[str]
        # No scaling_basis - batch size from outputs
```

### Continuous Process Example (per-unit)

```yaml
# Regolith crushing (kWh/kg)
process_type: continuous
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: regolith_coarse_fraction  # Input that drives energy
  notes: "Bond work index ~15-30 kWh/t for lunar regolith"
```

**Calculation (100 kg input):**
- Energy: 100 kg × 0.3 kWh/kg = 30 kWh

```yaml
# Motor assembly (kWh/unit)
process_type: continuous
energy_model:
  type: per_unit
  value: 2.5
  unit: kWh/unit
  scaling_basis: assembled_motor  # Output that drives energy
  notes: "Energy per motor assembled (testing, tools)"
```

**Calculation (10 motors):**
- Energy: 10 unit × 2.5 kWh/unit = 25 kWh

### Batch Process Example (fixed per batch)

```yaml
# Ceramic firing (fixed energy per batch)
process_type: batch
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
  notes: "Kiln energy per firing cycle, independent of load within 5-15 kg"
```

**Calculation (10 batches):**
- Energy: 10 batches × 120 kWh = 1200 kWh

### Multi-Output Example with Explicit Scaling

```yaml
# Water electrolysis - energy per kg water input
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
energy_model:
  type: per_unit
  value: 15.0
  unit: kWh/kg
  scaling_basis: water  # ← EXPLICIT: per kg water input
  notes: "15 kWh per kg water = ~135 kWh per kg H2"
```

**Alternative: per kg H2 output**
```yaml
energy_model:
  type: per_unit
  value: 135.0  # ~15 / 0.111
  unit: kWh/kg
  scaling_basis: hydrogen_gas  # ← Per kg hydrogen output
  notes: "~50-60 kWh per kg H2 (alkaline electrolysis)"
```

**Both are valid - scaling_basis makes it explicit!**

---

## Energy Unit Specification

### Supported Energy Units

**Standard:**
- `kWh` - Kilowatt-hour
- `MWh` - Megawatt-hour
- `Wh` - Watt-hour
- `MJ` - Megajoule
- `GJ` - Gigajoule
- `BTU` - British Thermal Unit

**Conversions:**
```python
ENERGY_UNIT_TO_KWH = {
    "kWh": 1.0,
    "MWh": 1000.0,
    "Wh": 0.001,
    "MJ": 0.2778,  # 1 MJ = 0.2778 kWh
    "GJ": 277.8,
    "BTU": 0.000293,
}
```

### Energy Rate Format

**Pattern:** `<energy_unit>/<scaling_unit>`

**Examples:**
- `kWh/kg` - Energy per kilogram
- `kWh/unit` - Energy per unit
- `MJ/L` - Energy per liter
- `kWh/m` - Energy per meter (e.g., wire drawing)
- `GJ/batch` - Energy per batch (but use fixed_per_batch instead)

**Parsing:**
```python
def parse_energy_unit(unit: str) -> tuple[str, Optional[str]]:
    """Parse energy unit into energy type and optional scaling unit."""
    if '/' in unit:
        energy, scaling = unit.split('/')
        return (energy.strip(), scaling.strip())
    else:
        return (unit.strip(), None)

# Examples
parse_energy_unit("kWh/kg") → ("kWh", "kg")
parse_energy_unit("kWh") → ("kWh", None)  # Fixed energy
parse_energy_unit("MJ/unit") → ("MJ", "unit")
```

---

## Scaling Basis Specification

### Required for per_unit Type

**Rule:** `scaling_basis` is **required** for `type: per_unit`.

```yaml
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: primary_input_item_id  # ← REQUIRED
```

### Not Used for fixed_per_batch

```yaml
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
  # No scaling_basis - batch size from outputs
```

### Validation Rules

Same as time_model:

1. **scaling_basis must exist:**
   ```python
   assert energy_model.scaling_basis in (inputs + outputs)
   ```

2. **Unit consistency:**
   ```python
   scaling_item = get_item(energy_model.scaling_basis)
   _, scaling_unit = parse_energy_unit(energy_model.unit)
   assert scaling_item.unit == scaling_unit or is_convertible(...)
   ```

3. **Type alignment:**
   ```python
   if energy_model.type == "fixed_per_batch":
       assert process_type == "batch"
   ```

---

## Alignment with Process Types

### Continuous Processes

**Typical:** `type: per_unit` with rate-based energy

```yaml
process_type: continuous
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: input_material
```

**Can also use:** `fixed_per_batch` if energy truly doesn't scale (rare in continuous)

### Batch Processes

**Option 1: Per-unit** (energy scales with batch size)
```yaml
process_type: batch
energy_model:
  type: per_unit
  value: 2.0
  unit: kWh/kg
  scaling_basis: ceramic_powder_mixture
  notes: "Energy scales with load size"
```

**Option 2: Fixed per batch** (energy doesn't scale)
```yaml
process_type: batch
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
  notes: "Kiln firing - fixed energy regardless of load within range"
```

**Decision:** Choose based on physical reality.
- If energy scales with quantity → per_unit
- If energy is fixed per cycle → fixed_per_batch

---

## Migration from Current Schema

### Mapping Old → New

#### kWh_per_kg (most common)

**Old:**
```yaml
energy_model:
  type: kWh_per_kg
  value: 0.3
```

**New:**
```yaml
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: <inferred_from_inputs>  # Must add!
```

**Migration:**
1. Change `type: kWh_per_kg` → `type: per_unit`
2. Add `unit: kWh/kg`
3. Infer `scaling_basis` from inputs (if single kg input)

#### kWh_per_batch

**Old:**
```yaml
energy_model:
  type: kWh_per_batch
  value: 120.0
```

**New:**
```yaml
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
```

**Migration:**
1. Change `type: kWh_per_batch` → `type: fixed_per_batch`
2. Add `unit: kWh`

#### kWh_per_unit_output

**Old:**
```yaml
energy_model:
  type: kWh_per_unit_output
  value: 2.5
```

**New:**
```yaml
energy_model:
  type: per_unit
  value: 2.5
  unit: kWh/unit
  scaling_basis: <inferred_from_outputs>  # Must specify!
```

**Migration:**
1. Change type to `per_unit`
2. Add `unit: kWh/unit`
3. Infer scaling_basis from outputs (which output?)

---

## Complete Examples

### Example 1: Regolith Crushing (Input Scaling)

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
  scaling_basis: regolith_coarse_fraction  # Same as time model
  notes: "Bond work index for lunar regolith comminution"
```

**Calculation (100 kg):**
- Time: 100 kg / 10 kg/hr = 10 hours
- Energy: 100 kg × 0.3 kWh/kg = 30 kWh
- Average power: 30 kWh / 10 hr = 3 kW

### Example 2: Water Electrolysis (Multi-Output)

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
  scaling_basis: water  # Per kg water input
  notes: "15 kWh/kg water = 135 kWh/kg H2 (stoichiometric)"
```

**Calculation (100 kg water):**
- Time: 100 kg / 0.5 kg/hr = 200 hours
- Energy: 100 kg × 15 kWh/kg = 1500 kWh
- H2 produced: 11.1 kg
- Average power: 1500 kWh / 200 hr = 7.5 kW

### Example 3: Ceramic Firing (Fixed Energy)

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
- Average power: 1200 kWh / 85 hr = 14.1 kW

### Example 4: Motor Assembly (Output Scaling)

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
  unit: kWh/unit
  scaling_basis: motor_electric_small  # Per motor output
  notes: "Testing and tool energy per motor"
```

**Calculation (10 motors = 10 batches):**
- Time: 10 × (0.1 + 0.9) = 10 hours
- Energy: 10 unit × 0.2 kWh/unit = 2 kWh
- Average power: 2 kWh / 10 hr = 0.2 kW

### Example 5: Aluminum Smelting (MJ/kg)

```yaml
process_id: aluminum_smelting_hall_heroult_v0
process_type: continuous
inputs:
  - item_id: alumina_powder
    qty: 1.92
    unit: kg  # 1.92 kg alumina → 1 kg aluminum
outputs:
  - item_id: aluminum_pure
    qty: 1.0
    unit: kg
time_model:
  type: linear_rate
  rate: 50.0
  rate_unit: kg/hr  # Aluminum output rate
  scaling_basis: aluminum_pure
energy_model:
  type: per_unit
  value: 50.0  # 180 MJ = 50 kWh
  unit: kWh/kg
  scaling_basis: aluminum_pure  # Per kg aluminum output
  notes: "Hall-Heroult process: ~45-55 kWh/kg Al (~160-200 MJ/kg)"
```

**Alternative with MJ:**
```yaml
energy_model:
  type: per_unit
  value: 180.0
  unit: MJ/kg
  scaling_basis: aluminum_pure
```

**Both equivalent:** 180 MJ/kg = 50 kWh/kg

---

## Energy-Time Coupling Validation

### Power Sanity Checks

**Average power** = Total energy / Total time

**Validation rule:**
```python
def validate_power_reasonable(process, time_model, energy_model):
    """Check that implied power is reasonable."""

    # Calculate for standard inputs
    energy_kwh = calculate_energy(process, energy_model, inputs)
    time_hr = calculate_time(process, time_model, inputs)

    avg_power_kw = energy_kwh / time_hr

    # Sanity check
    if not (0.001 < avg_power_kw < 10000):  # 1W to 10MW
        warnings.warn(
            f"Process {process.id} has unusual power: {avg_power_kw:.2f} kW. "
            f"Check energy_model and time_model for consistency."
        )
```

**Example:**
```yaml
# Crushing: 30 kWh / 10 hr = 3 kW ✓ (reasonable for crusher)
# Electrolysis: 1500 kWh / 200 hr = 7.5 kW ✓ (reasonable for electrolyzer)
# Smelting: 50 kWh / 1 hr = 50 kW ✓ (reasonable for smelter)
```

**Catches errors:**
```yaml
# ERROR: 10000 kWh / 1 hr = 10000 kW (10 MW - probably wrong!)
```

---

## Validation Rules

### Schema Validation

1. **Required fields:**
   - `type` (per_unit or fixed_per_batch)
   - `value` (numeric)
   - `unit` (string)
   - For per_unit: `scaling_basis`

2. **Type consistency:**
   - fixed_per_batch should be used with batch processes (warning if not)
   - Unit should be energy unit or energy/scaling unit

3. **No invalid fields:**
   - `kWh_per_kg` ✗ (type, use per_unit)
   - `kWh_per_batch` ✗ (type, use fixed_per_batch)
   - `kWh_per_unit_output` ✗ (type, use per_unit)

### Semantic Validation

1. **scaling_basis exists (for per_unit):**
   ```python
   if energy_model.type == "per_unit":
       assert energy_model.scaling_basis in (inputs + outputs)
   ```

2. **Unit consistency:**
   ```python
   scaling_item = get_item(energy_model.scaling_basis)
   _, scaling_unit = parse_energy_unit(energy_model.unit)
   assert scaling_item.unit == scaling_unit or is_convertible(...)
   ```

3. **No scaling_basis for fixed_per_batch:**
   ```python
   if energy_model.type == "fixed_per_batch":
       assert energy_model.scaling_basis is None
   ```

### Calculation Validation

1. **Positive energy:**
   ```python
   assert energy_model.value > 0, "Energy must be positive"
   ```

2. **Reasonable power:**
   ```python
   avg_power = calculate_power(process)
   if not (0.001 < avg_power < 10000):
       warn("Unusual power calculated")
   ```

---

## Benefits

### 1. Unit Flexibility
- ✅ Supports kWh, MJ, BTU, any energy unit
- ✅ Supports any scaling unit (kg, unit, L)
- ✅ Natural rates (kWh/unit, MJ/kg)

### 2. Clear Semantics
- ✅ scaling_basis eliminates "per kg of what?" ambiguity
- ✅ Explicit input vs output scaling
- ✅ Fixed vs scaling energy clear

### 3. Consistency with Time Model
- ✅ Same structure (type, value, unit, scaling_basis)
- ✅ Same validation approach
- ✅ Easy to learn (parallel design)

### 4. Validation Power
- ✅ Energy-time coupling checks
- ✅ Reasonable power validation
- ✅ Unit conversion validation

### 5. Migration Path
- ✅ Clear mapping from old schema
- ✅ Automated conversion possible
- ✅ Backward compatibility path

---

## Next Steps

1. **Implement in parallel with time_model** (ADR-012)
2. **Create unified validation** for time + energy
3. **Power sanity checks** in indexer
4. **Migration script** for existing processes
5. **Test cases** from examples

---

## Cross-References

**Related documents:**
- time-model-schema-redesign.md - Parallel time model changes
- batch-vs-continuous-process-types.md - Process type alignment
- validation-strategy.md - Validation rules (TODO)

**Related ADRs:**
- ADR-012: Process Types and Time Model Redesign
- ADR-014: Energy Model Redesign (this document feeds into it)
