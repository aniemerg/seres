# Fix Intelligence: recipe_nickel_oxide_waste_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_oxide_waste_v0.yaml`
- **Target item:** `nickel_oxide_waste_v0`
  - File: `kb/items/nickel_oxide_waste_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cathode_oxide_coating_process_v0') requires input 'nickel_sheet_rolling_v0' which is not available

**Location:** Step 0
**Process:** `cathode_oxide_coating_process_v0`
  - File: `kb/processes/cathode_oxide_coating_process_v0.yaml`

**Current step:**
```yaml
- process_id: cathode_oxide_coating_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nickel_oxide_waste_v0.yaml`
- **BOM available:** No
