# Fix Intelligence: recipe_heating_element_resistive_v0

## Files

- **Recipe:** `kb/recipes/recipe_heating_element_resistive_v0.yaml`
- **Target item:** `heating_element_resistive`
  - File: `kb/items/heating_element_resistive.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'heating_element_resistive_fabrication_v0') requires input 'nickel_chromium_alloy' which is not available

**Location:** Step 0
**Process:** `heating_element_resistive_fabrication_v0`
  - File: `kb/processes/heating_element_resistive_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: heating_element_resistive_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_heating_element_resistive_v0.yaml`
- **BOM available:** No
