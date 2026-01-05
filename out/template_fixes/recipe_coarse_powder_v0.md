# Fix Intelligence: recipe_coarse_powder_v0

## Files

- **Recipe:** `kb/recipes/recipe_coarse_powder_v0.yaml`
- **Target item:** `coarse_powder`
  - File: `kb/items/coarse_powder.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'coarse_powder_production_v0') requires input 'regolith_coarse_fraction' which is not available

**Location:** Step 0
**Process:** `coarse_powder_production_v0`
  - File: `kb/processes/coarse_powder_production_v0.yaml`

**Current step:**
```yaml
- process_id: coarse_powder_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coarse_powder_v0.yaml`
- **BOM available:** No
