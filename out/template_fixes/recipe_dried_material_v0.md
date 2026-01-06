# Fix Intelligence: recipe_dried_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_dried_material_v0.yaml`
- **Target item:** `dried_material`
  - File: `kb/items/dried_material.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'drying_and_curing_v0') requires input 'wet_material' which is not available

**Location:** Step 0
**Process:** `drying_and_curing_v0`
  - File: `kb/processes/drying_and_curing_v0.yaml`

**Current step:**
```yaml
- process_id: drying_and_curing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_dried_material_v0.yaml`
- **BOM available:** No
