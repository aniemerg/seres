# Fix Intelligence: recipe_copper_plate_or_sheet_v0

## Files

- **Recipe:** `kb/recipes/recipe_copper_plate_or_sheet_v0.yaml`
- **Target item:** `copper_plate_or_sheet`
  - File: `kb/items/copper_plate_or_sheet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_making_from_copper_ingot_to_copper_sheet_v0') requires input 'copper_rod_ingot' which is not available

**Location:** Step 0
**Process:** `sheet_making_from_copper_ingot_to_copper_sheet_v0`
  - File: `kb/processes/sheet_making_from_copper_ingot_to_copper_sheet_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_making_from_copper_ingot_to_copper_sheet_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_copper_plate_or_sheet_v0.yaml`
- **BOM available:** No
