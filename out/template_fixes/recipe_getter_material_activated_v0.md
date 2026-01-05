# Fix Intelligence: recipe_getter_material_activated_v0

## Files

- **Recipe:** `kb/recipes/recipe_getter_material_activated_v0.yaml`
- **Target item:** `getter_material_activated`
  - File: `kb/items/getter_material_activated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'getter_material_activation_v0') requires input 'getter_material_raw' which is not available

**Location:** Step 0
**Process:** `getter_material_activation_v0`
  - File: `kb/processes/getter_material_activation_v0.yaml`

**Current step:**
```yaml
- process_id: getter_material_activation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_getter_material_activated_v0.yaml`
- **BOM available:** No
