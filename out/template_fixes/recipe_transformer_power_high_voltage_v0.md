# Fix Intelligence: recipe_transformer_power_high_voltage_v0

## Files

- **Recipe:** `kb/recipes/recipe_transformer_power_high_voltage_v0.yaml`
- **Target item:** `transformer_power_high_voltage`
  - File: `kb/items/transformer_power_high_voltage.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

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

#### Option B: Use previous step outputs

- Step 0 produces: `motor_coil_wound` (2.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'potting_and_sealing_v0') requires input 'potting_compound' which is not available

**Location:** Step 2
**Process:** `potting_and_sealing_v0`
  - File: `kb/processes/potting_and_sealing_v0.yaml`

**Current step:**
```yaml
- process_id: potting_and_sealing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'electrical_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `motor_coil_wound` (2.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

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

- Step 0 produces: `motor_coil_wound` (2.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `tested_electrical_equipment` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_transformer_power_high_voltage_v0.yaml`
- **BOM available:** No
