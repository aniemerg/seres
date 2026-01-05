# Fix Intelligence: recipe_conveyor_frame_small_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_conveyor_frame_small_import_v0.yaml`
- **Target item:** `conveyor_frame_small`
  - File: `kb/items/conveyor_frame_small.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welded_fabrication_basic_v0`
  - File: `kb/processes/welded_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welded_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'coating_insulation_v0') requires input 'substrate_part_or_wire' which is not available

**Location:** Step 3
**Process:** `coating_insulation_v0`
  - File: `kb/processes/coating_insulation_v0.yaml`

**Current step:**
```yaml
- process_id: coating_insulation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_fabrications` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `insulated_part_or_wire` (1.3 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_conveyor_frame_small_import_v0.yaml`
- **BOM available:** No
