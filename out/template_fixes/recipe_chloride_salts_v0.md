# Fix Intelligence: recipe_chloride_salts_v0

## Files

- **Recipe:** `kb/recipes/recipe_chloride_salts_v0.yaml`
- **Target item:** `chloride_salts_v0`
  - File: `kb/items/chloride_salts_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hcl_recovery_distillation_v0') requires input 'spent_solution_v0' which is not available

**Location:** Step 0
**Process:** `hcl_recovery_distillation_v0`
  - File: `kb/processes/hcl_recovery_distillation_v0.yaml`

**Current step:**
```yaml
- process_id: hcl_recovery_distillation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_chloride_salts_v0.yaml`
- **BOM available:** No
