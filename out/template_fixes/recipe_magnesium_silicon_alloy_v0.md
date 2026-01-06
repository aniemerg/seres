# Fix Intelligence: recipe_magnesium_silicon_alloy_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnesium_silicon_alloy_v0.yaml`
- **Target item:** `magnesium_silicon_alloy`
  - File: `kb/items/magnesium_silicon_alloy.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ffc_olivine_mgsi_alloy_v0') requires input 'olivine_concentrate' which is not available

**Location:** Step 0
**Process:** `ffc_olivine_mgsi_alloy_v0`
  - File: `kb/processes/ffc_olivine_mgsi_alloy_v0.yaml`

**Current step:**
```yaml
- process_id: ffc_olivine_mgsi_alloy_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnesium_silicon_alloy_v0.yaml`
- **BOM available:** No
