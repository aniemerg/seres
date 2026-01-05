# Fix Intelligence: recipe_chemical_reactor_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_reactor_unit_v0.yaml`
- **Target item:** `chemical_reactor_unit_v0`
  - File: `kb/items/chemical_reactor_unit_v0.yaml`
- **BOM:** `kb/boms/bom_chemical_reactor_unit_v0.yaml` ✓
  - Components: 7
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_chemical_reactor_unit_v1` → chemical_reactor_unit_v1 (3 steps)
- `recipe_chemical_reactor_unit_v1_v1` → chemical_reactor_unit_v1 (3 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_reactor_unit_fabrication_v0') requires input 'steel_ingot' which is not available

**Location:** Step 0
**Process:** `chemical_reactor_unit_fabrication_v0`
  - File: `kb/processes/chemical_reactor_unit_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: chemical_reactor_unit_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_chemical_reactor_unit_v0.yaml`
- **BOM available:** Yes (7 components)
- **Similar recipes:** 2 found
