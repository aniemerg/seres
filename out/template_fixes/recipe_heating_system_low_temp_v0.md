# Fix Intelligence: recipe_heating_system_low_temp_v0

## Files

- **Recipe:** `kb/recipes/recipe_heating_system_low_temp_v0.yaml`
- **Target item:** `heating_system_low_temp`
  - File: `kb/items/heating_system_low_temp.yaml`
- **BOM:** `kb/boms/bom_heating_system_low_temp.yaml` ✓
  - Components: 10
- **Steps:** 6 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_forming_v0') requires input 'steel_plate_or_sheet' which is not available

**Location:** Step 0
**Process:** `sheet_metal_forming_v0`
  - File: `kb/processes/sheet_metal_forming_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_basic_v0`
  - File: `kb/processes/welding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `heating_chamber_large` (qty: 1 None)
- `heating_element_electric` (qty: 2 None)
- `blower_fan_small` (qty: 1 None)
- `insulation_thermal_blanket` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `furnace_door_assembly` (qty: 1 None)
- `power_cable_assembly` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_basic_v0
  inputs:
  - item_id: heating_chamber_large
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 2
    unit: None
  - item_id: blower_fan_small
    qty: 1
    unit: None
  - item_id: insulation_thermal_blanket
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: furnace_door_assembly
    qty: 1
    unit: None
  - item_id: power_cable_assembly
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- `heating_chamber_large` (qty: 1 None)
- `heating_element_electric` (qty: 2 None)
- `blower_fan_small` (qty: 1 None)
- `insulation_thermal_blanket` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `furnace_door_assembly` (qty: 1 None)
- `power_cable_assembly` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: heating_chamber_large
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 2
    unit: None
  - item_id: blower_fan_small
    qty: 1
    unit: None
  - item_id: insulation_thermal_blanket
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: furnace_door_assembly
    qty: 1
    unit: None
  - item_id: power_cable_assembly
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `insulated_assembly` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 4
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `heating_chamber_large` (qty: 1 None)
- `heating_element_electric` (qty: 2 None)
- `blower_fan_small` (qty: 1 None)
- `insulation_thermal_blanket` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `furnace_door_assembly` (qty: 1 None)
- `power_cable_assembly` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: heating_chamber_large
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 2
    unit: None
  - item_id: blower_fan_small
    qty: 1
    unit: None
  - item_id: insulation_thermal_blanket
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: furnace_door_assembly
    qty: 1
    unit: None
  - item_id: power_cable_assembly
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `formed_sheet_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `insulated_assembly` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_heating_system_low_temp_v0.yaml`
- **BOM available:** Yes (10 components)
