# Fix Intelligence: recipe_formation_rack_frame_v0

## Files

- **Recipe:** `kb/recipes/recipe_formation_rack_frame_v0.yaml`
- **Target item:** `formation_rack_frame`
  - File: `kb/items/formation_rack_frame.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'frame_fabrication_from_raw_metal_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `frame_fabrication_from_raw_metal_v0`
  - File: `kb/processes/frame_fabrication_from_raw_metal_v0.yaml`

**Current step:**
```yaml
- process_id: frame_fabrication_from_raw_metal_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_formation_rack_frame_v0.yaml`
- **BOM available:** No
