# Fix Intelligence: recipe_ebm_powder_handling_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_ebm_powder_handling_system_v0.yaml`
- **Target item:** `ebm_powder_handling_system_v0`
  - File: `kb/items/ebm_powder_handling_system_v0.yaml`
- **BOM:** `kb/boms/bom_ebm_powder_handling_system_v0.yaml` ✓
  - Components: 8
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `collection_hopper_set` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_forming_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: collection_hopper_set
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
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

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `collection_hopper_set` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: collection_hopper_set
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_metal_part` (0.95 kg)

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

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `collection_hopper_set` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: collection_hopper_set
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_metal_part` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'surface_treatment_basic_v0') requires input 'formed_metal_part' which is not available

**Location:** Step 3
**Process:** `surface_treatment_basic_v0`
  - File: `kb/processes/surface_treatment_basic_v0.yaml`

**Current step:**
```yaml
- process_id: surface_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `collection_hopper_set` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: collection_hopper_set
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_metal_part` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `metal_part_surface_treated` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `alignment_and_testing_basic_v0`
  - File: `kb/processes/alignment_and_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: alignment_and_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `collection_hopper_set` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: alignment_and_testing_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: collection_hopper_set
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_metal_part` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `metal_part_surface_treated` (1.0 kg)
- Step 4 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_ebm_powder_handling_system_v0.yaml`
- **BOM available:** Yes (8 components)
