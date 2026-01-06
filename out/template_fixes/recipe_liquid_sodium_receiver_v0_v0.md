# Fix Intelligence: recipe_liquid_sodium_receiver_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_liquid_sodium_receiver_v0_v0.yaml`
- **Target item:** `liquid_sodium_receiver_v0`
  - File: `kb/items/liquid_sodium_receiver_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'liquid_sodium_receiver_fabrication_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `liquid_sodium_receiver_fabrication_v0`
  - File: `kb/processes/liquid_sodium_receiver_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: liquid_sodium_receiver_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_liquid_sodium_receiver_v0_v0.yaml`
- **BOM available:** No
