# Fix Intelligence: recipe_feed_horn_antenna_v0

## Files

- **Recipe:** `kb/recipes/recipe_feed_horn_antenna_v0.yaml`
- **Target item:** `feed_horn_antenna_v0`
  - File: `kb/items/feed_horn_antenna_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_cutting_process_v0') requires input 'metal_sheet' which is not available

**Location:** Step 0
**Process:** `metal_cutting_process_v0`
  - File: `kb/processes/metal_cutting_process_v0.yaml`

**Current step:**
```yaml
- process_id: metal_cutting_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (0.9 kg)
- Step 0 produces: `metal_scrap` (0.1 kg)

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

- Step 0 produces: `cut_parts` (0.9 kg)
- Step 0 produces: `metal_scrap` (0.1 kg)
- Step 1 produces: `formed_metal_part` (0.95 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_feed_horn_antenna_v0.yaml`
- **BOM available:** No
