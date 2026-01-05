# Fix Intelligence: recipe_nickel_sheet_rolling_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_sheet_rolling_v0.yaml`
- **Target item:** `nickel_sheet_rolling_v0`
  - File: `kb/items/nickel_sheet_rolling_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'mond_carbonyl_process_nickel_v0') requires input 'nickel_metal' which is not available

**Location:** Step 0
**Process:** `mond_carbonyl_process_nickel_v0`
  - File: `kb/processes/mond_carbonyl_process_nickel_v0.yaml`

**Current step:**
```yaml
- process_id: mond_carbonyl_process_nickel_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `nickel_metal_pure` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'rolling_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `rolling_basic_v0`
  - File: `kb/processes/rolling_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: rolling_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `nickel_metal_pure` (1.0 kg)
- Step 1 produces: `cast_metal_parts` (0.95 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_nickel_sheet_rolling_v0.yaml`
- **BOM available:** No
