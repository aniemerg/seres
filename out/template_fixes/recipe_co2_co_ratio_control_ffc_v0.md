# Fix Intelligence: recipe_co2_co_ratio_control_ffc_v0

## Files

- **Recipe:** `kb/recipes/recipe_co2_co_ratio_control_ffc_v0.yaml`
- **Target item:** `co2_co_ratio_control_ffc_v0`
  - File: `kb/items/co2_co_ratio_control_ffc_v0.yaml`
- **BOM:** `kb/boms/bom_co2_co_ratio_control_ffc_v0.yaml` ✓
  - Components: 3
- **Steps:** 4 total

## Errors (4 found)

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

#### Option A: Use BOM components

BOM has 3 components:

- `control_panel_basic` (qty: 1.0 unit)
- `structural_frame_steel` (qty: 2.0 kg)
- `fastener_kit_medium` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: control_panel_basic
    qty: 1.0
    unit: unit
  - item_id: structural_frame_steel
    qty: 2.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
```

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

### Error 3: recipe_template_missing_step_inputs

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

BOM has 3 components:

- `control_panel_basic` (qty: 1.0 unit)
- `structural_frame_steel` (qty: 2.0 kg)
- `fastener_kit_medium` (qty: 1.0 unit)

Suggested fix:
```yaml
- process_id: calibration_basic_v0
  inputs:
  - item_id: control_panel_basic
    qty: 1.0
    unit: unit
  - item_id: structural_frame_steel
    qty: 2.0
    unit: kg
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `sensor_equipped_system` (1.0 unit)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'electrical_testing_and_calibration_v0') requires input 'ffc_power_supply_assembled' which is not available

**Location:** Step 3
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

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_co2_co_ratio_control_ffc_v0.yaml`
- **BOM available:** Yes (3 components)
