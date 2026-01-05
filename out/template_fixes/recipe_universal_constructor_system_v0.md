# Fix Intelligence: recipe_universal_constructor_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_universal_constructor_system_v0.yaml`
- **Target item:** `universal_constructor_system_v0`
  - File: `kb/items/universal_constructor_system_v0.yaml`
- **BOM:** `kb/boms/bom_universal_constructor_system_v0.yaml` ✓
  - Components: 5
- **Steps:** 5 total

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

BOM has 5 components:

- `machine_frame_medium` (qty: 1 None)
- `frame_and_supports_basic` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `structural_steel_frame` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1
    unit: None
  - item_id: frame_and_supports_basic
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: structural_steel_frame
    qty: 1
    unit: None
```

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 1
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 5 components:

- `machine_frame_medium` (qty: 1 None)
- `frame_and_supports_basic` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `structural_steel_frame` (qty: 1 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1
    unit: None
  - item_id: frame_and_supports_basic
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: structural_steel_frame
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `assembled_electronics` (1.0 unit)

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

BOM has 5 components:

- `machine_frame_medium` (qty: 1 None)
- `frame_and_supports_basic` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `structural_steel_frame` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1
    unit: None
  - item_id: frame_and_supports_basic
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: structural_steel_frame
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `assembled_electronics` (1.0 unit)
- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `machine_frame_medium` (qty: 1 None)
- `frame_and_supports_basic` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `structural_steel_frame` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1
    unit: None
  - item_id: frame_and_supports_basic
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: structural_steel_frame
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `assembled_electronics` (1.0 unit)
- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_universal_constructor_system_v0.yaml`
- **BOM available:** Yes (5 components)
