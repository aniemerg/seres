# Fix Intelligence: recipe_cryolite_flux_v0

## Files

- **Recipe:** `kb/recipes/recipe_cryolite_flux_v0.yaml`
- **Target item:** `cryolite_flux`
  - File: `kb/items/cryolite_flux.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cryolite_flux_synthesis_v0') requires input 'sodium_hydroxide' which is not available

**Location:** Step 0
**Process:** `cryolite_flux_synthesis_v0`
  - File: `kb/processes/cryolite_flux_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: cryolite_flux_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cryolite_flux_v0.yaml`
- **BOM available:** No
