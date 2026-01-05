# Fix Intelligence: recipe_potassium_nitrate_v0

## Files

- **Recipe:** `kb/recipes/recipe_potassium_nitrate_v0.yaml`
- **Target item:** `potassium_nitrate`
  - File: `kb/items/potassium_nitrate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'nacl_regeneration_from_nano3_v0') requires input 'sodium_nitrate' which is not available

**Location:** Step 0
**Process:** `nacl_regeneration_from_nano3_v0`
  - File: `kb/processes/nacl_regeneration_from_nano3_v0.yaml`

**Current step:**
```yaml
- process_id: nacl_regeneration_from_nano3_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_potassium_nitrate_v0.yaml`
- **BOM available:** No
