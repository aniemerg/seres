# Fix Intelligence: recipe_hauler_v0

## Files

- **Recipe:** `kb/recipes/recipe_hauler_v0.yaml`
- **Target item:** `hauler_v0`
  - File: `kb/items/hauler_v0.yaml`
- **BOM:** `kb/boms/bom_hauler_v0.yaml` ✓
  - Components: 10
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_hauler_v0_alias_v0` → hauler (7 steps)

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

BOM has 10 components:

- `machine_frame_medium` (qty: 1 None)
- `motor_electric_medium` (qty: 2 None)
- `drive_assembly` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `battery_pack_large` (qty: 1 None)
- `cargo_platform_assembly` (qty: 1 None)
- `wheel_set_industrial` (qty: 4 None)
- `hydraulic_cylinder_medium` (qty: 2 None)
- `sensor_suite_general` (qty: 1 None)
- `fastener_kit_large` (qty: 2 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_frame_medium
    qty: 1
    unit: None
  - item_id: motor_electric_medium
    qty: 2
    unit: None
  - item_id: drive_assembly
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: battery_pack_large
    qty: 1
    unit: None
  - item_id: cargo_platform_assembly
    qty: 1
    unit: None
  - item_id: wheel_set_industrial
    qty: 4
    unit: None
  - item_id: hydraulic_cylinder_medium
    qty: 2
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: fastener_kit_large
    qty: 2
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_hauler_v0.yaml`
- **BOM available:** Yes (10 components)
- **Similar recipes:** 1 found
