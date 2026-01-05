# Fix Intelligence: recipe_phosphorus_white_v0

## Files

- **Recipe:** `kb/recipes/recipe_phosphorus_white_v0.yaml`
- **Target item:** `phosphorus_white`
  - File: `kb/items/phosphorus_white.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'phosphorus_extraction_from_kreep_v0') requires input 'basalt_aggregate' which is not available

**Location:** Step 0
**Process:** `phosphorus_extraction_from_kreep_v0`
  - File: `kb/processes/phosphorus_extraction_from_kreep_v0.yaml`

**Current step:**
```yaml
- process_id: phosphorus_extraction_from_kreep_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_phosphorus_white_v0.yaml`
- **BOM available:** No
