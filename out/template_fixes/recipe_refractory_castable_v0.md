# Fix Intelligence: recipe_refractory_castable_v0

## Files

- **Recipe:** `kb/recipes/recipe_refractory_castable_v0.yaml`
- **Target item:** `refractory_castable`
  - File: `kb/items/refractory_castable.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'refractory_castable_mixing_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `refractory_castable_mixing_v0`
  - File: `kb/processes/refractory_castable_mixing_v0.yaml`

**Current step:**
```yaml
- process_id: refractory_castable_mixing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_refractory_castable_v0.yaml`
- **BOM available:** No
