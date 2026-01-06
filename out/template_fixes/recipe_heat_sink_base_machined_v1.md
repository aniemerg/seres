# Fix Intelligence: recipe_heat_sink_base_machined_v1

## Files

- **Recipe:** `kb/recipes/recipe_heat_sink_base_machined_v1.yaml`
- **Target item:** `heat_sink_base_machined`
  - File: `kb/items/heat_sink_base_machined.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_heat_sink_base_machined_v0` → heat_sink_base_machined (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'aluminum_housing_machined' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: aluminum_housing_machined
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_housing_machined` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_heat_sink_base_machined_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
