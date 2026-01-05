# Fix Intelligence: recipe_plastic_pellets_v0

## Files

- **Recipe:** `kb/recipes/recipe_plastic_pellets_v0.yaml`
- **Target item:** `plastic_pellets`
  - File: `kb/items/plastic_pellets.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'polymer_pelletization_v0') requires input 'polymer_printing_feedstock' which is not available

**Location:** Step 0
**Process:** `polymer_pelletization_v0`
  - File: `kb/processes/polymer_pelletization_v0.yaml`

**Current step:**
```yaml
- process_id: polymer_pelletization_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_plastic_pellets_v0.yaml`
- **BOM available:** No
