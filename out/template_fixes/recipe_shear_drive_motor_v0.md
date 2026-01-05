# Fix Intelligence: recipe_shear_drive_motor_v0

## Files

- **Recipe:** `kb/recipes/recipe_shear_drive_motor_v0.yaml`
- **Target item:** `shear_drive_motor`
  - File: `kb/items/shear_drive_motor.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'assembly_basic_v0') requires input 'drive_motor_medium' which is not available

**Location:** Step 0
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: drive_motor_medium
    qty: 1.0
    unit: unit
  - item_id: belt_and_pulley_set
    qty: 1.0
    unit: unit
  - item_id: control_circuit_motor_drive
    qty: 1.0
    unit: unit
  - item_id: wire_copper_insulated
    qty: 0.2
    unit: kg
  - item_id: fastener_kit_small
    qty: 0.5
    unit: kg
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

#### Problem: Item `drive_motor_medium` not found

This item doesn't exist in the KB.

#### Problem: Item `belt_and_pulley_set` not found

This item doesn't exist in the KB.

#### Problem: Item `control_circuit_motor_drive` not found

This item doesn't exist in the KB.

#### Problem: Item `wire_copper_insulated` not found

This item doesn't exist in the KB.

#### Problem: Item `fastener_kit_small` not found

This item doesn't exist in the KB.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `shear_drive_motor` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `shear_drive_motor` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `shear_drive_motor` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)

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

#### Option B: Use previous step outputs

- Step 0 produces: `shear_drive_motor` (1.0 unit)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_shear_drive_motor_v0.yaml`
- **BOM available:** No
