# Fix Intelligence: recipe_vane_set_or_diaphragm_v0

## Files

- **Recipe:** `kb/recipes/recipe_vane_set_or_diaphragm_v0.yaml`
- **Target item:** `vane_set_or_diaphragm`
  - File: `kb/items/vane_set_or_diaphragm.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'nitrile_rubber' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: nitrile_rubber
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nitrile_rubber` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_vane_set_or_diaphragm_v0.yaml`
- **BOM available:** No
