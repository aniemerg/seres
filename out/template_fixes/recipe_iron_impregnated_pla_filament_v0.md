# Fix Intelligence: recipe_iron_impregnated_pla_filament_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_impregnated_pla_filament_v0.yaml`
- **Target item:** `iron_impregnated_pla_filament_v0`
  - File: `kb/items/iron_impregnated_pla_filament_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_plastic_filament_extrusion_v0') requires input 'iron_powder_or_sheet' which is not available

**Location:** Step 0
**Process:** `metal_plastic_filament_extrusion_v0`
  - File: `kb/processes/metal_plastic_filament_extrusion_v0.yaml`

**Current step:**
```yaml
- process_id: metal_plastic_filament_extrusion_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_iron_impregnated_pla_filament_v0.yaml`
- **BOM available:** No
