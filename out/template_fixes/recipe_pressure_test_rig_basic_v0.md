# Fix Intelligence: recipe_pressure_test_rig_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_pressure_test_rig_basic_v0.yaml`
- **Target item:** `pressure_test_rig_basic_v0`
  - File: `kb/items/pressure_test_rig_basic_v0.yaml`
- **BOM:** `kb/boms/bom_pressure_test_rig_basic_v0.yaml` ✓
  - Components: 11
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_pressure_test_rig_basic_alias_v0` → pressure_test_rig_basic (2 steps)

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

- `hydraulic_pump_high_pressure` (qty: 1.0 each)
- `pressure_vessel_steel` (qty: 1.0 each)
- `press_platen_steel` (qty: 1.0 each)
- `brick_mold_steel_set` (qty: 1.0 each)
- `hydraulic_hoses_and_fittings` (qty: 1.0 each)
- `pressure_gauge_set` (qty: 1.0 each)
- `control_panel_basic` (qty: 1.0 each)
- `electric_motor_3_phase_5kw` (qty: 1.0 each)
- `steel_frame_heavy_duty` (qty: 1.0 each)
- `hydraulic_cylinder_large` (qty: 1.0 each)
- `pressure_control_valve_set` (qty: 1.0 each)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: hydraulic_pump_high_pressure
    qty: 1.0
    unit: each
  - item_id: pressure_vessel_steel
    qty: 1.0
    unit: each
  - item_id: press_platen_steel
    qty: 1.0
    unit: each
  - item_id: brick_mold_steel_set
    qty: 1.0
    unit: each
  - item_id: hydraulic_hoses_and_fittings
    qty: 1.0
    unit: each
  - item_id: pressure_gauge_set
    qty: 1.0
    unit: each
  - item_id: control_panel_basic
    qty: 1.0
    unit: each
  - item_id: electric_motor_3_phase_5kw
    qty: 1.0
    unit: each
  - item_id: steel_frame_heavy_duty
    qty: 1.0
    unit: each
  - item_id: hydraulic_cylinder_large
    qty: 1.0
    unit: each
  - item_id: pressure_control_valve_set
    qty: 1.0
    unit: each
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pressure_test_rig_basic_v0.yaml`
- **BOM available:** Yes (11 components)
- **Similar recipes:** 1 found
