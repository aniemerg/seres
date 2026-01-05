# Fix Intelligence: recipe_kovar_alloy_fe_ni_co_v0

## Files

- **Recipe:** `kb/recipes/recipe_kovar_alloy_fe_ni_co_v0.yaml`
- **Target item:** `kovar_alloy_fe_ni_co_v0`
  - File: `kb/items/kovar_alloy_fe_ni_co_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'kovar_alloy_production_v0') requires input 'powder_mixture' which is not available

**Location:** Step 0
**Process:** `kovar_alloy_production_v0`
  - File: `kb/processes/kovar_alloy_production_v0.yaml`

**Current step:**
```yaml
- process_id: kovar_alloy_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_kovar_alloy_fe_ni_co_v0.yaml`
- **BOM available:** No
