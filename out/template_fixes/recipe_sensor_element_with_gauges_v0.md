# Fix Intelligence: recipe_sensor_element_with_gauges_v0

## Files

- **Recipe:** `kb/recipes/recipe_sensor_element_with_gauges_v0.yaml`
- **Target item:** `sensor_element_with_gauges`
  - File: `kb/items/sensor_element_with_gauges.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'strain_gauge_bonding_process_v0') requires input 'strain_gauge_foil_v0' which is not available

**Location:** Step 0
**Process:** `strain_gauge_bonding_process_v0`
  - File: `kb/processes/strain_gauge_bonding_process_v0.yaml`

**Current step:**
```yaml
- process_id: strain_gauge_bonding_process_v0
  inputs:
  - item_id: strain_gauge_foil_v0
    qty: 1.0
    unit: each
  - item_id: adhesive_cyanoacrylate
    qty: 0.002
    unit: kg
  - item_id: test_part_surface
    qty: 1.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `strain_gauge_foil_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `adhesive_cyanoacrylate` not found

This item doesn't exist in the KB.

#### Problem: Item `test_part_surface` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sensor_element_with_gauges_v0.yaml`
- **BOM available:** No
