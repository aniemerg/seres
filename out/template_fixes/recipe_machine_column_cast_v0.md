# Fix Intelligence: recipe_machine_column_cast_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_column_cast_v0.yaml`
- **Target item:** `machine_column_cast`
  - File: `kb/items/machine_column_cast.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'pattern_making_basic_v0') requires input 'wood_or_composite_material' which is not available

**Location:** Step 0
**Process:** `pattern_making_basic_v0`
  - File: `kb/processes/pattern_making_basic_v0.yaml`

**Current step:**
```yaml
- process_id: pattern_making_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'sand_casting_large_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 1
**Process:** `sand_casting_large_v0`
  - File: `kb/processes/sand_casting_large_v0.yaml`

**Current step:**
```yaml
- process_id: sand_casting_large_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'stress_relief_annealing_v0') requires input 'machined_part_raw' which is not available

**Location:** Step 2
**Process:** `stress_relief_annealing_v0`
  - File: `kb/processes/stress_relief_annealing_v0.yaml`

**Current step:**
```yaml
- process_id: stress_relief_annealing_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `casting_patterns_wooden` (1.0 kg)
- Step 1 produces: `sand_casting_large_v0` (45.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

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

- Step 0 produces: `casting_patterns_wooden` (1.0 kg)
- Step 1 produces: `sand_casting_large_v0` (45.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_machine_column_cast_v0.yaml`
- **BOM available:** No
