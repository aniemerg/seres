# Fix Intelligence: recipe_molding_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_molding_press_v0.yaml`
- **Target item:** `molding_press_v0`
  - File: `kb/items/molding_press_v0.yaml`
- **BOM:** `kb/boms/bom_molding_press_v0.yaml` ✓
  - Components: 7
- **Steps:** 5 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_molding_press_v0_v0` → molding_press_v0 (3 steps)
- `recipe_molding_press_v1` → molding_press (5 steps)
- `recipe_molding_press_unversioned_v0` → molding_press (5 steps)

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 7 components:

- `steel_frame_molding_press_v0` (qty: 1 None)
- `hydraulic_pump_unit_v0` (qty: 1 None)
- `mold_platen_assembly_v0` (qty: 2 None)
- `control_panel_basic_v0` (qty: 1 None)
- `bearing_set_v0` (qty: 4 None)
- `fastener_kit_large_v0` (qty: 1 None)
- `motor_assembly_standard_v0` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: steel_frame_molding_press_v0
    qty: 1
    unit: None
  - item_id: hydraulic_pump_unit_v0
    qty: 1
    unit: None
  - item_id: mold_platen_assembly_v0
    qty: 2
    unit: None
  - item_id: control_panel_basic_v0
    qty: 1
    unit: None
  - item_id: bearing_set_v0
    qty: 4
    unit: None
  - item_id: fastener_kit_large_v0
    qty: 1
    unit: None
  - item_id: motor_assembly_standard_v0
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

BOM has 7 components:

- `steel_frame_molding_press_v0` (qty: 1 None)
- `hydraulic_pump_unit_v0` (qty: 1 None)
- `mold_platen_assembly_v0` (qty: 2 None)
- `control_panel_basic_v0` (qty: 1 None)
- `bearing_set_v0` (qty: 4 None)
- `fastener_kit_large_v0` (qty: 1 None)
- `motor_assembly_standard_v0` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: steel_frame_molding_press_v0
    qty: 1
    unit: None
  - item_id: hydraulic_pump_unit_v0
    qty: 1
    unit: None
  - item_id: mold_platen_assembly_v0
    qty: 2
    unit: None
  - item_id: control_panel_basic_v0
    qty: 1
    unit: None
  - item_id: bearing_set_v0
    qty: 4
    unit: None
  - item_id: fastener_kit_large_v0
    qty: 1
    unit: None
  - item_id: motor_assembly_standard_v0
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)

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

- `steel_frame_molding_press_v0` (qty: 1 None)
- `hydraulic_pump_unit_v0` (qty: 1 None)
- `mold_platen_assembly_v0` (qty: 2 None)
- `control_panel_basic_v0` (qty: 1 None)
- `bearing_set_v0` (qty: 4 None)
- `fastener_kit_large_v0` (qty: 1 None)
- `motor_assembly_standard_v0` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_frame_molding_press_v0
    qty: 1
    unit: None
  - item_id: hydraulic_pump_unit_v0
    qty: 1
    unit: None
  - item_id: mold_platen_assembly_v0
    qty: 2
    unit: None
  - item_id: control_panel_basic_v0
    qty: 1
    unit: None
  - item_id: bearing_set_v0
    qty: 4
    unit: None
  - item_id: fastener_kit_large_v0
    qty: 1
    unit: None
  - item_id: motor_assembly_standard_v0
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
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

BOM has 7 components:

- `steel_frame_molding_press_v0` (qty: 1 None)
- `hydraulic_pump_unit_v0` (qty: 1 None)
- `mold_platen_assembly_v0` (qty: 2 None)
- `control_panel_basic_v0` (qty: 1 None)
- `bearing_set_v0` (qty: 4 None)
- `fastener_kit_large_v0` (qty: 1 None)
- `motor_assembly_standard_v0` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_frame_molding_press_v0
    qty: 1
    unit: None
  - item_id: hydraulic_pump_unit_v0
    qty: 1
    unit: None
  - item_id: mold_platen_assembly_v0
    qty: 2
    unit: None
  - item_id: control_panel_basic_v0
    qty: 1
    unit: None
  - item_id: bearing_set_v0
    qty: 4
    unit: None
  - item_id: fastener_kit_large_v0
    qty: 1
    unit: None
  - item_id: motor_assembly_standard_v0
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

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

#### Option A: Use BOM components

BOM has 7 components:

- `steel_frame_molding_press_v0` (qty: 1 None)
- `hydraulic_pump_unit_v0` (qty: 1 None)
- `mold_platen_assembly_v0` (qty: 2 None)
- `control_panel_basic_v0` (qty: 1 None)
- `bearing_set_v0` (qty: 4 None)
- `fastener_kit_large_v0` (qty: 1 None)
- `motor_assembly_standard_v0` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: steel_frame_molding_press_v0
    qty: 1
    unit: None
  - item_id: hydraulic_pump_unit_v0
    qty: 1
    unit: None
  - item_id: mold_platen_assembly_v0
    qty: 2
    unit: None
  - item_id: control_panel_basic_v0
    qty: 1
    unit: None
  - item_id: bearing_set_v0
    qty: 4
    unit: None
  - item_id: fastener_kit_large_v0
    qty: 1
    unit: None
  - item_id: motor_assembly_standard_v0
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_molding_press_v0.yaml`
- **BOM available:** Yes (7 components)
- **Similar recipes:** 3 found
