# Fix Intelligence: recipe_thermionic_converter_v0

## Files

- **Recipe:** `kb/recipes/recipe_thermionic_converter_v0.yaml`
- **Target item:** `thermionic_converter`
  - File: `kb/items/thermionic_converter.yaml`
- **BOM:** None
- **Steps:** 5 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_thermionic_converter_v0_v0` → thermionic_converter_v0 (8 steps)
- `recipe_machine_thermionic_converter_v0` → thermionic_converter (3 steps)

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'ceramic_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `ceramic_forming_basic_v0`
  - File: `kb/processes/ceramic_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: ceramic_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'sintering_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `sintering_basic_v0`
  - File: `kb/processes/sintering_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sintering_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `green_ceramic_parts` (5.0 kg)

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

- Step 0 produces: `green_ceramic_parts` (5.0 kg)
- Step 1 produces: `sintered_parts` (0.95 kg)

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

- Step 0 produces: `green_ceramic_parts` (5.0 kg)
- Step 1 produces: `sintered_parts` (0.95 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

#### Option C: Pattern from `recipe_machine_thermionic_converter_v0`

Similar recipe uses this process (step 0) with:

```yaml
  inputs:
  - item_id: thermionic_vacuum_tube
    qty: 1.0
    unit: unit
  - item_id: converter_housing_assembly
    qty: 1.0
    unit: unit
  - item_id: vacuum_seal_assembly
    qty: 1.0
    unit: unit
```

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `green_ceramic_parts` (5.0 kg)
- Step 1 produces: `sintered_parts` (0.95 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_thermionic_converter_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
