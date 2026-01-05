# Fix Intelligence: recipe_ilmenite_concentrate_v0

## Files

- **Recipe:** `kb/recipes/recipe_ilmenite_concentrate_v0.yaml`
- **Target item:** `ilmenite_concentrate`
  - File: `kb/items/ilmenite_concentrate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'beneficiate_regolith_magnetic_v0') requires input 'regolith_powder' which is not available

**Location:** Step 0
**Process:** `beneficiate_regolith_magnetic_v0`
  - File: `kb/processes/beneficiate_regolith_magnetic_v0.yaml`

**Current step:**
```yaml
- process_id: beneficiate_regolith_magnetic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ilmenite_concentrate_v0.yaml`
- **BOM available:** No
