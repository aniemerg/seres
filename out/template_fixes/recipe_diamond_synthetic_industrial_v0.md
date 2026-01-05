# Fix Intelligence: recipe_diamond_synthetic_industrial_v0

## Files

- **Recipe:** `kb/recipes/recipe_diamond_synthetic_industrial_v0.yaml`
- **Target item:** `diamond_synthetic_industrial`
  - File: `kb/items/diamond_synthetic_industrial.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'diamond_synthesis_hpht_v0') requires input 'graphite_powder' which is not available

**Location:** Step 0
**Process:** `diamond_synthesis_hpht_v0`
  - File: `kb/processes/diamond_synthesis_hpht_v0.yaml`

**Current step:**
```yaml
- process_id: diamond_synthesis_hpht_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_diamond_synthetic_industrial_v0.yaml`
- **BOM available:** No
