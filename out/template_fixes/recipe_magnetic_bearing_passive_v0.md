# Fix Intelligence: recipe_magnetic_bearing_passive_v0

## Files

- **Recipe:** `kb/recipes/recipe_magnetic_bearing_passive_v0.yaml`
- **Target item:** `magnetic_bearing_passive_v0`
  - File: `kb/items/magnetic_bearing_passive_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'forming_passive_magnetic_bearing_v0') requires input 'permanent_magnet_neodymium' which is not available

**Location:** Step 0
**Process:** `forming_passive_magnetic_bearing_v0`
  - File: `kb/processes/forming_passive_magnetic_bearing_v0.yaml`

**Current step:**
```yaml
- process_id: forming_passive_magnetic_bearing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_magnetic_bearing_passive_v0.yaml`
- **BOM available:** No
