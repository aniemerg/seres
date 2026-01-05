# Fix Intelligence: recipe_machine_regolith_brick_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_regolith_brick_press_v0.yaml`
- **Target item:** `regolith_brick_press_v0`
  - File: `kb/items/regolith_brick_press_v0.yaml`
- **BOM:** `kb/boms/bom_regolith_brick_press_v0.yaml` ✓
  - Components: 7
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

#### Option A: Use BOM components

BOM has 7 components:

- `press_frame_medium` (qty: 1 None)
- `press_platen_set` (qty: 1 None)
- `press_cylinder_medium` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `hydraulic_hoses_and_fittings` (qty: 1 None)
- `pressing_mold_set` (qty: 1 None)
- `control_circuit_board_basic` (qty: 1 None)

Suggested fix:
```yaml
- process_id: cutting_basic_v0
  inputs:
  - item_id: press_frame_medium
    qty: 1
    unit: None
  - item_id: press_platen_set
    qty: 1
    unit: None
  - item_id: press_cylinder_medium
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: hydraulic_hoses_and_fittings
    qty: 1
    unit: None
  - item_id: pressing_mold_set
    qty: 1
    unit: None
  - item_id: control_circuit_board_basic
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welded_fabrication_basic_v0`
  - File: `kb/processes/welded_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welded_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `press_frame_medium` (qty: 1 None)
- `press_platen_set` (qty: 1 None)
- `press_cylinder_medium` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `hydraulic_hoses_and_fittings` (qty: 1 None)
- `pressing_mold_set` (qty: 1 None)
- `control_circuit_board_basic` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welded_fabrication_basic_v0
  inputs:
  - item_id: press_frame_medium
    qty: 1
    unit: None
  - item_id: press_platen_set
    qty: 1
    unit: None
  - item_id: press_cylinder_medium
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: hydraulic_hoses_and_fittings
    qty: 1
    unit: None
  - item_id: pressing_mold_set
    qty: 1
    unit: None
  - item_id: control_circuit_board_basic
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

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

BOM has 7 components:

- `press_frame_medium` (qty: 1 None)
- `press_platen_set` (qty: 1 None)
- `press_cylinder_medium` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `hydraulic_hoses_and_fittings` (qty: 1 None)
- `pressing_mold_set` (qty: 1 None)
- `control_circuit_board_basic` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: press_frame_medium
    qty: 1
    unit: None
  - item_id: press_platen_set
    qty: 1
    unit: None
  - item_id: press_cylinder_medium
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: hydraulic_hoses_and_fittings
    qty: 1
    unit: None
  - item_id: pressing_mold_set
    qty: 1
    unit: None
  - item_id: control_circuit_board_basic
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'hydraulic_system_integration_v0') requires input 'hydraulic_control_valve_set' which is not available

**Location:** Step 4
**Process:** `hydraulic_system_integration_v0`
  - File: `kb/processes/hydraulic_system_integration_v0.yaml`

**Current step:**
```yaml
- process_id: hydraulic_system_integration_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'wiring_and_electronics_integration_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

BOM has 7 components:

- `press_frame_medium` (qty: 1 None)
- `press_platen_set` (qty: 1 None)
- `press_cylinder_medium` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `hydraulic_hoses_and_fittings` (qty: 1 None)
- `pressing_mold_set` (qty: 1 None)
- `control_circuit_board_basic` (qty: 1 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: press_frame_medium
    qty: 1
    unit: None
  - item_id: press_platen_set
    qty: 1
    unit: None
  - item_id: press_cylinder_medium
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: hydraulic_hoses_and_fittings
    qty: 1
    unit: None
  - item_id: pressing_mold_set
    qty: 1
    unit: None
  - item_id: control_circuit_board_basic
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `hydraulic_system_medium` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

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

BOM has 7 components:

- `press_frame_medium` (qty: 1 None)
- `press_platen_set` (qty: 1 None)
- `press_cylinder_medium` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `hydraulic_hoses_and_fittings` (qty: 1 None)
- `pressing_mold_set` (qty: 1 None)
- `control_circuit_board_basic` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: press_frame_medium
    qty: 1
    unit: None
  - item_id: press_platen_set
    qty: 1
    unit: None
  - item_id: press_cylinder_medium
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: hydraulic_hoses_and_fittings
    qty: 1
    unit: None
  - item_id: pressing_mold_set
    qty: 1
    unit: None
  - item_id: control_circuit_board_basic
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 4 produces: `hydraulic_system_medium` (1.0 kg)
- Step 5 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_machine_regolith_brick_press_v0.yaml`
- **BOM available:** Yes (7 components)
