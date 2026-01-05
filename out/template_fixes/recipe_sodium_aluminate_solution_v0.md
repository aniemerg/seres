# Fix Intelligence: recipe_sodium_aluminate_solution_v0

## Files

- **Recipe:** `kb/recipes/recipe_sodium_aluminate_solution_v0.yaml`
- **Target item:** `sodium_aluminate_solution`
  - File: `kb/items/sodium_aluminate_solution.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'anorthite_lime_soda_process_v0') requires input 'anorthite_ore' which is not available

**Location:** Step 0
**Process:** `anorthite_lime_soda_process_v0`
  - File: `kb/processes/anorthite_lime_soda_process_v0.yaml`

**Current step:**
```yaml
- process_id: anorthite_lime_soda_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sodium_aluminate_solution_v0.yaml`
- **BOM available:** No
