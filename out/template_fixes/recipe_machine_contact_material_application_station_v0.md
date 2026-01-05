# Fix Intelligence: recipe_machine_contact_material_application_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_contact_material_application_station_v0.yaml`
- **Target item:** `contact_material_application_station_v0`
  - File: `kb/items/contact_material_application_station_v0.yaml`
- **BOM:** `kb/boms/bom_contact_material_application_station_v0.yaml` ✓
  - Components: 8
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'import_receiving_basic_v0') requires input 'bulk_material_or_parts' which is not available

**Location:** Step 0
**Process:** `import_receiving_basic_v0`
  - File: `kb/processes/import_receiving_basic_v0.yaml`

**Current step:**
```yaml
- process_id: import_receiving_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

BOM has 8 components:

- `welding_power_supply_spot` (qty: 1.0 each)
- `welding_electrode_copper` (qty: 2.0 each)
- `brazing_torch_oxy_fuel` (qty: 1.0 each)
- `fixture_assembly_contacts` (qty: 5.0 each)
- `microscope_inspection_stereo` (qty: 1.0 each)
- `resistance_meter_micro_ohm` (qty: 1.0 each)
- `steel_workbench_heavy` (qty: 80.0 kg)
- `ventilation_fume_hood` (qty: 1.0 each)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: welding_power_supply_spot
    qty: 1.0
    unit: each
  - item_id: welding_electrode_copper
    qty: 2.0
    unit: each
  - item_id: brazing_torch_oxy_fuel
    qty: 1.0
    unit: each
  - item_id: fixture_assembly_contacts
    qty: 5.0
    unit: each
  - item_id: microscope_inspection_stereo
    qty: 1.0
    unit: each
  - item_id: resistance_meter_micro_ohm
    qty: 1.0
    unit: each
  - item_id: steel_workbench_heavy
    qty: 80.0
    unit: kg
  - item_id: ventilation_fume_hood
    qty: 1.0
    unit: each
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

BOM has 8 components:

- `welding_power_supply_spot` (qty: 1.0 each)
- `welding_electrode_copper` (qty: 2.0 each)
- `brazing_torch_oxy_fuel` (qty: 1.0 each)
- `fixture_assembly_contacts` (qty: 5.0 each)
- `microscope_inspection_stereo` (qty: 1.0 each)
- `resistance_meter_micro_ohm` (qty: 1.0 each)
- `steel_workbench_heavy` (qty: 80.0 kg)
- `ventilation_fume_hood` (qty: 1.0 each)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: welding_power_supply_spot
    qty: 1.0
    unit: each
  - item_id: welding_electrode_copper
    qty: 2.0
    unit: each
  - item_id: brazing_torch_oxy_fuel
    qty: 1.0
    unit: each
  - item_id: fixture_assembly_contacts
    qty: 5.0
    unit: each
  - item_id: microscope_inspection_stereo
    qty: 1.0
    unit: each
  - item_id: resistance_meter_micro_ohm
    qty: 1.0
    unit: each
  - item_id: steel_workbench_heavy
    qty: 80.0
    unit: kg
  - item_id: ventilation_fume_hood
    qty: 1.0
    unit: each
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_machine_contact_material_application_station_v0.yaml`
- **BOM available:** Yes (8 components)
