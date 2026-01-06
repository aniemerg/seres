# Fix Intelligence: recipe_furnace_chamber_unequipped_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_furnace_chamber_unequipped_import_v0.yaml`
- **Target item:** `furnace_chamber_unequipped`
  - File: `kb/items/furnace_chamber_unequipped.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  inputs:
  - item_id: bulk_material_or_parts
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Generic placeholder `bulk_material_or_parts`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `sintered_parts`
- `bulk_material_or_parts`
- `bulk_material`
- `cut_parts`
- `cast_metal_parts`
- `positioned_material_or_parts`
- `green_ceramic_parts`
- `formed_sheet_metal_parts`
- `cast_glass_parts`
- `base_metal_parts`

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_furnace_chamber_unequipped_import_v0.yaml`
- **BOM available:** No
