# Fix Intelligence: recipe_bent_tube_sections_v0

## Files

- **Recipe:** `kb/recipes/recipe_bent_tube_sections_v0.yaml`
- **Target item:** `bent_tube_sections`
  - File: `kb/items/bent_tube_sections.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_bending_and_cutting_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `tube_bending_and_cutting_v0`
  - File: `kb/processes/tube_bending_and_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: tube_bending_and_cutting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bent_tube_sections_v0.yaml`
- **BOM available:** No
