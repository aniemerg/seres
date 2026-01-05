# Fix Intelligence: recipe_plastic_extruder_v0

## Files

- **Recipe:** `kb/recipes/recipe_plastic_extruder_v0.yaml`
- **Target item:** `plastic_extruder_v0`
  - File: `kb/items/plastic_extruder_v0.yaml`
- **BOM:** `kb/boms/bom_plastic_extruder_v0.yaml` ✓
  - Components: 6
- **Steps:** 6 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_machine_plastic_extruder_v0` → plastic_extruder (5 steps)

## Errors (6 found)

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

BOM has 6 components:

- `extruder_head_basic` (qty: 1 None)
- `heating_plate_or_induction_heater` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `steel_frame_welded` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: heating_plate_or_induction_heater
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: steel_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `extruder_head_basic` (qty: 1 None)
- `heating_plate_or_induction_heater` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `steel_frame_welded` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: heating_plate_or_induction_heater
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: steel_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

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

- `extruder_head_basic` (qty: 1 None)
- `heating_plate_or_induction_heater` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `steel_frame_welded` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: heating_plate_or_induction_heater
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: steel_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

BOM has 6 components:

- `extruder_head_basic` (qty: 1 None)
- `heating_plate_or_induction_heater` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `steel_frame_welded` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: heating_plate_or_induction_heater
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: steel_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 4
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

BOM has 6 components:

- `extruder_head_basic` (qty: 1 None)
- `heating_plate_or_induction_heater` (qty: 1 None)
- `drive_motor_medium` (qty: 1 None)
- `gearbox_reducer_medium` (qty: 1 None)
- `steel_frame_welded` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: extruder_head_basic
    qty: 1
    unit: None
  - item_id: heating_plate_or_induction_heater
    qty: 1
    unit: None
  - item_id: drive_motor_medium
    qty: 1
    unit: None
  - item_id: gearbox_reducer_medium
    qty: 1
    unit: None
  - item_id: steel_frame_welded
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_plastic_extruder_v0.yaml`
- **BOM available:** Yes (6 components)
- **Similar recipes:** 1 found
