# Fix Intelligence: recipe_water_electrolyzer_v0

## Files

- **Recipe:** `kb/recipes/recipe_water_electrolyzer_v0.yaml`
- **Target item:** `water_electrolyzer_v0`
  - File: `kb/items/water_electrolyzer_v0.yaml`
- **BOM:** `kb/boms/bom_water_electrolyzer_v0.yaml` ✓
  - Components: 5
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

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `electrode_set_mre` (qty: 2 None)
- `separator_robust` (qty: 5 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: electrode_set_mre
    qty: 2
    unit: None
  - item_id: separator_robust
    qty: 5
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `electrode_set_mre` (qty: 2 None)
- `separator_robust` (qty: 5 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: electrode_set_mre
    qty: 2
    unit: None
  - item_id: separator_robust
    qty: 5
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `wiring_and_electronics_integration_v0`
  - File: `kb/processes/wiring_and_electronics_integration_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: wiring_and_electronics_integration_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `electrode_set_mre` (qty: 2 None)
- `separator_robust` (qty: 5 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: electrode_set_mre
    qty: 2
    unit: None
  - item_id: separator_robust
    qty: 5
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

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

#### Option A: Use BOM components

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `electrode_set_mre` (qty: 2 None)
- `separator_robust` (qty: 5 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: electrode_set_mre
    qty: 2
    unit: None
  - item_id: separator_robust
    qty: 5
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `wired_electrical_system` (1.0 unit)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

BOM has 5 components:

- `electrolyzer_cell_stack` (qty: 1 None)
- `electrode_set_mre` (qty: 2 None)
- `separator_robust` (qty: 5 None)
- `power_supply_dc_high_current` (qty: 1 None)
- `gas_collection_system` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: electrolyzer_cell_stack
    qty: 1
    unit: None
  - item_id: electrode_set_mre
    qty: 2
    unit: None
  - item_id: separator_robust
    qty: 5
    unit: None
  - item_id: power_supply_dc_high_current
    qty: 1
    unit: None
  - item_id: gas_collection_system
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `wired_electrical_system` (1.0 unit)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_water_electrolyzer_v0.yaml`
- **BOM available:** Yes (5 components)
