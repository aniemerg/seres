# Fix Intelligence: recipe_machine_magnetic_separator_drum_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_magnetic_separator_drum_v0.yaml`
- **Target item:** `magnetic_separator_drum_v0`
  - File: `kb/items/magnetic_separator_drum_v0.yaml`
- **BOM:** `kb/boms/bom_magnetic_separator_drum_v0.yaml` ✓
  - Components: 9
- **Steps:** 1 total

## Errors (1 found)

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

BOM has 9 components:

- `magnetic_separator_drum_body` (qty: 1 None)
- `magnet_assembly` (qty: 1 None)
- `separator_frame` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `bearing_set_heavy` (qty: 2 None)
- `vibratory_feeder_v0` (qty: 1 unit)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: magnetic_separator_drum_body
    qty: 1
    unit: None
  - item_id: magnet_assembly
    qty: 1
    unit: None
  - item_id: separator_frame
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 2
    unit: None
  - item_id: vibratory_feeder_v0
    qty: 1
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machine_magnetic_separator_drum_v0.yaml`
- **BOM available:** Yes (9 components)
