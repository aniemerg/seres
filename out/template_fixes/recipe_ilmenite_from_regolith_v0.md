# Fix Intelligence: recipe_ilmenite_from_regolith_v0

## Files

- **Recipe:** `kb/recipes/recipe_ilmenite_from_regolith_v0.yaml`
- **Target item:** `iron_ore_or_ilmenite`
  - File: `kb/items/iron_ore_or_ilmenite.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_iron_ore_or_ilmenite_basic_v0` → iron_ore_or_ilmenite (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ilmenite_extraction_from_regolith_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 0
**Process:** `ilmenite_extraction_from_regolith_v0`
  - File: `kb/processes/ilmenite_extraction_from_regolith_v0.yaml`

**Current step:**
```yaml
- process_id: ilmenite_extraction_from_regolith_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ilmenite_from_regolith_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
