# Fix Intelligence: recipe_cacl2_electrolyte_v0

## Files

- **Recipe:** `kb/recipes/recipe_cacl2_electrolyte_v0.yaml`
- **Target item:** `cacl2_electrolyte_v0`
  - File: `kb/items/cacl2_electrolyte_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cacl2_electrolyte_production_v0') requires input 'calcium_chloride_dihydrate_v0' which is not available

**Location:** Step 0
**Process:** `cacl2_electrolyte_production_v0`
  - File: `kb/processes/cacl2_electrolyte_production_v0.yaml`

**Current step:**
```yaml
- process_id: cacl2_electrolyte_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cacl2_electrolyte_v0.yaml`
- **BOM available:** No
