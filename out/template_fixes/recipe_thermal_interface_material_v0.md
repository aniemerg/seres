# Fix Intelligence: recipe_thermal_interface_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermal_interface_material_v0.yaml`
- **Target item:** `thermal_interface_material`
  - File: `kb/items/thermal_interface_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_thermal_interface_material_import_v0` → thermal_interface_material (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'thermal_interface_material_synthesis_v0') requires input 'silicone_polymer' which is not available

**Location:** Step 0
**Process:** `thermal_interface_material_synthesis_v0`
  - File: `kb/processes/thermal_interface_material_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: thermal_interface_material_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_thermal_interface_material_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
