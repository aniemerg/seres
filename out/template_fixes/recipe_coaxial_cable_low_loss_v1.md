# Fix Intelligence: recipe_coaxial_cable_low_loss_v1

## Files

- **Recipe:** `kb/recipes/recipe_coaxial_cable_low_loss_v1.yaml`
- **Target item:** `coaxial_cable_low_loss`
  - File: `kb/items/coaxial_cable_low_loss.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_coaxial_cable_low_loss_v0` → coaxial_cable_low_loss_v0 (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cable_harness_assembly_v0') requires input 'wire_copper_insulated' which is not available

**Location:** Step 0
**Process:** `cable_harness_assembly_v0`
  - File: `kb/processes/cable_harness_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: cable_harness_assembly_v0
  inputs:
  - item_id: wire_copper_insulated
    qty: 0.6
    unit: kg
  - item_id: electrical_wire_and_connectors
    qty: 0.2
    unit: kg
  - item_id: insulation_coating_material
    qty: 0.2
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `electrical_wire_and_connectors` not found

This item doesn't exist in the KB.

#### Problem: Item `insulation_coating_material` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coaxial_cable_low_loss_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
