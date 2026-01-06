# Fix Intelligence: recipe_shaft_and_bearing_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_shaft_and_bearing_set_v0.yaml`
- **Target item:** `shaft_and_bearing_set`
  - File: `kb/items/shaft_and_bearing_set.yaml`
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

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'steel_shaft_machining_v0') requires input 'steel_bar_raw' which is not available

**Location:** Step 1
**Process:** `steel_shaft_machining_v0`
  - File: `kb/processes/steel_shaft_machining_v0.yaml`

**Current step:**
```yaml
- process_id: steel_shaft_machining_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `steel_shaft_machined_v0` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'heat_treatment_hardening_v0') requires input 'bearing_rings_machined' which is not available

**Location:** Step 4
**Process:** `heat_treatment_hardening_v0`
  - File: `kb/processes/heat_treatment_hardening_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_hardening_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'bearing_set_fabrication_v0') requires input 'steel_stock' which is not available

**Location:** Step 5
**Process:** `bearing_set_fabrication_v0`
  - File: `kb/processes/bearing_set_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: bearing_set_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'bearing_installation_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
**Process:** `bearing_installation_basic_v0`
  - File: `kb/processes/bearing_installation_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: bearing_installation_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_rings_hardened` (1.05 kg)
- Step 5 produces: `bearing_set` (1.0 kg)

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
- Step 1 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_rings_hardened` (1.05 kg)
- Step 5 produces: `bearing_set` (1.0 kg)
- Step 6 produces: `finished_part` (2.0 kg)

---

### Error 9: recipe_template_missing_step_inputs

**Message:** Step 8 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 8
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_rings_hardened` (1.05 kg)
- Step 5 produces: `bearing_set` (1.0 kg)
- Step 6 produces: `finished_part` (2.0 kg)
- Step 7 produces: `assembled_equipment` (1.0 kg)

---

### Error 10: recipe_template_missing_step_inputs

**Message:** Step 9 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 9
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

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)
- Step 4 produces: `bearing_rings_hardened` (1.05 kg)
- Step 5 produces: `bearing_set` (1.0 kg)
- Step 6 produces: `finished_part` (2.0 kg)
- Step 7 produces: `assembled_equipment` (1.0 kg)
- Step 8 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 10
- **Recipe file:** `kb/recipes/recipe_shaft_and_bearing_set_v0.yaml`
- **BOM available:** No
