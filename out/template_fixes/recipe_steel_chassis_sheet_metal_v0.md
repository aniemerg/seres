# Fix Intelligence: recipe_steel_chassis_sheet_metal_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_chassis_sheet_metal_v0.yaml`
- **Target item:** `steel_chassis_sheet_metal`
  - File: `kb/items/steel_chassis_sheet_metal.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_forming_process_v0') requires input 'steel_sheet_3mm' which is not available

**Location:** Step 0
**Process:** `sheet_metal_forming_process_v0`
  - File: `kb/processes/sheet_metal_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_forming_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_chassis_sheet_metal_v0.yaml`
- **BOM available:** No
