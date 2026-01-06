# Fix Intelligence: recipe_pcb_fab_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_pcb_fab_station_v0.yaml`
- **Target item:** `pcb_fab_station`
  - File: `kb/items/pcb_fab_station.yaml`
- **BOM:** `kb/boms/bom_pcb_fab_station.yaml` ✓
  - Components: 3
- **Steps:** 6 total

## Errors (6 found)

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

BOM has 3 components:

- `electronic_components_set` (qty: 1 None)
- `machine_frame_small` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
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

BOM has 3 components:

- `electronic_components_set` (qty: 1 None)
- `machine_frame_small` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

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

#### Option A: Use BOM components

BOM has 3 components:

- `electronic_components_set` (qty: 1 None)
- `machine_frame_small` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
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

BOM has 3 components:

- `electronic_components_set` (qty: 1 None)
- `machine_frame_small` (qty: 1 None)
- `enclosure_electrical_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: electronic_components_set
    qty: 1
    unit: None
  - item_id: machine_frame_small
    qty: 1
    unit: None
  - item_id: enclosure_electrical_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'electrical_wiring_and_controls_v0') requires input 'electrical_wire_and_connectors' which is not available

**Location:** Step 4
**Process:** `electrical_wiring_and_controls_v0`
  - File: `kb/processes/electrical_wiring_and_controls_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_wiring_and_controls_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_step_input_not_satisfied

**Message:** Step 5 (process 'electrical_testing_and_calibration_v0') requires input 'ffc_power_supply_assembled' which is not available

**Location:** Step 5
**Process:** `electrical_testing_and_calibration_v0`
  - File: `kb/processes/electrical_testing_and_calibration_v0.yaml`

**Current step:**
```yaml
- process_id: electrical_testing_and_calibration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_pcb_fab_station_v0.yaml`
- **BOM available:** Yes (3 components)
