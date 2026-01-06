# Fix Intelligence: recipe_solder_tin_lead_v0

## Files

- **Recipe:** `kb/recipes/recipe_solder_tin_lead_v0.yaml`
- **Target item:** `solder_tin_lead`
  - File: `kb/items/solder_tin_lead.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_casting_basic_v0') requires input 'tin_metal_pure' which is not available

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: tin_metal_pure
    qty: 0.63
    unit: kg
  - item_id: lead_metal
    qty: 0.37
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `tin_metal_pure` not found

This item doesn't exist in the KB.

#### Problem: Item `lead_metal` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_solder_tin_lead_v0.yaml`
- **BOM available:** No
