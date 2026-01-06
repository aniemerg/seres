# Fix Intelligence: recipe_raw_formation_control_material_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_raw_formation_control_material_v0_v0.yaml`
- **Target item:** `raw_formation_control_material_v0`
  - File: `kb/items/raw_formation_control_material_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'extraction_raw_formation_control_material_v0_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `extraction_raw_formation_control_material_v0_v0`
  - File: `kb/processes/extraction_raw_formation_control_material_v0_v0.yaml`

**Current step:**
```yaml
- process_id: extraction_raw_formation_control_material_v0_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_raw_formation_control_material_v0_v0.yaml`
- **BOM available:** No
