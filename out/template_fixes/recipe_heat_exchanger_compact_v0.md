# Fix Intelligence: recipe_heat_exchanger_compact_v0

## Files

- **Recipe:** `kb/recipes/recipe_heat_exchanger_compact_v0.yaml`
- **Target item:** `heat_exchanger_compact`
  - File: `kb/items/heat_exchanger_compact.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'brazing_heat_exchanger_compact_v0') requires input 'base_metal_parts' which is not available

**Location:** Step 0
**Process:** `brazing_heat_exchanger_compact_v0`
  - File: `kb/processes/brazing_heat_exchanger_compact_v0.yaml`

**Current step:**
```yaml
- process_id: brazing_heat_exchanger_compact_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_heat_exchanger_compact_v0.yaml`
- **BOM available:** No
