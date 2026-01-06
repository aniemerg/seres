# Fix Intelligence: recipe_power_supply_dc_high_current_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_supply_dc_high_current_v0.yaml`
- **Target item:** `power_supply_dc_high_current`
  - File: `kb/items/power_supply_dc_high_current.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'transformer_power_medium' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: transformer_power_medium
    qty: 25.0
    unit: kg
  - item_id: rectifier_bridge_heavy_duty
    qty: 2.0
    unit: kg
  - item_id: capacitor_bank_power
    qty: 5.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `transformer_power_medium` not found

This item doesn't exist in the KB.

#### Problem: Item `rectifier_bridge_heavy_duty` not found

This item doesn't exist in the KB.

#### Problem: Item `capacitor_bank_power` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'wiring_and_electronics_integration_v0') requires input 'control_circuit_board_power' which is not available

**Location:** Step 1
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: control_circuit_board_power
    qty: 2.0
    unit: kg
  - item_id: enclosure_steel_large
    qty: 3.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `control_circuit_board_power` not found

This item doesn't exist in the KB.

#### Problem: Item `enclosure_steel_large` not found

This item doesn't exist in the KB.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_power_supply_dc_high_current_v0.yaml`
- **BOM available:** No
