# Fix Intelligence: recipe_czochralski_puller_v0

## Files

- **Recipe:** `kb/recipes/recipe_czochralski_puller_v0.yaml`
- **Target item:** `czochralski_puller_v0`
  - File: `kb/items/czochralski_puller_v0.yaml`
- **BOM:** `kb/boms/bom_czochralski_puller_v0.yaml` ✓
  - Components: 10
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `structural_frame_steel` (qty: 1 None)
- `vacuum_chamber` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)
- `linear_actuator_precision` (qty: 1 unit)
- `spindle_assembly_precision` (qty: 2 None)
- `heating_element_set_high_temp` (qty: 1 None)
- `temperature_controller_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `motor_servo_precision` (qty: 3 None)

Suggested fix:
```yaml
- process_id: welding_and_fabrication_v0
  inputs:
  - item_id: structural_frame_steel
    qty: 1
    unit: None
  - item_id: vacuum_chamber
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
  - item_id: linear_actuator_precision
    qty: 1
    unit: unit
  - item_id: spindle_assembly_precision
    qty: 2
    unit: None
  - item_id: heating_element_set_high_temp
    qty: 1
    unit: None
  - item_id: temperature_controller_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: motor_servo_precision
    qty: 3
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `structural_frame_steel` (qty: 1 None)
- `vacuum_chamber` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)
- `linear_actuator_precision` (qty: 1 unit)
- `spindle_assembly_precision` (qty: 2 None)
- `heating_element_set_high_temp` (qty: 1 None)
- `temperature_controller_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `motor_servo_precision` (qty: 3 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: structural_frame_steel
    qty: 1
    unit: None
  - item_id: vacuum_chamber
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
  - item_id: linear_actuator_precision
    qty: 1
    unit: unit
  - item_id: spindle_assembly_precision
    qty: 2
    unit: None
  - item_id: heating_element_set_high_temp
    qty: 1
    unit: None
  - item_id: temperature_controller_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: motor_servo_precision
    qty: 3
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)

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

BOM has 10 components:

- `structural_frame_steel` (qty: 1 None)
- `vacuum_chamber` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)
- `linear_actuator_precision` (qty: 1 unit)
- `spindle_assembly_precision` (qty: 2 None)
- `heating_element_set_high_temp` (qty: 1 None)
- `temperature_controller_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `motor_servo_precision` (qty: 3 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: structural_frame_steel
    qty: 1
    unit: None
  - item_id: vacuum_chamber
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
  - item_id: linear_actuator_precision
    qty: 1
    unit: unit
  - item_id: spindle_assembly_precision
    qty: 2
    unit: None
  - item_id: heating_element_set_high_temp
    qty: 1
    unit: None
  - item_id: temperature_controller_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: motor_servo_precision
    qty: 3
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

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

- `structural_frame_steel` (qty: 1 None)
- `vacuum_chamber` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)
- `linear_actuator_precision` (qty: 1 unit)
- `spindle_assembly_precision` (qty: 2 None)
- `heating_element_set_high_temp` (qty: 1 None)
- `temperature_controller_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `motor_servo_precision` (qty: 3 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: structural_frame_steel
    qty: 1
    unit: None
  - item_id: vacuum_chamber
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
  - item_id: linear_actuator_precision
    qty: 1
    unit: unit
  - item_id: spindle_assembly_precision
    qty: 2
    unit: None
  - item_id: heating_element_set_high_temp
    qty: 1
    unit: None
  - item_id: temperature_controller_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: motor_servo_precision
    qty: 3
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- `structural_frame_steel` (qty: 1 None)
- `vacuum_chamber` (qty: 1 None)
- `support_frame_welded` (qty: 1 None)
- `mounting_fixtures_adjustable` (qty: 1 None)
- `linear_actuator_precision` (qty: 1 unit)
- `spindle_assembly_precision` (qty: 2 None)
- `heating_element_set_high_temp` (qty: 1 None)
- `temperature_controller_module` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `motor_servo_precision` (qty: 3 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: structural_frame_steel
    qty: 1
    unit: None
  - item_id: vacuum_chamber
    qty: 1
    unit: None
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: mounting_fixtures_adjustable
    qty: 1
    unit: None
  - item_id: linear_actuator_precision
    qty: 1
    unit: unit
  - item_id: spindle_assembly_precision
    qty: 2
    unit: None
  - item_id: heating_element_set_high_temp
    qty: 1
    unit: None
  - item_id: temperature_controller_module
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: motor_servo_precision
    qty: 3
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_czochralski_puller_v0.yaml`
- **BOM available:** Yes (10 components)
