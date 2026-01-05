# Fix Intelligence: recipe_mixed_batch_v0

## Files

- **Recipe:** `kb/recipes/recipe_mixed_batch_v0.yaml`
- **Target item:** `mixed_batch`
  - File: `kb/items/mixed_batch.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mixing_basic_v0') requires input 'powder_components' which is not available

**Location:** Step 0
**Process:** `mixing_basic_v0`
  - File: `kb/processes/mixing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: mixing_basic_v0
  inputs:
  - item_id: powder_components
    qty: 10.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `powder_components` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_mixed_batch_v0.yaml`
- **BOM available:** No
