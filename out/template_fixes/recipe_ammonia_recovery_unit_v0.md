# Fix Intelligence: recipe_ammonia_recovery_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_ammonia_recovery_unit_v0.yaml`
- **Target item:** `ammonia_recovery_unit_v0`
  - File: `kb/items/ammonia_recovery_unit_v0.yaml`
- **BOM:** `kb/boms/bom_ammonia_recovery_unit_v0.yaml` ✓
  - Components: 9
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
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

BOM has 9 components:

- `pressure_vessel_steel` (qty: 150.0 kg)
- `heating_element_resistive` (qty: 2 unit)
- `vapor_condenser_cold_trap` (qty: 1 unit)
- `piping_and_fittings_thermal` (qty: 50.0 kg)
- `valve_set_gas_handling` (qty: 1 unit)
- `structural_frame_steel` (qty: 100.0 kg)
- `thermal_insulation_basic` (qty: 30.0 kg)
- `control_panel_basic` (qty: 1 unit)
- `fastener_kit_medium` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 150.0
    unit: kg
  - item_id: heating_element_resistive
    qty: 2
    unit: unit
  - item_id: vapor_condenser_cold_trap
    qty: 1
    unit: unit
  - item_id: piping_and_fittings_thermal
    qty: 50.0
    unit: kg
  - item_id: valve_set_gas_handling
    qty: 1
    unit: unit
  - item_id: structural_frame_steel
    qty: 100.0
    unit: kg
  - item_id: thermal_insulation_basic
    qty: 30.0
    unit: kg
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_ammonia_recovery_unit_v0.yaml`
- **BOM available:** Yes (9 components)
