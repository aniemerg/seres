# Fix Intelligence: recipe_electrolysis_cell_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrolysis_cell_unit_v0.yaml`
- **Target item:** `electrolysis_cell_unit_v0`
  - File: `kb/items/electrolysis_cell_unit_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrolysis_cell_unit_shell_fabrication_v0') requires input 'steel_sheet_3mm' which is not available

**Location:** Step 0
**Process:** `electrolysis_cell_unit_shell_fabrication_v0`
  - File: `kb/processes/electrolysis_cell_unit_shell_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: electrolysis_cell_unit_shell_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrolysis_cell_unit_v0.yaml`
- **BOM available:** No
