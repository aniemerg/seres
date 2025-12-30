# Time Model Schema Redesign

**Status:** In Progress
**Date:** 2024-12-28
**Purpose:** Propose new time_model schema with scaling basis and flexible units

## Overview

The current time_model schema has fundamental limitations:
1. **Hard-coded units** - `hr_per_kg` and `rate_kg_per_hr` only work for kg-based processes
2. **No scaling basis** - unclear which input/output drives the rate when multiple exist
3. **Unit mismatches** - can't handle L (volume), unit (count), or other units
4. **Type confusion** - `fixed_time` vs batch semantics unclear

This document proposes a **new time_model schema** that:
- Supports **any unit** (kg, L, unit, count, etc.)
- **Explicitly specifies scaling basis** (which input/output drives time)
- Aligns with **batch vs continuous process types**
- Enables **validation and calculation**
- Provides **clear migration path**

---

## Current Schema Problems

### Problem 1: Hard-Coded Units

**Current (from kbtool/models.py):**
```python
class TimeModel:
    type: str  # linear_rate, fixed_time, boundary
    hr_per_kg: Optional[float]
    rate_kg_per_hr: Optional[float]
    setup_hr: Optional[float]
    hr_per_batch: Optional[float]
```

**Issues:**
- Only works for **kg-based** processes
- Can't handle:
  - Volume inputs (10 L water)
  - Count inputs (50 units motors)
  - Other units (100 m wire, 5 kWh energy)

**Example failure:**
```yaml
# Pump housing machining
inputs:
  - item_id: machined_part_raw
    qty: 25.0
    unit: kg  # ✓ kg works
  - item_id: cutting_fluid
    qty: 1.8
    unit: L   # ✗ Can't use rate_kg_per_hr!

time_model:
  type: linear_rate
  rate_kg_per_hr: 12.0  # Based on what? kg input or L input?
```

### Problem 2: No Scaling Basis

**Question:** When process has multiple inputs, which drives the time?

**Example:**
```yaml
# Metal forming
inputs:
  - item_id: steel_sheet
    qty: 10.0
    unit: kg
  - item_id: lubricant
    qty: 0.5
    unit: L

time_model:
  rate_kg_per_hr: 5.0  # Is this for steel (10 kg) or lubricant (0.5 L)?
```

**Current state:** **Undefined!** User must guess or infer from context.

### Problem 3: Count-Based Rates

**User feedback:** Count-based rates should use **natural format** (10 unit/hr).

**Current schema can't represent:**
```yaml
# Motor assembly
time_model:
  rate_unit_per_hr: 10.0  # ✗ Not a valid field!
  # Can only use rate_kg_per_hr
```

### Problem 4: Type Ambiguity

**Current:**
- `type: fixed_time` - what does this mean?
- `type: linear_rate` - always kg-based?
- Relationship to batch vs continuous unclear

**Solution:** Align with explicit `process_type` (see batch-vs-continuous-process-types.md).

---

## Proposed New Schema

### Core Principles

1. **Explicit process_type** - batch or continuous (from batch-vs-continuous document)
2. **Flexible units** - support any unit type
3. **Required scaling_basis** - specify which input/output drives time
4. **Natural rates** - count-based uses natural format (10 unit/hr, not 0.1 hr/unit)
5. **Structured rate specification** - clear numerator and denominator

### Schema V2: Structured Approach

```python
class TimeModelV2:
    """New time model schema with flexible units and scaling basis."""

    # For continuous processes
    class ContinuousTimeModel:
        type: Literal["linear_rate"]
        rate: float  # Numeric value
        rate_unit: str  # Unit string (e.g., "kg/hr", "unit/hr", "L/hr")
        scaling_basis: str  # Item ID that drives the rate
        notes: Optional[str]

    # For batch processes
    class BatchTimeModel:
        type: Literal["batch"]
        setup_hr: Optional[float] = 0.0  # Default 0 if not specified
        hr_per_batch: float  # Time per batch
        notes: Optional[str]
        # No scaling_basis - batch size from outputs
```

### Continuous Process Example

```yaml
# Regolith crushing (kg-based)
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
  scaling_basis: regolith_coarse_fraction  # Input that drives time
```

**Calculation:**
- 100 kg input / 10 kg/hr = 10 hours

```yaml
# Motor assembly (count-based)
process_type: continuous
inputs:
  - item_id: motor_housing
    qty: 10
    unit: unit
outputs:
  - item_id: assembled_motor
    qty: 10
    unit: unit
time_model:
  type: linear_rate
  rate: 12.0  # Natural rate format
  rate_unit: unit/hr  # 12 units per hour
  scaling_basis: motor_housing  # Input that drives time
```

**Calculation:**
- 100 units / 12 unit/hr = 8.33 hours

```yaml
# Pump housing machining (count-based, ignoring consumables)
process_type: continuous
inputs:
  - item_id: machined_part_raw
    qty: 25.0
    unit: unit  # ← Changed to count
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
  rate_unit: unit/hr  # Count-based rate
  scaling_basis: machined_part_raw  # ← Explicit!
```

**Calculation:**
- 25 units / 12 unit/hr = 2.08 hours
- Cutting fluid is consumable, doesn't affect time

### Batch Process Example

```yaml
# Motor final assembly (batch)
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
    qty: 1.0  # ← 1 batch = 1 motor
    unit: unit
time_model:
  type: batch
  setup_hr: 0.1  # Tool setup
  hr_per_batch: 0.9  # Assembly time
  # No scaling_basis - batch size from outputs
```

**Calculation:**
- 1 motor = 1 batch = 0.1 + 0.9 = 1.0 hour
- 10 motors = 10 batches = 10 × 1.0 = 10 hours

---

## Rate Unit Specification

### Supported Units

**Mass:** kg, g, ton
**Volume:** L, mL, m³
**Count:** unit, each, count
**Length:** m, mm, km
**Area:** m²
**Energy:** kWh, MJ
**Custom:** Any unit defined in items

### Rate Unit Format

**Pattern:** `<numerator_unit>/<denominator_unit>`

**Examples:**
- `kg/hr` - Mass per hour
- `unit/hr` - Count per hour (natural format)
- `L/min` - Volume per minute
- `m/hr` - Length per hour
- `kWh/day` - Energy per day

**Parsing:**
```python
def parse_rate_unit(rate_unit: str) -> tuple[str, str]:
    """Parse rate unit into numerator and denominator."""
    numerator, denominator = rate_unit.split('/')
    return (numerator.strip(), denominator.strip())

# Examples
parse_rate_unit("kg/hr") → ("kg", "hr")
parse_rate_unit("unit/hr") → ("unit", "hr")
parse_rate_unit("L/min") → ("L", "min")
```

### Time Unit Normalization

**All rates normalized to hours internally:**
```python
TIME_UNIT_TO_HOURS = {
    "hr": 1.0,
    "hour": 1.0,
    "min": 1/60,
    "minute": 1/60,
    "sec": 1/3600,
    "second": 1/3600,
    "day": 24.0,
}

def normalize_to_hours(rate: float, rate_unit: str) -> float:
    """Convert rate to hours."""
    numerator, denominator = parse_rate_unit(rate_unit)
    time_factor = TIME_UNIT_TO_HOURS[denominator]
    return rate * time_factor
```

**Examples:**
- `rate: 10.0, rate_unit: kg/min` → 10 kg/min × 60 min/hr = **600 kg/hr**
- `rate: 5.0, rate_unit: unit/hr` → **5 unit/hr** (already in hours)

---

## Scaling Basis Specification

### Required Field

**User directive:** "scaling basis should just be specified."

**Rule:** `scaling_basis` is **required** for continuous processes.

```yaml
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: primary_input_item_id  # ← REQUIRED
```

### Scaling Basis Options

**Option 1: Input item** (most common)
```yaml
scaling_basis: regolith_coarse_fraction  # Input item ID
```

**Option 2: Output item** (less common)
```yaml
scaling_basis: regolith_powder  # Output item ID
```

**Option 3: Specific input when multiple**
```yaml
inputs:
  - item_id: steel_sheet
    qty: 10.0
    unit: kg
  - item_id: lubricant
    qty: 0.5
    unit: L
time_model:
  scaling_basis: steel_sheet  # ← Explicitly steel, not lubricant
```

### Validation Rules

1. **scaling_basis must exist** - refers to actual input or output item_id
2. **Unit consistency** - scaling_basis unit must match rate_unit numerator
3. **Single reference** - can't specify multiple scaling bases

**Example validation:**
```yaml
# VALID
inputs:
  - item_id: water
    qty: 10.0
    unit: kg
time_model:
  rate: 5.0
  rate_unit: kg/hr
  scaling_basis: water  # ✓ Exists, unit matches (kg)

# INVALID - unit mismatch
inputs:
  - item_id: water
    qty: 10.0
    unit: L  # ← Liters!
time_model:
  rate: 5.0
  rate_unit: kg/hr  # ← kg/hr rate
  scaling_basis: water  # ✗ Unit mismatch (L vs kg)
```

**Error:** "scaling_basis 'water' has unit 'L' but rate_unit is 'kg/hr'. Units must match or be convertible."

### Implicit Unit Conversion

**User directive:** "Units should be implicitly converted where possible."

**If conversion is known:**
```yaml
inputs:
  - item_id: water
    qty: 10.0
    unit: L
time_model:
  rate: 5.0
  rate_unit: kg/hr
  scaling_basis: water  # L input, kg/hr rate
```

**Validation:**
- Check if L → kg conversion exists for water
- Water density: 1 kg/L
- 10 L × 1 kg/L = 10 kg
- ✓ Calculation possible

**If conversion unknown:**
```yaml
inputs:
  - item_id: mystery_fluid
    qty: 10.0
    unit: L
time_model:
  rate: 5.0
  rate_unit: kg/hr
  scaling_basis: mystery_fluid
```

**Error:** "Cannot convert scaling_basis 'mystery_fluid' from L to kg. Item 'mystery_fluid' missing density_kg_per_L."

---

## Migration from Current Schema

### Mapping Old → New

#### Continuous Process (rate_kg_per_hr)

**Old:**
```yaml
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0
```

**New:**
```yaml
time_model:
  type: linear_rate
  rate: 10.0
  rate_unit: kg/hr
  scaling_basis: <inferred_from_inputs>  # Must add!
```

**Migration strategy:**
1. Convert `rate_kg_per_hr` → `rate` + `rate_unit: kg/hr`
2. Infer `scaling_basis` from inputs (if only one kg input, use it)
3. Warn if scaling_basis ambiguous (multiple kg inputs)

#### Continuous Process (hr_per_kg)

**Old:**
```yaml
time_model:
  type: linear_rate
  hr_per_kg: 0.1  # 0.1 hr/kg = 10 kg/hr
```

**New:**
```yaml
time_model:
  type: linear_rate
  rate: 10.0  # Inverted
  rate_unit: kg/hr
  scaling_basis: <inferred_from_inputs>
```

**Migration strategy:**
1. Invert: `rate = 1 / hr_per_kg`
2. Set `rate_unit: kg/hr`
3. Infer `scaling_basis`

#### Batch Process (fixed_time)

**Old:**
```yaml
time_model:
  type: fixed_time
  hr_per_batch: 1.0
```

**New:**
```yaml
time_model:
  type: batch
  setup_hr: 0.0  # Default
  hr_per_batch: 1.0
```

**Migration strategy:**
1. Change `type: fixed_time` → `type: batch`
2. Add `setup_hr: 0.0` if not present
3. Keep `hr_per_batch` unchanged

#### Batch Process with Setup

**Old:**
```yaml
time_model:
  type: linear_rate  # ← Wrong type
  hr_per_kg: 0.5
  setup_hr: 0.2  # ← Suggests batch!
```

**New - Option 1 (batch):**
```yaml
process_type: batch
time_model:
  type: batch
  setup_hr: 0.2
  hr_per_batch: 2.5  # Assuming 5 kg batch: 5 kg × 0.5 hr/kg
```

**New - Option 2 (split):**
```yaml
# Setup process
process_id: ceramic_press_startup_v0
process_type: batch
time_model:
  type: batch
  hr_per_batch: 0.2

# Main process (continuous)
process_id: ceramic_forming_v0
process_type: continuous
time_model:
  type: linear_rate
  rate: 2.0  # 1/0.5
  rate_unit: kg/hr
  scaling_basis: ceramic_powder_mixture
```

---

## Complete Examples

### Example 1: Simple Crushing (kg-based)

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
energy_model:
  type: per_unit
  value: 0.3
  unit: kWh/kg
  scaling_basis: regolith_coarse_fraction
```

**Calculation (100 kg input):**
- Time: 100 kg / 10 kg/hr = 10 hours
- Energy: 100 kg × 0.3 kWh/kg = 30 kWh

### Example 2: Motor Assembly (count-based batch)

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
  - item_id: motor_shaft_steel
    qty: 1.0
    unit: kg
  - item_id: bearing_set_small
    qty: 0.5
    unit: kg
  - item_id: motor_housing_steel
    qty: 3.0
    unit: kg
outputs:
  - item_id: motor_electric_small
    qty: 1.0  # 1 batch = 1 motor
    unit: unit
time_model:
  type: batch
  setup_hr: 0.1
  hr_per_batch: 0.9
  notes: "Assembly of 1 motor per batch"
energy_model:
  type: fixed_per_batch
  value: 0.2
  unit: kWh
  notes: "Fixed energy per motor assembled"
```

**Calculation (10 motors needed):**
- Batches: 10 / 1 = 10 batches
- Time: 10 × (0.1 + 0.9) = 10 hours
- Energy: 10 × 0.2 = 2 kWh

### Example 3: Water Electrolysis (kg-based continuous)

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
  rate: 0.5  # 0.5 kg water per hour
  rate_unit: kg/hr
  scaling_basis: water
  notes: "Continuous electrolysis"
energy_model:
  type: per_unit
  value: 15.0  # Per kg of water
  unit: kWh/kg
  scaling_basis: water
  notes: "~50 kWh per kg H2, ~4-5 kWh per kg water"
```

**Calculation (100 kg water):**
- Time: 100 kg / 0.5 kg/hr = 200 hours
- Energy: 100 kg × 15.0 kWh/kg = 1500 kWh
- H2 output: 100 × 0.111 = 11.1 kg
- O2 output: 100 × 0.889 = 88.9 kg

### Example 4: Pump Housing Machining (count-based)

```yaml
process_id: pump_housing_machining_v0
process_type: continuous
inputs:
  - item_id: machined_part_raw
    qty: 25.0
    unit: unit  # Count-based
  - item_id: cutting_fluid
    qty: 1.8
    unit: L  # Consumable
outputs:
  - item_id: pump_housing_machined
    qty: 25.0
    unit: unit
time_model:
  type: linear_rate
  rate: 12.0  # Natural rate: 12 units per hour
  rate_unit: unit/hr
  scaling_basis: machined_part_raw  # Parts, not fluid
  notes: "Machining rate based on part count, not fluid consumption"
energy_model:
  type: per_unit
  value: 3.0
  unit: kWh/unit  # Per part
  scaling_basis: machined_part_raw
```

**Calculation (25 parts):**
- Time: 25 unit / 12 unit/hr = 2.08 hours
- Energy: 25 unit × 3.0 kWh/unit = 75 kWh
- Cutting fluid: Consumed at fixed ratio (1.8 L / 25 parts)

### Example 5: Ceramic Firing (batch with variable load)

```yaml
process_id: ceramic_firing_v0
process_type: batch
inputs:
  - item_id: green_ceramic_parts
    qty: 10.0  # Standard batch size
    unit: kg
outputs:
  - item_id: fired_ceramic_parts
    qty: 9.5  # 5% shrinkage
    unit: kg
time_model:
  type: batch
  setup_hr: 0.5  # Load kiln
  hr_per_batch: 8.0  # Firing time (independent of load mass)
  notes: "Fixed firing time regardless of load within 5-15 kg range"
energy_model:
  type: fixed_per_batch
  value: 120.0
  unit: kWh
  notes: "Kiln energy per firing cycle"
```

**Calculation (100 kg green parts):**
- Batches: 100 kg / 10 kg per batch = 10 batches
- Time: 10 × (0.5 + 8.0) = 85 hours
- Energy: 10 × 120 = 1200 kWh

---

## Validation Rules

### Schema Validation

1. **Required fields:**
   - `type` (linear_rate or batch)
   - For linear_rate: `rate`, `rate_unit`, `scaling_basis`
   - For batch: `hr_per_batch`

2. **Type consistency:**
   - Continuous process → type: linear_rate
   - Batch process → type: batch

3. **No invalid fields:**
   - `rate_kg_per_hr` ✗ (deprecated)
   - `hr_per_kg` ✗ (deprecated)
   - `fixed_time` ✗ (use batch)

### Semantic Validation

1. **scaling_basis exists:**
   ```python
   assert time_model.scaling_basis in (inputs + outputs)
   ```

2. **Unit consistency:**
   ```python
   scaling_item = get_item(time_model.scaling_basis)
   rate_numerator = parse_rate_unit(time_model.rate_unit)[0]
   assert scaling_item.unit == rate_numerator or is_convertible(scaling_item.unit, rate_numerator)
   ```

3. **setup_hr only in batch:**
   ```python
   if time_model.type == "linear_rate":
       assert time_model.setup_hr is None, "setup_hr not allowed in continuous processes"
   ```

### Calculation Validation

1. **Can calculate duration:**
   ```python
   def validate_calculable(process, time_model):
       scaling_item = process.get_input_or_output(time_model.scaling_basis)
       if scaling_item is None:
           raise ValidationError(f"scaling_basis '{time_model.scaling_basis}' not found in inputs or outputs")

       # Check unit conversion possible
       if not can_convert(scaling_item.unit, rate_numerator):
           raise ValidationError(f"Cannot convert {scaling_item.unit} to {rate_numerator}")
   ```

---

## Benefits

### 1. Unit Flexibility
- ✅ Supports kg, L, unit, count, any unit
- ✅ Natural count-based rates (12 unit/hr)
- ✅ Explicit rate units

### 2. Clear Semantics
- ✅ scaling_basis eliminates ambiguity
- ✅ Explicit which input/output drives time
- ✅ Validation catches errors

### 3. Calculation Reliability
- ✅ Unambiguous calculations
- ✅ Unit conversion when possible
- ✅ Errors when conversion impossible

### 4. Batch Alignment
- ✅ Consistent with process_type
- ✅ Batch semantics clear
- ✅ No more fixed_time ambiguity

### 5. Migration Path
- ✅ Clear mapping from old schema
- ✅ Automated conversion possible
- ✅ Validation catches issues

---

## Next Steps

1. **Update kbtool/models.py** with new TimeModel schema
2. **Implement validation** in indexer
3. **Create migration script** to convert existing processes
4. **Update documentation** with new schema
5. **Create test cases** from examples in this document
6. **Parallel: Energy model redesign** (ADR-014)

---

## Cross-References

**Related documents:**
- batch-vs-continuous-process-types.md - Process type definitions
- feedback-synthesis-and-next-steps.md - Overall redesign context
- energy-model-redesign.md - Parallel energy model changes (TODO)
- validation-strategy.md - Validation rules (TODO)

**Related ADRs:**
- ADR-012: Process Types and Time Model Redesign (this document feeds into it)
- ADR-014: Energy Model Redesign (parallel effort)
