# Fix Intelligence: recipe_wire_copper_magnet_v0

## Files

- **Recipe:** `kb/recipes/recipe_wire_copper_magnet_v0.yaml`
- **Target item:** `wire_copper_magnet`
  - File: `kb/items/wire_copper_magnet.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'wire_copper_magnet_production_v0') requires input 'copper_rod_ingot' which is not available

**Location:** Step 0
**Process:** `wire_copper_magnet_production_v0`
  - File: `kb/processes/wire_copper_magnet_production_v0.yaml`

**Current step:**
```yaml
- process_id: wire_copper_magnet_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_wire_copper_magnet_v0.yaml`
- **BOM available:** No
