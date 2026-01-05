# Fix Intelligence: recipe_alnico_magnet_alloy_v0

## Files

- **Recipe:** `kb/recipes/recipe_alnico_magnet_alloy_v0.yaml`
- **Target item:** `alnico_magnet_alloy_v0`
  - File: `kb/items/alnico_magnet_alloy_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'alnico_alloy_synthesis_v0') requires input 'aluminum_metal_pure' which is not available

**Location:** Step 0
**Process:** `alnico_alloy_synthesis_v0`
  - File: `kb/processes/alnico_alloy_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: alnico_alloy_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_alnico_magnet_alloy_v0.yaml`
- **BOM available:** No
