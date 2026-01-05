# Fix Intelligence: recipe_prism_glass_optical_v0

## Files

- **Recipe:** `kb/recipes/recipe_prism_glass_optical_v0.yaml`
- **Target item:** `prism_glass_optical`
  - File: `kb/items/prism_glass_optical.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'prism_cut_and_polish_v0') requires input 'cast_glass_parts' which is not available

**Location:** Step 0
**Process:** `prism_cut_and_polish_v0`
  - File: `kb/processes/prism_cut_and_polish_v0.yaml`

**Current step:**
```yaml
- process_id: prism_cut_and_polish_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_prism_glass_optical_v0.yaml`
- **BOM available:** No
