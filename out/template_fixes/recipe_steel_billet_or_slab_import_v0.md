# Fix Intelligence: recipe_steel_billet_or_slab_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_billet_or_slab_import_v0.yaml`
- **Target item:** `steel_billet_or_slab`
  - File: `kb/items/steel_billet_or_slab.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_steel_billet_or_slab_v0` → steel_billet_or_slab (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'steel_refining_basic_v0') requires input 'iron_pig_or_ingot' which is not available

**Location:** Step 0
**Process:** `steel_refining_basic_v0`
  - File: `kb/processes/steel_refining_basic_v0.yaml`

**Current step:**
```yaml
- process_id: steel_refining_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_billet_or_slab_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
