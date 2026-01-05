# Fix Intelligence: recipe_sensor_equipped_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_sensor_equipped_system_v0.yaml`
- **Target item:** `sensor_equipped_system`
  - File: `kb/items/sensor_equipped_system.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `assembled_electronics` (1.0 unit)

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

- Step 0 produces: `assembled_electronics` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)

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

- Step 0 produces: `assembled_electronics` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `electrical_testing_basic_v0`
  - File: `kb/processes/electrical_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_electronics` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `instrument_calibrated` (1.0 unit)

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

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_electronics` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `instrument_calibrated` (1.0 unit)
- Step 4 produces: `tested_electrical_equipment` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_sensor_equipped_system_v0.yaml`
- **BOM available:** No
