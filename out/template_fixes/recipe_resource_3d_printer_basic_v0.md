# Fix Intelligence: recipe_resource_3d_printer_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_resource_3d_printer_basic_v0.yaml`
- **Target item:** `resource_3d_printer_basic_v0`
  - File: `kb/items/resource_3d_printer_basic_v0.yaml`
- **BOM:** `kb/boms/bom_resource_3d_printer_basic_v0.yaml` ✓
  - Components: 11
- **Steps:** 3 total

## Errors (3 found)

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

BOM has 11 components:

- `printer_frame_generic` (qty: 1 None)
- `gantry_axes_set` (qty: 1 None)
- `extruder_head_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 3 None)
- `gearbox_reducer_medium` (qty: 3 None)
- `bearing_set_heavy` (qty: 3 None)
- `printer_control_module` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: printer_frame_generic
    qty: 1
    unit: None
  - item_id: gantry_axes_set
    qty: 1
    unit: None
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 3
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 3
    unit: None
  - item_id: bearing_set_heavy
    qty: 3
    unit: None
  - item_id: printer_control_module
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 11 components:

- `printer_frame_generic` (qty: 1 None)
- `gantry_axes_set` (qty: 1 None)
- `extruder_head_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 3 None)
- `gearbox_reducer_medium` (qty: 3 None)
- `bearing_set_heavy` (qty: 3 None)
- `printer_control_module` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: printer_frame_generic
    qty: 1
    unit: None
  - item_id: gantry_axes_set
    qty: 1
    unit: None
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 3
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 3
    unit: None
  - item_id: bearing_set_heavy
    qty: 3
    unit: None
  - item_id: printer_control_module
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'calibration_and_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `calibration_and_test_basic_v0`
  - File: `kb/processes/calibration_and_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_and_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 11 components:

- `printer_frame_generic` (qty: 1 None)
- `gantry_axes_set` (qty: 1 None)
- `extruder_head_basic` (qty: 1 None)
- `drive_motor_medium` (qty: 3 None)
- `gearbox_reducer_medium` (qty: 3 None)
- `bearing_set_heavy` (qty: 3 None)
- `printer_control_module` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: calibration_and_test_basic_v0
  inputs:
  - item_id: printer_frame_generic
    qty: 1
    unit: None
  - item_id: gantry_axes_set
    qty: 1
    unit: None
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 3
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 3
    unit: None
  - item_id: bearing_set_heavy
    qty: 3
    unit: None
  - item_id: printer_control_module
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_resource_3d_printer_basic_v0.yaml`
- **BOM available:** Yes (11 components)
