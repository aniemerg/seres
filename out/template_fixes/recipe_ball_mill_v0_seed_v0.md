# Fix Intelligence: recipe_ball_mill_v0_seed_v0

## Files

- **Recipe:** `kb/recipes/recipe_ball_mill_v0_seed_v0.yaml`
- **Target item:** `ball_mill_v0`
  - File: `kb/items/ball_mill_v0.yaml`
- **BOM:** `kb/boms/bom_ball_mill_v0.yaml` ✓
  - Components: 8
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_ball_mill_v0` → ball_mill_v0 (1 steps)
- `recipe_ball_mill_v0` → ball_mill_v0 (4 steps)

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

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ball_mill_v0_seed_v0.yaml`
- **BOM available:** Yes (8 components)
- **Similar recipes:** 2 found
