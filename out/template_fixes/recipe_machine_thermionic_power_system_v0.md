# Fix Intelligence: recipe_machine_thermionic_power_system_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_thermionic_power_system_v0.yaml`
- **Target item:** `thermionic_power_system_v0`
  - File: `kb/items/thermionic_power_system_v0.yaml`
- **BOM:** `kb/boms/bom_thermionic_power_system_v0.yaml` ✓
  - Components: 6
- **Steps:** 8 total

## Errors (8 found)

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

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'concentrator_alignment_v0') requires input 'solar_concentrator_assembly' which is not available

**Location:** Step 2
**Process:** `concentrator_alignment_v0`
  - File: `kb/processes/concentrator_alignment_v0.yaml`

**Current step:**
```yaml
- process_id: concentrator_alignment_v0
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

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `aligned_solar_concentrator` (1.0 unit)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `aligned_solar_concentrator` (1.0 unit)
- Step 3 produces: `assembled_equipment` (1.0 kg)

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

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: wiring_and_electronics_integration_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `aligned_solar_concentrator` (1.0 unit)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

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

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `aligned_solar_concentrator` (1.0 unit)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)
- Step 5 produces: `wired_electrical_system` (1.0 unit)

---

### Error 8: recipe_template_missing_step_inputs

**Message:** Step 7 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 7
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `concentrator_frame_structure` (qty: 1 unit)
- `fresnel_lens_segment` (qty: 4 unit)
- `thermal_receiver_assembly` (qty: 1 unit)
- `thermionic_converter` (qty: 1 unit)
- `heat_pipes_set` (qty: 1 unit)
- `power_conditioning_equipment` (qty: 1 unit)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: concentrator_frame_structure
    qty: 1
    unit: unit
  - item_id: fresnel_lens_segment
    qty: 4
    unit: unit
  - item_id: thermal_receiver_assembly
    qty: 1
    unit: unit
  - item_id: thermionic_converter
    qty: 1
    unit: unit
  - item_id: heat_pipes_set
    qty: 1
    unit: unit
  - item_id: power_conditioning_equipment
    qty: 1
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `aligned_solar_concentrator` (1.0 unit)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)
- Step 5 produces: `wired_electrical_system` (1.0 unit)
- Step 6 produces: `assembled_electronics` (1.0 kg)

---

## Summary

- **Total errors:** 8
- **Recipe file:** `kb/recipes/recipe_machine_thermionic_power_system_v0.yaml`
- **BOM available:** Yes (6 components)
