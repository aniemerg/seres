# Fix Intelligence: recipe_permanent_magnet_neodymium_v0

## Files

- **Recipe:** `kb/recipes/recipe_permanent_magnet_neodymium_v0.yaml`
- **Target item:** `permanent_magnet_neodymium`
  - File: `kb/items/permanent_magnet_neodymium.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ndfeb_magnet_sintering_v0') requires input 'processed_powder_mixture' which is not available

**Location:** Step 0
**Process:** `ndfeb_magnet_sintering_v0`
  - File: `kb/processes/ndfeb_magnet_sintering_v0.yaml`

**Current step:**
```yaml
- process_id: ndfeb_magnet_sintering_v0
  inputs:
  - item_id: processed_powder_mixture
    qty: 1.05
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `processed_powder_mixture` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_permanent_magnet_neodymium_v0.yaml`
- **BOM available:** No
