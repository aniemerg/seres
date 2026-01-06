# Fix Intelligence: recipe_iron_powder_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_powder_v0_v0.yaml`
- **Target item:** `iron_powder_v0`
  - File: `kb/items/iron_powder_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_iron_powder_from_ilmenite_v0` → iron_powder_v0 (2 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'iron_powder_synthesis_v0') requires input 'iron_metal_pure' which is not available

**Location:** Step 0
**Process:** `iron_powder_synthesis_v0`
  - File: `kb/processes/iron_powder_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: iron_powder_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_iron_powder_v0_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
