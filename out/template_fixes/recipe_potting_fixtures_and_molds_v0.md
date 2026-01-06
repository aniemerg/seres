# Fix Intelligence: recipe_potting_fixtures_and_molds_v0

## Files

- **Recipe:** `kb/recipes/recipe_potting_fixtures_and_molds_v0.yaml`
- **Target item:** `potting_fixtures_and_molds`
  - File: `kb/items/potting_fixtures_and_molds.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'fixture_and_mold_fabrication_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `fixture_and_mold_fabrication_v0`
  - File: `kb/processes/fixture_and_mold_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: fixture_and_mold_fabrication_v0
  inputs:
  - item_id: steel_plate_or_sheet
    qty: 12.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `steel_plate_or_sheet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `gasket_sheet_material_v0`
- `gasket_sheet`
- `steel_plate_raw`
- `steel_plate_or_sheet`
- `iron_powder_or_sheet`
- `sheet_metal_or_structural_steel`
- `brass_sheet`
- `nickel_sheet_rolling_forming_v0`
- `steel_sheet_1mm`
- `steel_sheet_3mm`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_potting_fixtures_and_molds_v0.yaml`
- **BOM available:** No
