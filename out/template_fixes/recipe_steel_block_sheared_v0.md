# Fix Intelligence: recipe_steel_block_sheared_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_block_sheared_v0.yaml`
- **Target item:** `steel_block_sheared_v0`
  - File: `kb/items/steel_block_sheared_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'shear_metal_cutting_v0') requires input 'steel_block_raw_v0' which is not available

**Location:** Step 0
**Process:** `shear_metal_cutting_v0`
  - File: `kb/processes/shear_metal_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: shear_metal_cutting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_block_sheared_v0.yaml`
- **BOM available:** No
