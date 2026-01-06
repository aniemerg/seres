# Fix Intelligence: recipe_motor_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_motor_assembly_v0.yaml`
- **Target item:** `motor_assembly`
  - File: `kb/items/motor_assembly.yaml`
- **BOM:** None
- **Steps:** 10 total

## Errors (10 found)

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

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'lamination_stamping_v0') requires input 'electrical_steel_sheet' which is not available

**Location:** Step 2
**Process:** `lamination_stamping_v0`
  - File: `kb/processes/lamination_stamping_v0.yaml`

**Current step:**
```yaml
- process_id: lamination_stamping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `stator_rotor_lamination_set` (0.95 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 3 produces: `cast_metal_parts` (0.95 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `coil_winding_basic_v0`
  - File: `kb/processes/coil_winding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: coil_winding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 3 produces: `cast_metal_parts` (0.95 kg)
- Step 4 produces: `machined_part_raw` (1.0 kg)

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 3 produces: `cast_metal_parts` (0.95 kg)
- Step 4 produces: `machined_part_raw` (1.0 kg)
- Step 5 produces: `motor_coil_wound` (2.0 kg)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 3 produces: `cast_metal_parts` (0.95 kg)
- Step 4 produces: `machined_part_raw` (1.0 kg)
- Step 5 produces: `motor_coil_wound` (2.0 kg)
- Step 6 produces: `assembled_equipment` (1.0 kg)

---

### Error 9: recipe_template_missing_step_inputs

**Message:** Step 8 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 8
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 3 produces: `cast_metal_parts` (0.95 kg)
- Step 4 produces: `machined_part_raw` (1.0 kg)
- Step 5 produces: `motor_coil_wound` (2.0 kg)
- Step 6 produces: `assembled_equipment` (1.0 kg)
- Step 7 produces: `assembled_equipment` (1.0 kg)

---

### Error 10: recipe_step_input_not_satisfied

**Message:** Step 9 (process 'motor_final_assembly_v0') requires input 'motor_coil_wound' which is not available

**Location:** Step 9
**Process:** `motor_final_assembly_v0`
  - File: `kb/processes/motor_final_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: motor_final_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 10
- **Recipe file:** `kb/recipes/recipe_motor_assembly_v0.yaml`
- **BOM available:** No
