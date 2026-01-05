# Fix Intelligence: recipe_hose_end_fittings_v0

## Files

- **Recipe:** `kb/recipes/recipe_hose_end_fittings_v0.yaml`
- **Target item:** `hose_end_fittings_v0`
  - File: `kb/items/hose_end_fittings_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hose_end_fittings_fabrication_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `hose_end_fittings_fabrication_v0`
  - File: `kb/processes/hose_end_fittings_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: hose_end_fittings_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hose_end_fittings_v0.yaml`
- **BOM available:** No
