# Fix Intelligence: recipe_brazing_alloy_generic_v0

## Files

- **Recipe:** `kb/recipes/recipe_brazing_alloy_generic_v0.yaml`
- **Target item:** `brazing_alloy_generic`
  - File: `kb/items/brazing_alloy_generic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'brazing_alloy_synthesis_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `brazing_alloy_synthesis_v0`
  - File: `kb/processes/brazing_alloy_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: brazing_alloy_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_brazing_alloy_generic_v0.yaml`
- **BOM available:** No
