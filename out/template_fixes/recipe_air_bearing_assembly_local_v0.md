# Fix Intelligence: recipe_air_bearing_assembly_local_v0

## Files

- **Recipe:** `kb/recipes/recipe_air_bearing_assembly_local_v0.yaml`
- **Target item:** `air_bearing_assembly`
  - File: `kb/items/air_bearing_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_air_bearing_assembly_v0` → air_bearing_assembly (1 steps)
- `recipe_air_bearing_assembly_v1` → air_bearing_assembly (1 steps)
- `recipe_air_bearing_assembly_v2` → air_bearing_assembly (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'air_bearing_assembly_basic_v0') requires input 'bearing_set' which is not available

**Location:** Step 0
**Process:** `air_bearing_assembly_basic_v0`
  - File: `kb/processes/air_bearing_assembly_basic_v0.yaml`

**Current step:**
```yaml
- process_id: air_bearing_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_air_bearing_assembly_local_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
