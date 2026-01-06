# Fix Intelligence: recipe_cobalt_sulfate_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_cobalt_sulfate_solution_v0.yaml`
- **Target item:** `cobalt_sulfate_solution`
  - File: `kb/items/cobalt_sulfate_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cobalt_sulfate_extraction_v0') requires input 'cobalt_metal_impure' which is not available

**Location:** Step 0
**Process:** `cobalt_sulfate_extraction_v0`
  - File: `kb/processes/cobalt_sulfate_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: cobalt_sulfate_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cobalt_sulfate_solution_v0.yaml`
- **BOM available:** No
