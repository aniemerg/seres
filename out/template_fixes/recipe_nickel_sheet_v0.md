# Fix Intelligence: recipe_nickel_sheet_v0

## Files

- **Recipe:** `kb/recipes/recipe_nickel_sheet_v0.yaml`
- **Target item:** `nickel_sheet`
  - File: `kb/items/nickel_sheet.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'nickel_extraction_meteorite_v0') requires input 'meteorite_iron' which is not available

**Location:** Step 0
**Process:** `nickel_extraction_meteorite_v0`
  - File: `kb/processes/nickel_extraction_meteorite_v0.yaml`

**Current step:**
```yaml
- process_id: nickel_extraction_meteorite_v0
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

- Step 0 produces: `nickel_metal` (1.0 kg)
- Step 0 produces: `iron_metal` (8.0 kg)

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

- Step 0 produces: `nickel_metal` (1.0 kg)
- Step 0 produces: `iron_metal` (8.0 kg)
- Step 1 produces: `cast_metal_parts` (0.95 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_nickel_sheet_v0.yaml`
- **BOM available:** No
