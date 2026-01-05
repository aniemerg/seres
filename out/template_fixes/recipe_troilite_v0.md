# Fix Intelligence: recipe_troilite_v0

## Files

- **Recipe:** `kb/recipes/recipe_troilite_v0.yaml`
- **Target item:** `troilite`
  - File: `kb/items/troilite.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'troilite_concentration_v0') requires input 'regolith_powder' which is not available

**Location:** Step 0
**Process:** `troilite_concentration_v0`
  - File: `kb/processes/troilite_concentration_v0.yaml`

**Current step:**
```yaml
- process_id: troilite_concentration_v0
  inputs:
  - item_id: regolith_powder
    qty: 10.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `regolith_powder` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_troilite_v0.yaml`
- **BOM available:** No
