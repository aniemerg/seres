# Fix Intelligence: recipe_cathode_coated_v0

## Files

- **Recipe:** `kb/recipes/recipe_cathode_coated_v0.yaml`
- **Target item:** `cathode_coated`
  - File: `kb/items/cathode_coated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'oxide_coating_cathode_v0') requires input 'tube_electrode_set' which is not available

**Location:** Step 0
**Process:** `oxide_coating_cathode_v0`
  - File: `kb/processes/oxide_coating_cathode_v0.yaml`

**Current step:**
```yaml
- process_id: oxide_coating_cathode_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cathode_coated_v0.yaml`
- **BOM available:** No
