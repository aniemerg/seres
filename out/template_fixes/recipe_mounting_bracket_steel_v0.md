# Fix Intelligence: recipe_mounting_bracket_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_mounting_bracket_steel_v0.yaml`
- **Target item:** `mounting_bracket_steel_v0`
  - File: `kb/items/mounting_bracket_steel_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_mounting_bracket_steel_v1` → mounting_bracket_steel (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mounting_bracket_steel_forming_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `mounting_bracket_steel_forming_v0`
  - File: `kb/processes/mounting_bracket_steel_forming_v0.yaml`

**Current step:**
```yaml
- process_id: mounting_bracket_steel_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_mounting_bracket_steel_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
