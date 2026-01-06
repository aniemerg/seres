# Fix Intelligence: recipe_etching_waste_solution_v3

## Files

- **Recipe:** `kb/recipes/recipe_etching_waste_solution_v3.yaml`
- **Target item:** `etching_waste_solution`
  - File: `kb/items/etching_waste_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_etching_waste_solution_v1` → etching_waste_solution (1 steps)
- `recipe_etching_waste_solution_v0` → etching_waste_solution (1 steps)
- `recipe_etching_waste_solution_v2` → etching_waste_solution (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'copper_etching_process_v0') requires input 'copper_clad_laminate' which is not available

**Location:** Step 0
**Process:** `copper_etching_process_v0`
  - File: `kb/processes/copper_etching_process_v0.yaml`

**Current step:**
```yaml
- process_id: copper_etching_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_etching_waste_solution_v3.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
