# Fix Intelligence: recipe_steel_frame_heavy_v0

## Files

- **Recipe:** `kb/recipes/recipe_steel_frame_heavy_v0.yaml`
- **Target item:** `steel_frame_heavy`
  - File: `kb/items/steel_frame_heavy.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_steel_frame_heavy_import_v0` → steel_frame_heavy (3 steps)

## Errors (3 found)

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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_sheet_or_plate` (0.98 kg)

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

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_steel_frame_heavy_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
