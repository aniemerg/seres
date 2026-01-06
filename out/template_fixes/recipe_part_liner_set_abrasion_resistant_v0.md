# Fix Intelligence: recipe_part_liner_set_abrasion_resistant_v0

## Files

- **Recipe:** `kb/recipes/recipe_part_liner_set_abrasion_resistant_v0.yaml`
- **Target item:** `liner_set_abrasion_resistant`
  - File: `kb/items/liner_set_abrasion_resistant.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sintering_and_hot_pressing_v0') requires input 'regolith_fine_fraction' which is not available

**Location:** Step 0
**Process:** `sintering_and_hot_pressing_v0`
  - File: `kb/processes/sintering_and_hot_pressing_v0.yaml`

**Current step:**
```yaml
- process_id: sintering_and_hot_pressing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_part_liner_set_abrasion_resistant_v0.yaml`
- **BOM available:** No
