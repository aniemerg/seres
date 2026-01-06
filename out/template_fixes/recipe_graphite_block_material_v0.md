# Fix Intelligence: recipe_graphite_block_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_graphite_block_material_v0.yaml`
- **Target item:** `graphite_block_material_v0`
  - File: `kb/items/graphite_block_material_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'powder_processing_v0') requires input 'powder_metal_or_ceramic' which is not available

**Location:** Step 0
**Process:** `powder_processing_v0`
  - File: `kb/processes/powder_processing_v0.yaml`

**Current step:**
```yaml
- process_id: powder_processing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_graphite_block_material_v0.yaml`
- **BOM available:** No
