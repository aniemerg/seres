# Fix Intelligence: recipe_dynamic_balancing_stand_v0_alt_v0

## Files

- **Recipe:** `kb/recipes/recipe_dynamic_balancing_stand_v0_alt_v0.yaml`
- **Target item:** `dynamic_balancing_stand_v0`
  - File: `kb/items/dynamic_balancing_stand_v0.yaml`
- **BOM:** `kb/boms/bom_dynamic_balancing_stand_v0.yaml` ✓
  - Components: 4
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_dynamic_balancing_stand_v0` → dynamic_balancing_stand_v0 (1 steps)

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

BOM has 4 components:

- `machine_frame_medium` (qty: 1 None)
- `drive_motor_small` (qty: 1 None)
- `bearing_set_heavy` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1
    unit: None
  - item_id: drive_motor_small
    qty: 1
    unit: None
  - item_id: bearing_set_heavy
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_dynamic_balancing_stand_v0_alt_v0.yaml`
- **BOM available:** Yes (4 components)
- **Similar recipes:** 1 found
