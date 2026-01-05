# Fix Intelligence: recipe_electricity_v0

## Files

- **Recipe:** `kb/recipes/recipe_electricity_v0.yaml`
- **Target item:** `electricity`
  - File: `kb/items/electricity.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electricity_generation_placeholder_v0') requires input 'fuel_generic' which is not available

**Location:** Step 0
**Process:** `electricity_generation_placeholder_v0`
  - File: `kb/processes/electricity_generation_placeholder_v0.yaml`

**Current step:**
```yaml
- process_id: electricity_generation_placeholder_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electricity_v0.yaml`
- **BOM available:** No
