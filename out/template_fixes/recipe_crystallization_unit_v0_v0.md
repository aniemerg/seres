# Fix Intelligence: recipe_crystallization_unit_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_crystallization_unit_v0_v0.yaml`
- **Target item:** `crystallization_unit_v0`
  - File: `kb/items/crystallization_unit_v0.yaml`
- **BOM:** `kb/boms/bom_crystallization_unit_v0.yaml` ✓
  - Components: 2
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'crystallization_unit_assembly_v0') requires input 'aluminum_housing_machined' which is not available

**Location:** Step 0
**Process:** `crystallization_unit_assembly_v0`
  - File: `kb/processes/crystallization_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: crystallization_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_crystallization_unit_v0_v0.yaml`
- **BOM available:** Yes (2 components)
