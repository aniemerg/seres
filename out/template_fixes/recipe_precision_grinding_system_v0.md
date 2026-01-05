# Fix Intelligence: recipe_precision_grinding_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_precision_grinding_system_v0.yaml`
- **Target item:** `precision_grinding_system_v0`
  - File: `kb/items/precision_grinding_system_v0.yaml`
- **BOM:** `kb/boms/bom_precision_grinding_system_v0.yaml` ✓
  - Components: 8
- **Steps:** 6 total

## Errors (6 found)

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

BOM has 8 components:

- `grinding_wheels` (qty: 1.0 None)
- `spindle_assembly_precision` (qty: 1.0 None)
- `bearing_ball_precision` (qty: 8.0 None)
- `bearing_rings_hardened` (qty: 2.0 None)
- `coolant_pump_system` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `precision_mounts_and_fixtures` (qty: 1.0 None)
- `linear_stage_xyz_precision` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: grinding_wheels
    qty: 1.0
    unit: None
  - item_id: spindle_assembly_precision
    qty: 1.0
    unit: None
  - item_id: bearing_ball_precision
    qty: 8.0
    unit: None
  - item_id: bearing_rings_hardened
    qty: 2.0
    unit: None
  - item_id: coolant_pump_system
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: precision_mounts_and_fixtures
    qty: 1.0
    unit: None
  - item_id: linear_stage_xyz_precision
    qty: 1.0
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

- `grinding_wheels` (qty: 1.0 None)
- `spindle_assembly_precision` (qty: 1.0 None)
- `bearing_ball_precision` (qty: 8.0 None)
- `bearing_rings_hardened` (qty: 2.0 None)
- `coolant_pump_system` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `precision_mounts_and_fixtures` (qty: 1.0 None)
- `linear_stage_xyz_precision` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: grinding_wheels
    qty: 1.0
    unit: None
  - item_id: spindle_assembly_precision
    qty: 1.0
    unit: None
  - item_id: bearing_ball_precision
    qty: 8.0
    unit: None
  - item_id: bearing_rings_hardened
    qty: 2.0
    unit: None
  - item_id: coolant_pump_system
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: precision_mounts_and_fixtures
    qty: 1.0
    unit: None
  - item_id: linear_stage_xyz_precision
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `grinding_wheels` (qty: 1.0 None)
- `spindle_assembly_precision` (qty: 1.0 None)
- `bearing_ball_precision` (qty: 8.0 None)
- `bearing_rings_hardened` (qty: 2.0 None)
- `coolant_pump_system` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `precision_mounts_and_fixtures` (qty: 1.0 None)
- `linear_stage_xyz_precision` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: precision_grinding_basic_v0
  inputs:
  - item_id: grinding_wheels
    qty: 1.0
    unit: None
  - item_id: spindle_assembly_precision
    qty: 1.0
    unit: None
  - item_id: bearing_ball_precision
    qty: 8.0
    unit: None
  - item_id: bearing_rings_hardened
    qty: 2.0
    unit: None
  - item_id: coolant_pump_system
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: precision_mounts_and_fixtures
    qty: 1.0
    unit: None
  - item_id: linear_stage_xyz_precision
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'bearing_installation_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `bearing_installation_basic_v0`
  - File: `kb/processes/bearing_installation_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: bearing_installation_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `grinding_wheels` (qty: 1.0 None)
- `spindle_assembly_precision` (qty: 1.0 None)
- `bearing_ball_precision` (qty: 8.0 None)
- `bearing_rings_hardened` (qty: 2.0 None)
- `coolant_pump_system` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `precision_mounts_and_fixtures` (qty: 1.0 None)
- `linear_stage_xyz_precision` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: bearing_installation_basic_v0
  inputs:
  - item_id: grinding_wheels
    qty: 1.0
    unit: None
  - item_id: spindle_assembly_precision
    qty: 1.0
    unit: None
  - item_id: bearing_ball_precision
    qty: 8.0
    unit: None
  - item_id: bearing_rings_hardened
    qty: 2.0
    unit: None
  - item_id: coolant_pump_system
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: precision_mounts_and_fixtures
    qty: 1.0
    unit: None
  - item_id: linear_stage_xyz_precision
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `finished_part_deburred` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- `grinding_wheels` (qty: 1.0 None)
- `spindle_assembly_precision` (qty: 1.0 None)
- `bearing_ball_precision` (qty: 8.0 None)
- `bearing_rings_hardened` (qty: 2.0 None)
- `coolant_pump_system` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `precision_mounts_and_fixtures` (qty: 1.0 None)
- `linear_stage_xyz_precision` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: grinding_wheels
    qty: 1.0
    unit: None
  - item_id: spindle_assembly_precision
    qty: 1.0
    unit: None
  - item_id: bearing_ball_precision
    qty: 8.0
    unit: None
  - item_id: bearing_rings_hardened
    qty: 2.0
    unit: None
  - item_id: coolant_pump_system
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: precision_mounts_and_fixtures
    qty: 1.0
    unit: None
  - item_id: linear_stage_xyz_precision
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `finished_part_deburred` (1.0 kg)
- Step 3 produces: `finished_part` (2.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `grinding_wheels` (qty: 1.0 None)
- `spindle_assembly_precision` (qty: 1.0 None)
- `bearing_ball_precision` (qty: 8.0 None)
- `bearing_rings_hardened` (qty: 2.0 None)
- `coolant_pump_system` (qty: 1.0 None)
- `control_panel_basic` (qty: 1.0 None)
- `precision_mounts_and_fixtures` (qty: 1.0 None)
- `linear_stage_xyz_precision` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: balancing_dynamic_basic_v0
  inputs:
  - item_id: grinding_wheels
    qty: 1.0
    unit: None
  - item_id: spindle_assembly_precision
    qty: 1.0
    unit: None
  - item_id: bearing_ball_precision
    qty: 8.0
    unit: None
  - item_id: bearing_rings_hardened
    qty: 2.0
    unit: None
  - item_id: coolant_pump_system
    qty: 1.0
    unit: None
  - item_id: control_panel_basic
    qty: 1.0
    unit: None
  - item_id: precision_mounts_and_fixtures
    qty: 1.0
    unit: None
  - item_id: linear_stage_xyz_precision
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `finished_part_deburred` (1.0 kg)
- Step 3 produces: `finished_part` (2.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_precision_grinding_system_v0.yaml`
- **BOM available:** Yes (8 components)
