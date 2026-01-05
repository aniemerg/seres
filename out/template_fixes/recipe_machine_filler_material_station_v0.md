# Fix Intelligence: recipe_machine_filler_material_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_filler_material_station_v0.yaml`
- **Target item:** `filler_material_station_v0`
  - File: `kb/items/filler_material_station_v0.yaml`
- **BOM:** `kb/boms/bom_filler_material_station_v0.yaml` ✓
  - Components: 2
- **Steps:** 2 total

## Errors (2 found)

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

BOM has 2 components:

- `filler_wire_basic` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: filler_wire_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

BOM has 2 components:

- `filler_wire_basic` (qty: 1 None)
- `fastener_kit_small` (qty: 1 None)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: filler_wire_basic
    qty: 1
    unit: None
  - item_id: fastener_kit_small
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_machine_filler_material_station_v0.yaml`
- **BOM available:** Yes (2 components)
