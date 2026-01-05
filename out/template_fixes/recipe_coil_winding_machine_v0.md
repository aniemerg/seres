# Fix Intelligence: recipe_coil_winding_machine_v0

## Files

- **Recipe:** `kb/recipes/recipe_coil_winding_machine_v0.yaml`
- **Target item:** `coil_winding_machine_v0`
  - File: `kb/items/coil_winding_machine_v0.yaml`
- **BOM:** `kb/boms/bom_coil_winding_machine_v0.yaml` ✓
  - Components: 7
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_coil_winding_machine_v1` → coil_winding_machine (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `machine_frame_small` (qty: 1 None)
- `spindle_drive_motor_small` (qty: 1 None)
- `wire_tensioning_mechanism` (qty: 1 None)
- `turn_counter_module` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: spindle_drive_motor_small
    qty: 1
    unit: None
  - item_id: wire_tensioning_mechanism
    qty: 1
    unit: None
  - item_id: turn_counter_module
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 7 components:

- `machine_frame_small` (qty: 1 None)
- `spindle_drive_motor_small` (qty: 1 None)
- `wire_tensioning_mechanism` (qty: 1 None)
- `turn_counter_module` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: spindle_drive_motor_small
    qty: 1
    unit: None
  - item_id: wire_tensioning_mechanism
    qty: 1
    unit: None
  - item_id: turn_counter_module
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 7 components:

- `machine_frame_small` (qty: 1 None)
- `spindle_drive_motor_small` (qty: 1 None)
- `wire_tensioning_mechanism` (qty: 1 None)
- `turn_counter_module` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: spindle_drive_motor_small
    qty: 1
    unit: None
  - item_id: wire_tensioning_mechanism
    qty: 1
    unit: None
  - item_id: turn_counter_module
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 7 components:

- `machine_frame_small` (qty: 1 None)
- `spindle_drive_motor_small` (qty: 1 None)
- `wire_tensioning_mechanism` (qty: 1 None)
- `turn_counter_module` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: spindle_drive_motor_small
    qty: 1
    unit: None
  - item_id: wire_tensioning_mechanism
    qty: 1
    unit: None
  - item_id: turn_counter_module
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_coil_winding_machine_v0.yaml`
- **BOM available:** Yes (7 components)
- **Similar recipes:** 1 found
