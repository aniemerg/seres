# Fix Intelligence: recipe_material_annealed_v0

## Files

- **Recipe:** `kb/recipes/recipe_material_annealed_v0.yaml`
- **Target item:** `material_annealed`
  - File: `kb/items/material_annealed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'annealing_v0') requires input 'material_unannealed' which is not available

**Location:** Step 0
**Process:** `annealing_v0`
  - File: `kb/processes/annealing_v0.yaml`

**Current step:**
```yaml
- process_id: annealing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_material_annealed_v0.yaml`
- **BOM available:** No
