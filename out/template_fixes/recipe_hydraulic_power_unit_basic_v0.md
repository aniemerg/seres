# Fix Intelligence: recipe_hydraulic_power_unit_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_power_unit_basic_v0.yaml`
- **Target item:** `hydraulic_power_unit_basic`
  - File: `kb/items/hydraulic_power_unit_basic.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'hydraulic_reservoir_basic' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: hydraulic_reservoir_basic
    qty: 1.0
    unit: unit
  - item_id: hydraulic_pump_basic
    qty: 1.0
    unit: unit
  - item_id: hydraulic_valve_manifold_basic
    qty: 1.0
    unit: unit
  - item_id: motor_electric_small
    qty: 1.0
    unit: unit
  - item_id: power_output_terminals
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `hydraulic_reservoir_basic` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_pump_basic` not found

This item doesn't exist in the KB.

#### Problem: Item `hydraulic_valve_manifold_basic` not found

This item doesn't exist in the KB.

#### Problem: Item `motor_electric_small` not found

This item doesn't exist in the KB.

#### Problem: Item `power_output_terminals` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_medium` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `hydraulic_power_unit_basic` (1.0 unit)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_hydraulic_power_unit_basic_v0.yaml`
- **BOM available:** No
