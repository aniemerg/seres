# Fix Intelligence: recipe_invar_alloy_v0

## Files

- **Recipe:** `kb/recipes/recipe_invar_alloy_v0.yaml`
- **Target item:** `invar_alloy`
  - File: `kb/items/invar_alloy.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'nife_alloy_melting_and_casting_v0') requires input 'nickel_metal_pure' which is not available

**Location:** Step 0
**Process:** `nife_alloy_melting_and_casting_v0`
  - File: `kb/processes/nife_alloy_melting_and_casting_v0.yaml`

**Current step:**
```yaml
- process_id: nife_alloy_melting_and_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_invar_alloy_v0.yaml`
- **BOM available:** No
