# Fix Intelligence: recipe_bearing_set_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_bearing_set_v0_v0.yaml`
- **Target item:** `bearing_set_v0`
  - File: `kb/items/bearing_set_v0.yaml`
- **BOM:** `kb/boms/bom_bearing_set_v0.yaml` ✓
  - Components: 2
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_bearing_set_v0` → bearing_set (10 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'bearing_set_fabrication_v0_v0') requires input 'steel_stock' which is not available

**Location:** Step 0
**Process:** `bearing_set_fabrication_v0_v0`
  - File: `kb/processes/bearing_set_fabrication_v0_v0.yaml`

**Current step:**
```yaml
- process_id: bearing_set_fabrication_v0_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bearing_set_v0_v0.yaml`
- **BOM available:** Yes (2 components)
- **Similar recipes:** 1 found
