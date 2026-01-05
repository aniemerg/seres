# Fix Intelligence: recipe_cellular_manufacturing_layout_v0

## Files

- **Recipe:** `kb/recipes/recipe_cellular_manufacturing_layout_v0.yaml`
- **Target item:** `cellular_manufacturing_layout_v0`
  - File: `kb/items/cellular_manufacturing_layout_v0.yaml`
- **BOM:** `kb/boms/bom_cellular_manufacturing_layout_v0.yaml` ✓
  - Components: 1
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_cutting_basic_v0`
  - File: `kb/processes/metal_cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 1 components:

- `raw_metal_block` (qty: 1 None)

Suggested fix:
```yaml
- process_id: metal_cutting_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 1
    unit: None
```

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 1 components:

- `raw_metal_block` (qty: 1 None)

Suggested fix:
```yaml
- process_id: welding_and_fabrication_v0
  inputs:
  - item_id: raw_metal_block
    qty: 1
    unit: None
```

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

BOM has 1 components:

- `raw_metal_block` (qty: 1 None)

Suggested fix:
```yaml
- process_id: machining_finish_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 1 produces: `welded_fabrications` (9.5 kg)

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

BOM has 1 components:

- `raw_metal_block` (qty: 1 None)

Suggested fix:
```yaml
- process_id: assembly_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 1 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'surface_treatment_basic_v0') requires input 'formed_metal_part' which is not available

**Location:** Step 4
**Process:** `surface_treatment_basic_v0`
  - File: `kb/processes/surface_treatment_basic_v0.yaml`

**Current step:**
```yaml
- process_id: surface_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

BOM has 1 components:

- `raw_metal_block` (qty: 1 None)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: raw_metal_block
    qty: 1
    unit: None
```

#### Option B: Use previous step outputs

- Step 1 produces: `welded_fabrications` (9.5 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)
- Step 4 produces: `metal_part_surface_treated` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_cellular_manufacturing_layout_v0.yaml`
- **BOM available:** Yes (1 components)
