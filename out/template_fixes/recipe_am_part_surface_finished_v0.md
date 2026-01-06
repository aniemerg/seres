# Fix Intelligence: recipe_am_part_surface_finished_v0

## Files

- **Recipe:** `kb/recipes/recipe_am_part_surface_finished_v0.yaml`
- **Target item:** `am_part_surface_finished_v0`
  - File: `kb/items/am_part_surface_finished_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'surface_finishing_am_parts_v0') requires input 'deposited_metal_structure' which is not available

**Location:** Step 0
**Process:** `surface_finishing_am_parts_v0`
  - File: `kb/processes/surface_finishing_am_parts_v0.yaml`

**Current step:**
```yaml
- process_id: surface_finishing_am_parts_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_am_part_surface_finished_v0.yaml`
- **BOM available:** No
