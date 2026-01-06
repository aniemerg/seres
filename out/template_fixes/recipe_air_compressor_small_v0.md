# Fix Intelligence: recipe_air_compressor_small_v0

## Files

- **Recipe:** `kb/recipes/recipe_air_compressor_small_v0.yaml`
- **Target item:** `air_compressor_small`
  - File: `kb/items/air_compressor_small.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'air_compressor_basic_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 0
**Process:** `air_compressor_basic_v0`
  - File: `kb/processes/air_compressor_basic_v0.yaml`

**Current step:**
```yaml
- process_id: air_compressor_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_air_compressor_small_v0.yaml`
- **BOM available:** No
