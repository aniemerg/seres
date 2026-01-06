# Fix Intelligence: recipe_press_brake_v0

## Files

- **Recipe:** `kb/recipes/recipe_press_brake_v0.yaml`
- **Target item:** `press_brake_v0`
  - File: `kb/items/press_brake_v0.yaml`
- **BOM:** `kb/boms/bom_press_brake_v0.yaml` ✓
  - Components: 6
- **Steps:** 3 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_press_brake_v0` → press_brake (3 steps)
- `recipe_machine_press_brake_import_v0` → press_brake (3 steps)

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

BOM has 6 components:

- `machined_steel_part_precision` (qty: 120.0 kg)
- `structural_steel_frame` (qty: 500.0 kg)
- `hydraulic_system_medium` (qty: 1.0 unit)
- `power_electronics_module` (qty: 1.0 unit)
- `control_panel_assembly_v0` (qty: 1.0 unit)
- `fastener_kit_medium` (qty: 1.0 kit)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: machined_steel_part_precision
    qty: 120.0
    unit: kg
  - item_id: structural_steel_frame
    qty: 500.0
    unit: kg
  - item_id: hydraulic_system_medium
    qty: 1.0
    unit: unit
  - item_id: power_electronics_module
    qty: 1.0
    unit: unit
  - item_id: control_panel_assembly_v0
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kit
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

BOM has 6 components:

- `machined_steel_part_precision` (qty: 120.0 kg)
- `structural_steel_frame` (qty: 500.0 kg)
- `hydraulic_system_medium` (qty: 1.0 unit)
- `power_electronics_module` (qty: 1.0 unit)
- `control_panel_assembly_v0` (qty: 1.0 unit)
- `fastener_kit_medium` (qty: 1.0 kit)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: machined_steel_part_precision
    qty: 120.0
    unit: kg
  - item_id: structural_steel_frame
    qty: 500.0
    unit: kg
  - item_id: hydraulic_system_medium
    qty: 1.0
    unit: unit
  - item_id: power_electronics_module
    qty: 1.0
    unit: unit
  - item_id: control_panel_assembly_v0
    qty: 1.0
    unit: unit
  - item_id: fastener_kit_medium
    qty: 1.0
    unit: kit
```

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material_or_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_press_brake_v0.yaml`
- **BOM available:** Yes (6 components)
- **Similar recipes:** 2 found
