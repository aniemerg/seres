# Fix Intelligence: recipe_drilling_equipment_v0

## Files

- **Recipe:** `kb/recipes/recipe_drilling_equipment_v0.yaml`
- **Target item:** `drilling_equipment_v0`
  - File: `kb/items/drilling_equipment_v0.yaml`
- **BOM:** `kb/boms/bom_drilling_equipment_v0.yaml` ✓
  - Components: 8
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'welding_structural_v0') requires input 'cut_parts' which is not available

**Location:** Step 0
**Process:** `welding_structural_v0`
  - File: `kb/processes/welding_structural_v0.yaml`

**Current step:**
```yaml
- process_id: welding_structural_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 8 components:

- `motor_electric_medium` (qty: 2 unit)
- `structural_frame_steel` (qty: 150.0 kg)
- `drill_string_steel` (qty: 100.0 kg)
- `hydraulic_power_unit_basic` (qty: 1 unit)
- `cutting_tool_set_basic` (qty: 5 unit)
- `bearing_set_heavy` (qty: 4 unit)
- `control_panel_basic` (qty: 1 unit)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: machining_precision_v0
  inputs:
  - item_id: motor_electric_medium
    qty: 2
    unit: unit
  - item_id: structural_frame_steel
    qty: 150.0
    unit: kg
  - item_id: drill_string_steel
    qty: 100.0
    unit: kg
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: unit
  - item_id: cutting_tool_set_basic
    qty: 5
    unit: unit
  - item_id: bearing_set_heavy
    qty: 4
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.05 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- `motor_electric_medium` (qty: 2 unit)
- `structural_frame_steel` (qty: 150.0 kg)
- `drill_string_steel` (qty: 100.0 kg)
- `hydraulic_power_unit_basic` (qty: 1 unit)
- `cutting_tool_set_basic` (qty: 5 unit)
- `bearing_set_heavy` (qty: 4 unit)
- `control_panel_basic` (qty: 1 unit)
- `fastener_kit_medium` (qty: 2 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: motor_electric_medium
    qty: 2
    unit: unit
  - item_id: structural_frame_steel
    qty: 150.0
    unit: kg
  - item_id: drill_string_steel
    qty: 100.0
    unit: kg
  - item_id: hydraulic_power_unit_basic
    qty: 1
    unit: unit
  - item_id: cutting_tool_set_basic
    qty: 5
    unit: unit
  - item_id: bearing_set_heavy
    qty: 4
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 2
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.05 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_drilling_equipment_v0.yaml`
- **BOM available:** Yes (8 components)
