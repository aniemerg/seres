# Fix Intelligence: recipe_machine_high_temp_furnace_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_high_temp_furnace_v0.yaml`
- **Target item:** `high_temp_furnace_v0`
  - File: `kb/items/high_temp_furnace_v0.yaml`
- **BOM:** `kb/boms/bom_high_temp_furnace_v0.yaml` ✓
  - Components: 11
- **Steps:** 1 total

## Errors (1 found)

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

BOM has 11 components:

- `furnace_shell_refractory` (qty: 1 None)
- `heating_element_set_high_temp` (qty: 1 None)
- `insulation_pack_high_temp` (qty: 1 None)
- `gas_handling_system` (qty: 1 None)
- `offgas_manifold` (qty: 1 None)
- `cooling_loop_basic` (qty: 1 None)
- `power_bus_high_current` (qty: 1 None)
- `temperature_sensing` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: furnace_shell_refractory
    qty: 1
    unit: None
  - item_id: heating_element_set_high_temp
    qty: 1
    unit: None
  - item_id: insulation_pack_high_temp
    qty: 1
    unit: None
  - item_id: gas_handling_system
    qty: 1
    unit: None
  - item_id: offgas_manifold
    qty: 1
    unit: None
  - item_id: cooling_loop_basic
    qty: 1
    unit: None
  - item_id: power_bus_high_current
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
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_machine_high_temp_furnace_v0.yaml`
- **BOM available:** Yes (11 components)
