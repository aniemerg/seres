# Fix Intelligence: recipe_electrolyzer_pem_v0

## Files

- **Recipe:** `kb/recipes/recipe_electrolyzer_pem_v0.yaml`
- **Target item:** `electrolyzer_pem_v0`
  - File: `kb/items/electrolyzer_pem_v0.yaml`
- **BOM:** `kb/boms/bom_electrolyzer_pem_v0.yaml` ✓
  - Components: 5
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machine_assembly_basic_v0`
  - File: `kb/processes/machine_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machine_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `separator_membrane_porous` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: separator_membrane_porous
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `separator_membrane_porous` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: separator_membrane_porous
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `separator_membrane_porous` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: separator_membrane_porous
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `separator_membrane_porous` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: separator_membrane_porous
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_electrolyzer_pem_v0.yaml`
- **BOM available:** Yes (5 components)
