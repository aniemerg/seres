# Fix Intelligence: recipe_atmosphere_sensors_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_atmosphere_sensors_basic_v0.yaml`
- **Target item:** `atmosphere_sensors_basic`
  - File: `kb/items/atmosphere_sensors_basic.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'pcb_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sensor_integration_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 1
**Process:** `sensor_integration_v0`
  - File: `kb/processes/sensor_integration_v0.yaml`

**Current step:**
```yaml
- process_id: sensor_integration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'sensor_calibration_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 2
**Process:** `sensor_calibration_v0`
  - File: `kb/processes/sensor_calibration_v0.yaml`

**Current step:**
```yaml
- process_id: sensor_calibration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

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

#### Option B: Use previous step outputs

- Step 1 produces: `sensor_equipped_system` (1.0 unit)
- Step 2 produces: `sensor_suite_general` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_atmosphere_sensors_basic_v0.yaml`
- **BOM available:** No
