# Fix Intelligence: recipe_bearing_rings_hardened_v1

## Files

- **Recipe:** `kb/recipes/recipe_bearing_rings_hardened_v1.yaml`
- **Target item:** `bearing_rings_hardened`
  - File: `kb/items/bearing_rings_hardened.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_bearing_rings_hardened_v0` → bearing_rings_hardened_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 0
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  inputs:
  - item_id: bearing_rings_machined
    qty: 0.25
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `bearing_rings_machined` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_bearing_rings_hardened_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
