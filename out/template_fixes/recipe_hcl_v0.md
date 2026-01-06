# Fix Intelligence: recipe_hcl_v0

## Files

- **Recipe:** `kb/recipes/recipe_hcl_v0.yaml`
- **Target item:** `hcl`
  - File: `kb/items/hcl.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hcl_synthesis_from_h2_cl2_v0') requires input 'hydrogen_gas' which is not available

**Location:** Step 0
**Process:** `hcl_synthesis_from_h2_cl2_v0`
  - File: `kb/processes/hcl_synthesis_from_h2_cl2_v0.yaml`

**Current step:**
```yaml
- process_id: hcl_synthesis_from_h2_cl2_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hcl_v0.yaml`
- **BOM available:** No
