# Fix Intelligence: recipe_stewart_platform_structure_v0

## Files

- **Recipe:** `kb/recipes/recipe_stewart_platform_structure_v0.yaml`
- **Target item:** `stewart_platform_structure`
  - File: `kb/items/stewart_platform_structure.yaml`
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

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `metal_sheet_or_plate` (0.98 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welding_and_fabrication_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `welding_and_fabrication_v0`
  - File: `kb/processes/welding_and_fabrication_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_and_fabrication_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `metal_sheet_or_plate` (0.98 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'surface_finishing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `metal_sheet_or_plate` (0.98 kg)
- Step 1 produces: `machined_steel_part_precision` (7.0 kg)
- Step 2 produces: `welded_fabrications` (9.5 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_stewart_platform_structure_v0.yaml`
- **BOM available:** No
