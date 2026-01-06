# Fix Intelligence: recipe_photolithographic_coil_winding_v0

## Files

- **Recipe:** `kb/recipes/recipe_photolithographic_coil_winding_v0.yaml`
- **Target item:** `photolithographic_coil_winding_v0`
  - File: `kb/items/photolithographic_coil_winding_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'photolithographic_coil_winding_v0') requires input 'copper_patterned_substrate_v0' which is not available

**Location:** Step 0
**Process:** `photolithographic_coil_winding_v0`
  - File: `kb/processes/photolithographic_coil_winding_v0.yaml`

**Current step:**
```yaml
- process_id: photolithographic_coil_winding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_photolithographic_coil_winding_v0.yaml`
- **BOM available:** No
