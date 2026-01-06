# Fix Intelligence: recipe_battery_pack_medium_v0

## Files

- **Recipe:** `kb/recipes/recipe_battery_pack_medium_v0.yaml`
- **Target item:** `battery_pack_medium`
  - File: `kb/items/battery_pack_medium.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'battery_cell_casing_metal' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: battery_cell_casing_metal
    qty: 5.0
    unit: kg
  - item_id: electrodes_nife_set
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `battery_cell_casing_metal` not found

This item doesn't exist in the KB.

#### Problem: Item `electrodes_nife_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_battery_pack_medium_v0.yaml`
- **BOM available:** No
