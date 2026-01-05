# Fix Intelligence: recipe_electric_motor_3_phase_5kw_v0

## Files

- **Recipe:** `kb/recipes/recipe_electric_motor_3_phase_5kw_v0.yaml`
- **Target item:** `electric_motor_3_phase_5kw`
  - File: `kb/items/electric_motor_3_phase_5kw.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'lamination_stamping_v0') requires input 'electrical_steel_sheet' which is not available

**Location:** Step 0
**Process:** `lamination_stamping_v0`
  - File: `kb/processes/lamination_stamping_v0.yaml`

**Current step:**
```yaml
- process_id: lamination_stamping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'coil_winding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `stator_rotor_lamination_set` (0.95 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'motor_final_assembly_v0') requires input 'motor_coil_wound' which is not available

**Location:** Step 2
**Process:** `motor_final_assembly_v0`
  - File: `kb/processes/motor_final_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: motor_final_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `motor_electric_small` (1.0 unit)

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

- Step 0 produces: `stator_rotor_lamination_set` (0.95 kg)
- Step 1 produces: `motor_coil_wound` (2.0 kg)
- Step 2 produces: `motor_electric_small` (1.0 unit)
- Step 3 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_electric_motor_3_phase_5kw_v0.yaml`
- **BOM available:** No
