# Fix Intelligence: recipe_vacuum_tube_sealed_v0

## Files

- **Recipe:** `kb/recipes/recipe_vacuum_tube_sealed_v0.yaml`
- **Target item:** `vacuum_tube_sealed`
  - File: `kb/items/vacuum_tube_sealed.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'vacuum_tube_assembly_v0') requires input 'tungsten_cathode_coated' which is not available

**Location:** Step 0
**Process:** `vacuum_tube_assembly_v0`
  - File: `kb/processes/vacuum_tube_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: vacuum_tube_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_vacuum_tube_sealed_v0.yaml`
- **BOM available:** No
