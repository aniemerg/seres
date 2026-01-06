# Fix Intelligence: recipe_aramid_precursor_v0

## Files

- **Recipe:** `kb/recipes/recipe_aramid_precursor_v0.yaml`
- **Target item:** `aramid_precursor_v0`
  - File: `kb/items/aramid_precursor_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aramid_precursor_synthesis_v0') requires input 'polymer_feedstock' which is not available

**Location:** Step 0
**Process:** `aramid_precursor_synthesis_v0`
  - File: `kb/processes/aramid_precursor_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: aramid_precursor_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aramid_precursor_v0.yaml`
- **BOM available:** No
