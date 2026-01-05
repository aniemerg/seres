# Fix Intelligence: recipe_build_atmosphere_control_v0

## Files

- **Recipe:** `kb/recipes/recipe_build_atmosphere_control_v0.yaml`
- **Target item:** `build_atmosphere_control_v0`
  - File: `kb/items/build_atmosphere_control_v0.yaml`
- **BOM:** `kb/boms/bom_build_atmosphere_control_v0.yaml` ✓
  - Components: 9
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- `vacuum_pump_small` (qty: 1 None)
- `gas_cylinder_mount` (qty: 2 None)
- `flow_controller_valve_set` (qty: 1 None)
- `oxygen_sensor_zirconia` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `piping_assembly_small` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `enclosure_steel_small` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: vacuum_pump_small
    qty: 1
    unit: None
  - item_id: gas_cylinder_mount
    qty: 2
    unit: None
  - item_id: flow_controller_valve_set
    qty: 1
    unit: None
  - item_id: oxygen_sensor_zirconia
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: piping_assembly_small
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: enclosure_steel_small
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 9 components:

- `vacuum_pump_small` (qty: 1 None)
- `gas_cylinder_mount` (qty: 2 None)
- `flow_controller_valve_set` (qty: 1 None)
- `oxygen_sensor_zirconia` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `piping_assembly_small` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `enclosure_steel_small` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: vacuum_pump_small
    qty: 1
    unit: None
  - item_id: gas_cylinder_mount
    qty: 2
    unit: None
  - item_id: flow_controller_valve_set
    qty: 1
    unit: None
  - item_id: oxygen_sensor_zirconia
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: piping_assembly_small
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: enclosure_steel_small
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 9 components:

- `vacuum_pump_small` (qty: 1 None)
- `gas_cylinder_mount` (qty: 2 None)
- `flow_controller_valve_set` (qty: 1 None)
- `oxygen_sensor_zirconia` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `piping_assembly_small` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `enclosure_steel_small` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: vacuum_pump_small
    qty: 1
    unit: None
  - item_id: gas_cylinder_mount
    qty: 2
    unit: None
  - item_id: flow_controller_valve_set
    qty: 1
    unit: None
  - item_id: oxygen_sensor_zirconia
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: piping_assembly_small
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: enclosure_steel_small
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 9 components:

- `vacuum_pump_small` (qty: 1 None)
- `gas_cylinder_mount` (qty: 2 None)
- `flow_controller_valve_set` (qty: 1 None)
- `oxygen_sensor_zirconia` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `piping_assembly_small` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `enclosure_steel_small` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: vacuum_pump_small
    qty: 1
    unit: None
  - item_id: gas_cylinder_mount
    qty: 2
    unit: None
  - item_id: flow_controller_valve_set
    qty: 1
    unit: None
  - item_id: oxygen_sensor_zirconia
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: piping_assembly_small
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: enclosure_steel_small
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `enclosure_electrical_medium` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 9 components:

- `vacuum_pump_small` (qty: 1 None)
- `gas_cylinder_mount` (qty: 2 None)
- `flow_controller_valve_set` (qty: 1 None)
- `oxygen_sensor_zirconia` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `piping_assembly_small` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `enclosure_steel_small` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: vacuum_pump_small
    qty: 1
    unit: None
  - item_id: gas_cylinder_mount
    qty: 2
    unit: None
  - item_id: flow_controller_valve_set
    qty: 1
    unit: None
  - item_id: oxygen_sensor_zirconia
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: piping_assembly_small
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: enclosure_steel_small
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_build_atmosphere_control_v0.yaml`
- **BOM available:** Yes (9 components)
