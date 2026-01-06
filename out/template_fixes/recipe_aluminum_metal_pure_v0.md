# Fix Intelligence: recipe_aluminum_metal_pure_v0

## Files

- **Recipe:** `kb/recipes/recipe_aluminum_metal_pure_v0.yaml`
- **Target item:** `aluminum_metal_pure`
  - File: `kb/items/aluminum_metal_pure.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'aluminum_smelting_hall_heroult_v0') requires input 'alumina_powder' which is not available

**Location:** Step 0
**Process:** `aluminum_smelting_hall_heroult_v0`
  - File: `kb/processes/aluminum_smelting_hall_heroult_v0.yaml`

**Current step:**
```yaml
- process_id: aluminum_smelting_hall_heroult_v0
  inputs:
  - item_id: alumina_powder
    qty: 2.0
    unit: kg
  - item_id: carbon_anode
    qty: 0.5
    unit: kg
  - item_id: cryolite_flux
    qty: 0.15
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `alumina_powder` not found

This item doesn't exist in the KB.

#### Problem: Item `carbon_anode` not found

This item doesn't exist in the KB.

#### Problem: Item `cryolite_flux` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_aluminum_metal_pure_v0.yaml`
- **BOM available:** No
