# Fix Intelligence: recipe_cable_ties_and_sleeving_v0

## Files

- **Recipe:** `kb/recipes/recipe_cable_ties_and_sleeving_v0.yaml`
- **Target item:** `cable_ties_and_sleeving`
  - File: `kb/items/cable_ties_and_sleeving.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'plastic_extrusion_v0') requires input 'plastic_pellets' which is not available

**Location:** Step 0
**Process:** `plastic_extrusion_v0`
  - File: `kb/processes/plastic_extrusion_v0.yaml`

**Current step:**
```yaml
- process_id: plastic_extrusion_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'molding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `molding_basic_v0`
  - File: `kb/processes/molding_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: molding_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `extruded_plastic_profile` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `extruded_plastic_profile` (1.0 kg)
- Step 1 produces: `plastic_housing_molded` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'inspection_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `extruded_plastic_profile` (1.0 kg)
- Step 1 produces: `plastic_housing_molded` (1.0 kg)
- Step 2 produces: `cut_parts` (9.5 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_cable_ties_and_sleeving_v0.yaml`
- **BOM available:** No
