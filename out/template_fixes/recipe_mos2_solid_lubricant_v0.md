# Fix Intelligence: recipe_mos2_solid_lubricant_v0

## Files

- **Recipe:** `kb/recipes/recipe_mos2_solid_lubricant_v0.yaml`
- **Target item:** `mos2_solid_lubricant_v0`
  - File: `kb/items/mos2_solid_lubricant_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mos2_solid_lubricant_synthesis_v0') requires input 'mos2_precursor_v0' which is not available

**Location:** Step 0
**Process:** `mos2_solid_lubricant_synthesis_v0`
  - File: `kb/processes/mos2_solid_lubricant_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: mos2_solid_lubricant_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_mos2_solid_lubricant_v0.yaml`
- **BOM available:** No
