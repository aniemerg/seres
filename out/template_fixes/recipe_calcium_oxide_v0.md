# Fix Intelligence: recipe_calcium_oxide_v0

## Files

- **Recipe:** `kb/recipes/recipe_calcium_oxide_v0.yaml`
- **Target item:** `calcium_oxide`
  - File: `kb/items/calcium_oxide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'calcium_oxide_extraction_v0') requires input 'regolith_powder' which is not available

**Location:** Step 0
**Process:** `calcium_oxide_extraction_v0`
  - File: `kb/processes/calcium_oxide_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: calcium_oxide_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_calcium_oxide_v0.yaml`
- **BOM available:** No
