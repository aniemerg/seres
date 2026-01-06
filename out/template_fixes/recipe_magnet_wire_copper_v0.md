# Fix Intelligence: recipe_magnet_wire_copper_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnet_wire_copper_v0.yaml`
- **Target item:** `magnet_wire_copper`
  - File: `kb/items/magnet_wire_copper.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_magnet_wire_copper_v1` → magnet_wire_copper (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'copper_wire_drawing_and_insulation_v0') requires input 'copper_rod_ingot' which is not available

**Location:** Step 0
**Process:** `copper_wire_drawing_and_insulation_v0`
  - File: `kb/processes/copper_wire_drawing_and_insulation_v0.yaml`

**Current step:**
```yaml
- process_id: copper_wire_drawing_and_insulation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnet_wire_copper_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
