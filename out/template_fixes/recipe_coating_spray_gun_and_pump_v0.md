# Fix Intelligence: recipe_coating_spray_gun_and_pump_v0

## Files

- **Recipe:** `kb/recipes/recipe_coating_spray_gun_and_pump_v0.yaml`
- **Target item:** `coating_spray_gun_and_pump`
  - File: `kb/items/coating_spray_gun_and_pump.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'raw_metal_block' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 8.0
    unit: kg
  - item_id: compressor_pump_small
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: applicator_nozzle
    qty: 1.0
    unit: unit
  - item_id: hydraulic_hose_assembly
    qty: 1.0
    unit: unit
  - item_id: fittings_and_valves
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `raw_metal_block` not found

This item doesn't exist in the KB.

#### Problem: Item `compressor_pump_small` not found

This item doesn't exist in the KB.

#### Problem: Item `motor_electric_small` not found

This item doesn't exist in the KB.

#### Problem: Item `applicator_nozzle` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_hose_assembly` not found

This item doesn't exist in the KB.

#### Problem: Item `fittings_and_valves` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_coating_spray_gun_and_pump_v0.yaml`
- **BOM available:** No
