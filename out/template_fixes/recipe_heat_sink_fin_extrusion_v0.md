# Fix Intelligence: recipe_heat_sink_fin_extrusion_v0

## Files

- **Recipe:** `kb/recipes/recipe_heat_sink_fin_extrusion_v0.yaml`
- **Target item:** `heat_sink_fin_extrusion`
  - File: `kb/items/heat_sink_fin_extrusion.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_extrusion_process_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `metal_extrusion_process_v0`
  - File: `kb/processes/metal_extrusion_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_extrusion_process_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 25.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_heat_sink_fin_extrusion_v0.yaml`
- **BOM available:** No
