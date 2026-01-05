# Fix Intelligence: recipe_forsterite_from_regolith_v0

## Files

- **Recipe:** `kb/recipes/recipe_forsterite_from_regolith_v0.yaml`
- **Target item:** `forsterite_extraction_v0`
  - File: `kb/items/forsterite_extraction_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'forsterite_extraction_from_regolith_v0') requires input 'regolith_lunar_highlands' which is not available

**Location:** Step 0
**Process:** `forsterite_extraction_from_regolith_v0`
  - File: `kb/processes/forsterite_extraction_from_regolith_v0.yaml`

**Current step:**
```yaml
- process_id: forsterite_extraction_from_regolith_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_forsterite_from_regolith_v0.yaml`
- **BOM available:** No
