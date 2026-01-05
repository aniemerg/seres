# Fix Intelligence: recipe_nak_glass_to_metal_sealed_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_nak_glass_to_metal_sealed_unit_v0.yaml`
- **Target item:** `nak_glass_to_metal_sealed_unit_v0`
  - File: `kb/items/nak_glass_to_metal_sealed_unit_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'nak_fill_and_seal_process_v0') requires input 'vacuum_tube_empty_v0' which is not available

**Location:** Step 0
**Process:** `nak_fill_and_seal_process_v0`
  - File: `kb/processes/nak_fill_and_seal_process_v0.yaml`

**Current step:**
```yaml
- process_id: nak_fill_and_seal_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nak_glass_to_metal_sealed_unit_v0.yaml`
- **BOM available:** No
