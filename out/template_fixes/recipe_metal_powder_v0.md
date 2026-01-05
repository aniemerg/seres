# Fix Intelligence: recipe_metal_powder_v0

## Files

- **Recipe:** `kb/recipes/recipe_metal_powder_v0.yaml`
- **Target item:** `metal_powder_v0`
  - File: `kb/items/metal_powder_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_powdering_process_v0') requires input 'metal_ingot_v0' which is not available

**Location:** Step 0
**Process:** `metal_powdering_process_v0`
  - File: `kb/processes/metal_powdering_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_powdering_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_metal_powder_v0.yaml`
- **BOM available:** No
