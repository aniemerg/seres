# Fix Intelligence: recipe_heating_jacket_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_heating_jacket_assembly_v0.yaml`
- **Target item:** `heating_jacket_assembly`
  - File: `kb/items/heating_jacket_assembly.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'metal_fabrication_welding_v0') requires input 'sheet_metal_or_structural_steel' which is not available

**Location:** Step 0
**Process:** `metal_fabrication_welding_v0`
  - File: `kb/processes/metal_fabrication_welding_v0.yaml`

**Current step:**
```yaml
- process_id: metal_fabrication_welding_v0
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

- Step 0 produces: `welded_fabrications` (9.5 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_heating_jacket_assembly_v0.yaml`
- **BOM available:** No
