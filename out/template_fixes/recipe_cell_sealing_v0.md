# Fix Intelligence: recipe_cell_sealing_v0

## Files

- **Recipe:** `kb/recipes/recipe_cell_sealing_v0.yaml`
- **Target item:** `cell_sealing`
  - File: `kb/items/cell_sealing.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cell_sealing_fabrication_v0') requires input 'silicone_polymer' which is not available

**Location:** Step 0
**Process:** `cell_sealing_fabrication_v0`
  - File: `kb/processes/cell_sealing_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: cell_sealing_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cell_sealing_v0.yaml`
- **BOM available:** No
