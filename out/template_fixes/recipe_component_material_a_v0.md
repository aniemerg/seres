# Fix Intelligence: recipe_component_material_a_v0

## Files

- **Recipe:** `kb/recipes/recipe_component_material_a_v0.yaml`
- **Target item:** `component_material_a`
  - File: `kb/items/component_material_a.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'manufacture_component_material_a_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `manufacture_component_material_a_v0`
  - File: `kb/processes/manufacture_component_material_a_v0.yaml`

**Current step:**
```yaml
- process_id: manufacture_component_material_a_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_component_material_a_v0.yaml`
- **BOM available:** No
