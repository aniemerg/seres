# Fix Intelligence: recipe_coil_insulation_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_coil_insulation_material_v0.yaml`
- **Target item:** `coil_insulation_material`
  - File: `kb/items/coil_insulation_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'coil_insulation_production_v0') requires input 'silicone_polymer' which is not available

**Location:** Step 0
**Process:** `coil_insulation_production_v0`
  - File: `kb/processes/coil_insulation_production_v0.yaml`

**Current step:**
```yaml
- process_id: coil_insulation_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coil_insulation_material_v0.yaml`
- **BOM available:** No
