# Fix Intelligence: recipe_reduced_metal_oxides_v0

## Files

- **Recipe:** `kb/recipes/recipe_reduced_metal_oxides_v0.yaml`
- **Target item:** `reduced_metal_oxides`
  - File: `kb/items/reduced_metal_oxides.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'regolith_screening_sieving_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 1
**Process:** `regolith_screening_sieving_v0`
  - File: `kb/processes/regolith_screening_sieving_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_screening_sieving_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'oxygen_extraction_carbothermal_reduction_v0') requires input 'carbon_reductant' which is not available

**Location:** Step 3
**Process:** `oxygen_extraction_carbothermal_reduction_v0`
  - File: `kb/processes/oxygen_extraction_carbothermal_reduction_v0.yaml`

**Current step:**
```yaml
- process_id: oxygen_extraction_carbothermal_reduction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `regolith_lunar_mare` (100.0 kg)
- Step 1 produces: `regolith_coarse_fraction` (0.6 kg)
- Step 1 produces: `regolith_fine_fraction` (0.4 kg)
- Step 2 produces: `regolith_powder` (28.5 kg)
- Step 3 produces: `oxygen_gas` (1.0 kg)
- Step 3 produces: `reduced_metal_oxides` (10.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_reduced_metal_oxides_v0.yaml`
- **BOM available:** No
