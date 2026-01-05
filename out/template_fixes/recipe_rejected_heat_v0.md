# Fix Intelligence: recipe_rejected_heat_v0

## Files

- **Recipe:** `kb/recipes/recipe_rejected_heat_v0.yaml`
- **Target item:** `rejected_heat`
  - File: `kb/items/rejected_heat.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'thermal_management_radiators_basic_v0') requires input 'waste_heat' which is not available

**Location:** Step 0
**Process:** `thermal_management_radiators_basic_v0`
  - File: `kb/processes/thermal_management_radiators_basic_v0.yaml`

**Current step:**
```yaml
- process_id: thermal_management_radiators_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_rejected_heat_v0.yaml`
- **BOM available:** No
