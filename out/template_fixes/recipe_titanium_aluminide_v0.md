# Fix Intelligence: recipe_titanium_aluminide_v0

## Files

- **Recipe:** `kb/recipes/recipe_titanium_aluminide_v0.yaml`
- **Target item:** `titanium_aluminide`
  - File: `kb/items/titanium_aluminide.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'alloy_mixing_v0') requires input 'nickel_chromium_alloy' which is not available

**Location:** Step 0
**Process:** `alloy_mixing_v0`
  - File: `kb/processes/alloy_mixing_v0.yaml`

**Current step:**
```yaml
- process_id: alloy_mixing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_titanium_aluminide_v0.yaml`
- **BOM available:** No
