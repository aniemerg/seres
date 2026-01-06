# Fix Intelligence: recipe_heat_exchanger_tube_bundle_v0

## Files

- **Recipe:** `kb/recipes/recipe_heat_exchanger_tube_bundle_v0.yaml`
- **Target item:** `heat_exchanger_tube_bundle`
  - File: `kb/items/heat_exchanger_tube_bundle.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'tube_forming_process_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `tube_forming_process_v0`
  - File: `kb/processes/tube_forming_process_v0.yaml`

**Current step:**
```yaml
- process_id: tube_forming_process_v0
  inputs:
  - item_id: metal_tubing_stock
    qty: 110.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_tubing_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_process_tig_v0') requires input 'fittings_and_valves' which is not available

**Location:** Step 1
**Process:** `welding_process_tig_v0`
  - File: `kb/processes/welding_process_tig_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_tig_v0
  inputs:
  - item_id: tube_coils_formed
    qty: 105.0
    unit: kg
  - item_id: fittings_and_valves
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tube_coils_formed` not found

This item doesn't exist in the KB.

#### Problem: Item `fittings_and_valves` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_heat_exchanger_tube_bundle_v0.yaml`
- **BOM available:** No
