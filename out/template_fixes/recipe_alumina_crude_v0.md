# Fix Intelligence: recipe_alumina_crude_v0

## Files

- **Recipe:** `kb/recipes/recipe_alumina_crude_v0.yaml`
- **Target item:** `alumina_crude`
  - File: `kb/items/alumina_crude.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'alumina_crude_extraction_v0') requires input 'anorthite_ore' which is not available

**Location:** Step 0
**Process:** `alumina_crude_extraction_v0`
  - File: `kb/processes/alumina_crude_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: alumina_crude_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_alumina_crude_v0.yaml`
- **BOM available:** No
