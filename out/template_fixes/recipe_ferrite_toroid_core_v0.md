# Fix Intelligence: recipe_ferrite_toroid_core_v0

## Files

- **Recipe:** `kb/recipes/recipe_ferrite_toroid_core_v0.yaml`
- **Target item:** `ferrite_toroid_core_v0`
  - File: `kb/items/ferrite_toroid_core_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'ball_milling_v0') requires input 'coarse_powder' which is not available

**Location:** Step 0
**Process:** `ball_milling_v0`
  - File: `kb/processes/ball_milling_v0.yaml`

**Current step:**
```yaml
- process_id: ball_milling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ferrite_toroid_sintering_v0') requires input 'powder_metal_or_ceramic' which is not available

**Location:** Step 1
**Process:** `ferrite_toroid_sintering_v0`
  - File: `kb/processes/ferrite_toroid_sintering_v0.yaml`

**Current step:**
```yaml
- process_id: ferrite_toroid_sintering_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_ferrite_toroid_core_v0.yaml`
- **BOM available:** No
