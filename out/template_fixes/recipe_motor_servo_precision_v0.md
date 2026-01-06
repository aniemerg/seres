# Fix Intelligence: recipe_motor_servo_precision_v0

## Files

- **Recipe:** `kb/recipes/recipe_motor_servo_precision_v0.yaml`
- **Target item:** `motor_servo_precision`
  - File: `kb/items/motor_servo_precision.yaml`
- **BOM:** None
- **Steps:** 7 total

## Errors (7 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'coil_winding_motor_v0') requires input 'aluminum_wire' which is not available

**Location:** Step 1
**Process:** `coil_winding_motor_v0`
  - File: `kb/processes/coil_winding_motor_v0.yaml`

**Current step:**
```yaml
- process_id: coil_winding_motor_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'sensor_integration_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 3
**Process:** `sensor_integration_v0`
  - File: `kb/processes/sensor_integration_v0.yaml`

**Current step:**
```yaml
- process_id: sensor_integration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'motor_final_assembly_v0') requires input 'stator_rotor_lamination_set' which is not available

**Location:** Step 4
**Process:** `motor_final_assembly_v0`
  - File: `kb/processes/motor_final_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: motor_final_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `sensor_equipped_system` (1.0 unit)
- Step 4 produces: `motor_electric_small` (1.0 unit)

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `sensor_equipped_system` (1.0 unit)
- Step 4 produces: `motor_electric_small` (1.0 unit)
- Step 5 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 7
- **Recipe file:** `kb/recipes/recipe_motor_servo_precision_v0.yaml`
- **BOM available:** No
