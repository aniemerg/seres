# Fix Intelligence: recipe_hydraulic_cylinder_body_machined_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_cylinder_body_machined_v0.yaml`
- **Target item:** `hydraulic_cylinder_body_machined`
  - File: `kb/items/hydraulic_cylinder_body_machined.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_process_boring_v0') requires input 'hydraulic_cylinder_body_cast' which is not available

**Location:** Step 0
**Process:** `machining_process_boring_v0`
  - File: `kb/processes/machining_process_boring_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_boring_v0
  inputs:
  - item_id: hydraulic_cylinder_body_cast
    qty: 7.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `hydraulic_cylinder_body_cast` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hydraulic_cylinder_body_machined_v0.yaml`
- **BOM available:** No
