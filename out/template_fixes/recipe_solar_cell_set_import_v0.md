# Fix Intelligence: recipe_solar_cell_set_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_solar_cell_set_import_v0.yaml`
- **Target item:** `solar_cell_set`
  - File: `kb/items/solar_cell_set.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'solar_cell_fabrication_v0') requires input 'silicon_single_crystal_ingot' which is not available

**Location:** Step 0
**Process:** `solar_cell_fabrication_v0`
  - File: `kb/processes/solar_cell_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: solar_cell_fabrication_v0
  inputs:
  - item_id: silicon_single_crystal_ingot
    qty: 9.0
    unit: kg
  - item_id: phosphorus_white
    qty: 0.05
    unit: kg
  - item_id: silver_contact_material
    qty: 0.2
    unit: kg
  - item_id: silicon_nitride_ceramic_v0
    qty: 0.1
    unit: kg
  - item_id: etching_chemicals
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `silicon_single_crystal_ingot` not found

This item doesn't exist in the KB.

#### Problem: Item `phosphorus_white` not found

This item doesn't exist in the KB.

#### Problem: Item `silver_contact_material` not found

This item doesn't exist in the KB.

#### Problem: Item `silicon_nitride_ceramic_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `etching_chemicals` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_solar_cell_set_import_v0.yaml`
- **BOM available:** No
