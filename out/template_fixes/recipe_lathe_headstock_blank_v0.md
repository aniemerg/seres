# Fix Intelligence: recipe_lathe_headstock_blank_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_headstock_blank_v0.yaml`
- **Target item:** `lathe_headstock_blank`
  - File: `kb/items/lathe_headstock_blank.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lathe_headstock_blank_cast_v0') requires input 'steel_billet_or_slab' which is not available

**Location:** Step 0
**Process:** `lathe_headstock_blank_cast_v0`
  - File: `kb/processes/lathe_headstock_blank_cast_v0.yaml`

**Current step:**
```yaml
- process_id: lathe_headstock_blank_cast_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lathe_headstock_blank_v0.yaml`
- **BOM available:** No
