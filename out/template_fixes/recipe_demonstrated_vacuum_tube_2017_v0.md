# Fix Intelligence: recipe_demonstrated_vacuum_tube_2017_v0

## Files

- **Recipe:** `kb/recipes/recipe_demonstrated_vacuum_tube_2017_v0.yaml`
- **Target item:** `demonstrated_vacuum_tube_2017_v0`
  - File: `kb/items/demonstrated_vacuum_tube_2017_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'demonstrated_vacuum_tube_2017_v0_assembly_v0') requires input 'glass_envelope_vacuum_tube_v0' which is not available

**Location:** Step 0
**Process:** `demonstrated_vacuum_tube_2017_v0_assembly_v0`
  - File: `kb/processes/demonstrated_vacuum_tube_2017_v0_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: demonstrated_vacuum_tube_2017_v0_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_demonstrated_vacuum_tube_2017_v0.yaml`
- **BOM available:** No
