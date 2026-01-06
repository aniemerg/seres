# Fix Intelligence: recipe_slag_coproduct_v0

## Files

- **Recipe:** `kb/recipes/recipe_slag_coproduct_v0.yaml`
- **Target item:** `slag`
  - File: `kb/items/slag.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'iron_smelting_reduction_v0') requires input 'iron_ore_or_ilmenite' which is not available

**Location:** Step 0
**Process:** `iron_smelting_reduction_v0`
  - File: `kb/processes/iron_smelting_reduction_v0.yaml`

**Current step:**
```yaml
- process_id: iron_smelting_reduction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_slag_coproduct_v0.yaml`
- **BOM available:** No
