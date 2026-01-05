# Fix Intelligence: recipe_volumetric_receiver_porous_v0

## Files

- **Recipe:** `kb/recipes/recipe_volumetric_receiver_porous_v0.yaml`
- **Target item:** `volumetric_receiver_porous_v0`
  - File: `kb/items/volumetric_receiver_porous_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'porous_receiver_fabrication_v0') requires input 'volumetric_receiver_porous_raw_template_v0' which is not available

**Location:** Step 0
**Process:** `porous_receiver_fabrication_v0`
  - File: `kb/processes/porous_receiver_fabrication_v0.yaml`

**Current step:**
```yaml
- process_id: porous_receiver_fabrication_v0
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

- Step 0 produces: `volumetric_receiver_porous_v0` (1.0 unit)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_volumetric_receiver_porous_v0.yaml`
- **BOM available:** No
