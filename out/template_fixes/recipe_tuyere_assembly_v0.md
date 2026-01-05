# Fix Intelligence: recipe_tuyere_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_tuyere_assembly_v0.yaml`
- **Target item:** `tuyere_assembly`
  - File: `kb/items/tuyere_assembly.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sand_casting_medium_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 0
**Process:** `sand_casting_medium_v0`
  - File: `kb/processes/sand_casting_medium_v0.yaml`

**Current step:**
```yaml
- process_id: sand_casting_medium_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `sand_casting_medium_v0` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `welding_basic_v0`
  - File: `kb/processes/welding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `sand_casting_medium_v0` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

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

- Step 0 produces: `sand_casting_medium_v0` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `welded_assemblies` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_tuyere_assembly_v0.yaml`
- **BOM available:** No
