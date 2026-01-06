# Fix Intelligence: recipe_neural_analog_tile_v0

## Files

- **Recipe:** `kb/recipes/recipe_neural_analog_tile_v0.yaml`
- **Target item:** `neural_analog_tile`
  - File: `kb/items/neural_analog_tile.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'neural_analog_tile_generation_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `neural_analog_tile_generation_v0`
  - File: `kb/processes/neural_analog_tile_generation_v0.yaml`

**Current step:**
```yaml
- process_id: neural_analog_tile_generation_v0
  inputs:
  - item_id: pcb_populated
    qty: 1.0
    unit: unit
  - item_id: wire_copper_insulated
    qty: 0.05
    unit: kg
  - item_id: fastener_kit_small
    qty: 0.1
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `pcb_populated` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_neural_analog_tile_v0.yaml`
- **BOM available:** No
