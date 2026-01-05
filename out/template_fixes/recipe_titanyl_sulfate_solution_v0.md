# Fix Intelligence: recipe_titanyl_sulfate_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_titanyl_sulfate_solution_v0.yaml`
- **Target item:** `titanyl_sulfate_solution`
  - File: `kb/items/titanyl_sulfate_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ilmenite_sulfuric_acid_route_v0') requires input 'ilmenite_concentrate' which is not available

**Location:** Step 0
**Process:** `ilmenite_sulfuric_acid_route_v0`
  - File: `kb/processes/ilmenite_sulfuric_acid_route_v0.yaml`

**Current step:**
```yaml
- process_id: ilmenite_sulfuric_acid_route_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_titanyl_sulfate_solution_v0.yaml`
- **BOM available:** No
