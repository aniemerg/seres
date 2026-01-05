# Fix Intelligence: recipe_machine_cell_sealer_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_cell_sealer_station_v0.yaml`
- **Target item:** `cell_sealer_station`
  - File: `kb/items/cell_sealer_station.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_machine_cell_sealer_station_import_v0` → cell_sealer_station (3 steps)

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_parts_fabrication_v0') requires input 'base_metal_parts' which is not available

**Location:** Step 0
**Process:** `metal_parts_fabrication_v0`
  - File: `kb/processes/metal_parts_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: metal_parts_fabrication_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `cast_metal_parts` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `alignment_and_testing_basic_v0`
  - File: `kb/processes/alignment_and_testing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: alignment_and_testing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cast_metal_parts` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_machine_cell_sealer_station_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
