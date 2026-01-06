# Fix Intelligence: recipe_coating_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_coating_station_v0.yaml`
- **Target item:** `coating_station_v0`
  - File: `kb/items/coating_station_v0.yaml`
- **BOM:** `kb/boms/bom_coating_station_v0.yaml` ✓
  - Components: 6
- **Steps:** 5 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_coating_station_v1` → coating_station (3 steps)

## Errors (5 found)

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

BOM has 6 components:

- `coating_booth_enclosure` (qty: 1 None)
- `coating_spray_gun_and_pump` (qty: 1 None)
- `coating_drying_oven` (qty: 1 None)
- `chemical_bath_ventilation` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welded_fabrication_basic_v0
  inputs:
  - item_id: coating_booth_enclosure
    qty: 1
    unit: None
  - item_id: coating_spray_gun_and_pump
    qty: 1
    unit: None
  - item_id: coating_drying_oven
    qty: 1
    unit: None
  - item_id: chemical_bath_ventilation
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 6 components:

- `coating_booth_enclosure` (qty: 1 None)
- `coating_spray_gun_and_pump` (qty: 1 None)
- `coating_drying_oven` (qty: 1 None)
- `chemical_bath_ventilation` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: enclosure_assembly_basic_v0
  inputs:
  - item_id: coating_booth_enclosure
    qty: 1
    unit: None
  - item_id: coating_spray_gun_and_pump
    qty: 1
    unit: None
  - item_id: coating_drying_oven
    qty: 1
    unit: None
  - item_id: chemical_bath_ventilation
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 6 components:

- `coating_booth_enclosure` (qty: 1 None)
- `coating_spray_gun_and_pump` (qty: 1 None)
- `coating_drying_oven` (qty: 1 None)
- `chemical_bath_ventilation` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: electrical_assembly_basic_v0
  inputs:
  - item_id: coating_booth_enclosure
    qty: 1
    unit: None
  - item_id: coating_spray_gun_and_pump
    qty: 1
    unit: None
  - item_id: coating_drying_oven
    qty: 1
    unit: None
  - item_id: chemical_bath_ventilation
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

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

- `coating_booth_enclosure` (qty: 1 None)
- `coating_spray_gun_and_pump` (qty: 1 None)
- `coating_drying_oven` (qty: 1 None)
- `chemical_bath_ventilation` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: coating_booth_enclosure
    qty: 1
    unit: None
  - item_id: coating_spray_gun_and_pump
    qty: 1
    unit: None
  - item_id: coating_drying_oven
    qty: 1
    unit: None
  - item_id: chemical_bath_ventilation
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)

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

BOM has 6 components:

- `coating_booth_enclosure` (qty: 1 None)
- `coating_spray_gun_and_pump` (qty: 1 None)
- `coating_drying_oven` (qty: 1 None)
- `chemical_bath_ventilation` (qty: 1 None)
- `control_panel_basic` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: integration_test_basic_v0
  inputs:
  - item_id: coating_booth_enclosure
    qty: 1
    unit: None
  - item_id: coating_spray_gun_and_pump
    qty: 1
    unit: None
  - item_id: coating_drying_oven
    qty: 1
    unit: None
  - item_id: chemical_bath_ventilation
    qty: 1
    unit: None
  - item_id: control_panel_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)
- Step 1 produces: `enclosure_electrical_medium` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_coating_station_v0.yaml`
- **BOM available:** Yes (6 components)
- **Similar recipes:** 1 found
