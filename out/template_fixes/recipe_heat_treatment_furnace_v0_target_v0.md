# Fix Intelligence: recipe_heat_treatment_furnace_v0_target_v0

## Files

- **Recipe:** `kb/recipes/recipe_heat_treatment_furnace_v0_target_v0.yaml`
- **Target item:** `heat_treatment_furnace_v0`
  - File: `kb/items/heat_treatment_furnace_v0.yaml`
- **BOM:** `kb/boms/bom_heat_treatment_furnace_v0.yaml` ✓
  - Components: 10
- **Steps:** 5 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_heat_treatment_furnace_v0` → heat_treatment_furnace (5 steps)
- `recipe_heat_treatment_furnace_v0_v0` → heat_treatment_furnace_v0 (5 steps)
- `recipe_machine_heat_treatment_furnace_v0` → heat_treatment_furnace (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
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

BOM has 10 components:

- `furnace_shell_insulated` (qty: 1 None)
- `refractory_lining_set` (qty: 1 None)
- `heating_element_set_basic` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `level_sensor_basic` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `quench_rack_and_baskets` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: furnace_shell_insulated
    qty: 1
    unit: None
  - item_id: refractory_lining_set
    qty: 1
    unit: None
  - item_id: heating_element_set_basic
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: level_sensor_basic
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: quench_rack_and_baskets
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `coil_winding_basic_v0`
  - File: `kb/processes/coil_winding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: coil_winding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 10 components:

- `furnace_shell_insulated` (qty: 1 None)
- `refractory_lining_set` (qty: 1 None)
- `heating_element_set_basic` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `level_sensor_basic` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `quench_rack_and_baskets` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: coil_winding_basic_v0
  inputs:
  - item_id: furnace_shell_insulated
    qty: 1
    unit: None
  - item_id: refractory_lining_set
    qty: 1
    unit: None
  - item_id: heating_element_set_basic
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: level_sensor_basic
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: quench_rack_and_baskets
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

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

- `furnace_shell_insulated` (qty: 1 None)
- `refractory_lining_set` (qty: 1 None)
- `heating_element_set_basic` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `level_sensor_basic` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `quench_rack_and_baskets` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: furnace_shell_insulated
    qty: 1
    unit: None
  - item_id: refractory_lining_set
    qty: 1
    unit: None
  - item_id: heating_element_set_basic
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: level_sensor_basic
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: quench_rack_and_baskets
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 2 produces: `motor_coil_wound` (2.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- `furnace_shell_insulated` (qty: 1 None)
- `refractory_lining_set` (qty: 1 None)
- `heating_element_set_basic` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `level_sensor_basic` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `quench_rack_and_baskets` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: furnace_shell_insulated
    qty: 1
    unit: None
  - item_id: refractory_lining_set
    qty: 1
    unit: None
  - item_id: heating_element_set_basic
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: level_sensor_basic
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: quench_rack_and_baskets
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 2 produces: `motor_coil_wound` (2.0 kg)
- Step 3 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_heat_treatment_furnace_v0_target_v0.yaml`
- **BOM available:** Yes (10 components)
- **Similar recipes:** 3 found
