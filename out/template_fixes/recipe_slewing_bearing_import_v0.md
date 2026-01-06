# Fix Intelligence: recipe_slewing_bearing_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_slewing_bearing_import_v0.yaml`
- **Target item:** `slewing_bearing`
  - File: `kb/items/slewing_bearing.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_slewing_bearing_v0` → slewing_bearing (2 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_forging_process_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `metal_forging_process_v0`
  - File: `kb/processes/metal_forging_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_forging_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_slewing_bearing_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
