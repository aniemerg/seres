# Fix Intelligence: recipe_roasting_furnace_v0

## Files

- **Recipe:** `kb/recipes/recipe_roasting_furnace_v0.yaml`
- **Target item:** `roasting_furnace_v0`
  - File: `kb/items/roasting_furnace_v0.yaml`
- **BOM:** `kb/boms/bom_roasting_furnace_v0.yaml` ✓
  - Components: 10
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_fabrication_welding_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `refractory_brick_set` (qty: 200.0 kg)
- `structural_steel_frame` (qty: 300.0 kg)
- `heating_element_set_high_temp` (qty: 2 unit)
- `thermal_insulation_basic` (qty: 100.0 kg)
- `air_blower_industrial` (qty: 1 unit)
- `piping_and_fittings_thermal` (qty: 50.0 kg)
- `temperature_controller_basic` (qty: 1 unit)
- `thermocouple_type_s_v0` (qty: 2 unit)
- `valve_set_gas_handling` (qty: 1 unit)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: refractory_brick_set
    qty: 200.0
    unit: kg
  - item_id: structural_steel_frame
    qty: 300.0
    unit: kg
  - item_id: heating_element_set_high_temp
    qty: 2
    unit: unit
  - item_id: thermal_insulation_basic
    qty: 100.0
    unit: kg
  - item_id: air_blower_industrial
    qty: 1
    unit: unit
  - item_id: piping_and_fittings_thermal
    qty: 50.0
    unit: kg
  - item_id: temperature_controller_basic
    qty: 1
    unit: unit
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: unit
  - item_id: valve_set_gas_handling
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `refractory_brick_set` (qty: 200.0 kg)
- `structural_steel_frame` (qty: 300.0 kg)
- `heating_element_set_high_temp` (qty: 2 unit)
- `thermal_insulation_basic` (qty: 100.0 kg)
- `air_blower_industrial` (qty: 1 unit)
- `piping_and_fittings_thermal` (qty: 50.0 kg)
- `temperature_controller_basic` (qty: 1 unit)
- `thermocouple_type_s_v0` (qty: 2 unit)
- `valve_set_gas_handling` (qty: 1 unit)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: refractory_brick_set
    qty: 200.0
    unit: kg
  - item_id: structural_steel_frame
    qty: 300.0
    unit: kg
  - item_id: heating_element_set_high_temp
    qty: 2
    unit: unit
  - item_id: thermal_insulation_basic
    qty: 100.0
    unit: kg
  - item_id: air_blower_industrial
    qty: 1
    unit: unit
  - item_id: piping_and_fittings_thermal
    qty: 50.0
    unit: kg
  - item_id: temperature_controller_basic
    qty: 1
    unit: unit
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: unit
  - item_id: valve_set_gas_handling
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_roasting_furnace_v0.yaml`
- **BOM available:** Yes (10 components)
