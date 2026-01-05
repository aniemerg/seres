# Fix Intelligence: recipe_sodium_nitrate_v0

## Files

- **Recipe:** `kb/recipes/recipe_sodium_nitrate_v0.yaml`
- **Target item:** `sodium_nitrate`
  - File: `kb/items/sodium_nitrate.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hcl_generation_from_nacl_v0') requires input 'sodium_chloride' which is not available

**Location:** Step 0
**Process:** `hcl_generation_from_nacl_v0`
  - File: `kb/processes/hcl_generation_from_nacl_v0.yaml`

**Current step:**
```yaml
- process_id: hcl_generation_from_nacl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sodium_nitrate_v0.yaml`
- **BOM available:** No
