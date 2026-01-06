# Fix Intelligence: recipe_plain_bearing_bronze_v0

## Files

- **Recipe:** `kb/recipes/recipe_plain_bearing_bronze_v0.yaml`
- **Target item:** `plain_bearing_bronze_v0`
  - File: `kb/items/plain_bearing_bronze_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_bronze_bearing_block_v0') requires input 'bronze_block_material_v0' which is not available

**Location:** Step 0
**Process:** `machining_bronze_bearing_block_v0`
  - File: `kb/processes/machining_bronze_bearing_block_v0.yaml`

**Current step:**
```yaml
- process_id: machining_bronze_bearing_block_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_plain_bearing_bronze_v0.yaml`
- **BOM available:** No
