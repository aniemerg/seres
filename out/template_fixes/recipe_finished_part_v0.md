# Fix Intelligence: recipe_finished_part_v0

## Files

- **Recipe:** `kb/recipes/recipe_finished_part_v0.yaml`
- **Target item:** `finished_part`
  - File: `kb/items/finished_part.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'grinding_and_finishing_v0') requires input 'rough_part' which is not available

**Location:** Step 0
**Process:** `grinding_and_finishing_v0`
  - File: `kb/processes/grinding_and_finishing_v0.yaml`

**Current step:**
```yaml
- process_id: grinding_and_finishing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_finished_part_v0.yaml`
- **BOM available:** No
