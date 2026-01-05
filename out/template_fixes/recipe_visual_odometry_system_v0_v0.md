# Fix Intelligence: recipe_visual_odometry_system_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_visual_odometry_system_v0_v0.yaml`
- **Target item:** `visual_odometry_system_v0_v0`
  - File: `kb/items/visual_odometry_system_v0_v0.yaml`
- **BOM:** `kb/boms/bom_visual_odometry_system_v0_v0.yaml` ✓
  - Components: 4
- **Steps:** 3 total

## Errors (3 found)

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

- `camera_vacuum_tube_vidicon_v0` (qty: 2.0 unit)
- `control_panel_basic` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 1.0 unit)
- `steel_frame_heavy` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: camera_vacuum_tube_vidicon_v0
    qty: 2.0
    unit: unit
  - item_id: control_panel_basic
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 1.0
    unit: unit
  - item_id: steel_frame_heavy
    qty: 1.0
    unit: unit
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

- `camera_vacuum_tube_vidicon_v0` (qty: 2.0 unit)
- `control_panel_basic` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 1.0 unit)
- `steel_frame_heavy` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: camera_vacuum_tube_vidicon_v0
    qty: 2.0
    unit: unit
  - item_id: control_panel_basic
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 1.0
    unit: unit
  - item_id: steel_frame_heavy
    qty: 1.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 4 components:

- `camera_vacuum_tube_vidicon_v0` (qty: 2.0 unit)
- `control_panel_basic` (qty: 1.0 unit)
- `bearing_set_heavy` (qty: 1.0 unit)
- `steel_frame_heavy` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: camera_vacuum_tube_vidicon_v0
    qty: 2.0
    unit: unit
  - item_id: control_panel_basic
    qty: 1.0
    unit: unit
  - item_id: bearing_set_heavy
    qty: 1.0
    unit: unit
  - item_id: steel_frame_heavy
    qty: 1.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_visual_odometry_system_v0_v0.yaml`
- **BOM available:** Yes (4 components)
