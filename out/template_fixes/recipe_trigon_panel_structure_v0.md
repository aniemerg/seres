# Fix Intelligence: recipe_trigon_panel_structure_v0

## Files

- **Recipe:** `kb/recipes/recipe_trigon_panel_structure_v0.yaml`
- **Target item:** `trigon_panel_structure_v0`
  - File: `kb/items/trigon_panel_structure_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'panel_structure_formation_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `panel_structure_formation_basic_v0`
  - File: `kb/processes/panel_structure_formation_basic_v0.yaml`

**Current step:**
```yaml
- process_id: panel_structure_formation_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_trigon_panel_structure_v0.yaml`
- **BOM available:** No
