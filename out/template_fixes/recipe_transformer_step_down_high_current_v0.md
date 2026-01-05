# Fix Intelligence: recipe_transformer_step_down_high_current_v0

## Files

- **Recipe:** `kb/recipes/recipe_transformer_step_down_high_current_v0.yaml`
- **Target item:** `transformer_step_down_high_current`
  - File: `kb/items/transformer_step_down_high_current.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_process_general_v0') requires input 'transformer_core' which is not available

**Location:** Step 0
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: transformer_core
    qty: 1.0
    unit: unit
  - item_id: wound_transformer
    qty: 1.0
    unit: unit
  - item_id: heat_sink_assembly_large
    qty: 1.0
    unit: unit
  - item_id: enclosure_steel_large
    qty: 1.0
    unit: unit
  - item_id: shaft_and_bearing_set
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `transformer_core` not found

This item doesn't exist in the KB.

#### Problem: Item `wound_transformer` not found

This item doesn't exist in the KB.

#### Problem: Item `heat_sink_assembly_large` not found

This item doesn't exist in the KB.

#### Problem: Item `enclosure_steel_large` not found

This item doesn't exist in the KB.

#### Problem: Item `shaft_and_bearing_set` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_transformer_step_down_high_current_v0.yaml`
- **BOM available:** No
