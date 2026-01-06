# Fix Intelligence: recipe_chemical_reactor_vessel_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_reactor_vessel_v0.yaml`
- **Target item:** `chemical_reactor_vessel_v0`
  - File: `kb/items/chemical_reactor_vessel_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_parts_fabrication_v0') requires input 'base_metal_parts' which is not available

**Location:** Step 0
**Process:** `metal_parts_fabrication_v0`
  - File: `kb/processes/metal_parts_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: metal_parts_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_chemical_reactor_vessel_v0.yaml`
- **BOM available:** No
