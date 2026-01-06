# Fix Intelligence: recipe_space_frame_structure_v0

## Files

- **Recipe:** `kb/recipes/recipe_space_frame_structure_v0.yaml`
- **Target item:** `space_frame_structure_v0`
  - File: `kb/items/space_frame_structure_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'space_frame_structure_fabrication_v0') requires input 'aluminum_tube_stock' which is not available

**Location:** Step 0
**Process:** `space_frame_structure_fabrication_v0`
  - File: `kb/processes/space_frame_structure_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: space_frame_structure_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_space_frame_structure_v0.yaml`
- **BOM available:** No
