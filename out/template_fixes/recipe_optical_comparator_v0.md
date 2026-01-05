# Fix Intelligence: recipe_optical_comparator_v0

## Files

- **Recipe:** `kb/recipes/recipe_optical_comparator_v0.yaml`
- **Target item:** `optical_comparator_v0`
  - File: `kb/items/optical_comparator_v0.yaml`
- **BOM:** `kb/boms/bom_optical_comparator_v0.yaml` ✓
  - Components: 7
- **Steps:** 4 total

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

BOM has 7 components:

- `light_source_bright` (qty: 1 None)
- `lens_assembly_magnifying` (qty: 1 None)
- `projection_screen_translucent` (qty: 1 None)
- `worktable_adjustable` (qty: 1 None)
- `measuring_scale_linear` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: light_source_bright
    qty: 1
    unit: None
  - item_id: lens_assembly_magnifying
    qty: 1
    unit: None
  - item_id: projection_screen_translucent
    qty: 1
    unit: None
  - item_id: worktable_adjustable
    qty: 1
    unit: None
  - item_id: measuring_scale_linear
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 1
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 7 components:

- `light_source_bright` (qty: 1 None)
- `lens_assembly_magnifying` (qty: 1 None)
- `projection_screen_translucent` (qty: 1 None)
- `worktable_adjustable` (qty: 1 None)
- `measuring_scale_linear` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: calibration_basic_v0
  inputs:
  - item_id: light_source_bright
    qty: 1
    unit: None
  - item_id: lens_assembly_magnifying
    qty: 1
    unit: None
  - item_id: projection_screen_translucent
    qty: 1
    unit: None
  - item_id: worktable_adjustable
    qty: 1
    unit: None
  - item_id: measuring_scale_linear
    qty: 2
    unit: None
  - item_id: structural_frame_medium
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

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 7 components:

- `light_source_bright` (qty: 1 None)
- `lens_assembly_magnifying` (qty: 1 None)
- `projection_screen_translucent` (qty: 1 None)
- `worktable_adjustable` (qty: 1 None)
- `measuring_scale_linear` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: alignment_and_testing_basic_v0
  inputs:
  - item_id: light_source_bright
    qty: 1
    unit: None
  - item_id: lens_assembly_magnifying
    qty: 1
    unit: None
  - item_id: projection_screen_translucent
    qty: 1
    unit: None
  - item_id: worktable_adjustable
    qty: 1
    unit: None
  - item_id: measuring_scale_linear
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `instrument_calibrated` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_optical_comparator_v0.yaml`
- **BOM available:** Yes (7 components)
