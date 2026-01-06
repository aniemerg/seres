# Fix Intelligence: recipe_metal_wire_feed_v0

## Files

- **Recipe:** `kb/recipes/recipe_metal_wire_feed_v0.yaml`
- **Target item:** `metal_wire_feed`
  - File: `kb/items/metal_wire_feed.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_wire_drawing_process_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `metal_wire_drawing_process_v0`
  - File: `kb/processes/metal_wire_drawing_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_wire_drawing_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metal_wire_feed_v0.yaml`
- **BOM available:** No
