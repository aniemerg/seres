# Fix Intelligence: recipe_ferrite_powder_precursor_ni_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_ferrite_powder_precursor_ni_v0_v0.yaml`
- **Target item:** `ferrite_powder_precursor_ni_v0`
  - File: `kb/items/ferrite_powder_precursor_ni_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ferrite_powder_precursor_synthesis_ni_v0') requires input 'nickel_ore_raw' which is not available

**Location:** Step 0
**Process:** `ferrite_powder_precursor_synthesis_ni_v0`
  - File: `kb/processes/ferrite_powder_precursor_synthesis_ni_v0.yaml`

**Current step:**
```yaml
- process_id: ferrite_powder_precursor_synthesis_ni_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ferrite_powder_precursor_ni_v0_v0.yaml`
- **BOM available:** No
