# Fix Intelligence: recipe_work_rest_adjustable_v0

## Files

- **Recipe:** `kb/recipes/recipe_work_rest_adjustable_v0.yaml`
- **Target item:** `work_rest_adjustable`
  - File: `kb/items/work_rest_adjustable.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'welding_structural_v0') requires input 'cut_parts' which is not available

**Location:** Step 1
**Process:** `welding_structural_v0`
  - File: `kb/processes/welding_structural_v0.yaml`

**Current step:**
```yaml
- process_id: welding_structural_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `welded_fabrications` (1.05 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'surface_finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `surface_finishing_basic_v0`
  - File: `kb/processes/surface_finishing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: surface_finishing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `welded_fabrications` (1.05 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
**Process:** `inspection_basic_v0`
  - File: `kb/processes/inspection_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: inspection_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `welded_fabrications` (1.05 kg)
- Step 2 produces: `assembled_equipment` (1.0 kg)
- Step 3 produces: `finished_part` (0.95 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_work_rest_adjustable_v0.yaml`
- **BOM available:** No
