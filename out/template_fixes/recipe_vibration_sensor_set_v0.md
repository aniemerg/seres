# Fix Intelligence: recipe_vibration_sensor_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_vibration_sensor_set_v0.yaml`
- **Target item:** `vibration_sensor_set`
  - File: `kb/items/vibration_sensor_set.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'assembly_basic_v0') requires input 'accelerometer_mechanical_v0' which is not available

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: accelerometer_mechanical_v0
    qty: 4.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `accelerometer_mechanical_v0` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `calibration_basic_v0`
  - File: `kb/processes/calibration_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_vibration_sensor_set_v0.yaml`
- **BOM available:** No
