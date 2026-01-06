# Fix Intelligence: recipe_nickel_wire_fine_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_wire_fine_v0.yaml`
- **Target item:** `nickel_wire_fine`
  - File: `kb/items/nickel_wire_fine.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_nickel_wire_fine_v1` → nickel_wire_fine (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_drawing_basic_v0') requires input 'nickel_metal_pure' which is not available

**Location:** Step 0
**Process:** `wire_drawing_basic_v0`
  - File: `kb/processes/wire_drawing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wire_drawing_basic_v0
  inputs:
  - item_id: nickel_metal_pure
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nickel_metal_pure` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nickel_wire_fine_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
