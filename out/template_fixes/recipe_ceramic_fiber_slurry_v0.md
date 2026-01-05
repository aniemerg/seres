# Fix Intelligence: recipe_ceramic_fiber_slurry_v0

## Files

- **Recipe:** `kb/recipes/recipe_ceramic_fiber_slurry_v0.yaml`
- **Target item:** `ceramic_fiber_slurry`
  - File: `kb/items/ceramic_fiber_slurry.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ceramic_fiber_slurry_mixing_v0') requires input 'ceramic_fiber_raw' which is not available

**Location:** Step 0
**Process:** `ceramic_fiber_slurry_mixing_v0`
  - File: `kb/processes/ceramic_fiber_slurry_mixing_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_fiber_slurry_mixing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ceramic_fiber_slurry_v0.yaml`
- **BOM available:** No
