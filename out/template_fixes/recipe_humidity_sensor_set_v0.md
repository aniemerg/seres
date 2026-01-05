# Fix Intelligence: recipe_humidity_sensor_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_humidity_sensor_set_v0.yaml`
- **Target item:** `humidity_sensor_set`
  - File: `kb/items/humidity_sensor_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sensor_integration_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 0
**Process:** `sensor_integration_v0`
  - File: `kb/processes/sensor_integration_v0.yaml`

**Current step:**
```yaml
- process_id: sensor_integration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sensor_calibration_v0') requires input 'sensor_suite_general' which is not available

**Location:** Step 1
**Process:** `sensor_calibration_v0`
  - File: `kb/processes/sensor_calibration_v0.yaml`

**Current step:**
```yaml
- process_id: sensor_calibration_v0
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

- Step 0 produces: `sensor_equipped_system` (1.0 unit)
- Step 1 produces: `sensor_suite_general` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_humidity_sensor_set_v0.yaml`
- **BOM available:** No
