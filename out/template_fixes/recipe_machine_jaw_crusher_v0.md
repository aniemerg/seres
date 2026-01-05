# Fix Intelligence: recipe_machine_jaw_crusher_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_jaw_crusher_v0.yaml`
- **Target item:** `jaw_crusher_v0`
  - File: `kb/items/jaw_crusher_v0.yaml`
- **BOM:** `kb/boms/bom_jaw_crusher_v0.yaml` ✓
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

- `crusher_frame_medium` (qty: 1 None)
- `jaw_plates_set` (qty: 1 None)
- `flywheel_medium` (qty: 1 None)
- `toggle_mechanism_set` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `bearing_set_heavy` (qty: 2 None)
- `support_frame_welded` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: crusher_frame_medium
    qty: 1
    unit: None
  - item_id: jaw_plates_set
    qty: 1
    unit: None
  - item_id: flywheel_medium
    qty: 1
    unit: None
  - item_id: toggle_mechanism_set
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 2
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machine_jaw_crusher_v0.yaml`
- **BOM available:** Yes (9 components)
