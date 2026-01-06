# Fix Intelligence: recipe_metal_powder_sieving_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_metal_powder_sieving_system_v0.yaml`
- **Target item:** `metal_powder_sieving_system_v0`
  - File: `kb/items/metal_powder_sieving_system_v0.yaml`
- **BOM:** `kb/boms/bom_metal_powder_sieving_system_v0.yaml` ✓
  - Components: 5
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

BOM has 5 components:

- `screen_deck_basic` (qty: 1.0 None)
- `vibrator_motor_small` (qty: 1.0 None)
- `machine_frame_small` (qty: 1.0 None)
- `collection_hopper_set` (qty: 1.0 None)
- `power_conditioning_module` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: screen_deck_basic
    qty: 1.0
    unit: None
  - item_id: vibrator_motor_small
    qty: 1.0
    unit: None
  - item_id: machine_frame_small
    qty: 1.0
    unit: None
  - item_id: collection_hopper_set
    qty: 1.0
    unit: None
  - item_id: power_conditioning_module
    qty: 1.0
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metal_powder_sieving_system_v0.yaml`
- **BOM available:** Yes (5 components)
