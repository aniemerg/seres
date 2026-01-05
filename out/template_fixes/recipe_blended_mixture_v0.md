# Fix Intelligence: recipe_blended_mixture_v0

## Files

- **Recipe:** `kb/recipes/recipe_blended_mixture_v0.yaml`
- **Target item:** `blended_mixture`
  - File: `kb/items/blended_mixture.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mixing_and_blending_v0') requires input 'component_material_a' which is not available

**Location:** Step 0
**Process:** `mixing_and_blending_v0`
  - File: `kb/processes/mixing_and_blending_v0.yaml`

**Current step:**
```yaml
- process_id: mixing_and_blending_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_blended_mixture_v0.yaml`
- **BOM available:** No
