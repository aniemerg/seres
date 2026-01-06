# Fix Intelligence: recipe_welding_arc_welder_v0

## Files

- **Recipe:** `kb/recipes/recipe_welding_arc_welder_v0.yaml`
- **Target item:** `welding_arc_welder_v0`
  - File: `kb/items/welding_arc_welder_v0.yaml`
- **BOM:** `kb/boms/bom_welding_arc_welder_v0.yaml` ✓
  - Components: 3
- **Steps:** 6 total

## Errors (6 found)

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

BOM has 3 components:

- `steel_frame_welded` (qty: 1.0 unit)
- `motor_electric_small` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 2.0 unit)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: steel_frame_welded
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_frame_welded` (qty: 1.0 unit)
- `motor_electric_small` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 2.0 unit)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: steel_frame_welded
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_frame_welded` (qty: 1.0 unit)
- `motor_electric_small` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 2.0 unit)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_frame_welded
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_frame_welded` (qty: 1.0 unit)
- `motor_electric_small` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 2.0 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_frame_welded
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 3 components:

- `steel_frame_welded` (qty: 1.0 unit)
- `motor_electric_small` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 2.0 unit)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: steel_frame_welded
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 3 components:

- `steel_frame_welded` (qty: 1.0 unit)
- `motor_electric_small` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 2.0 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: steel_frame_welded
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_welding_arc_welder_v0.yaml`
- **BOM available:** Yes (3 components)
