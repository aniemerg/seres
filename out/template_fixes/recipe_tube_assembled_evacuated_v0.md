# Fix Intelligence: recipe_tube_assembled_evacuated_v0

## Files

- **Recipe:** `kb/recipes/recipe_tube_assembled_evacuated_v0.yaml`
- **Target item:** `tube_assembled_evacuated`
  - File: `kb/items/tube_assembled_evacuated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_assembly_and_evacuation_v0') requires input 'tube_envelope_blown' which is not available

**Location:** Step 0
**Process:** `tube_assembly_and_evacuation_v0`
  - File: `kb/processes/tube_assembly_and_evacuation_v0.yaml`

**Current step:**
```yaml
- process_id: tube_assembly_and_evacuation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_tube_assembled_evacuated_v0.yaml`
- **BOM available:** No
