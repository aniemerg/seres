# Fix Intelligence: recipe_mixer_agitator_shaft_and_paddles_v0

## Files

- **Recipe:** `kb/recipes/recipe_mixer_agitator_shaft_and_paddles_v0.yaml`
- **Target item:** `mixer_agitator_shaft_and_paddles`
  - File: `kb/items/mixer_agitator_shaft_and_paddles.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_bar_stock
    qty: 14.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_bar_stock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_mixer_agitator_shaft_and_paddles_v0.yaml`
- **BOM available:** No
