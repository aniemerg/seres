# Fix Intelligence: recipe_stainless_steel_bar_v0

## Files

- **Recipe:** `kb/recipes/recipe_stainless_steel_bar_v0.yaml`
- **Target item:** `stainless_steel_bar`
  - File: `kb/items/stainless_steel_bar.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'rolling_process_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `rolling_process_v0`
  - File: `kb/processes/rolling_process_v0.yaml`

**Current step:**
```yaml
- process_id: rolling_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_stainless_steel_bar_v0.yaml`
- **BOM available:** No
