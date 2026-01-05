# Fix Intelligence: recipe_power_distribution_panel_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_distribution_panel_basic_v0.yaml`
- **Target item:** `power_distribution_panel_basic`
  - File: `kb/items/power_distribution_panel_basic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'power_distribution_panel_assembly_v0') requires input 'formed_sheet_metal_parts' which is not available

**Location:** Step 0
**Process:** `power_distribution_panel_assembly_v0`
  - File: `kb/processes/power_distribution_panel_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: power_distribution_panel_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_power_distribution_panel_basic_v0.yaml`
- **BOM available:** No
