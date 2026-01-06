# Fix Intelligence: recipe_machine_fiber_spinneret_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_fiber_spinneret_v0.yaml`
- **Target item:** `fiber_spinneret_v0`
  - File: `kb/items/fiber_spinneret_v0.yaml`
- **BOM:** `kb/boms/bom_fiber_spinneret_v0.yaml` ✓
  - Components: 6
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `spinneret_block_basic` (qty: 1 None)
- `spinneret_heating_module` (qty: 1 None)
- `temperature_sensing` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: spinneret_block_basic
    qty: 1
    unit: None
  - item_id: spinneret_heating_module
    qty: 1
    unit: None
  - item_id: temperature_sensing
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 6 components:

- `spinneret_block_basic` (qty: 1 None)
- `spinneret_heating_module` (qty: 1 None)
- `temperature_sensing` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: spinneret_block_basic
    qty: 1
    unit: None
  - item_id: spinneret_heating_module
    qty: 1
    unit: None
  - item_id: temperature_sensing
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 1 produces: `cast_metal_parts` (0.95 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_machine_fiber_spinneret_v0.yaml`
- **BOM available:** Yes (6 components)
