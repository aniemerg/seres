# Fix Intelligence: recipe_acid_reactor_v0

## Files

- **Recipe:** `kb/recipes/recipe_acid_reactor_v0.yaml`
- **Target item:** `acid_reactor_v0`
  - File: `kb/items/acid_reactor_v0.yaml`
- **BOM:** `kb/boms/bom_acid_reactor_v0.yaml` ✓
  - Components: 7
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `chemical_reactor_vessel_v0` (qty: 1 None)
- `acid_resistant_lining` (qty: 1 None)
- `jacket_with_fittings` (qty: 1 None)
- `reactor_agitator_mixer_v0` (qty: 1 None)
- `gas_outlet_manifold` (qty: 2 None)
- `valve_set_gas_handling` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: welding_and_fabrication_v0
  inputs:
  - item_id: chemical_reactor_vessel_v0
    qty: 1
    unit: None
  - item_id: acid_resistant_lining
    qty: 1
    unit: None
  - item_id: jacket_with_fittings
    qty: 1
    unit: None
  - item_id: reactor_agitator_mixer_v0
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
```

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ceramic_coating_v0') requires input 'finished_part' which is not available

**Location:** Step 1
**Process:** `ceramic_coating_v0`
  - File: `kb/processes/ceramic_coating_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_coating_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `assembly_basic_v0`
  - File: `kb/processes/assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `chemical_reactor_vessel_v0` (qty: 1 None)
- `acid_resistant_lining` (qty: 1 None)
- `jacket_with_fittings` (qty: 1 None)
- `reactor_agitator_mixer_v0` (qty: 1 None)
- `gas_outlet_manifold` (qty: 2 None)
- `valve_set_gas_handling` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: chemical_reactor_vessel_v0
    qty: 1
    unit: None
  - item_id: acid_resistant_lining
    qty: 1
    unit: None
  - item_id: jacket_with_fittings
    qty: 1
    unit: None
  - item_id: reactor_agitator_mixer_v0
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `finished_part` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

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

#### Option A: Use BOM components

BOM has 7 components:

- `chemical_reactor_vessel_v0` (qty: 1 None)
- `acid_resistant_lining` (qty: 1 None)
- `jacket_with_fittings` (qty: 1 None)
- `reactor_agitator_mixer_v0` (qty: 1 None)
- `gas_outlet_manifold` (qty: 2 None)
- `valve_set_gas_handling` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: chemical_reactor_vessel_v0
    qty: 1
    unit: None
  - item_id: acid_resistant_lining
    qty: 1
    unit: None
  - item_id: jacket_with_fittings
    qty: 1
    unit: None
  - item_id: reactor_agitator_mixer_v0
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (9.5 kg)
- Step 1 produces: `finished_part` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_acid_reactor_v0.yaml`
- **BOM available:** Yes (7 components)
