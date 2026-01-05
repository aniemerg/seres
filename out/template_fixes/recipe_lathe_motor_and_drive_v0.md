# Fix Intelligence: recipe_lathe_motor_and_drive_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_motor_and_drive_v0.yaml`
- **Target item:** `lathe_motor_and_drive`
  - File: `kb/items/lathe_motor_and_drive.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'motor_final_assembly_v0') requires input 'stator_rotor_lamination_set' which is not available

**Location:** Step 0
**Process:** `motor_final_assembly_v0`
  - File: `kb/processes/motor_final_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: motor_final_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'coil_winding_motor_v0') requires input 'aluminum_wire' which is not available

**Location:** Step 1
**Process:** `coil_winding_motor_v0`
  - File: `kb/processes/coil_winding_motor_v0.yaml`

**Current step:**
```yaml
- process_id: coil_winding_motor_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'belt_installation_and_tensioning_v0') requires input 'belt_and_pulley_set' which is not available

**Location:** Step 2
**Process:** `belt_installation_and_tensioning_v0`
  - File: `kb/processes/belt_installation_and_tensioning_v0.yaml`

**Current step:**
```yaml
- process_id: belt_installation_and_tensioning_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `electrical_testing_basic_v0`
  - File: `kb/processes/electrical_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `motor_electric_small` (1.0 unit)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `installed_belt_drive` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_lathe_motor_and_drive_v0.yaml`
- **BOM available:** No
