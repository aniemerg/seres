# Fix Intelligence: recipe_fresnel_lens_segment_v0

## Files

- **Recipe:** `kb/recipes/recipe_fresnel_lens_segment_v0.yaml`
- **Target item:** `fresnel_lens_segment`
  - File: `kb/items/fresnel_lens_segment.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'glass_melting_v0') requires input 'glass_batch_mix' which is not available

**Location:** Step 0
**Process:** `glass_melting_v0`
  - File: `kb/processes/glass_melting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_melting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'glass_casting_v0') requires input 'glass_raw_materials' which is not available

**Location:** Step 1
**Process:** `glass_casting_v0`
  - File: `kb/processes/glass_casting_v0.yaml`

**Current step:**
```yaml
- process_id: glass_casting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'annealing_v0') requires input 'material_unannealed' which is not available

**Location:** Step 2
**Process:** `annealing_v0`
  - File: `kb/processes/annealing_v0.yaml`

**Current step:**
```yaml
- process_id: annealing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'precision_grinding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `precision_grinding_basic_v0`
  - File: `kb/processes/precision_grinding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: precision_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `molten_glass` (9.0 kg)
- Step 1 produces: `cast_glass_parts` (1.0 kg)
- Step 2 produces: `material_annealed` (5.0 kg)

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

- Step 0 produces: `molten_glass` (9.0 kg)
- Step 1 produces: `cast_glass_parts` (1.0 kg)
- Step 2 produces: `material_annealed` (5.0 kg)
- Step 3 produces: `finished_part_deburred` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_fresnel_lens_segment_v0.yaml`
- **BOM available:** No
