# Fix Intelligence: recipe_hydraulic_hose_segment_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_hose_segment_v0.yaml`
- **Target item:** `hydraulic_hose_segment_v0`
  - File: `kb/items/hydraulic_hose_segment_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hose_segment_fabrication_v0') requires input 'nitrile_rubber' which is not available

**Location:** Step 0
**Process:** `hose_segment_fabrication_v0`
  - File: `kb/processes/hose_segment_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: hose_segment_fabrication_v0
  inputs:
  - item_id: nitrile_rubber
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nitrile_rubber` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hydraulic_hose_segment_v0.yaml`
- **BOM available:** No
