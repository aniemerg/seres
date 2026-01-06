# Fix Intelligence: recipe_nife_meteorite_magnetic_detection_v0

## Files

- **Recipe:** `kb/recipes/recipe_nife_meteorite_magnetic_detection_v0.yaml`
- **Target item:** `nife_meteorite_magnetic_detection_v0`
  - File: `kb/items/nife_meteorite_magnetic_detection_v0.yaml`
- **BOM:** `kb/boms/bom_nife_meteorite_magnetic_detection_v0.yaml` ✓
  - Components: 3
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'frame_fabrication_from_raw_metal_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `frame_fabrication_from_raw_metal_v0`
  - File: `kb/processes/frame_fabrication_from_raw_metal_v0.yaml`

**Current step:**
```yaml
- process_id: frame_fabrication_from_raw_metal_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

BOM has 3 components:

- `sensor_suite_general` (qty: 1 None)
- `electronic_components_set` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formation_rack_frame` (200.0 kg)

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

BOM has 3 components:

- `sensor_suite_general` (qty: 1 None)
- `electronic_components_set` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formation_rack_frame` (200.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 3 components:

- `sensor_suite_general` (qty: 1 None)
- `electronic_components_set` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: calibration_basic_v0
  inputs:
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formation_rack_frame` (200.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_nife_meteorite_magnetic_detection_v0.yaml`
- **BOM available:** Yes (3 components)
