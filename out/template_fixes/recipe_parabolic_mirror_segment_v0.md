# Fix Intelligence: recipe_parabolic_mirror_segment_v0

## Files

- **Recipe:** `kb/recipes/recipe_parabolic_mirror_segment_v0.yaml`
- **Target item:** `parabolic_mirror_segment`
  - File: `kb/items/parabolic_mirror_segment.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

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

**Message:** Step 1 uses template process 'annealing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `annealing_basic_v0`
  - File: `kb/processes/annealing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: annealing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `glass_bulk` (9.0 kg)

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

- Step 0 produces: `glass_bulk` (9.0 kg)
- Step 1 produces: `material_annealed` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_parabolic_mirror_segment_v0.yaml`
- **BOM available:** No
