# Fix Intelligence: recipe_high_temp_additive_v0

## Files

- **Recipe:** `kb/recipes/recipe_high_temp_additive_v0.yaml`
- **Target item:** `high_temp_additive_v0`
  - File: `kb/items/high_temp_additive_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'high_temp_additive_synthesis_v0') requires input 'mos2_solid_lubricant_v0' which is not available

**Location:** Step 0
**Process:** `high_temp_additive_synthesis_v0`
  - File: `kb/processes/high_temp_additive_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: high_temp_additive_synthesis_v0
  inputs:
  - item_id: mos2_solid_lubricant_v0
    qty: 0.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `mos2_solid_lubricant_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_high_temp_additive_v0.yaml`
- **BOM available:** No
