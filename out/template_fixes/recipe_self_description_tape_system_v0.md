# Fix Intelligence: recipe_self_description_tape_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_self_description_tape_system_v0.yaml`
- **Target item:** `self_description_tape_system_v0`
  - File: `kb/items/self_description_tape_system_v0.yaml`
- **BOM:** `kb/boms/bom_self_description_tape_system_v0.yaml` ✓
  - Components: 8
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 8 components:

- `magnetic_tape_reel` (qty: 10.0 each)
- `tape_drive_mechanism` (qty: 2.0 each)
- `magnetic_read_write_head` (qty: 4.0 each)
- `stepper_motor_v0` (qty: 4.0 each)
- `steel_frame_welded` (qty: 30.0 kg)
- `electronic_control_circuit_v0` (qty: 5.0 kg)
- `bearing_ball_steel` (qty: 20.0 each)
- `wire_copper_insulated` (qty: 2.0 kg)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: magnetic_tape_reel
    qty: 10.0
    unit: each
  - item_id: tape_drive_mechanism
    qty: 2.0
    unit: each
  - item_id: magnetic_read_write_head
    qty: 4.0
    unit: each
  - item_id: stepper_motor_v0
    qty: 4.0
    unit: each
  - item_id: steel_frame_welded
    qty: 30.0
    unit: kg
  - item_id: electronic_control_circuit_v0
    qty: 5.0
    unit: kg
  - item_id: bearing_ball_steel
    qty: 20.0
    unit: each
  - item_id: wire_copper_insulated
    qty: 2.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `magnetic_tape_reel` (qty: 10.0 each)
- `tape_drive_mechanism` (qty: 2.0 each)
- `magnetic_read_write_head` (qty: 4.0 each)
- `stepper_motor_v0` (qty: 4.0 each)
- `steel_frame_welded` (qty: 30.0 kg)
- `electronic_control_circuit_v0` (qty: 5.0 kg)
- `bearing_ball_steel` (qty: 20.0 each)
- `wire_copper_insulated` (qty: 2.0 kg)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: magnetic_tape_reel
    qty: 10.0
    unit: each
  - item_id: tape_drive_mechanism
    qty: 2.0
    unit: each
  - item_id: magnetic_read_write_head
    qty: 4.0
    unit: each
  - item_id: stepper_motor_v0
    qty: 4.0
    unit: each
  - item_id: steel_frame_welded
    qty: 30.0
    unit: kg
  - item_id: electronic_control_circuit_v0
    qty: 5.0
    unit: kg
  - item_id: bearing_ball_steel
    qty: 20.0
    unit: each
  - item_id: wire_copper_insulated
    qty: 2.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- `magnetic_tape_reel` (qty: 10.0 each)
- `tape_drive_mechanism` (qty: 2.0 each)
- `magnetic_read_write_head` (qty: 4.0 each)
- `stepper_motor_v0` (qty: 4.0 each)
- `steel_frame_welded` (qty: 30.0 kg)
- `electronic_control_circuit_v0` (qty: 5.0 kg)
- `bearing_ball_steel` (qty: 20.0 each)
- `wire_copper_insulated` (qty: 2.0 kg)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: magnetic_tape_reel
    qty: 10.0
    unit: each
  - item_id: tape_drive_mechanism
    qty: 2.0
    unit: each
  - item_id: magnetic_read_write_head
    qty: 4.0
    unit: each
  - item_id: stepper_motor_v0
    qty: 4.0
    unit: each
  - item_id: steel_frame_welded
    qty: 30.0
    unit: kg
  - item_id: electronic_control_circuit_v0
    qty: 5.0
    unit: kg
  - item_id: bearing_ball_steel
    qty: 20.0
    unit: each
  - item_id: wire_copper_insulated
    qty: 2.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `magnetic_tape_reel` (qty: 10.0 each)
- `tape_drive_mechanism` (qty: 2.0 each)
- `magnetic_read_write_head` (qty: 4.0 each)
- `stepper_motor_v0` (qty: 4.0 each)
- `steel_frame_welded` (qty: 30.0 kg)
- `electronic_control_circuit_v0` (qty: 5.0 kg)
- `bearing_ball_steel` (qty: 20.0 each)
- `wire_copper_insulated` (qty: 2.0 kg)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: magnetic_tape_reel
    qty: 10.0
    unit: each
  - item_id: tape_drive_mechanism
    qty: 2.0
    unit: each
  - item_id: magnetic_read_write_head
    qty: 4.0
    unit: each
  - item_id: stepper_motor_v0
    qty: 4.0
    unit: each
  - item_id: steel_frame_welded
    qty: 30.0
    unit: kg
  - item_id: electronic_control_circuit_v0
    qty: 5.0
    unit: kg
  - item_id: bearing_ball_steel
    qty: 20.0
    unit: each
  - item_id: wire_copper_insulated
    qty: 2.0
    unit: kg
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_self_description_tape_system_v0.yaml`
- **BOM available:** Yes (8 components)
