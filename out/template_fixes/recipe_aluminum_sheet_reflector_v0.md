# Fix Intelligence: recipe_aluminum_sheet_reflector_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminum_sheet_reflector_v0.yaml`
- **Target item:** `aluminum_sheet_reflector_v0`
  - File: `kb/items/aluminum_sheet_reflector_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aluminum_sheet_reflector_fabrication_v0') requires input 'aluminum_sheet_2mm' which is not available

**Location:** Step 0
**Process:** `aluminum_sheet_reflector_fabrication_v0`
  - File: `kb/processes/aluminum_sheet_reflector_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: aluminum_sheet_reflector_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminum_sheet_reflector_v0.yaml`
- **BOM available:** No
