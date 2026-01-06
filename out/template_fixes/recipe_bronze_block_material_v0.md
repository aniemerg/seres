# Fix Intelligence: recipe_bronze_block_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_bronze_block_material_v0.yaml`
- **Target item:** `bronze_block_material_v0`
  - File: `kb/items/bronze_block_material_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'bronze_alloy_casting_v0') requires input 'metal_alloy_bulk' which is not available

**Location:** Step 0
**Process:** `bronze_alloy_casting_v0`
  - File: `kb/processes/bronze_alloy_casting_v0.yaml`

**Current step:**
```yaml
- process_id: bronze_alloy_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bronze_block_material_v0.yaml`
- **BOM available:** No
