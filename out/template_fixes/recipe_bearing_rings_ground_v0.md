# Fix Intelligence: recipe_bearing_rings_ground_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_rings_ground_v0.yaml`
- **Target item:** `bearing_rings_ground`
  - File: `kb/items/bearing_rings_ground.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'grinding_process_precision_v0') requires input 'bearing_rings_hardened' which is not available

**Location:** Step 0
**Process:** `grinding_process_precision_v0`
  - File: `kb/processes/grinding_process_precision_v0.yaml`

**Current step:**
```yaml
- process_id: grinding_process_precision_v0
  inputs:
  - item_id: bearing_rings_hardened
    qty: 1.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bearing_rings_hardened` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bearing_rings_ground_v0.yaml`
- **BOM available:** No
