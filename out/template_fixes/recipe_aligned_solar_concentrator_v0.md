# Fix Intelligence: recipe_aligned_solar_concentrator_v0

## Files

- **Recipe:** `kb/recipes/recipe_aligned_solar_concentrator_v0.yaml`
- **Target item:** `aligned_solar_concentrator`
  - File: `kb/items/aligned_solar_concentrator.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'concentrator_alignment_v0') requires input 'solar_concentrator_assembly' which is not available

**Location:** Step 0
**Process:** `concentrator_alignment_v0`
  - File: `kb/processes/concentrator_alignment_v0.yaml`

**Current step:**
```yaml
- process_id: concentrator_alignment_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aligned_solar_concentrator_v0.yaml`
- **BOM available:** No
