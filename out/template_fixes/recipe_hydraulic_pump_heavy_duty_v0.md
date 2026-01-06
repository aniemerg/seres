# Fix Intelligence: recipe_hydraulic_pump_heavy_duty_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_pump_heavy_duty_v0.yaml`
- **Target item:** `hydraulic_pump_heavy_duty`
  - File: `kb/items/hydraulic_pump_heavy_duty.yaml`
- **BOM:** None
- **Steps:** 7 total

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'heat_treatment_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `heat_treatment_basic_v0`
  - File: `kb/processes/heat_treatment_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: heat_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `machined_steel_part_precision` (7.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `machined_steel_part_precision` (7.0 kg)
- Step 3 produces: `finished_part` (10.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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

- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `machined_steel_part_precision` (7.0 kg)
- Step 3 produces: `finished_part` (10.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_hydraulic_pump_heavy_duty_v0.yaml`
- **BOM available:** No
