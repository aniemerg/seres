# Fix Intelligence: recipe_protective_coating_aluminum_v0

## Files

- **Recipe:** `kb/recipes/recipe_protective_coating_aluminum_v0.yaml`
- **Target item:** `protective_coating_aluminum`
  - File: `kb/items/protective_coating_aluminum.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mixing_basic_v0') requires input 'aluminum_metal_pure' which is not available

**Location:** Step 0
**Process:** `mixing_basic_v0`
  - File: `kb/processes/mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: mixing_basic_v0
  inputs:
  - item_id: aluminum_metal_pure
    qty: 0.7
    unit: kg
  - item_id: binder_material
    qty: 0.3
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_metal_pure` not found

This item doesn't exist in the KB.

#### Problem: Item `binder_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_protective_coating_aluminum_v0.yaml`
- **BOM available:** No
