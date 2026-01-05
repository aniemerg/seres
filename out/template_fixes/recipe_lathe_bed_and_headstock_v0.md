# Fix Intelligence: recipe_lathe_bed_and_headstock_v0

## Files

- **Recipe:** `kb/recipes/recipe_lathe_bed_and_headstock_v0.yaml`
- **Target item:** `lathe_bed_and_headstock`
  - File: `kb/items/lathe_bed_and_headstock.yaml`
- **BOM:** None
- **Steps:** 6 total

## Errors (6 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
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

**Message:** Step 2 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 1 produces: `welded_fabrications` (1.05 kg)

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'precision_alignment_and_leveling_v0') requires input 'machine_frame_small' which is not available

**Location:** Step 3
**Process:** `precision_alignment_and_leveling_v0`
  - File: `kb/processes/precision_alignment_and_leveling_v0.yaml`

**Current step:**
```yaml
- process_id: precision_alignment_and_leveling_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'surface_finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 1 produces: `welded_fabrications` (1.05 kg)
- Step 2 produces: `machined_steel_part_precision` (7.0 kg)
- Step 3 produces: `machine_frame_small` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
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

- Step 1 produces: `welded_fabrications` (1.05 kg)
- Step 2 produces: `machined_steel_part_precision` (7.0 kg)
- Step 3 produces: `machine_frame_small` (1.0 kg)
- Step 4 produces: `finished_part` (0.95 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_lathe_bed_and_headstock_v0.yaml`
- **BOM available:** No
