# Fix Intelligence: recipe_brazed_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_brazed_assembly_v0.yaml`
- **Target item:** `brazed_assembly`
  - File: `kb/items/brazed_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_brazed_assembly_v1` → brazed_assembly (1 steps)
- `recipe_brazed_assembly_v2` → brazed_assembly (1 steps)
- `recipe_brazed_assembly_v3` → brazed_assembly (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'brazing_process_v0') requires input 'base_metal_parts' which is not available

**Location:** Step 0
**Process:** `brazing_process_v0`
  - File: `kb/processes/brazing_process_v0.yaml`

**Current step:**
```yaml
- process_id: brazing_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_brazed_assembly_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
