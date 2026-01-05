# Fix Intelligence: recipe_powder_feedstock_v0

## Files

- **Recipe:** `kb/recipes/recipe_powder_feedstock_v0.yaml`
- **Target item:** `powder_feedstock`
  - File: `kb/items/powder_feedstock.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `grinding_basic_v0`
  - File: `kb/processes/grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'screening_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `screening_basic_v0`
  - File: `kb/processes/screening_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: screening_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (0.99 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'drying_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `drying_basic_v0`
  - File: `kb/processes/drying_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: drying_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `finished_part_deburred` (0.99 kg)
- Step 1 produces: `powder_feedstock` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `finished_part_deburred` (0.99 kg)
- Step 1 produces: `powder_feedstock` (1.0 kg)
- Step 2 produces: `dried_material` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_powder_feedstock_v0.yaml`
- **BOM available:** No
