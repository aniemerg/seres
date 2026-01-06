# Fix Intelligence: recipe_ball_mill_v0

## Files

- **Recipe:** `kb/recipes/recipe_ball_mill_v0.yaml`
- **Target item:** `ball_mill_v0`
  - File: `kb/items/ball_mill_v0.yaml`
- **BOM:** `kb/boms/bom_ball_mill_v0.yaml` ✓
  - Components: 8
- **Steps:** 4 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_ball_mill_v0` → ball_mill_v0 (1 steps)
- `recipe_ball_mill_v0_seed_v0` → ball_mill_v0 (1 steps)

## Errors (4 found)

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

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `trunnion_supports` (qty: 2 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: trunnion_supports
    qty: 2
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

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `trunnion_supports` (qty: 2 None)
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
  - item_id: trunnion_supports
    qty: 2
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

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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
- `trunnion_supports` (qty: 2 None)
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
  - item_id: trunnion_supports
    qty: 2
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

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 8 components:

- `mill_shell_generic` (qty: 1 None)
- `liner_set_abrasion_resistant` (qty: 1 None)
- `trunnion_supports` (qty: 2 None)
- `bearing_set_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: mill_shell_generic
    qty: 1
    unit: None
  - item_id: liner_set_abrasion_resistant
    qty: 1
    unit: None
  - item_id: trunnion_supports
    qty: 2
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

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_ball_mill_v0.yaml`
- **BOM available:** Yes (8 components)
- **Similar recipes:** 2 found
