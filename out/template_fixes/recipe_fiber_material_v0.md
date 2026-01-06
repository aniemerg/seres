# Fix Intelligence: recipe_fiber_material_v0

## Files

- **Recipe:** `kb/recipes/recipe_fiber_material_v0.yaml`
- **Target item:** `fiber_material`
  - File: `kb/items/fiber_material.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'basalt_melting_v0') requires input 'basalt_aggregate' which is not available

**Location:** Step 0
**Process:** `basalt_melting_v0`
  - File: `kb/processes/basalt_melting_v0.yaml`

**Current step:**
```yaml
- process_id: basalt_melting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'fiber_drawing_basic_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 1
**Process:** `fiber_drawing_basic_v0`
  - File: `kb/processes/fiber_drawing_basic_v0.yaml`

**Current step:**
```yaml
- process_id: fiber_drawing_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_fiber_material_v0.yaml`
- **BOM available:** No
