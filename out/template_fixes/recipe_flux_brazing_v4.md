# Fix Intelligence: recipe_flux_brazing_v4

## Files

- **Recipe:** `kb/recipes/recipe_flux_brazing_v4.yaml`
- **Target item:** `flux_brazing`
  - File: `kb/items/flux_brazing.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'flux_brazing_synthesis_v0') requires input 'sodium_carbonate' which is not available

**Location:** Step 0
**Process:** `flux_brazing_synthesis_v0`
  - File: `kb/processes/flux_brazing_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: flux_brazing_synthesis_v0
  inputs:
  - item_id: sodium_carbonate
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `sodium_carbonate` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_flux_brazing_v4.yaml`
- **BOM available:** No
