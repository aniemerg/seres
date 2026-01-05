# Fix Intelligence: recipe_lathe_spindle_and_bearings_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_spindle_and_bearings_v0.yaml`
- **Target item:** `lathe_spindle_and_bearings`
  - File: `kb/items/lathe_spindle_and_bearings.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lathe_spindle_and_bearings_assembly_v0') requires input 'spindle_assembly_precision' which is not available

**Location:** Step 0
**Process:** `lathe_spindle_and_bearings_assembly_v0`
  - File: `kb/processes/lathe_spindle_and_bearings_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: lathe_spindle_and_bearings_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lathe_spindle_and_bearings_v0.yaml`
- **BOM available:** No
