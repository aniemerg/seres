# Fix Intelligence: recipe_camera_vacuum_tube_vidicon_v0

## Files

- **Recipe:** `kb/recipes/recipe_camera_vacuum_tube_vidicon_v0.yaml`
- **Target item:** `camera_vacuum_tube_vidicon_v0`
  - File: `kb/items/camera_vacuum_tube_vidicon_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'camera_vacuum_tube_vidicon_v0') requires input 'glass_envelope_vacuum_tube_v0' which is not available

**Location:** Step 0
**Process:** `camera_vacuum_tube_vidicon_v0`
  - File: `kb/processes/camera_vacuum_tube_vidicon_v0.yaml`

**Current step:**
```yaml
- process_id: camera_vacuum_tube_vidicon_v0
  inputs:
  - item_id: glass_envelope_vacuum_tube_v0
    qty: 1.0
    unit: unit
  - item_id: vacuum_tube_subassembly
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `glass_envelope_vacuum_tube_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `vacuum_tube_subassembly` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_camera_vacuum_tube_vidicon_v0.yaml`
- **BOM available:** No
