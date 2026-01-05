# Fix Intelligence: recipe_ball_screw_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_ball_screw_assembly_v0.yaml`
- **Target item:** `ball_screw_assembly`
  - File: `kb/items/ball_screw_assembly.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_ball_screw_assembly_v2` → ball_screw_assembly (1 steps)
- `recipe_ball_screw_assembly_v1` → ball_screw_assembly (1 steps)
- `recipe_ball_screw_assembly_import_v0` → ball_screw_assembly (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ball_screw_fabrication_v0') requires input 'steel_bar_stock' which is not available

**Location:** Step 0
**Process:** `ball_screw_fabrication_v0`
  - File: `kb/processes/ball_screw_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: ball_screw_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ball_screw_assembly_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
