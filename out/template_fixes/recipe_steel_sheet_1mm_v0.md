# Fix Intelligence: recipe_steel_sheet_1mm_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_sheet_1mm_v0.yaml`
- **Target item:** `steel_sheet_1mm`
  - File: `kb/items/steel_sheet_1mm.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_making_from_ingot_1mm_v0') requires input 'steel_ingot' which is not available

**Location:** Step 0
**Process:** `sheet_making_from_ingot_1mm_v0`
  - File: `kb/processes/sheet_making_from_ingot_1mm_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_making_from_ingot_1mm_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_sheet_1mm_v0.yaml`
- **BOM available:** No
