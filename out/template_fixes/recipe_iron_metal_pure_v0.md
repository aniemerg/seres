# Fix Intelligence: recipe_iron_metal_pure_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_metal_pure_v0.yaml`
- **Target item:** `iron_metal_pure`
  - File: `kb/items/iron_metal_pure.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_metalysis_ffc_reduction_v0` → iron_metal_pure (1 steps)
- `recipe_iron_metal_pure_from_ilmenite_v0` → iron_metal_pure (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'iron_pure_production_from_ilmenite_v0') requires input 'iron_ore_or_ilmenite' which is not available

**Location:** Step 0
**Process:** `iron_pure_production_from_ilmenite_v0`
  - File: `kb/processes/iron_pure_production_from_ilmenite_v0.yaml`

**Current step:**
```yaml
- process_id: iron_pure_production_from_ilmenite_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_iron_metal_pure_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
