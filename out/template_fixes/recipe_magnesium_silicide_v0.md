# Fix Intelligence: recipe_magnesium_silicide_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnesium_silicide_v0.yaml`
- **Target item:** `magnesium_silicide`
  - File: `kb/items/magnesium_silicide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'silicide_formation_basic_v0') requires input 'import_magnesium_powder' which is not available

**Location:** Step 0
**Process:** `silicide_formation_basic_v0`
  - File: `kb/processes/silicide_formation_basic_v0.yaml`

**Current step:**
```yaml
- process_id: silicide_formation_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnesium_silicide_v0.yaml`
- **BOM available:** No
