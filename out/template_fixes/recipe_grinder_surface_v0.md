# Fix Intelligence: recipe_grinder_surface_v0

## Files

- **Recipe:** `kb/recipes/recipe_grinder_surface_v0.yaml`
- **Target item:** `grinder_surface_v0`
  - File: `kb/items/grinder_surface_v0.yaml`
- **BOM:** `kb/boms/bom_grinder_surface_v0.yaml` ✓
  - Components: 9
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

BOM has 9 components:

- `machine_base_large` (qty: 1 None)
- `grinding_spindle_assembly` (qty: 1 None)
- `table_drive_assembly` (qty: 1 None)
- `magnetic_chuck_surface_grinder` (qty: 1 None)
- `coolant_system_basic` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: machine_base_large
    qty: 1
    unit: None
  - item_id: grinding_spindle_assembly
    qty: 1
    unit: None
  - item_id: table_drive_assembly
    qty: 1
    unit: None
  - item_id: magnetic_chuck_surface_grinder
    qty: 1
    unit: None
  - item_id: coolant_system_basic
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_large
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

BOM has 9 components:

- `machine_base_large` (qty: 1 None)
- `grinding_spindle_assembly` (qty: 1 None)
- `table_drive_assembly` (qty: 1 None)
- `magnetic_chuck_surface_grinder` (qty: 1 None)
- `coolant_system_basic` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: machine_base_large
    qty: 1
    unit: None
  - item_id: grinding_spindle_assembly
    qty: 1
    unit: None
  - item_id: table_drive_assembly
    qty: 1
    unit: None
  - item_id: magnetic_chuck_surface_grinder
    qty: 1
    unit: None
  - item_id: coolant_system_basic
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_large
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

BOM has 9 components:

- `machine_base_large` (qty: 1 None)
- `grinding_spindle_assembly` (qty: 1 None)
- `table_drive_assembly` (qty: 1 None)
- `magnetic_chuck_surface_grinder` (qty: 1 None)
- `coolant_system_basic` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: machine_base_large
    qty: 1
    unit: None
  - item_id: grinding_spindle_assembly
    qty: 1
    unit: None
  - item_id: table_drive_assembly
    qty: 1
    unit: None
  - item_id: magnetic_chuck_surface_grinder
    qty: 1
    unit: None
  - item_id: coolant_system_basic
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_large
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

BOM has 9 components:

- `machine_base_large` (qty: 1 None)
- `grinding_spindle_assembly` (qty: 1 None)
- `table_drive_assembly` (qty: 1 None)
- `magnetic_chuck_surface_grinder` (qty: 1 None)
- `coolant_system_basic` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machine_base_large
    qty: 1
    unit: None
  - item_id: grinding_spindle_assembly
    qty: 1
    unit: None
  - item_id: table_drive_assembly
    qty: 1
    unit: None
  - item_id: magnetic_chuck_surface_grinder
    qty: 1
    unit: None
  - item_id: coolant_system_basic
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_large
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 9 components:

- `machine_base_large` (qty: 1 None)
- `grinding_spindle_assembly` (qty: 1 None)
- `table_drive_assembly` (qty: 1 None)
- `magnetic_chuck_surface_grinder` (qty: 1 None)
- `coolant_system_basic` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: machine_base_large
    qty: 1
    unit: None
  - item_id: grinding_spindle_assembly
    qty: 1
    unit: None
  - item_id: table_drive_assembly
    qty: 1
    unit: None
  - item_id: magnetic_chuck_surface_grinder
    qty: 1
    unit: None
  - item_id: coolant_system_basic
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_large
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `alignment_and_testing_basic_v0`
  - File: `kb/processes/alignment_and_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: alignment_and_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 9 components:

- `machine_base_large` (qty: 1 None)
- `grinding_spindle_assembly` (qty: 1 None)
- `table_drive_assembly` (qty: 1 None)
- `magnetic_chuck_surface_grinder` (qty: 1 None)
- `coolant_system_basic` (qty: 1 None)
- `control_compute_module_imported` (qty: 1 None)
- `sensor_suite_general` (qty: 1 None)
- `power_conditioning_module` (qty: 1 None)
- `fastener_kit_large` (qty: 1 None)

Suggested fix:
```yaml
- process_id: alignment_and_testing_basic_v0
  inputs:
  - item_id: machine_base_large
    qty: 1
    unit: None
  - item_id: grinding_spindle_assembly
    qty: 1
    unit: None
  - item_id: table_drive_assembly
    qty: 1
    unit: None
  - item_id: magnetic_chuck_surface_grinder
    qty: 1
    unit: None
  - item_id: coolant_system_basic
    qty: 1
    unit: None
  - item_id: control_compute_module_imported
    qty: 1
    unit: None
  - item_id: sensor_suite_general
    qty: 1
    unit: None
  - item_id: power_conditioning_module
    qty: 1
    unit: None
  - item_id: fastener_kit_large
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `analog_test_bench_neural_circuits_v0` (1.0 unit)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_grinder_surface_v0.yaml`
- **BOM available:** Yes (9 components)
