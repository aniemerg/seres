# Fix Intelligence: recipe_power_supply_components_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_supply_components_basic_v0.yaml`
- **Target item:** `power_supply_components_basic`
  - File: `kb/items/power_supply_components_basic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'power_supply_components_basic_fabrication_v0') requires input 'electronic_components_set' which is not available

**Location:** Step 0
**Process:** `power_supply_components_basic_fabrication_v0`
  - File: `kb/processes/power_supply_components_basic_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: power_supply_components_basic_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_power_supply_components_basic_v0.yaml`
- **BOM available:** No
