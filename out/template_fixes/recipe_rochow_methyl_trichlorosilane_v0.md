# Fix Intelligence: recipe_rochow_methyl_trichlorosilane_v0

## Files

- **Recipe:** `kb/recipes/recipe_rochow_methyl_trichlorosilane_v0.yaml`
- **Target item:** `methyl_trichlorosilane_v0`
  - File: `kb/items/methyl_trichlorosilane_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'rochow_process_reactor_v0') requires input 'methyl_chloride_gas' which is not available

**Location:** Step 0
**Process:** `rochow_process_reactor_v0`
  - File: `kb/processes/rochow_process_reactor_v0.yaml`

**Current step:**
```yaml
- process_id: rochow_process_reactor_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_rochow_methyl_trichlorosilane_v0.yaml`
- **BOM available:** No
