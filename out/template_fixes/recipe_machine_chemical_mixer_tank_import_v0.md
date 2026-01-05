# Fix Intelligence: recipe_machine_chemical_mixer_tank_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_machine_chemical_mixer_tank_import_v0.yaml`
- **Target item:** `chemical_mixer_tank`
  - File: `kb/items/chemical_mixer_tank.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_machine_chemical_mixer_tank_v0` → chemical_mixer_tank (3 steps)

## Errors (2 found)

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

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_machine_chemical_mixer_tank_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
