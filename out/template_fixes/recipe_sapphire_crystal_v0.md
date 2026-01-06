# Fix Intelligence: recipe_sapphire_crystal_v0

## Files

- **Recipe:** `kb/recipes/recipe_sapphire_crystal_v0.yaml`
- **Target item:** `sapphire_crystal`
  - File: `kb/items/sapphire_crystal.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sapphire_crystal_growth_czochralski_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `sapphire_crystal_growth_czochralski_v0`
  - File: `kb/processes/sapphire_crystal_growth_czochralski_v0.yaml`

**Current step:**
```yaml
- process_id: sapphire_crystal_growth_czochralski_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sapphire_crystal_v0.yaml`
- **BOM available:** No
