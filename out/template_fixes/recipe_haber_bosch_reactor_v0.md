# Fix Intelligence: recipe_haber_bosch_reactor_v0

## Files

- **Recipe:** `kb/recipes/recipe_haber_bosch_reactor_v0.yaml`
- **Target item:** `haber_bosch_reactor_v0`
  - File: `kb/items/haber_bosch_reactor_v0.yaml`
- **BOM:** `kb/boms/bom_haber_bosch_reactor_v0.yaml` ✓
  - Components: 4
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
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

BOM has 4 components:

- `furnace_shell_refractory` (qty: 1.0 unit)
- `refractory_brick_set` (qty: 1.0 unit)
- `steel_plate_raw` (qty: 400.0 kg)
- `steel_plate_or_sheet` (qty: 150.0 kg)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: furnace_shell_refractory
    qty: 1.0
    unit: unit
  - item_id: refractory_brick_set
    qty: 1.0
    unit: unit
  - item_id: steel_plate_raw
    qty: 400.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 150.0
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

- `furnace_shell_refractory` (qty: 1.0 unit)
- `refractory_brick_set` (qty: 1.0 unit)
- `steel_plate_raw` (qty: 400.0 kg)
- `steel_plate_or_sheet` (qty: 150.0 kg)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: furnace_shell_refractory
    qty: 1.0
    unit: unit
  - item_id: refractory_brick_set
    qty: 1.0
    unit: unit
  - item_id: steel_plate_raw
    qty: 400.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 150.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- `furnace_shell_refractory` (qty: 1.0 unit)
- `refractory_brick_set` (qty: 1.0 unit)
- `steel_plate_raw` (qty: 400.0 kg)
- `steel_plate_or_sheet` (qty: 150.0 kg)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: furnace_shell_refractory
    qty: 1.0
    unit: unit
  - item_id: refractory_brick_set
    qty: 1.0
    unit: unit
  - item_id: steel_plate_raw
    qty: 400.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 150.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
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

- `furnace_shell_refractory` (qty: 1.0 unit)
- `refractory_brick_set` (qty: 1.0 unit)
- `steel_plate_raw` (qty: 400.0 kg)
- `steel_plate_or_sheet` (qty: 150.0 kg)

Suggested fix:
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: furnace_shell_refractory
    qty: 1.0
    unit: unit
  - item_id: refractory_brick_set
    qty: 1.0
    unit: unit
  - item_id: steel_plate_raw
    qty: 400.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 150.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 2 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

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

- `furnace_shell_refractory` (qty: 1.0 unit)
- `refractory_brick_set` (qty: 1.0 unit)
- `steel_plate_raw` (qty: 400.0 kg)
- `steel_plate_or_sheet` (qty: 150.0 kg)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: furnace_shell_refractory
    qty: 1.0
    unit: unit
  - item_id: refractory_brick_set
    qty: 1.0
    unit: unit
  - item_id: steel_plate_raw
    qty: 400.0
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 150.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 2 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_haber_bosch_reactor_v0.yaml`
- **BOM available:** Yes (4 components)
