# Fix Intelligence: recipe_hydrogen_oxygen_torch_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydrogen_oxygen_torch_v0.yaml`
- **Target item:** `hydrogen_oxygen_torch_v0`
  - File: `kb/items/hydrogen_oxygen_torch_v0.yaml`
- **BOM:** `kb/boms/bom_hydrogen_oxygen_torch_v0.yaml` ✓
  - Components: 7
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_basic_v0`
  - File: `kb/processes/machining_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `torch_or_burner_oxy_fuel` (qty: 1 None)
- `gas_mixing_chamber_steel` (qty: 1 None)
- `valve_solenoid` (qty: 2 None)
- `valve_set_gas_handling` (qty: 2 None)
- `pressure_gauge` (qty: 2 None)
- `mounting_bracket_steel` (qty: 1 None)
- `hose_end_fittings_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: machining_basic_v0
  inputs:
  - item_id: torch_or_burner_oxy_fuel
    qty: 1
    unit: None
  - item_id: gas_mixing_chamber_steel
    qty: 1
    unit: None
  - item_id: valve_solenoid
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 2
    unit: None
  - item_id: pressure_gauge
    qty: 2
    unit: None
  - item_id: mounting_bracket_steel
    qty: 1
    unit: None
  - item_id: hose_end_fittings_v0
    qty: 2
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_basic_v0`
  - File: `kb/processes/welding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `torch_or_burner_oxy_fuel` (qty: 1 None)
- `gas_mixing_chamber_steel` (qty: 1 None)
- `valve_solenoid` (qty: 2 None)
- `valve_set_gas_handling` (qty: 2 None)
- `pressure_gauge` (qty: 2 None)
- `mounting_bracket_steel` (qty: 1 None)
- `hose_end_fittings_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: welding_basic_v0
  inputs:
  - item_id: torch_or_burner_oxy_fuel
    qty: 1
    unit: None
  - item_id: gas_mixing_chamber_steel
    qty: 1
    unit: None
  - item_id: valve_solenoid
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 2
    unit: None
  - item_id: pressure_gauge
    qty: 2
    unit: None
  - item_id: mounting_bracket_steel
    qty: 1
    unit: None
  - item_id: hose_end_fittings_v0
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `machined_metal_block_v0` (1.8 kg)

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

- `torch_or_burner_oxy_fuel` (qty: 1 None)
- `gas_mixing_chamber_steel` (qty: 1 None)
- `valve_solenoid` (qty: 2 None)
- `valve_set_gas_handling` (qty: 2 None)
- `pressure_gauge` (qty: 2 None)
- `mounting_bracket_steel` (qty: 1 None)
- `hose_end_fittings_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: torch_or_burner_oxy_fuel
    qty: 1
    unit: None
  - item_id: gas_mixing_chamber_steel
    qty: 1
    unit: None
  - item_id: valve_solenoid
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 2
    unit: None
  - item_id: pressure_gauge
    qty: 2
    unit: None
  - item_id: mounting_bracket_steel
    qty: 1
    unit: None
  - item_id: hose_end_fittings_v0
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `machined_metal_block_v0` (1.8 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

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

- `torch_or_burner_oxy_fuel` (qty: 1 None)
- `gas_mixing_chamber_steel` (qty: 1 None)
- `valve_solenoid` (qty: 2 None)
- `valve_set_gas_handling` (qty: 2 None)
- `pressure_gauge` (qty: 2 None)
- `mounting_bracket_steel` (qty: 1 None)
- `hose_end_fittings_v0` (qty: 2 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: torch_or_burner_oxy_fuel
    qty: 1
    unit: None
  - item_id: gas_mixing_chamber_steel
    qty: 1
    unit: None
  - item_id: valve_solenoid
    qty: 2
    unit: None
  - item_id: valve_set_gas_handling
    qty: 2
    unit: None
  - item_id: pressure_gauge
    qty: 2
    unit: None
  - item_id: mounting_bracket_steel
    qty: 1
    unit: None
  - item_id: hose_end_fittings_v0
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `machined_metal_block_v0` (1.8 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_hydrogen_oxygen_torch_v0.yaml`
- **BOM available:** Yes (7 components)
