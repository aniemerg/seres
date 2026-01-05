# Fix Intelligence: recipe_load_cell_strain_gauge_v0

## Files

- **Recipe:** `kb/recipes/recipe_load_cell_strain_gauge_v0.yaml`
- **Target item:** `load_cell_strain_gauge_v0`
  - File: `kb/items/load_cell_strain_gauge_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'load_cell_strain_gauge_fabrication_v0') requires input 'strain_gauge_foil_v0' which is not available

**Location:** Step 0
**Process:** `load_cell_strain_gauge_fabrication_v0`
  - File: `kb/processes/load_cell_strain_gauge_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: load_cell_strain_gauge_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_load_cell_strain_gauge_v0.yaml`
- **BOM available:** No
