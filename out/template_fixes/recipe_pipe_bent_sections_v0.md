# Fix Intelligence: recipe_pipe_bent_sections_v0

## Files

- **Recipe:** `kb/recipes/recipe_pipe_bent_sections_v0.yaml`
- **Target item:** `pipe_bent_sections`
  - File: `kb/items/pipe_bent_sections.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_bending_process_v0') requires input 'aluminum_tube_stock' which is not available

**Location:** Step 0
**Process:** `tube_bending_process_v0`
  - File: `kb/processes/tube_bending_process_v0.yaml`

**Current step:**
```yaml
- process_id: tube_bending_process_v0
  inputs:
  - item_id: aluminum_tube_stock
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_tube_stock` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pipe_bent_sections_v0.yaml`
- **BOM available:** No
