# Fix Intelligence: recipe_bulk_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_bulk_material_v0.yaml`
- **Target item:** `bulk_material`
  - File: `kb/items/bulk_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'material_handling_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `material_handling_v0`
  - File: `kb/processes/material_handling_v0.yaml`

**Current step:**
```yaml
- process_id: material_handling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bulk_material_v0.yaml`
- **BOM available:** No
