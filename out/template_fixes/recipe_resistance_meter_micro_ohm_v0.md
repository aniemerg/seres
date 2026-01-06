# Fix Intelligence: recipe_resistance_meter_micro_ohm_v0

## Files

- **Recipe:** `kb/recipes/recipe_resistance_meter_micro_ohm_v0.yaml`
- **Target item:** `resistance_meter_micro_ohm`
  - File: `kb/items/resistance_meter_micro_ohm.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'electrical_testing_and_calibration_v0') requires input 'ffc_power_supply_assembled' which is not available

**Location:** Step 2
**Process:** `electrical_testing_and_calibration_v0`
  - File: `kb/processes/electrical_testing_and_calibration_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_testing_and_calibration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_resistance_meter_micro_ohm_v0.yaml`
- **BOM available:** No
