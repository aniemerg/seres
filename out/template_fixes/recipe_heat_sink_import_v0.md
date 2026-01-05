# Fix Intelligence: recipe_heat_sink_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_heat_sink_import_v0.yaml`
- **Target item:** `heat_sink`
  - File: `kb/items/heat_sink.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_heat_sink_v0` → heat_sink (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'heat_sink_extrusion_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `heat_sink_extrusion_v0`
  - File: `kb/processes/heat_sink_extrusion_v0.yaml`

**Current step:**
```yaml
- process_id: heat_sink_extrusion_v0
  inputs:
  - item_id: aluminum_alloy_ingot
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_alloy_ingot` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_heat_sink_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
