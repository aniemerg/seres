# Fix Intelligence: recipe_electrode_copper_welding_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrode_copper_welding_v0.yaml`
- **Target item:** `electrode_copper_welding`
  - File: `kb/items/electrode_copper_welding.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electrode_fabrication_copper_welding_v0') requires input 'copper_rod_ingot' which is not available

**Location:** Step 0
**Process:** `electrode_fabrication_copper_welding_v0`
  - File: `kb/processes/electrode_fabrication_copper_welding_v0.yaml`

**Current step:**
```yaml
- process_id: electrode_fabrication_copper_welding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_electrode_copper_welding_v0.yaml`
- **BOM available:** No
