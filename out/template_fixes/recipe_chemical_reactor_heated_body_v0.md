# Fix Intelligence: recipe_chemical_reactor_heated_body_v0

## Files

- **Recipe:** `kb/recipes/recipe_chemical_reactor_heated_body_v0.yaml`
- **Target item:** `chemical_reactor_heated_body`
  - File: `kb/items/chemical_reactor_heated_body.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'metal_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `metal_forming_basic_v0`
  - File: `kb/processes/metal_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

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

- Step 0 produces: `formed_metal_part` (0.95 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'regolith_based_thermal_insulation_v0') requires input 'regolith_powder' which is not available

**Location:** Step 3
**Process:** `regolith_based_thermal_insulation_v0`
  - File: `kb/processes/regolith_based_thermal_insulation_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_based_thermal_insulation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 0 produces: `formed_metal_part` (0.95 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 3 produces: `thermal_insulation_regolith_based_v0` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_chemical_reactor_heated_body_v0.yaml`
- **BOM available:** No
