# Fix Intelligence: recipe_dust_fines_v0

## Files

- **Recipe:** `kb/recipes/recipe_dust_fines_v0.yaml`
- **Target item:** `dust_fines_v0`
  - File: `kb/items/dust_fines_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_dust_fines_alias_v0` → dust_fines (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_pressing_process_v0') requires input 'powder_feedstock' which is not available

**Location:** Step 0
**Process:** `powder_pressing_process_v0`
  - File: `kb/processes/powder_pressing_process_v0.yaml`

**Current step:**
```yaml
- process_id: powder_pressing_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_dust_fines_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
