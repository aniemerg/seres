# Fix Intelligence: recipe_ceramic_substrate_rtd_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_substrate_rtd_v0.yaml`
- **Target item:** `ceramic_substrate_rtd`
  - File: `kb/items/ceramic_substrate_rtd.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ceramic_sintering_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `ceramic_sintering_v0`
  - File: `kb/processes/ceramic_sintering_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_sintering_v0
  inputs:
  - item_id: alumina_powder
    qty: 0.01
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ceramic_substrate_rtd_v0.yaml`
- **BOM available:** No
