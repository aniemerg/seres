# Fix Intelligence: recipe_electrolyte_koh_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrolyte_koh_solution_v0.yaml`
- **Target item:** `electrolyte_koh_solution`
  - File: `kb/items/electrolyte_koh_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrolyte_prep_koh') requires input 'potassium_hydroxide' which is not available

**Location:** Step 0
**Process:** `electrolyte_prep_koh`
  - File: `kb/processes/electrolyte_prep_koh.yaml`

**Current step:**
```yaml
- process_id: electrolyte_prep_koh
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrolyte_koh_solution_v0.yaml`
- **BOM available:** No
