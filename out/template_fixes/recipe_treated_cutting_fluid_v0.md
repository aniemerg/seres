# Fix Intelligence: recipe_treated_cutting_fluid_v0

## Files

- **Recipe:** `kb/recipes/recipe_treated_cutting_fluid_v0.yaml`
- **Target item:** `treated_cutting_fluid_v0`
  - File: `kb/items/treated_cutting_fluid_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_treatment_v0') requires input 'cutting_fluid' which is not available

**Location:** Step 0
**Process:** `chemical_treatment_v0`
  - File: `kb/processes/chemical_treatment_v0.yaml`

**Current step:**
```yaml
- process_id: chemical_treatment_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_treated_cutting_fluid_v0.yaml`
- **BOM available:** No
