# Fix Intelligence: recipe_wire_copper_insulated_import_v1

## Files

- **Recipe:** `kb/recipes/recipe_wire_copper_insulated_import_v1.yaml`
- **Target item:** `wire_copper_insulated`
  - File: `kb/items/wire_copper_insulated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_wire_copper_insulated_import_v0` → wire_copper_insulated_v0 (1 steps)
- `recipe_wire_copper_insulated_v0` → wire_copper_insulated_v0 (1 steps)
- `recipe_wire_copper_insulated_v1` → wire_copper_insulated (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'insulated_wire_formation_v0') requires input 'magnet_wire_copper' which is not available

**Location:** Step 0
**Process:** `insulated_wire_formation_v0`
  - File: `kb/processes/insulated_wire_formation_v0.yaml`

**Current step:**
```yaml
- process_id: insulated_wire_formation_v0
  inputs:
  - item_id: magnet_wire_copper
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `magnet_wire_copper` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_wire_copper_insulated_import_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
