# Fix Intelligence: recipe_ffc_reactor_enhanced_v0

## Files

- **Recipe:** `kb/recipes/recipe_ffc_reactor_enhanced_v0.yaml`
- **Target item:** `ffc_reactor_enhanced_v0`
  - File: `kb/items/ffc_reactor_enhanced_v0.yaml`
- **BOM:** `kb/boms/bom_ffc_reactor_enhanced_v0.yaml` ✓
  - Components: 3
- **Steps:** 7 total

## Errors (7 found)

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

- `molten_salt_containment_v0` (qty: 1.0 None)
- `graphite_anode_assembly_v0` (qty: 1.0 None)
- `temperature_control_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: molten_salt_containment_v0
    qty: 1.0
    unit: None
  - item_id: graphite_anode_assembly_v0
    qty: 1.0
    unit: None
  - item_id: temperature_control_system_v0
    qty: 1.0
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

- `molten_salt_containment_v0` (qty: 1.0 None)
- `graphite_anode_assembly_v0` (qty: 1.0 None)
- `temperature_control_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: molten_salt_containment_v0
    qty: 1.0
    unit: None
  - item_id: graphite_anode_assembly_v0
    qty: 1.0
    unit: None
  - item_id: temperature_control_system_v0
    qty: 1.0
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

- `molten_salt_containment_v0` (qty: 1.0 None)
- `graphite_anode_assembly_v0` (qty: 1.0 None)
- `temperature_control_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: molten_salt_containment_v0
    qty: 1.0
    unit: None
  - item_id: graphite_anode_assembly_v0
    qty: 1.0
    unit: None
  - item_id: temperature_control_system_v0
    qty: 1.0
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

BOM has 3 components:

- `molten_salt_containment_v0` (qty: 1.0 None)
- `graphite_anode_assembly_v0` (qty: 1.0 None)
- `temperature_control_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: molten_salt_containment_v0
    qty: 1.0
    unit: None
  - item_id: graphite_anode_assembly_v0
    qty: 1.0
    unit: None
  - item_id: temperature_control_system_v0
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

BOM has 3 components:

- `molten_salt_containment_v0` (qty: 1.0 None)
- `graphite_anode_assembly_v0` (qty: 1.0 None)
- `temperature_control_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: molten_salt_containment_v0
    qty: 1.0
    unit: None
  - item_id: graphite_anode_assembly_v0
    qty: 1.0
    unit: None
  - item_id: temperature_control_system_v0
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

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

**Message:** Step 6 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 6
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

- `molten_salt_containment_v0` (qty: 1.0 None)
- `graphite_anode_assembly_v0` (qty: 1.0 None)
- `temperature_control_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: molten_salt_containment_v0
    qty: 1.0
    unit: None
  - item_id: graphite_anode_assembly_v0
    qty: 1.0
    unit: None
  - item_id: temperature_control_system_v0
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 5 produces: `wired_electrical_system` (1.0 unit)

---

## Summary

- **Total errors:** 7
- **Recipe file:** `kb/recipes/recipe_ffc_reactor_enhanced_v0.yaml`
- **BOM available:** Yes (3 components)
