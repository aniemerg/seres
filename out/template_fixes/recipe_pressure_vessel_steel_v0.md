# Fix Intelligence: recipe_pressure_vessel_steel_v0

## Files

- **Recipe:** `kb/recipes/recipe_pressure_vessel_steel_v0.yaml`
- **Target item:** `pressure_vessel_steel`
  - File: `kb/items/pressure_vessel_steel.yaml`
- **BOM:** None
- **Steps:** 7 total

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'heat_treatment_stress_relief_v0') requires input 'welded_assemblies' which is not available

**Location:** Step 3
**Process:** `heat_treatment_stress_relief_v0`
  - File: `kb/processes/heat_treatment_stress_relief_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treatment_stress_relief_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)
- Step 3 produces: `finished_part` (5.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)
- Step 3 produces: `finished_part` (5.0 kg)
- Step 4 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_pressure_vessel_steel_v0.yaml`
- **BOM available:** No
