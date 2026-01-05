# Fix Intelligence: recipe_lattice_builder_gantry_robot_v0

## Files

- **Recipe:** `kb/recipes/recipe_lattice_builder_gantry_robot_v0.yaml`
- **Target item:** `lattice_builder_gantry_robot_v0`
  - File: `kb/items/lattice_builder_gantry_robot_v0.yaml`
- **BOM:** `kb/boms/bom_lattice_builder_gantry_robot_v0.yaml` ✓
  - Components: 5
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

BOM has 5 components:

- `gantry_axes_set` (qty: 1 None)
- `steel_frame_heavy` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `sensor_equipped_system` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: gantry_axes_set
    qty: 1
    unit: None
  - item_id: steel_frame_heavy
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: sensor_equipped_system
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_lattice_builder_gantry_robot_v0.yaml`
- **BOM available:** Yes (5 components)
