# Fix Intelligence: recipe_helium_3_v0

## Files

- **Recipe:** `kb/recipes/recipe_helium_3_v0.yaml`
- **Target item:** `helium_3`
  - File: `kb/items/helium_3.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'helium3_cryogenic_separation_v0') requires input 'helium_mixed_isotopes' which is not available

**Location:** Step 0
**Process:** `helium3_cryogenic_separation_v0`
  - File: `kb/processes/helium3_cryogenic_separation_v0.yaml`

**Current step:**
```yaml
- process_id: helium3_cryogenic_separation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_helium_3_v0.yaml`
- **BOM available:** No
