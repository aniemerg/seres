# Fix Intelligence: recipe_spindle_drive_motor_small_v0

## Files

- **Recipe:** `kb/recipes/recipe_spindle_drive_motor_small_v0.yaml`
- **Target item:** `spindle_drive_motor_small`
  - File: `kb/items/spindle_drive_motor_small.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `coil_winding_basic_v0`
  - File: `kb/processes/coil_winding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: coil_winding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `motor_coil_wound` (2.0 kg)

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

#### Option B: Use previous step outputs

- Step 0 produces: `motor_coil_wound` (2.0 kg)
- Step 1 produces: `cast_metal_parts` (0.95 kg)

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

#### Option B: Use previous step outputs

- Step 0 produces: `motor_coil_wound` (2.0 kg)
- Step 1 produces: `cast_metal_parts` (0.95 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 4
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_spindle_drive_motor_small_v0.yaml`
- **BOM available:** No
