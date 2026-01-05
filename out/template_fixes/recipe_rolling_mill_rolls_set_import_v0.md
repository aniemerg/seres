# Fix Intelligence: recipe_rolling_mill_rolls_set_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_rolling_mill_rolls_set_import_v0.yaml`
- **Target item:** `rolling_mill_rolls_set`
  - File: `kb/items/rolling_mill_rolls_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'forging_rolls_basic_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 0
**Process:** `forging_rolls_basic_v0`
  - File: `kb/processes/forging_rolls_basic_v0.yaml`

**Current step:**
```yaml
- process_id: forging_rolls_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'heat_treatment_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `rolling_mill_rolls_set` (1.0 set)

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

- Step 0 produces: `rolling_mill_rolls_set` (1.0 set)
- Step 1 produces: `finished_part` (10.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_rolling_mill_rolls_set_import_v0.yaml`
- **BOM available:** No
