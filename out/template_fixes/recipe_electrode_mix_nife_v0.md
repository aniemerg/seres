# Fix Intelligence: recipe_electrode_mix_nife_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrode_mix_nife_v0.yaml`
- **Target item:** `electrode_mix_nife`
  - File: `kb/items/electrode_mix_nife.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrode_powder_mixing_nife_v0') requires input 'nickel_hydroxide' which is not available

**Location:** Step 0
**Process:** `electrode_powder_mixing_nife_v0`
  - File: `kb/processes/electrode_powder_mixing_nife_v0.yaml`

**Current step:**
```yaml
- process_id: electrode_powder_mixing_nife_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrode_mix_nife_v0.yaml`
- **BOM available:** No
