# Fix Intelligence: recipe_mining_equipment_v0

## Files

- **Recipe:** `kb/recipes/recipe_mining_equipment_v0.yaml`
- **Target item:** `mining_equipment`
  - File: `kb/items/mining_equipment.yaml`
- **BOM:** `kb/boms/bom_mining_equipment.yaml` ✓
  - Components: 6
- **Steps:** 2 total

## Errors (2 found)

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

BOM has 6 components:

- `steel_frame_heavy` (qty: 2 unit)
- `motor_electric_large` (qty: 1 unit)
- `hydraulic_pump_basic` (qty: 1 unit)
- `bearing_set_heavy` (qty: 2 unit)
- `control_panel_basic` (qty: 1 unit)
- `fastener_kit_medium` (qty: 6 unit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: steel_frame_heavy
    qty: 2
    unit: unit
  - item_id: motor_electric_large
    qty: 1
    unit: unit
  - item_id: hydraulic_pump_basic
    qty: 1
    unit: unit
  - item_id: bearing_set_heavy
    qty: 2
    unit: unit
  - item_id: control_panel_basic
    qty: 1
    unit: unit
  - item_id: fastener_kit_medium
    qty: 6
    unit: unit
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_mining_equipment_v0.yaml`
- **BOM available:** Yes (6 components)
