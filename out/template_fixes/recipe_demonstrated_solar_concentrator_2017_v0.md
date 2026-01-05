# Fix Intelligence: recipe_demonstrated_solar_concentrator_2017_v0

## Files

- **Recipe:** `kb/recipes/recipe_demonstrated_solar_concentrator_2017_v0.yaml`
- **Target item:** `demonstrated_solar_concentrator_2017_v0`
  - File: `kb/items/demonstrated_solar_concentrator_2017_v0.yaml`
- **BOM:** `kb/boms/bom_demonstrated_solar_concentrator_2017_v0.yaml` ✓
  - Components: 2
- **Steps:** 3 total

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

- `solar_concentrator_assembly` (qty: 1.0 None)
- `aligned_solar_concentrator` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: solar_concentrator_assembly
    qty: 1.0
    unit: None
  - item_id: aligned_solar_concentrator
    qty: 1.0
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

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

BOM has 2 components:

- `solar_concentrator_assembly` (qty: 1.0 None)
- `aligned_solar_concentrator` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: solar_concentrator_assembly
    qty: 1.0
    unit: None
  - item_id: aligned_solar_concentrator
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `assembled_equipment` (1.0 kg)
- Step 1 produces: `aligned_solar_concentrator` (1.0 unit)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_demonstrated_solar_concentrator_2017_v0.yaml`
- **BOM available:** Yes (2 components)
