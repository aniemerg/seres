# Fix Intelligence: recipe_cesium_vapor_thermionic_v0

## Files

- **Recipe:** `kb/recipes/recipe_cesium_vapor_thermionic_v0.yaml`
- **Target item:** `cesium_vapor_thermionic_v0`
  - File: `kb/items/cesium_vapor_thermionic_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cesium_vaporization_basic_v0') requires input 'cesium_ampule' which is not available

**Location:** Step 0
**Process:** `cesium_vaporization_basic_v0`
  - File: `kb/processes/cesium_vaporization_basic_v0.yaml`

**Current step:**
```yaml
- process_id: cesium_vaporization_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cesium_vapor_thermionic_v0.yaml`
- **BOM available:** No
