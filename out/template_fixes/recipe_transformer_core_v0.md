# Fix Intelligence: recipe_transformer_core_v0

## Files

- **Recipe:** `kb/recipes/recipe_transformer_core_v0.yaml`
- **Target item:** `transformer_core`
  - File: `kb/items/transformer_core.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sheet_metal_cutting_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `sheet_metal_cutting_v0`
  - File: `kb/processes/sheet_metal_cutting_v0.yaml`

**Current step:**
```yaml
- process_id: sheet_metal_cutting_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'coating_insulation_v0') requires input 'substrate_part_or_wire' which is not available

**Location:** Step 1
**Process:** `coating_insulation_v0`
  - File: `kb/processes/coating_insulation_v0.yaml`

**Current step:**
```yaml
- process_id: coating_insulation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'stacking_and_clamping_v0') requires input 'electrical_steel_sheet' which is not available

**Location:** Step 2
**Process:** `stacking_and_clamping_v0`
  - File: `kb/processes/stacking_and_clamping_v0.yaml`

**Current step:**
```yaml
- process_id: stacking_and_clamping_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'annealing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `metal_sheet_or_plate` (0.98 kg)
- Step 1 produces: `insulated_part_or_wire` (1.3 kg)
- Step 2 produces: `lamination_stack_clamped` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_transformer_core_v0.yaml`
- **BOM available:** No
