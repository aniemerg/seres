# Fix Intelligence: recipe_chemical_reactor_basic_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_reactor_basic_v0.yaml`
- **Target item:** `chemical_reactor_basic`
  - File: `kb/items/chemical_reactor_basic.yaml`
- **BOM:** `kb/boms/bom_chemical_reactor_basic.yaml` ✓
  - Components: 10
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
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

BOM has 10 components:

- `chemical_reactor_vessel_v0` (qty: 1 None)
- `heating_jacket_assembly` (qty: 1 None)
- `reactor_agitator_mixer_v0` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `pressure_relief_valve` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welded_fabrication_basic_v0
  inputs:
  - item_id: chemical_reactor_vessel_v0
    qty: 1
    unit: None
  - item_id: heating_jacket_assembly
    qty: 1
    unit: None
  - item_id: reactor_agitator_mixer_v0
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: pressure_relief_valve
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
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

BOM has 10 components:

- `chemical_reactor_vessel_v0` (qty: 1 None)
- `heating_jacket_assembly` (qty: 1 None)
- `reactor_agitator_mixer_v0` (qty: 1 None)
- `gas_inlet_manifold` (qty: 1 None)
- `gas_outlet_manifold` (qty: 1 None)
- `pressure_relief_valve` (qty: 1 None)
- `temperature_controller_basic` (qty: 1 None)
- `thermocouple_type_s_v0` (qty: 2 None)
- `structural_frame_medium` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: chemical_reactor_vessel_v0
    qty: 1
    unit: None
  - item_id: heating_jacket_assembly
    qty: 1
    unit: None
  - item_id: reactor_agitator_mixer_v0
    qty: 1
    unit: None
  - item_id: gas_inlet_manifold
    qty: 1
    unit: None
  - item_id: gas_outlet_manifold
    qty: 1
    unit: None
  - item_id: pressure_relief_valve
    qty: 1
    unit: None
  - item_id: temperature_controller_basic
    qty: 1
    unit: None
  - item_id: thermocouple_type_s_v0
    qty: 2
    unit: None
  - item_id: structural_frame_medium
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_chemical_reactor_basic_v0.yaml`
- **BOM available:** Yes (10 components)
