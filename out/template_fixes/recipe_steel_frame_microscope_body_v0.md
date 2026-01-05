# Fix Intelligence: recipe_steel_frame_microscope_body_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_frame_microscope_body_v0.yaml`
- **Target item:** `steel_frame_microscope_body`
  - File: `kb/items/steel_frame_microscope_body.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_finish_basic_v0') requires input 'steel_block_raw_v0' which is not available

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_block_raw_v0
    qty: 9.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `steel_block_raw_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_frame_microscope_body_v0.yaml`
- **BOM available:** No
