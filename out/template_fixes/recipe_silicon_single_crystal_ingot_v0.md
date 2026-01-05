# Fix Intelligence: recipe_silicon_single_crystal_ingot_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_single_crystal_ingot_v0.yaml`
- **Target item:** `silicon_single_crystal_ingot`
  - File: `kb/items/silicon_single_crystal_ingot.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'czochralski_process_silicon_v0') requires input 'silicon_polycrystalline_ultrapure' which is not available

**Location:** Step 0
**Process:** `czochralski_process_silicon_v0`
  - File: `kb/processes/czochralski_process_silicon_v0.yaml`

**Current step:**
```yaml
- process_id: czochralski_process_silicon_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_silicon_single_crystal_ingot_v0.yaml`
- **BOM available:** No
