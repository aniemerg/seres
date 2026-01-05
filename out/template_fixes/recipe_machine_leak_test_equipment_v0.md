# Fix Intelligence: recipe_machine_leak_test_equipment_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_leak_test_equipment_v0.yaml`
- **Target item:** `leak_test_equipment`
  - File: `kb/items/leak_test_equipment.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (5 found)

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

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'plumbing_and_pneumatics_v0') requires input 'piping_components' which is not available

**Location:** Step 2
**Process:** `plumbing_and_pneumatics_v0`
  - File: `kb/processes/plumbing_and_pneumatics_v0.yaml`

**Current step:**
```yaml
- process_id: plumbing_and_pneumatics_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'calibration_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `calibration_basic_v0`
  - File: `kb/processes/calibration_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: calibration_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `plumbing_system_assembly` (1.0 unit)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `wired_electrical_system` (1.0 unit)
- Step 2 produces: `plumbing_system_assembly` (1.0 unit)
- Step 3 produces: `instrument_calibrated` (1.0 unit)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_machine_leak_test_equipment_v0.yaml`
- **BOM available:** No
