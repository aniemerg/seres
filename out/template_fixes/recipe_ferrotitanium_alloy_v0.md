# Fix Intelligence: recipe_ferrotitanium_alloy_v0

## Files

- **Recipe:** `kb/recipes/recipe_ferrotitanium_alloy_v0.yaml`
- **Target item:** `ferrotitanium_alloy`
  - File: `kb/items/ferrotitanium_alloy.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ffc_ilmenite_feti_alloy_v0') requires input 'ilmenite_concentrate' which is not available

**Location:** Step 0
**Process:** `ffc_ilmenite_feti_alloy_v0`
  - File: `kb/processes/ffc_ilmenite_feti_alloy_v0.yaml`

**Current step:**
```yaml
- process_id: ffc_ilmenite_feti_alloy_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ferrotitanium_alloy_v0.yaml`
- **BOM available:** No
