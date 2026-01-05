# Fix Intelligence: recipe_molded_rubber_or_plastic_piece_v0_v0

## Files

- **Recipe:** `kb/recipes/recipe_molded_rubber_or_plastic_piece_v0_v0.yaml`
- **Target item:** `molded_rubber_or_plastic_piece_v0`
  - File: `kb/items/molded_rubber_or_plastic_piece_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'molding_rubber_or_plastic_v0') requires input 'silicone_rubber' which is not available

**Location:** Step 0
**Process:** `molding_rubber_or_plastic_v0`
  - File: `kb/processes/molding_rubber_or_plastic_v0.yaml`

**Current step:**
```yaml
- process_id: molding_rubber_or_plastic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_molded_rubber_or_plastic_piece_v0_v0.yaml`
- **BOM available:** No
