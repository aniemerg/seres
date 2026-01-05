# Fix Intelligence: recipe_cryogenic_separation_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_cryogenic_separation_system_v0.yaml`
- **Target item:** `cryogenic_separation_system_v0`
  - File: `kb/items/cryogenic_separation_system_v0.yaml`
- **BOM:** `kb/boms/bom_cryogenic_separation_system_v0.yaml` ✓
  - Components: 11
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'welding_structural_v0') requires input 'cut_parts' which is not available

**Location:** Step 0
**Process:** `welding_structural_v0`
  - File: `kb/processes/welding_structural_v0.yaml`

**Current step:**
```yaml
- process_id: welding_structural_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 11 components:

- `cryocooler_active_v0` (qty: 1 unit)
- `pressure_vessel_steel` (qty: 200.0 kg)
- `distillation_column_module_v0` (qty: 1 unit)
- `thermal_insulation_basic` (qty: 50.0 kg)
- `vacuum_pump_station` (qty: 1 unit)
- `valve_set_gas_handling` (qty: 1 unit)
- `piping_and_fittings_thermal` (qty: 100.0 kg)
- `control_panel_basic` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)
- `structural_frame_steel` (qty: 150.0 kg)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: cryocooler_active_v0
    qty: 1
    unit: unit
  - item_id: pressure_vessel_steel
    qty: 200.0
    unit: kg
  - item_id: distillation_column_module_v0
    qty: 1
    unit: unit
  - item_id: thermal_insulation_basic
    qty: 50.0
    unit: kg
  - item_id: vacuum_pump_station
    qty: 1
    unit: unit
  - item_id: valve_set_gas_handling
    qty: 1
    unit: unit
  - item_id: piping_and_fittings_thermal
    qty: 100.0
    unit: kg
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
  - item_id: structural_frame_steel
    qty: 150.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.05 kg)

---

### Error 3: recipe_template_missing_step_inputs

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

BOM has 11 components:

- `cryocooler_active_v0` (qty: 1 unit)
- `pressure_vessel_steel` (qty: 200.0 kg)
- `distillation_column_module_v0` (qty: 1 unit)
- `thermal_insulation_basic` (qty: 50.0 kg)
- `vacuum_pump_station` (qty: 1 unit)
- `valve_set_gas_handling` (qty: 1 unit)
- `piping_and_fittings_thermal` (qty: 100.0 kg)
- `control_panel_basic` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)
- `structural_frame_steel` (qty: 150.0 kg)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: cryocooler_active_v0
    qty: 1
    unit: unit
  - item_id: pressure_vessel_steel
    qty: 200.0
    unit: kg
  - item_id: distillation_column_module_v0
    qty: 1
    unit: unit
  - item_id: thermal_insulation_basic
    qty: 50.0
    unit: kg
  - item_id: vacuum_pump_station
    qty: 1
    unit: unit
  - item_id: valve_set_gas_handling
    qty: 1
    unit: unit
  - item_id: piping_and_fittings_thermal
    qty: 100.0
    unit: kg
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
  - item_id: structural_frame_steel
    qty: 150.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.05 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_cryogenic_separation_system_v0.yaml`
- **BOM available:** Yes (11 components)
