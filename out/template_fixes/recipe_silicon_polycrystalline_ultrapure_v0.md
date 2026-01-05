# Fix Intelligence: recipe_silicon_polycrystalline_ultrapure_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_polycrystalline_ultrapure_v0.yaml`
- **Target item:** `silicon_polycrystalline_ultrapure`
  - File: `kb/items/silicon_polycrystalline_ultrapure.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'siemens_process_polysilicon_deposition_v0') requires input 'trichlorosilane_liquid' which is not available

**Location:** Step 0
**Process:** `siemens_process_polysilicon_deposition_v0`
  - File: `kb/processes/siemens_process_polysilicon_deposition_v0.yaml`

**Current step:**
```yaml
- process_id: siemens_process_polysilicon_deposition_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicon_polycrystalline_ultrapure_v0.yaml`
- **BOM available:** No
