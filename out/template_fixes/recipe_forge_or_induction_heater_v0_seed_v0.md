# Fix Intelligence: recipe_forge_or_induction_heater_v0_seed_v0

## Files

- **Recipe:** `kb/recipes/recipe_forge_or_induction_heater_v0_seed_v0.yaml`
- **Target item:** `forge_or_induction_heater_v0`
  - File: `kb/items/forge_or_induction_heater_v0.yaml`
- **BOM:** `kb/boms/bom_forge_or_induction_heater_v0.yaml` ✓
  - Components: 4
- **Steps:** 5 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_forge_or_induction_heater_alias_v0` → forge_or_induction_heater (5 steps)
- `recipe_forge_or_induction_heater_v0` → forge_or_induction_heater_v0 (5 steps)
- `recipe_forge_or_induction_heater_v0_v0` → forge_or_induction_heater_v0 (5 steps)

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `motor_assembly` (qty: 1.0 count)
- `shaft_and_bearing_set` (qty: 1.0 count)
- `bearing_set_heavy` (qty: 4.0 kg)
- `fastener_kit_medium` (qty: 1.0 kg)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: motor_assembly
    qty: 1.0
    unit: count
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: count
  - item_id: bearing_set_heavy
    qty: 4.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `motor_assembly` (qty: 1.0 count)
- `shaft_and_bearing_set` (qty: 1.0 count)
- `bearing_set_heavy` (qty: 4.0 kg)
- `fastener_kit_medium` (qty: 1.0 kg)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: motor_assembly
    qty: 1.0
    unit: count
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: count
  - item_id: bearing_set_heavy
    qty: 4.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `motor_assembly` (qty: 1.0 count)
- `shaft_and_bearing_set` (qty: 1.0 count)
- `bearing_set_heavy` (qty: 4.0 kg)
- `fastener_kit_medium` (qty: 1.0 kg)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: motor_assembly
    qty: 1.0
    unit: count
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: count
  - item_id: bearing_set_heavy
    qty: 4.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `motor_assembly` (qty: 1.0 count)
- `shaft_and_bearing_set` (qty: 1.0 count)
- `bearing_set_heavy` (qty: 4.0 kg)
- `fastener_kit_medium` (qty: 1.0 kg)

Suggested fix:
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: motor_assembly
    qty: 1.0
    unit: count
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: count
  - item_id: bearing_set_heavy
    qty: 4.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 4 components:

- `motor_assembly` (qty: 1.0 count)
- `shaft_and_bearing_set` (qty: 1.0 count)
- `bearing_set_heavy` (qty: 4.0 kg)
- `fastener_kit_medium` (qty: 1.0 kg)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: motor_assembly
    qty: 1.0
    unit: count
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: count
  - item_id: bearing_set_heavy
    qty: 4.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_forge_or_induction_heater_v0_seed_v0.yaml`
- **BOM available:** Yes (4 components)
- **Similar recipes:** 3 found
