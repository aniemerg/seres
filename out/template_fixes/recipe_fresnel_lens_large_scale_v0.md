# Fix Intelligence: recipe_fresnel_lens_large_scale_v0

## Files

- **Recipe:** `kb/recipes/recipe_fresnel_lens_large_scale_v0.yaml`
- **Target item:** `fresnel_lens_large_scale_v0`
  - File: `kb/items/fresnel_lens_large_scale_v0.yaml`
- **BOM:** `kb/boms/bom_fresnel_lens_large_scale_v0.yaml` ✓
  - Components: 2
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_casting_v0') requires input 'glass_raw_materials' which is not available

**Location:** Step 0
**Process:** `glass_casting_v0`
  - File: `kb/processes/glass_casting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option A: Use BOM components

BOM has 2 components:

- `glass_casting_process_v0` (qty: 1.0 None)
- `precision_grinding_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: precision_grinding_basic_v0
  inputs:
  - item_id: glass_casting_process_v0
    qty: 1.0
    unit: None
  - item_id: precision_grinding_system_v0
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_glass_parts` (1.0 kg)

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

BOM has 2 components:

- `glass_casting_process_v0` (qty: 1.0 None)
- `precision_grinding_system_v0` (qty: 1.0 None)

Suggested fix:
```yaml
- process_id: inspection_basic_v0
  inputs:
  - item_id: glass_casting_process_v0
    qty: 1.0
    unit: None
  - item_id: precision_grinding_system_v0
    qty: 1.0
    unit: None
```

#### Option B: Use previous step outputs

- Step 0 produces: `cast_glass_parts` (1.0 kg)
- Step 1 produces: `finished_part_deburred` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_fresnel_lens_large_scale_v0.yaml`
- **BOM available:** Yes (2 components)
