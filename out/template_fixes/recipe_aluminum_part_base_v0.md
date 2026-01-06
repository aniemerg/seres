# Fix Intelligence: recipe_aluminum_part_base_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminum_part_base_v0.yaml`
- **Target item:** `aluminum_part_base`
  - File: `kb/items/aluminum_part_base.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_fabrication_v0') requires input 'aluminum_sheet_2mm' which is not available

**Location:** Step 0
**Process:** `sheet_metal_fabrication_v0`
  - File: `kb/processes/sheet_metal_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_fabrication_v0
  inputs:
  - item_id: aluminum_sheet_2mm
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `aluminum_sheet_2mm` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminum_part_base_v0.yaml`
- **BOM available:** No
