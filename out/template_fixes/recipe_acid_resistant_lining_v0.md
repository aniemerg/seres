# Fix Intelligence: recipe_acid_resistant_lining_v0

## Files

- **Recipe:** `kb/recipes/recipe_acid_resistant_lining_v0.yaml`
- **Target item:** `acid_resistant_lining`
  - File: `kb/items/acid_resistant_lining.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_melting_and_forming_v0') requires input 'regolith_fine_fraction' which is not available

**Location:** Step 0
**Process:** `glass_melting_and_forming_v0`
  - File: `kb/processes/glass_melting_and_forming_v0.yaml`

**Current step:**
```yaml
- process_id: glass_melting_and_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'cleaning_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `cleaning_basic_v0`
  - File: `kb/processes/cleaning_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cleaning_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `glass_bulk` (9.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'ceramic_coating_v0') requires input 'finished_part' which is not available

**Location:** Step 2
**Process:** `ceramic_coating_v0`
  - File: `kb/processes/ceramic_coating_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_coating_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'heat_treatment_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `glass_bulk` (9.0 kg)
- Step 1 produces: `part_cleaned` (1.0 kg)
- Step 2 produces: `finished_part` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_acid_resistant_lining_v0.yaml`
- **BOM available:** No
