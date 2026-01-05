# Fix Intelligence: recipe_mounting_bracket_azimuth_elevation_v0

## Files

- **Recipe:** `kb/recipes/recipe_mounting_bracket_azimuth_elevation_v0.yaml`
- **Target item:** `mounting_bracket_azimuth_elevation`
  - File: `kb/items/mounting_bracket_azimuth_elevation.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_cutting_process_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 0
**Process:** `metal_cutting_process_v0`
  - File: `kb/processes/metal_cutting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_cutting_process_v0
  inputs:
  - item_id: metal_tubing_stock
    qty: 8.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_tubing_stock` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_process_general_v0') requires input 'metal_tubing_stock' which is not available

**Location:** Step 1
**Process:** `welding_process_general_v0`
  - File: `kb/processes/welding_process_general_v0.yaml`

**Current step:**
```yaml
- process_id: welding_process_general_v0
  inputs:
  - item_id: metal_tubing_stock
    qty: 7.5
    unit: kg
  - item_id: steel_plate_or_sheet
    qty: 2.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `metal_tubing_stock` not found

This item doesn't exist in the KB.

#### Problem: Generic placeholder `steel_plate_or_sheet`

This is not a real item. Need to replace with specific item.

**Specific items matching pattern:**

- `gasket_sheet_material_v0`
- `gasket_sheet`
- `steel_plate_raw`
- `steel_plate_or_sheet`
- `iron_powder_or_sheet`
- `sheet_metal_or_structural_steel`
- `brass_sheet`
- `nickel_sheet_rolling_forming_v0`
- `steel_sheet_1mm`
- `steel_sheet_3mm`

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'machining_process_boring_v0') requires input 'mount_frame_welded' which is not available

**Location:** Step 2
**Process:** `machining_process_boring_v0`
  - File: `kb/processes/machining_process_boring_v0.yaml`

**Current step:**
```yaml
- process_id: machining_process_boring_v0
  inputs:
  - item_id: mount_frame_welded
    qty: 9.0
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `mount_frame_welded` not found

This item doesn't exist in the KB.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'assembly_process_general_v0') requires input 'bearing_ball_steel' which is not available

**Location:** Step 3
**Process:** `assembly_process_general_v0`
  - File: `kb/processes/assembly_process_general_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_process_general_v0
  inputs:
  - item_id: mount_frame_bearing_bores
    qty: 8.8
    unit: kg
  - item_id: bearing_ball_steel
    qty: 4.0
    unit: each
  - item_id: stepper_motor_v0
    qty: 2.0
    unit: each
  - item_id: harmonic_drive_reducer_medium
    qty: 2.0
    unit: each
  - item_id: encoder_rotary_absolute
    qty: 2.0
    unit: each
  - item_id: proximity_sensor_inductive
    qty: 4.0
    unit: each
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `mount_frame_bearing_bores` not found

This item doesn't exist in the KB.

#### Problem: Item `bearing_ball_steel` not found

This item doesn't exist in the KB.

#### Problem: Item `stepper_motor_v0` not found

This item doesn't exist in the KB.

#### Problem: Item `harmonic_drive_reducer_medium` not found

This item doesn't exist in the KB.

#### Problem: Item `encoder_rotary_absolute` not found

This item doesn't exist in the KB.

#### Problem: Item `proximity_sensor_inductive` not found

This item doesn't exist in the KB.

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_mounting_bracket_azimuth_elevation_v0.yaml`
- **BOM available:** No
