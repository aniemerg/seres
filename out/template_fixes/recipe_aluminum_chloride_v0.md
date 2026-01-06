# Fix Intelligence: recipe_aluminum_chloride_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminum_chloride_v0.yaml`
- **Target item:** `aluminum_chloride`
  - File: `kb/items/aluminum_chloride.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'anorthite_carbochlorination_v0') requires input 'anorthite_ore' which is not available

**Location:** Step 0
**Process:** `anorthite_carbochlorination_v0`
  - File: `kb/processes/anorthite_carbochlorination_v0.yaml`

**Current step:**
```yaml
- process_id: anorthite_carbochlorination_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminum_chloride_v0.yaml`
- **BOM available:** No
