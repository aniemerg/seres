# Fix Intelligence: recipe_sabatier_reactor_co2_reduction_v0

## Files

- **Recipe:** `kb/recipes/recipe_sabatier_reactor_co2_reduction_v0.yaml`
- **Target item:** `sabatier_reactor_co2_reduction_v0`
  - File: `kb/items/sabatier_reactor_co2_reduction_v0.yaml`
- **BOM:** `kb/boms/bom_sabatier_reactor_co2_reduction_v0.yaml` ✓
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

- `pressure_vessel_steel` (qty: 1 None)
- `catalyst_bed_assembly` (qty: 1 None)
- `heating_element_electric` (qty: 1 None)
- `heat_exchanger_compact` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_casting_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 1
    unit: None
  - item_id: catalyst_bed_assembly
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 1
    unit: None
  - item_id: heat_exchanger_compact
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
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

- `pressure_vessel_steel` (qty: 1 None)
- `catalyst_bed_assembly` (qty: 1 None)
- `heating_element_electric` (qty: 1 None)
- `heat_exchanger_compact` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_brazing_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 1
    unit: None
  - item_id: catalyst_bed_assembly
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 1
    unit: None
  - item_id: heat_exchanger_compact
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
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

- `pressure_vessel_steel` (qty: 1 None)
- `catalyst_bed_assembly` (qty: 1 None)
- `heating_element_electric` (qty: 1 None)
- `heat_exchanger_compact` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 1
    unit: None
  - item_id: catalyst_bed_assembly
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 1
    unit: None
  - item_id: heat_exchanger_compact
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
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

- `pressure_vessel_steel` (qty: 1 None)
- `catalyst_bed_assembly` (qty: 1 None)
- `heating_element_electric` (qty: 1 None)
- `heat_exchanger_compact` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 1
    unit: None
  - item_id: catalyst_bed_assembly
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 1
    unit: None
  - item_id: heat_exchanger_compact
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 9 components:

- `pressure_vessel_steel` (qty: 1 None)
- `catalyst_bed_assembly` (qty: 1 None)
- `heating_element_electric` (qty: 1 None)
- `heat_exchanger_compact` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: sealing_and_assembly_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 1
    unit: None
  - item_id: catalyst_bed_assembly
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 1
    unit: None
  - item_id: heat_exchanger_compact
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
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

**Message:** Step 5 uses template process 'machine_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

- `pressure_vessel_steel` (qty: 1 None)
- `catalyst_bed_assembly` (qty: 1 None)
- `heating_element_electric` (qty: 1 None)
- `heat_exchanger_compact` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `pressure_gauge_set` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machine_assembly_basic_v0
  inputs:
  - item_id: pressure_vessel_steel
    qty: 1
    unit: None
  - item_id: catalyst_bed_assembly
    qty: 1
    unit: None
  - item_id: heating_element_electric
    qty: 1
    unit: None
  - item_id: heat_exchanger_compact
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: pressure_gauge_set
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
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

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_sabatier_reactor_co2_reduction_v0.yaml`
- **BOM available:** Yes (9 components)
