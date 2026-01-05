# Fix Intelligence: recipe_forged_steel_parts_v0

## Files

- **Recipe:** `kb/recipes/recipe_forged_steel_parts_v0.yaml`
- **Target item:** `forged_steel_parts`
  - File: `kb/items/forged_steel_parts.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'heating_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `heating_basic_v0`
  - File: `kb/processes/heating_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: heating_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'forging_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `forging_basic_v0`
  - File: `kb/processes/forging_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: forging_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'heat_treatment_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `heat_treatment_basic_v0`
  - File: `kb/processes/heat_treatment_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: heat_treatment_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material` (1.0 kg)
- Step 1 produces: `forged_steel_parts` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `bulk_material` (1.0 kg)
- Step 1 produces: `forged_steel_parts` (1.0 kg)
- Step 2 produces: `finished_part` (10.0 kg)

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

- Step 0 produces: `bulk_material` (1.0 kg)
- Step 1 produces: `forged_steel_parts` (1.0 kg)
- Step 2 produces: `finished_part` (10.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_forged_steel_parts_v0.yaml`
- **BOM available:** No
