# Fix Intelligence: recipe_magnalium_alloy_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnalium_alloy_v0.yaml`
- **Target item:** `magnalium_alloy`
  - File: `kb/items/magnalium_alloy.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'magnalium_alloying_v0') requires input 'aluminum_alloy_ingot' which is not available

**Location:** Step 0
**Process:** `magnalium_alloying_v0`
  - File: `kb/processes/magnalium_alloying_v0.yaml`

**Current step:**
```yaml
- process_id: magnalium_alloying_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnalium_alloy_v0.yaml`
- **BOM available:** No
