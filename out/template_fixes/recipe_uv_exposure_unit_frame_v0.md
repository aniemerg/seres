# Fix Intelligence: recipe_uv_exposure_unit_frame_v0

## Files

- **Recipe:** `kb/recipes/recipe_uv_exposure_unit_frame_v0.yaml`
- **Target item:** `uv_exposure_unit_frame`
  - File: `kb/items/uv_exposure_unit_frame.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_uv_exposure_unit_frame_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `machining_uv_exposure_unit_frame_basic_v0`
  - File: `kb/processes/machining_uv_exposure_unit_frame_basic_v0.yaml`

**Current step:**
```yaml
- process_id: machining_uv_exposure_unit_frame_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_uv_exposure_unit_frame_v0.yaml`
- **BOM available:** No
