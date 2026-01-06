# Fix Intelligence: recipe_filtration_unit_v0

## Files

- **Recipe:** `kb/recipes/recipe_filtration_unit_v0.yaml`
- **Target item:** `filtration_unit`
  - File: `kb/items/filtration_unit.yaml`
- **BOM:** `kb/boms/bom_filtration_unit.yaml` ✓
  - Components: 5
- **Steps:** 1 total

## Errors (1 found)

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

BOM has 5 components:

- `support_frame_welded` (qty: 1 None)
- `plumbing_system_assembly` (qty: 1 None)
- `coolant_pump_system` (qty: 1 None)
- `filter_cartridges_dust` (qty: 1 None)
- `fastener_kit_medium` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: support_frame_welded
    qty: 1
    unit: None
  - item_id: plumbing_system_assembly
    qty: 1
    unit: None
  - item_id: coolant_pump_system
    qty: 1
    unit: None
  - item_id: filter_cartridges_dust
    qty: 1
    unit: None
  - item_id: fastener_kit_medium
    qty: 1
    unit: None
```

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_filtration_unit_v0.yaml`
- **BOM available:** Yes (5 components)
