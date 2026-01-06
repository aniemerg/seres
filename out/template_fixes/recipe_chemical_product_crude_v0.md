# Fix Intelligence: recipe_chemical_product_crude_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_product_crude_v0.yaml`
- **Target item:** `chemical_product_crude`
  - File: `kb/items/chemical_product_crude.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chemical_synthesis_process_v0') requires input 'methanol_liquid' which is not available

**Location:** Step 0
**Process:** `chemical_synthesis_process_v0`
  - File: `kb/processes/chemical_synthesis_process_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: chemical_synthesis_process_v0
  inputs:
  - item_id: methanol_liquid
    qty: 1.0
    unit: kg
  - item_id: ammonia_gas
    qty: 1.0
    unit: kg
  - item_id: carbon_monoxide_gas
    qty: 1.0
    unit: kg
  - item_id: water
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `methanol_liquid` not found

This item doesn't exist in the KB.

#### Problem: Item `ammonia_gas` not found

This item doesn't exist in the KB.

#### Problem: Item `carbon_monoxide_gas` not found

This item doesn't exist in the KB.

#### Problem: Item `water` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_chemical_product_crude_v0.yaml`
- **BOM available:** No
