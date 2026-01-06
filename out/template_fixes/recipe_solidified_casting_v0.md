# Fix Intelligence: recipe_solidified_casting_v0

## Files

- **Recipe:** `kb/recipes/recipe_solidified_casting_v0.yaml`
- **Target item:** `solidified_casting`
  - File: `kb/items/solidified_casting.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cooling_solidification_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 0
**Process:** `cooling_solidification_v0`
  - File: `kb/processes/cooling_solidification_v0.yaml`

**Current step:**
```yaml
- process_id: cooling_solidification_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_solidified_casting_v0.yaml`
- **BOM available:** No
