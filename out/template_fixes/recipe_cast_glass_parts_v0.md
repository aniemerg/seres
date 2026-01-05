# Fix Intelligence: recipe_cast_glass_parts_v0

## Files

- **Recipe:** `kb/recipes/recipe_cast_glass_parts_v0.yaml`
- **Target item:** `cast_glass_parts`
  - File: `kb/items/cast_glass_parts.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_casting_v0') requires input 'glass_raw_materials' which is not available

**Location:** Step 0
**Process:** `glass_casting_v0`
  - File: `kb/processes/glass_casting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_casting_v0
  inputs:
  - item_id: glass_raw_materials
    qty: 5.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `glass_raw_materials` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cast_glass_parts_v0.yaml`
- **BOM available:** No
