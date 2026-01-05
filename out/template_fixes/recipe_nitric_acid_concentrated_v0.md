# Fix Intelligence: recipe_nitric_acid_concentrated_v0

## Files

- **Recipe:** `kb/recipes/recipe_nitric_acid_concentrated_v0.yaml`
- **Target item:** `nitric_acid_concentrated`
  - File: `kb/items/nitric_acid_concentrated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ostwald_process_nitric_acid_v0') requires input 'ammonia_gas' which is not available

**Location:** Step 0
**Process:** `ostwald_process_nitric_acid_v0`
  - File: `kb/processes/ostwald_process_nitric_acid_v0.yaml`

**Current step:**
```yaml
- process_id: ostwald_process_nitric_acid_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_nitric_acid_concentrated_v0.yaml`
- **BOM available:** No
