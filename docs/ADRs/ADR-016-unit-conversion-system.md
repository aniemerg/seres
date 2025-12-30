# ADR-016: Unit Conversion and Type System

**Status:** Proposed
**Date:** 2024-12-28
**Decision Makers:** Project team
**Related ADRs:** ADR-012 (Process Types), ADR-014 (Energy Model), ADR-013 (Recipe Overrides)

## Context

The knowledge base uses **9 different unit types** across thousands of quantity specifications. With the new flexible rate units introduced in ADR-012 (kg/hr, L/hr, unit/hr) and ADR-014 (kWh/kg, MJ/unit), we need a comprehensive unit conversion system to enable:

1. **Implicit conversions** - Convert between units automatically where possible
2. **Rate calculations** - Parse and apply compound units (kg/hr, L/min)
3. **Time normalization** - Convert all time units to hours internally
4. **Validation** - Verify conversions are possible before use
5. **Cross-unit processing** - Handle inputs in kg when rate is in L/hr, etc.

### Current State

**Existing UnitConverter** (`base_builder/unit_converter.py`) supports:
- Direct conversions: kg ↔ g, m³ ↔ L, count ↔ unit ↔ each
- Mass ↔ Volume: via material density (water: 10 L → 10 kg)
- Count ↔ Mass: via item mass_kg field (motor: 1 unit → 12 kg)

**What's missing:**
- Compound unit parsing (kg/hr, kWh/kg)
- Time unit normalization (min → hr, day → hr)
- Rate conversions across units
- Validation of convertibility
- Integration with time_model and energy_model

### Unit Census

From survey of 5000+ specifications:

| Unit | Count | Category | Notes |
|------|-------|----------|-------|
| kg | 2967 | Mass | Dominant unit |
| unit | 1158 | Count | Generic countable |
| hr | 799 | Time | Time model, resources |
| each | 93 | Count | Synonym for unit |
| kWh | 22 | Energy | Energy consumption |
| count | 12 | Count | Synonym for unit |
| set | 8 | Count | Collections |
| L | 8 | Volume | Liquids |
| kit | 3 | Count | Pre-packaged |

### User Requirements

From `design/time-model-hierarchy-feedback.txt`:
- "known conversions (L of water to volume, kg to tons) should be handled implicitly without KB having to explicitly model it"
- "implicit conversion requests should be possible, like inputs being in kg, outputs in count"

## Decision

We will implement a **comprehensive unit conversion system** with the following components:

### 1. Unit Categories and Standard Units

Define unit categories with standard (canonical) units for normalization:

| Category | Standard Unit | Other Units |
|----------|---------------|-------------|
| **Mass** | kg | g, tonne, lb |
| **Volume** | m³ | L, mL, m3 |
| **Count** | unit | each, count, set, kit |
| **Time** | hr | min, s, day |
| **Energy** | kWh | MJ, GJ, J, BTU |
| **Length** | m | cm, mm, km |

**Normalization rule:** All calculations performed in standard units, conversions applied at input/output.

### 2. Compound Unit Parsing

**Format:** `<numerator_unit>/<denominator_unit>`

**Examples:**
- `kg/hr` → Rate: mass per time
- `L/min` → Rate: volume per time → normalized to L/hr
- `unit/hr` → Rate: count per time
- `kWh/kg` → Intensity: energy per mass
- `MJ/unit` → Intensity: energy per count

**Parser specification:**
```python
def parse_compound_unit(unit_string: str) -> tuple[str, str]:
    """
    Parse compound unit string into numerator and denominator.

    Args:
        unit_string: Compound unit (e.g., "kg/hr", "L/min", "kWh/kg")

    Returns:
        (numerator_unit, denominator_unit)

    Examples:
        "kg/hr" → ("kg", "hr")
        "L/min" → ("L", "min")
        "kWh/kg" → ("kWh", "kg")
        "unit/hr" → ("unit", "hr")
    """
    if "/" not in unit_string:
        raise ValueError(f"Not a compound unit: {unit_string}")

    parts = unit_string.split("/")
    if len(parts) != 2:
        raise ValueError(f"Invalid compound unit format: {unit_string}")

    numerator, denominator = parts[0].strip(), parts[1].strip()

    # Validate both parts are known units
    if not is_valid_unit(numerator):
        raise ValueError(f"Unknown numerator unit: {numerator}")
    if not is_valid_unit(denominator):
        raise ValueError(f"Unknown denominator unit: {denominator}")

    return (numerator, denominator)
```

### 3. Time Unit Normalization

**Rule:** All time units normalized to **hours** internally.

**Supported conversions:**
```yaml
min → hr: factor 1/60 (0.01667)
s → hr: factor 1/3600 (0.000278)
day → hr: factor 24
hr → hr: factor 1 (identity)
```

**Application to compound units:**
```python
# Input: "kg/min"
# Step 1: Parse → ("kg", "min")
# Step 2: Normalize denominator → ("kg", "hr") with factor 60
# Result: 5 kg/min = 300 kg/hr

# Input: "L/day"
# Step 1: Parse → ("L", "day")
# Step 2: Normalize denominator → ("L", "hr") with factor 1/24
# Result: 240 L/day = 10 L/hr
```

**Note:** Energy compound units (kWh/kg) keep denominator as-is (no time normalization for denominators other than time).

### 4. Implicit Conversion Rules

**Conversion strategies:**

#### Strategy 1: Direct Conversion
Same category, different units (e.g., kg → g, L → mL)
```python
10 kg → 10000 g  # Direct factor: 1000
5 L → 5000 mL    # Direct factor: 1000
```

#### Strategy 2: Mass ↔ Volume via Density
Requires material density from KB
```python
# Water (density: 1000 kg/m³)
10 L → 10 kg     # 10 L × (1 m³/1000 L) × 1000 kg/m³ = 10 kg

# Aluminum (density: 2700 kg/m³)
5 kg → 0.00185 m³  # 5 kg / 2700 kg/m³
```

#### Strategy 3: Count ↔ Mass via Item Definition
Requires item `mass_kg` field
```python
# motor_electric_small (mass_kg: 12)
1 unit → 12 kg
5 units → 60 kg

# battery_pack (mass_kg: 45)
90 kg → 2 units
```

#### Strategy 4: Count ↔ Volume via Item Definition
Requires item `volume_m3` field (if exists)
```python
# container_tank (volume_m3: 2.0)
1 unit → 2.0 m³
10 m³ → 5 units
```

#### Strategy 5: Count Synonym Normalization
All count units are equivalent
```python
1 unit = 1 each = 1 count = 1 set = 1 kit
```

### 5. Conversion Validation

**Before allowing a process/recipe to use unit conversions, validate:**

#### Validation 1: Conversion Exists
```python
def can_convert(from_unit: str, to_unit: str, item_id: Optional[str] = None) -> bool:
    """
    Check if conversion is possible.

    Returns:
        True if conversion exists, False otherwise
    """
    # Try direct conversion
    if has_conversion_factor(from_unit, to_unit):
        return True

    # Try mass <-> volume (requires item_id for density lookup)
    if item_id and is_mass_volume_pair(from_unit, to_unit):
        return has_material_density(item_id)

    # Try count <-> mass/volume (requires item_id)
    if item_id and is_count_conversion(from_unit, to_unit):
        return has_item_mass_or_volume(item_id)

    return False
```

#### Validation 2: Scaling Basis Convertibility
For time_model with scaling_basis, validate conversion is possible:
```python
def validate_scaling_basis_conversion(process: Process) -> list[ValidationError]:
    """Validate that scaling_basis can be converted to rate_unit numerator."""
    errors = []

    if process.time_model.type != "linear_rate":
        return errors

    # Get scaling_basis item
    scaling_item = next(
        (i for i in process.inputs + process.outputs
         if i.item_id == process.time_model.scaling_basis),
        None
    )

    if not scaling_item:
        # Already caught by other validation
        return errors

    # Parse rate_unit to get numerator
    rate_numerator, _ = parse_compound_unit(process.time_model.rate_unit)

    # Check if conversion possible
    if scaling_item.unit != rate_numerator:
        if not can_convert(scaling_item.unit, rate_numerator, scaling_item.item_id):
            errors.append(ValidationError(
                f"Process '{process.id}' scaling_basis unit '{scaling_item.unit}' "
                f"cannot be converted to rate_unit numerator '{rate_numerator}'. "
                f"Add density (for mass<->volume) or mass_kg (for count<->mass) to item."
            ))

    return errors
```

### 6. Rate Conversion Algorithm

**Purpose:** Convert quantity from scaling_basis unit to rate_unit numerator for time calculation.

```python
def convert_for_time_calculation(
    quantity: float,
    from_unit: str,
    to_unit: str,
    item_id: str,
    converter: UnitConverter
) -> float:
    """
    Convert quantity for time calculation.

    Args:
        quantity: Amount to convert
        from_unit: Scaling basis item unit
        to_unit: Rate unit numerator
        item_id: Item identifier for context
        converter: UnitConverter instance

    Returns:
        Converted quantity

    Raises:
        ValueError: If conversion not possible

    Example:
        # Input: 10 L of water, rate is 5 kg/hr
        convert_for_time_calculation(10, "L", "kg", "water", converter)
        # → 10 kg (water density 1000 kg/m³)

        # Input: 5 units of motor, rate is 60 kg/hr
        convert_for_time_calculation(5, "unit", "kg", "motor_electric_small", converter)
        # → 60 kg (motor mass_kg: 12)
    """
    if from_unit == to_unit:
        return quantity

    result = converter.convert(quantity, from_unit, to_unit, item_id)

    if result is None:
        raise ValueError(
            f"Cannot convert {quantity} {from_unit} to {to_unit} for item '{item_id}'. "
            f"Check material density or item mass_kg definition."
        )

    return result
```

### 7. Integration with Time and Energy Models

#### Time Model Integration

```python
def calculate_duration_with_conversion(
    process: Process,
    inputs: dict[str, QuantitySpec],
    converter: UnitConverter
) -> float:
    """
    Calculate duration using time_model with unit conversion.

    Example:
        Process has rate: 5 kg/hr, scaling_basis: water
        Input: 10 L of water

        Step 1: Convert 10 L → 10 kg (water density)
        Step 2: Calculate time: 10 kg / 5 kg/hr = 2 hr
    """
    if process.time_model.type == "linear_rate":
        # Get scaling basis item
        scaling_item = inputs[process.time_model.scaling_basis]

        # Parse rate unit
        rate_numerator, rate_denominator = parse_compound_unit(
            process.time_model.rate_unit
        )

        # Normalize denominator to hours
        normalized_rate = normalize_rate_to_hours(
            process.time_model.rate,
            rate_denominator
        )

        # Convert quantity to match rate numerator
        converted_qty = convert_for_time_calculation(
            scaling_item.qty,
            scaling_item.unit,
            rate_numerator,
            scaling_item.item_id,
            converter
        )

        # Calculate duration
        duration_hr = converted_qty / normalized_rate

        return duration_hr

    elif process.time_model.type == "batch":
        # Batch doesn't need conversion
        return process.time_model.hr_per_batch
```

#### Energy Model Integration

```python
def calculate_energy_with_conversion(
    process: Process,
    inputs: dict[str, QuantitySpec],
    converter: UnitConverter
) -> float:
    """
    Calculate energy using energy_model with unit conversion.

    Example:
        Process has value: 50 kWh/kg, scaling_basis: water
        Input: 10 L of water

        Step 1: Convert 10 L → 10 kg (water density)
        Step 2: Calculate energy: 10 kg × 50 kWh/kg = 500 kWh
    """
    if process.energy_model.type == "per_unit":
        # Get scaling basis item
        scaling_item = inputs[process.energy_model.scaling_basis]

        # Parse unit (kWh/kg → ("kWh", "kg"))
        energy_unit, per_unit = parse_compound_unit(process.energy_model.unit)

        # Convert quantity to match per_unit
        converted_qty = convert_for_time_calculation(
            scaling_item.qty,
            scaling_item.unit,
            per_unit,
            scaling_item.item_id,
            converter
        )

        # Calculate energy
        energy = converted_qty * process.energy_model.value

        return energy

    elif process.energy_model.type == "fixed_per_batch":
        # Fixed energy doesn't need conversion
        return process.energy_model.value
```

### 8. Conversion Factor Storage

**Location:** KB conversion factors in `kb/conversions/`

**Format:**
```yaml
# kb/conversions/unit_conversions_v0.yaml
id: unit_conversions_v0
conversions:
  # Mass conversions
  - from_unit: kg
    to_unit: g
    factor: 1000

  - from_unit: kg
    to_unit: tonne
    factor: 0.001

  # Volume conversions
  - from_unit: L
    to_unit: mL
    factor: 1000

  - from_unit: m3
    to_unit: L
    factor: 1000

  # Time conversions
  - from_unit: hr
    to_unit: min
    factor: 60

  - from_unit: hr
    to_unit: s
    factor: 3600

  - from_unit: day
    to_unit: hr
    factor: 24

  # Energy conversions
  - from_unit: kWh
    to_unit: MJ
    factor: 3.6

  - from_unit: MJ
    to_unit: GJ
    factor: 0.001

  # Count synonyms (1:1)
  - from_unit: unit
    to_unit: each
    factor: 1.0

  - from_unit: unit
    to_unit: count
    factor: 1.0
```

**Bidirectional:** If factor exists for A → B, reverse conversion B → A uses 1/factor.

## Consequences

### Positive

1. **Flexible processing** - Can handle inputs in any unit with time_model in any compatible unit
2. **Implicit conversions** - Users don't need to manually convert, system handles it
3. **Validation power** - Can detect impossible conversions at validation time, not runtime
4. **Clear semantics** - Compound units (kg/hr, L/min) are explicit and unambiguous
5. **Extensible** - Easy to add new units and conversions
6. **Maintains precision** - Conversions use exact factors, no approximation
7. **Material-aware** - Density and mass lookups use actual material properties

### Negative

1. **Dependency on KB data** - Conversions fail if density or mass_kg missing
2. **Complexity** - More moving parts than fixed-unit system
3. **Performance** - Conversion lookups add overhead (mitigated by caching)
4. **Validation burden** - Must validate convertibility for all processes
5. **Error messages** - Need clear messages when conversion fails

### Neutral

1. **Migration impact** - Existing UnitConverter needs extension, not replacement
2. **Testing needs** - Comprehensive unit tests for all conversion paths
3. **Documentation** - Users need guide on when conversions happen

## Implementation Plan

### Phase 1: Extend UnitConverter

1. **Add compound unit parsing**
   - `parse_compound_unit(unit_string)` function
   - Unit validation

2. **Add time normalization**
   - `normalize_rate_to_hours(rate, time_unit)` function
   - Support min, s, day → hr

3. **Add validation helpers**
   - `can_convert(from, to, item_id)` function
   - `validate_scaling_basis_conversion(process)` function

### Phase 2: Integration with Models

1. **Update time calculation**
   - Integrate conversion in `calculate_duration()`
   - Use `convert_for_time_calculation()` for scaling_basis

2. **Update energy calculation**
   - Integrate conversion in `calculate_energy()`
   - Handle kWh/kg, MJ/unit, etc.

### Phase 3: Validation Integration

1. **Indexer validation**
   - Check all time_model scaling_basis are convertible
   - Check all energy_model scaling_basis are convertible
   - Generate errors for missing density/mass_kg

2. **Runtime validation**
   - Simulation validates conversion possible before execution
   - Clear error messages on conversion failure

### Phase 4: KB Enhancement

1. **Add missing density data**
   - Survey materials without density
   - Add density to material definitions

2. **Add missing mass_kg data**
   - Survey items without mass_kg
   - Add mass_kg to item definitions

3. **Add conversion factors**
   - Complete unit_conversions_v0.yaml
   - Add common engineering units

## Examples

### Example 1: Water Processing (Volume → Mass)

```yaml
# Process
id: water_distillation_v0
process_type: continuous

inputs:
  - item_id: water
    qty: 1.0
    unit: L  # ← Volume

outputs:
  - item_id: distilled_water
    qty: 0.9
    unit: L

time_model:
  type: linear_rate
  rate: 5.0
  rate_unit: kg/hr  # ← Mass rate!
  scaling_basis: water
```

**Calculation for 100 L input:**
1. Parse rate_unit: "kg/hr" → ("kg", "hr")
2. Normalize: rate_denominator "hr" → factor 1 (already hours)
3. Convert quantity: 100 L → 100 kg (water density 1000 kg/m³)
4. Calculate time: 100 kg / 5.0 kg/hr = **20 hours**

### Example 2: Motor Assembly (Count → Mass)

```yaml
# Process
id: motor_assembly_v0
process_type: continuous

inputs:
  - item_id: motor_housing
    qty: 10.0
    unit: unit  # ← Count

outputs:
  - item_id: motor_complete
    qty: 10.0
    unit: unit

time_model:
  type: linear_rate
  rate: 60.0
  rate_unit: kg/hr  # ← Mass rate!
  scaling_basis: motor_housing
```

**Requires:** Item `motor_housing` has `mass_kg: 12`

**Calculation for 10 units:**
1. Parse rate_unit: "kg/hr" → ("kg", "hr")
2. Convert quantity: 10 unit → 120 kg (motor_housing.mass_kg = 12)
3. Calculate time: 120 kg / 60.0 kg/hr = **2 hours**

### Example 3: Battery Assembly (Count Native)

```yaml
# Process
id: battery_assembly_v0
process_type: continuous

inputs:
  - item_id: battery_cells
    qty: 100.0
    unit: each

outputs:
  - item_id: battery_pack
    qty: 1.0
    unit: unit

time_model:
  type: linear_rate
  rate: 12.0
  rate_unit: unit/hr  # ← Count rate, matches output
  scaling_basis: battery_pack
```

**Calculation for 10 battery packs:**
1. Parse rate_unit: "unit/hr" → ("unit", "hr")
2. Convert quantity: 10 unit → 10 unit (no conversion, count = count)
3. Calculate time: 10 unit / 12.0 unit/hr = **0.83 hours**

### Example 4: Energy Calculation (Volume → Mass)

```yaml
# Process
id: water_electrolysis_v0
process_type: continuous

inputs:
  - item_id: water
    qty: 1.0
    unit: L

outputs:
  - item_id: hydrogen_gas
    qty: 0.111
    unit: kg

energy_model:
  type: per_unit
  value: 50.0
  unit: kWh/kg  # ← Energy per kg
  scaling_basis: water
```

**Calculation for 100 L water:**
1. Parse unit: "kWh/kg" → ("kWh", "kg")
2. Convert quantity: 100 L → 100 kg (water density)
3. Calculate energy: 100 kg × 50.0 kWh/kg = **5000 kWh**

### Example 5: Rate with Time Normalization

```yaml
# Process
id: liquid_mixing_v0
process_type: continuous

inputs:
  - item_id: solution_a
    qty: 10.0
    unit: L

time_model:
  type: linear_rate
  rate: 300.0
  rate_unit: L/min  # ← Per minute!
  scaling_basis: solution_a
```

**Calculation for 600 L:**
1. Parse rate_unit: "L/min" → ("L", "min")
2. Normalize denominator: min → hr (factor 60)
3. Normalized rate: 300 L/min × 60 = 18000 L/hr
4. Calculate time: 600 L / 18000 L/hr = **0.033 hours** (2 minutes)

## Validation Rules

1. **Compound unit format** - Must be "X/Y" with valid units
2. **Time denominator normalization** - Rates with time denominators normalized to /hr
3. **Scaling basis convertibility** - scaling_basis item unit must convert to rate_unit numerator
4. **Density required** - Mass ↔ Volume conversions require material density
5. **Mass required** - Count ↔ Mass conversions require item mass_kg
6. **No chained conversions** - Only one-step conversions allowed (no L → kg → unit chains without explicit data)

## References

- Investigation: `design/unit-systems-and-conversions.md`
- User feedback: `design/time-model-hierarchy-feedback.txt`
- Current converter: `base_builder/unit_converter.py`
- ADR-012: Process types and time model (defines rate_unit format)
- ADR-014: Energy model redesign (defines energy units)

## Related Decisions

- **ADR-012:** Introduced flexible rate units, this ADR enables them
- **ADR-014:** Introduced flexible energy units, this ADR enables them
- **ADR-013:** Recipe overrides can use any units, conversion validates them
- **ADR-017:** Validation system uses conversion validation rules

## Approval

- [ ] Architecture review
- [ ] Implementation team review
- [ ] Migration strategy approved
- [ ] Test plan approved
