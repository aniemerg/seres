# Fix Intelligence: recipe_coordinate_measuring_machine_v0

## Files

- **Recipe:** `kb/recipes/recipe_coordinate_measuring_machine_v0.yaml`
- **Target item:** `coordinate_measuring_machine_v0`
  - File: `kb/items/coordinate_measuring_machine_v0.yaml`
- **BOM:** `kb/boms/bom_coordinate_measuring_machine_v0.yaml` ✓
  - Components: 8
- **Steps:** 8 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_coordinate_measuring_machine_v0` → coordinate_measuring_machine_v0 (8 steps)
- `recipe_coordinate_measuring_machine_v1` → coordinate_measuring_machine (1 steps)

## Errors (8 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
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

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: precision_grinding_basic_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: machining_precision_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (1.0 kg)

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

BOM has 8 components:

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (1.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'precision_alignment_and_leveling_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 3
**Process:** `precision_alignment_and_leveling_v0`
  - File: `kb/processes/precision_alignment_and_leveling_v0.yaml`

**Current step:**
```yaml
- process_id: precision_alignment_and_leveling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 8 components:

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (1.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `machine_frame_small` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `calibration_basic_v0`
  - File: `kb/processes/calibration_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: calibration_basic_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (1.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `machine_frame_small` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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

BOM has 8 components:

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (1.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `machine_frame_small` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)
- Step 5 produces: `instrument_calibrated` (1.0 unit)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
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

BOM has 8 components:

- `granite_surface_plate_large` (qty: 1 unit)
- `linear_stage_xyz_precision` (qty: 1 unit)
- `touch_probe_assembly` (qty: 1 unit)
- `linear_encoder_set` (qty: 3 unit)
- `stepper_motor_precision` (qty: 3 unit)
- `computer_workstation` (qty: 1 unit)
- `air_bearing_assembly` (qty: 3 unit)
- `calibration_artifacts` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: granite_surface_plate_large
    qty: 1
    unit: unit
  - item_id: linear_stage_xyz_precision
    qty: 1
    unit: unit
  - item_id: touch_probe_assembly
    qty: 1
    unit: unit
  - item_id: linear_encoder_set
    qty: 3
    unit: unit
  - item_id: stepper_motor_precision
    qty: 3
    unit: unit
  - item_id: computer_workstation
    qty: 1
    unit: unit
  - item_id: air_bearing_assembly
    qty: 3
    unit: unit
  - item_id: calibration_artifacts
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (1.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `machine_frame_small` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)
- Step 5 produces: `instrument_calibrated` (1.0 unit)
- Step 6 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 8
- **Recipe file:** `kb/recipes/recipe_coordinate_measuring_machine_v0.yaml`
- **BOM available:** Yes (8 components)
- **Similar recipes:** 2 found
