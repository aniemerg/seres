# Fix Intelligence: recipe_base_metal_parts_v0

## Files

- **Recipe:** `kb/recipes/recipe_base_metal_parts_v0.yaml`
- **Target item:** `base_metal_parts`
  - File: `kb/items/base_metal_parts.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_base_metal_parts_v1` → base_metal_parts (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'base_metal_parts_from_raw_metal_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `base_metal_parts_from_raw_metal_v0`
  - File: `kb/processes/base_metal_parts_from_raw_metal_v0.yaml`

**Current step:**
```yaml
- process_id: base_metal_parts_from_raw_metal_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_base_metal_parts_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
