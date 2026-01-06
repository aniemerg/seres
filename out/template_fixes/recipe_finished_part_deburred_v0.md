# Fix Intelligence: recipe_finished_part_deburred_v0

## Files

- **Recipe:** `kb/recipes/recipe_finished_part_deburred_v0.yaml`
- **Target item:** `finished_part_deburred`
  - File: `kb/items/finished_part_deburred.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'finishing_deburring_v0') requires input 'machined_part_raw' which is not available

**Location:** Step 0
**Process:** `finishing_deburring_v0`
  - File: `kb/processes/finishing_deburring_v0.yaml`

**Current step:**
```yaml
- process_id: finishing_deburring_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_finished_part_deburred_v0.yaml`
- **BOM available:** No
