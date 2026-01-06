# Fix Intelligence: recipe_compressor_reciprocating_v0

## Files

- **Recipe:** `kb/recipes/recipe_compressor_reciprocating_v0.yaml`
- **Target item:** `compressor_reciprocating`
  - File: `kb/items/compressor_reciprocating.yaml`
- **BOM:** None
- **Steps:** 8 total

## Errors (8 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sand_casting_large_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 0
**Process:** `sand_casting_large_v0`
  - File: `kb/processes/sand_casting_large_v0.yaml`

**Current step:**
```yaml
- process_id: sand_casting_large_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

#### Option B: Use previous step outputs

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'steel_shaft_machining_v0') requires input 'steel_bar_raw' which is not available

**Location:** Step 2
**Process:** `steel_shaft_machining_v0`
  - File: `kb/processes/steel_shaft_machining_v0.yaml`

**Current step:**
```yaml
- process_id: steel_shaft_machining_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `steel_shaft_machined_v0` (1.0 kg)

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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 3 produces: `machined_steel_part_precision` (7.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 3 produces: `machined_steel_part_precision` (7.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 3 produces: `machined_steel_part_precision` (7.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)
- Step 5 produces: `assembled_equipment` (1.0 kg)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `steel_shaft_machined_v0` (1.0 kg)
- Step 3 produces: `machined_steel_part_precision` (7.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)
- Step 5 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 8
- **Recipe file:** `kb/recipes/recipe_compressor_reciprocating_v0.yaml`
- **BOM available:** No
