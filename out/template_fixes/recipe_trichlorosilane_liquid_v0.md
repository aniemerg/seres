# Fix Intelligence: recipe_trichlorosilane_liquid_v0

## Files

- **Recipe:** `kb/recipes/recipe_trichlorosilane_liquid_v0.yaml`
- **Target item:** `trichlorosilane_liquid`
  - File: `kb/items/trichlorosilane_liquid.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'siemens_process_trichlorosilane_v0') requires input 'silicon_metal_v0' which is not available

**Location:** Step 0
**Process:** `siemens_process_trichlorosilane_v0`
  - File: `kb/processes/siemens_process_trichlorosilane_v0.yaml`

**Current step:**
```yaml
- process_id: siemens_process_trichlorosilane_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'fractional_distillation_v0') requires input 'blended_mixture' which is not available

**Location:** Step 1
**Process:** `fractional_distillation_v0`
  - File: `kb/processes/fractional_distillation_v0.yaml`

**Current step:**
```yaml
- process_id: fractional_distillation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_trichlorosilane_liquid_v0.yaml`
- **BOM available:** No
