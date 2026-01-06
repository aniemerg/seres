# Fix Intelligence: recipe_steel_forming_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_forming_press_v0.yaml`
- **Target item:** `steel_forming_press`
  - File: `kb/items/steel_forming_press.yaml`
- **BOM:** `kb/boms/bom_steel_forming_press.yaml` ✓
  - Components: 8
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `press_frame_medium` (qty: 1 unit)
- `hydraulic_cylinder_press` (qty: 1 unit)
- `hydraulic_system_medium` (qty: 1 unit)
- `press_platen_set_medium` (qty: 1 unit)
- `power_conditioning_module` (qty: 1 unit)
- `control_compute_module_imported` (qty: 1 unit)
- `sensor_suite_general` (qty: 1 unit)
- `fastener_kit_medium` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: press_frame_medium
    qty: 1
    unit: unit
  - item_id: hydraulic_cylinder_press
    qty: 1
    unit: unit
  - item_id: hydraulic_system_medium
    qty: 1
    unit: unit
  - item_id: press_platen_set_medium
    qty: 1
    unit: unit
  - item_id: power_conditioning_module
    qty: 1
    unit: unit
  - item_id: control_compute_module_imported
    qty: 1
    unit: unit
  - item_id: sensor_suite_general
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1
    unit: unit
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_steel_forming_press_v0.yaml`
- **BOM available:** Yes (8 components)
