# Fix Intelligence: recipe_salt_waste_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_salt_waste_solution_v0.yaml`
- **Target item:** `salt_waste_solution`
  - File: `kb/items/salt_waste_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'precipitation_and_washing_v0') requires input 'cmc_solution' which is not available

**Location:** Step 0
**Process:** `precipitation_and_washing_v0`
  - File: `kb/processes/precipitation_and_washing_v0.yaml`

**Current step:**
```yaml
- process_id: precipitation_and_washing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_salt_waste_solution_v0.yaml`
- **BOM available:** No
