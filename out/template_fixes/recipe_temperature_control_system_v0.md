# Fix Intelligence: recipe_temperature_control_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_temperature_control_system_v0.yaml`
- **Target item:** `temperature_control_system_v0`
  - File: `kb/items/temperature_control_system_v0.yaml`
- **BOM:** `kb/boms/bom_temperature_control_system_v0.yaml` ✓
  - Components: 2
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

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

#### Option A: Use BOM components

BOM has 2 components:

- `temperature_controller_basic` (qty: 1.0 None)
- `temperature_controller_module` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: temperature_controller_basic
    qty: 1.0
    unit: None
  - item_id: temperature_controller_module
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `temperature_control_system_v0` (1.0 unit)

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `calibration_basic_v0`
  - File: `kb/processes/calibration_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 2 components:

- `temperature_controller_basic` (qty: 1.0 None)
- `temperature_controller_module` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: calibration_basic_v0
  inputs:
  - item_id: temperature_controller_basic
    qty: 1.0
    unit: None
  - item_id: temperature_controller_module
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `temperature_control_system_v0` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 2 components:

- `temperature_controller_basic` (qty: 1.0 None)
- `temperature_controller_module` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: temperature_controller_basic
    qty: 1.0
    unit: None
  - item_id: temperature_controller_module
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `temperature_control_system_v0` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `instrument_calibrated` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_temperature_control_system_v0.yaml`
- **BOM available:** Yes (2 components)
