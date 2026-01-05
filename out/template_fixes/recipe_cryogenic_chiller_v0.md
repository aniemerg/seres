# Fix Intelligence: recipe_cryogenic_chiller_v0

## Files

- **Recipe:** `kb/recipes/recipe_cryogenic_chiller_v0.yaml`
- **Target item:** `cryogenic_chiller_v0`
  - File: `kb/items/cryogenic_chiller_v0.yaml`
- **BOM:** `kb/boms/bom_cryogenic_chiller_v0.yaml` ✓
  - Components: 11
- **Steps:** 7 total

## Errors (7 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'machining_rough_v0') requires input 'cut_parts' which is not available

**Location:** Step 0
**Process:** `machining_rough_v0`
  - File: `kb/processes/machining_rough_v0.yaml`

**Current step:**
```yaml
- process_id: machining_rough_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_structural_v0') requires input 'cut_parts' which is not available

**Location:** Step 1
**Process:** `welding_structural_v0`
  - File: `kb/processes/welding_structural_v0.yaml`

**Current step:**
```yaml
- process_id: welding_structural_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'brazing_process_v0') requires input 'base_metal_parts' which is not available

**Location:** Step 2
**Process:** `brazing_process_v0`
  - File: `kb/processes/brazing_process_v0.yaml`

**Current step:**
```yaml
- process_id: brazing_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

BOM has 11 components:

- `compressor_reciprocating` (qty: 1 None)
- `heat_exchanger_tube_shell` (qty: 2 None)
- `expansion_valve_cryogenic` (qty: 1 None)
- `cryogenic_fluid_reservoir` (qty: 1 None)
- `heat_pipes_or_loop` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 3 None)
- `pressure_gauge` (qty: 2 None)
- `structural_frame_large` (qty: 1 None)
- `power_cable_assembly` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: compressor_reciprocating
    qty: 1
    unit: None
  - item_id: heat_exchanger_tube_shell
    qty: 2
    unit: None
  - item_id: expansion_valve_cryogenic
    qty: 1
    unit: None
  - item_id: cryogenic_fluid_reservoir
    qty: 1
    unit: None
  - item_id: heat_pipes_or_loop
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 3
    unit: None
  - item_id: pressure_gauge
    qty: 2
    unit: None
  - item_id: structural_frame_large
    qty: 1
    unit: None
  - item_id: power_cable_assembly
    qty: 1
    unit: None
  - item_id: fastener_kit_large
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `rough_part` (0.95 kg)
- Step 1 produces: `welded_fabrications` (1.05 kg)
- Step 2 produces: `brazed_assembly` (1.05 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'vacuum_testing_v0') requires input 'finished_part' which is not available

**Location:** Step 4
**Process:** `vacuum_testing_v0`
  - File: `kb/processes/vacuum_testing_v0.yaml`

**Current step:**
```yaml
- process_id: vacuum_testing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 5
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 7: recipe_template_missing_step_inputs

**Message:** Step 6 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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

BOM has 11 components:

- `compressor_reciprocating` (qty: 1 None)
- `heat_exchanger_tube_shell` (qty: 2 None)
- `expansion_valve_cryogenic` (qty: 1 None)
- `cryogenic_fluid_reservoir` (qty: 1 None)
- `heat_pipes_or_loop` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 3 None)
- `pressure_gauge` (qty: 2 None)
- `structural_frame_large` (qty: 1 None)
- `power_cable_assembly` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: compressor_reciprocating
    qty: 1
    unit: None
  - item_id: heat_exchanger_tube_shell
    qty: 2
    unit: None
  - item_id: expansion_valve_cryogenic
    qty: 1
    unit: None
  - item_id: cryogenic_fluid_reservoir
    qty: 1
    unit: None
  - item_id: heat_pipes_or_loop
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 3
    unit: None
  - item_id: pressure_gauge
    qty: 2
    unit: None
  - item_id: structural_frame_large
    qty: 1
    unit: None
  - item_id: power_cable_assembly
    qty: 1
    unit: None
  - item_id: fastener_kit_large
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `rough_part` (0.95 kg)
- Step 1 produces: `welded_fabrications` (1.05 kg)
- Step 2 produces: `brazed_assembly` (1.05 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `finished_part` (1.0 kg)
- Step 5 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 7
- **Recipe file:** `kb/recipes/recipe_cryogenic_chiller_v0.yaml`
- **BOM available:** Yes (11 components)
