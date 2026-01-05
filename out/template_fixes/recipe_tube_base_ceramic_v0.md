# Fix Intelligence: recipe_tube_base_ceramic_v0

## Files

- **Recipe:** `kb/recipes/recipe_tube_base_ceramic_v0.yaml`
- **Target item:** `tube_base_ceramic`
  - File: `kb/items/tube_base_ceramic.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ceramic_base_fabrication_v0') requires input 'ceramic_powder' which is not available

**Location:** Step 0
**Process:** `ceramic_base_fabrication_v0`
  - File: `kb/processes/ceramic_base_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_base_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tube_base_ceramic_v0.yaml`
- **BOM available:** No
