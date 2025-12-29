# Unit Systems and Conversions Analysis

**Status:** Investigation
**Date:** 2024-12-28
**Purpose:** Analyze unit heterogeneity across the KB and implications for time/energy calculations

## Executive Summary

The KB uses **9 different unit types** across thousands of quantity specifications, with **kg dominating (2967 uses)** but significant use of count-based units (unit, each, count) and time (hr). A UnitConverter exists but **time_model calculations don't integrate with it**, creating mismatches when processes use rate_kg_per_hr but inputs/outputs are in liters or units.

## Unit Type Census

### Survey Results

From 5000+ unit specifications across processes and recipes:

| Unit | Count | Category | Notes |
|------|-------|----------|-------|
| kg | 2967 | Mass | Dominant, used for most materials |
| unit | 1158 | Count | Generic countable items |
| hr | 799 | Time | Used in time_model and resource_requirements |
| each | 93 | Count | Synonym for "unit", interchangeable |
| kWh | 22 | Energy | Energy consumption/generation |
| count | 12 | Count | Synonym for "unit" |
| set | 8 | Count | Collections/assemblies |
| L | 8 | Volume | Liquids (rarely used) |
| kit | 3 | Count | Pre-packaged collections |

### Unit Categories

**1. Mass Units**
- `kg` (kilogram) - standard mass unit
- `g` (gram) - supported by converter but rarely used in KB
- `tonne` - supported by converter but not found in KB

**2. Count Units**
- `unit` - generic discrete item
- `each` - synonym for unit
- `count` - synonym for unit
- `set` - collection of items (still counted as 1 set)
- `kit` - pre-packaged collection

**Current handling:** UnitConverter treats all count units as synonymous (1:1 conversion).

**3. Volume Units**
- `L` (liter) - used for liquids (8 occurrences)
- `m³` - supported by converter but not found in KB

**4. Time Units**
- `hr` (hour) - used in time_model and resource_requirements

**5. Energy Units**
- `kWh` (kilowatt-hour) - energy consumption/generation

## Unit Converter Capabilities

### What It Can Do (base_builder/unit_converter.py)

**1. Direct conversions** - via KB conversion factors
```python
kg -> g (factor: 1000)
m³ -> L (factor: 1000)
count <-> unit <-> each (1:1)
```

**2. Mass <-> Volume** - via material density
```python
water: 10 L -> 10 kg (density: 1000 kg/m³)
aluminum: 5 kg -> 0.00185 m³ (density: 2700 kg/m³)
```

**3. Count <-> Mass** - via item mass_kg field
```python
motor (mass_kg: 12) -> 1 unit = 12 kg
battery_pack (mass_kg: 45) -> 2 units = 90 kg
```

### What It Cannot Do

**1. Time conversions in process context**
- No integration with time_model calculations
- Can't convert between time units and mass/volume
- Example: Can't answer "how long to process 10 L of water if rate is 5 kg/hr?"

**2. Energy <-> Time coupling**
- No way to relate kWh/kg energy model to hr/kg time model
- Can't calculate total energy from time and power
- Example: Can't compute "process takes 5 hrs at 2 kW = 10 kWh total"

**3. Rate conversions**
- No support for compound units like kg/hr, L/min, kWh/kg
- Can't convert "rate_kg_per_hr: 5.0" to "rate_L_per_hr" for water

**4. Context-dependent conversions**
- Can't vary conversion based on material class or process type
- Density lookup is simple item_id match, not material_class aware

## Time_Model Unit Mismatches

### Problem: Fixed Units in Time Model

```python
class TimeModel:
    hr_per_kg: Optional[float]      # ALWAYS kg
    rate_kg_per_hr: Optional[float]  # ALWAYS kg
    hr_per_batch: Optional[float]
```

**Issue:** What if process inputs/outputs are NOT in kg?

### Example 1: Volume-Based Input

```yaml
id: water_distillation_v0
inputs:
  - item_id: water
    qty: 10
    unit: L  # ← Liters!
outputs:
  - item_id: distilled_water
    qty: 9
    unit: L
time_model:
  type: linear_rate
  rate_kg_per_hr: 5.0  # ← kg/hr, but input is liters!
```

**Questions:**
- Does `rate_kg_per_hr: 5.0` mean 5 L/hr (since water ≈ 1 kg/L)?
- Or does it mean we need to convert 10 L → 10 kg, then apply 5 kg/hr = 2 hr?
- Or is this just broken/unspecified?

**Current simulation behavior:** Agent provides duration_hours, so this mismatch is never encountered.

### Example 2: Count-Based Input

```yaml
id: motor_assembly_v0
inputs:
  - item_id: motor_housing
    qty: 10
    unit: unit  # ← Count-based!
outputs:
  - item_id: motor_complete
    qty: 10
    unit: unit
time_model:
  type: linear_rate
  rate_kg_per_hr: 2.0  # ← kg/hr, but input is units!
```

**Questions:**
- Does `rate_kg_per_hr: 2.0` mean 2 units/hr?
- Or do we look up motor_housing.mass_kg, convert 10 units → kg, then apply rate?
- What if motor_housing doesn't have mass_kg defined?

**Possible interpretation:**
```python
# Convert count to mass
housing_mass_kg = 10 units × motor_housing.mass_kg (e.g., 3 kg/unit) = 30 kg
# Apply rate
time_hr = 30 kg / 2.0 kg/hr = 15 hours
```

But this is **not implemented** and **not specified anywhere**.

### Example 3: Multi-Unit Process

```yaml
id: battery_assembly_v0
inputs:
  - item_id: battery_cells
    qty: 100
    unit: each  # Count
  - item_id: electrolyte
    qty: 5
    unit: L     # Volume
  - item_id: casing
    qty: 20
    unit: kg    # Mass
outputs:
  - item_id: battery_pack
    qty: 1
    unit: unit
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # ← Which input does this apply to?!
```

**Problem:** Process has inputs in THREE different units. What does `rate_kg_per_hr` mean?

**Possible interpretations:**
1. Apply to casing only (20 kg / 10 kg/hr = 2 hr)
2. Convert everything to kg, sum, apply rate
3. Use total output mass if defined
4. Undefined - agent must guess

## Energy_Model Unit Issues

### Problem: Similar to time_model

```python
class EnergyModel:
    type: str  # kWh_per_kg, kWh_per_batch, kWh_per_unit_output
    value: float
```

**Types:**
- `kWh_per_kg` - assumes mass-based processing
- `kWh_per_batch` - independent of units
- `kWh_per_unit_output` - assumes count-based output

### Example: Volume Input, Mass-Based Energy

```yaml
id: water_electrolysis_v0
inputs:
  - item_id: water
    qty: 10
    unit: L  # Volume!
outputs:
  - item_id: hydrogen
    qty: 1.1
    unit: kg
  - item_id: oxygen
    qty: 8.9
    unit: kg
energy_model:
  type: kWh_per_kg
  value: 50.0  # ← kg of what? Input or output?
```

**Questions:**
- Is it 50 kWh per kg of water input (10 L × 1 kg/L × 50 = 500 kWh)?
- Or 50 kWh per kg of hydrogen output (1.1 kg × 50 = 55 kWh)?
- Or per kg of total output (10 kg × 50 = 500 kWh)?

**Not specified anywhere.**

## Implications for Time Calculation

### If Simulation Were to Calculate Duration from time_model

**Step 1: Determine input mass**
```python
def calculate_duration(process, inputs_used):
    time_model = process.time_model

    if time_model.type == "linear_rate":
        # Need to determine "mass" to process
        total_mass_kg = 0

        for inp in inputs_used:
            # Problem: inp.unit might not be kg!
            if inp.unit == "kg":
                total_mass_kg += inp.qty
            elif inp.unit in ["L", "m3"]:
                # Need density to convert
                mass = convert_to_kg(inp.qty, inp.unit, inp.item_id)
                total_mass_kg += mass
            elif inp.unit in ["unit", "each", "count"]:
                # Need item mass_kg to convert
                mass = inp.qty * get_item_mass(inp.item_id)
                total_mass_kg += mass
            else:
                # Unknown unit - error? ignore? guess?
                ???

        # Apply time model
        setup = time_model.setup_hr or 0
        rate = time_model.rate_kg_per_hr or time_model.hr_per_kg

        if rate:
            duration = setup + (total_mass_kg / rate)
        else:
            # No rate specified - error? default?
            ???

    elif time_model.type == "fixed_time":
        duration = time_model.hr_per_batch

    return duration
```

**Problems with this approach:**
1. Assumes all inputs should be summed (may not be correct)
2. Requires all items to have mass_kg (many don't)
3. Requires all materials to have density (many don't)
4. Doesn't handle multi-unit inputs well (which one dominates rate?)
5. What if outputs are in different units than inputs?

### Alternative: Standardize to Primary Input

```python
# Instead of summing all inputs, use the "primary" input
# (largest quantity, or first listed, or specified somehow)
primary_input = inputs_used[0]

# Convert to kg regardless of original unit
mass_kg = convert_to_kg(primary_input.qty, primary_input.unit, primary_input.item_id)

# Apply time model
duration = setup + (mass_kg / rate_kg_per_hr)
```

**Still requires:**
- Defining what "primary" means
- Universal conversion to kg
- All items/materials to have conversion data

## Proposed Solutions

### Option 1: Require kg for All Rate-Based Processes

**Rule:** If process has `type: linear_rate`, all inputs and outputs MUST be in kg.

**Pros:**
- Simple, unambiguous
- No conversion needed
- Easy to validate

**Cons:**
- Forces unnatural units (counting motors in kg instead of units)
- Doesn't match real-world process descriptions
- Breaks current KB (many processes use unit/each)

### Option 2: Unit-Aware Time Models

**Extend time_model to specify units:**
```yaml
time_model:
  type: linear_rate
  rate: 5.0
  rate_unit: L/hr  # ← Explicit compound unit
  input_refers_to: water  # ← Which input this rate applies to
```

**Pros:**
- Flexible, matches real process descriptions
- Can handle volume-based, count-based, mass-based
- Clear semantics

**Cons:**
- Requires parser for compound units (L/hr, kg/min, units/hr)
- More complex validation
- Need to define all possible compound units

### Option 3: Normalized Internal Representation

**Keep YAML simple, normalize internally:**
```yaml
# YAML stays simple
time_model:
  type: linear_rate
  rate_kg_per_hr: 5.0

# But converter normalizes inputs first
```

**Process:**
1. Before calculating time, convert all inputs to kg using UnitConverter
2. Apply rate_kg_per_hr to total kg
3. Convert result if needed

**Pros:**
- YAML stays simple
- Leverages existing UnitConverter
- Backward compatible

**Cons:**
- Requires all items to have mass_kg or material to have density
- Hidden complexity (not obvious from YAML what will happen)
- Fails if conversion impossible

### Option 4: Multiple Time Models per Process

**Allow material-specific time models:**
```yaml
time_models:
  - material_class: metal
    type: linear_rate
    rate_kg_per_hr: 10.0
  - material_class: ceramic
    type: linear_rate
    rate_kg_per_hr: 3.0
  - default:
    type: fixed_time
    hr_per_batch: 2.0
```

**Pros:**
- Handles material-dependent rates
- Very flexible
- Accurate modeling

**Cons:**
- Much more complex
- Requires material_class on all items
- Validation harder
- Unclear which model to use if multiple materials

## Energy Calculation Coupling

### Current Energy Model

```yaml
energy_model:
  type: kWh_per_kg  # or kWh_per_batch, kWh_per_unit_output
  value: 50.0
```

**Same unit issues as time_model!**

### Coupled Calculation

For many processes, energy and time are coupled:
```
Energy = Power × Time
Total_kWh = kW × hours
```

**Example:**
```yaml
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0  # 10 kg takes 1 hour
energy_model:
  type: kWh_per_kg
  value: 5.0            # 5 kWh per kg

# For 100 kg:
time = 100 kg / 10 kg/hr = 10 hours
energy = 100 kg × 5 kWh/kg = 500 kWh
power = 500 kWh / 10 hr = 50 kW average
```

**Could we specify power instead?**
```yaml
time_model:
  type: linear_rate
  rate_kg_per_hr: 10.0
power_requirement:
  kW: 50.0  # ← Average power draw

# Energy calculated as power × time
```

**Pros:**
- More intuitive (processes draw power, not energy per kg)
- Automatically coupled
- Can handle variable power (startup surge, etc.)

**Cons:**
- Changes current model significantly
- What about batch processes with idle time?

## Validation Implications

### What Indexer Should Check

**Currently:** Just warns if time_model missing.

**Could check:**
1. **Unit consistency:** If rate_kg_per_hr used, do inputs/outputs have kg-convertible units?
2. **Conversion feasibility:** Can all input units be converted to kg (density/mass defined)?
3. **Rate realism:** Is rate_kg_per_hr reasonable for this process type?
4. **Energy-time coupling:** Does energy_model make sense given time_model?

**Example validation:**
```python
def validate_time_model(process):
    if process.time_model.type == "linear_rate":
        if process.time_model.rate_kg_per_hr:
            # Check all inputs are kg-convertible
            for inp in process.inputs:
                if inp.unit not in ["kg", "L", "m3", "unit", "each"]:
                    warn(f"Input {inp.item_id} unit {inp.unit} may not be convertible to kg")

                if inp.unit in ["L", "m3"]:
                    # Check material has density
                    if not has_density(inp.item_id):
                        error(f"Input {inp.item_id} is volume-based but has no density for kg conversion")

                if inp.unit in ["unit", "each", "count"]:
                    # Check item has mass_kg
                    if not has_mass_kg(inp.item_id):
                        error(f"Input {inp.item_id} is count-based but has no mass_kg for kg conversion")
```

## Recommendations

1. **Document current unit usage** ✅ (this document)

2. **Specify conversion rules** - Define exactly how time_model units relate to input/output units

3. **Enhance UnitConverter** - Add support for:
   - Compound units (kg/hr, L/min)
   - Context-aware conversions (material_class)
   - Rate calculations

4. **Add validation** - Indexer should check unit convertibility for processes with rate-based time_models

5. **Test implementation** - Before changing specs, prototype calculation in simulation to find edge cases

6. **Consider unit-aware time_model** - Allow explicit rate units (rate_L_per_hr, rate_units_per_hr) instead of forcing kg

## Open Questions

1. Should we require all processes to be kg-normalizable, or allow native units (L/hr for liquids, units/hr for discrete items)?

2. How to handle multi-material processes where different inputs have different rate-limiting steps?

3. Should time_model be required to specify which input it applies to (for multi-input processes)?

4. How to model processes where time depends on output quality/precision rather than quantity?

5. Should we couple energy_model and time_model more explicitly (via power requirements)?

## Next Documents

- **override-hierarchy-problems.md** - How recipe step timing overrides process time_model
- **material-dependent-models.md** - Material-specific rates and characteristics
- **consumers-and-use-cases.md** - How different systems need to use this data
