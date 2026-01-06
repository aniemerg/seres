# Fix Intelligence: recipe_forging_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_forging_press_v0.yaml`
- **Target item:** `forging_press_v0`
  - File: `kb/items/forging_press_v0.yaml`
- **BOM:** `kb/boms/bom_forging_press_v0.yaml` ✓
  - Components: 3
- **Steps:** 6 total

## Errors (6 found)

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

BOM has 3 components:

- `steel_frame_heavy` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `base_metal_parts` (qty: 2 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: steel_frame_heavy
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: base_metal_parts
    qty: 2
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

- `steel_frame_heavy` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `base_metal_parts` (qty: 2 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: steel_frame_heavy
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: base_metal_parts
    qty: 2
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

BOM has 3 components:

- `steel_frame_heavy` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `base_metal_parts` (qty: 2 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: steel_frame_heavy
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: base_metal_parts
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'hip_press_unit_assembly_v0') requires input 'steel_shell_thick' which is not available

**Location:** Step 3
**Process:** `hip_press_unit_assembly_v0`
  - File: `kb/processes/hip_press_unit_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: hip_press_unit_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_step_input_not_satisfied

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

### Error 6: recipe_template_missing_step_inputs

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

BOM has 3 components:

- `steel_frame_heavy` (qty: 1 None)
- `hydraulic_power_unit_basic` (qty: 1 None)
- `base_metal_parts` (qty: 2 None)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: steel_frame_heavy
    qty: 1
    unit: None
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: None
  - item_id: base_metal_parts
    qty: 2
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `hip_press_unit_v0` (1.0 unit)
- Step 4 produces: `hydraulic_system_medium` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_forging_press_v0.yaml`
- **BOM available:** Yes (3 components)
