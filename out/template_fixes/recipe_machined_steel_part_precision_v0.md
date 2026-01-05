# Fix Intelligence: recipe_machined_steel_part_precision_v0

## Files

- **Recipe:** `kb/recipes/recipe_machined_steel_part_precision_v0.yaml`
- **Target item:** `machined_steel_part_precision`
  - File: `kb/items/machined_steel_part_precision.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'forging_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `forging_basic_v0`
  - File: `kb/processes/forging_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: forging_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `forged_steel_parts` (1.0 kg)

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

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_machined_steel_part_precision_v0.yaml`
- **BOM available:** No
