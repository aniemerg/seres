# Fix Intelligence: recipe_hydraulic_hoses_and_fittings_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_hoses_and_fittings_v0.yaml`
- **Target item:** `hydraulic_hoses_and_fittings`
  - File: `kb/items/hydraulic_hoses_and_fittings.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'hose_cutting_and_crimping_v0') requires input 'nitrile_rubber' which is not available

**Location:** Step 0
**Process:** `hose_cutting_and_crimping_v0`
  - File: `kb/processes/hose_cutting_and_crimping_v0.yaml`

**Current step:**
```yaml
- process_id: hose_cutting_and_crimping_v0
  inputs:
  - item_id: nitrile_rubber
    qty: 5.0
    unit: kg
  - item_id: metal_tubing_stock
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `nitrile_rubber` not found

This item doesn't exist in the KB.

#### Problem: Item `metal_tubing_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'fitting_assembly_basic_v0') requires input 'fastener_kit_medium' which is not available

**Location:** Step 1
**Process:** `fitting_assembly_basic_v0`
  - File: `kb/processes/fitting_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: fitting_assembly_basic_v0
  inputs:
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_hydraulic_hoses_and_fittings_v0.yaml`
- **BOM available:** No
