# Fix Intelligence: recipe_lathe_headstock_simple_v5

## Files

- **Recipe:** `kb/recipes/recipe_lathe_headstock_simple_v5.yaml`
- **Target item:** `lathe_headstock_simple`
  - File: `kb/items/lathe_headstock_simple.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_lathe_headstock_simple_v3` → lathe_headstock_simple (1 steps)
- `recipe_lathe_headstock_simple_v2` → lathe_headstock_simple (1 steps)
- `recipe_lathe_headstock_simple_v4` → lathe_headstock_simple (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lathe_headstock_turn_v0') requires input 'lathe_headstock_blank' which is not available

**Location:** Step 0
**Process:** `lathe_headstock_turn_v0`
  - File: `kb/processes/lathe_headstock_turn_v0.yaml`

**Current step:**
```yaml
- process_id: lathe_headstock_turn_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lathe_headstock_simple_v5.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
