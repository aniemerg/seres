# Fix Intelligence: recipe_binder_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_binder_material_v0.yaml`
- **Target item:** `binder_material`
  - File: `kb/items/binder_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mixing_and_blending_v0') requires input 'binder_simple' which is not available

**Location:** Step 0
**Process:** `mixing_and_blending_v0`
  - File: `kb/processes/mixing_and_blending_v0.yaml`

**Current step:**
```yaml
- process_id: mixing_and_blending_v0
  inputs:
  - item_id: binder_simple
    qty: 0.5
    unit: kg
  - item_id: ceramic_binder
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `binder_simple` not found

This item doesn't exist in the KB.

#### Problem: Item `ceramic_binder` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_binder_material_v0.yaml`
- **BOM available:** No
