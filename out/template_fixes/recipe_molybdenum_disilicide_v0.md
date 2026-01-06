# Fix Intelligence: recipe_molybdenum_disilicide_v0

## Files

- **Recipe:** `kb/recipes/recipe_molybdenum_disilicide_v0.yaml`
- **Target item:** `molybdenum_disilicide`
  - File: `kb/items/molybdenum_disilicide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'stock_material' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  inputs:
  - item_id: stock_material
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `stock_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_molybdenum_disilicide_v0.yaml`
- **BOM available:** No
