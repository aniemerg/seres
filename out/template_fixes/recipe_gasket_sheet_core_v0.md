# Fix Intelligence: recipe_gasket_sheet_core_v0

## Files

- **Recipe:** `kb/recipes/recipe_gasket_sheet_core_v0.yaml`
- **Target item:** `gasket_sheet_core_v0`
  - File: `kb/items/gasket_sheet_core_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_gasket_sheet_core_part_v0` → gasket_sheet_core_v0_part (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'gasket_sheet_material_v0' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  inputs:
  - item_id: gasket_sheet_material_v0
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `gasket_sheet_material_v0` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_gasket_sheet_core_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
