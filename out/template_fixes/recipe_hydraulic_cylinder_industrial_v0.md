# Fix Intelligence: recipe_hydraulic_cylinder_industrial_v0

## Files

- **Recipe:** `kb/recipes/recipe_hydraulic_cylinder_industrial_v0.yaml`
- **Target item:** `hydraulic_cylinder_industrial`
  - File: `kb/items/hydraulic_cylinder_industrial.yaml`
- **BOM:** None
- **Steps:** 4 total

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_finish_basic_v0`
  - File: `kb/processes/machining_finish_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_finish_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'surface_grinding_precision_v0') requires input 'rough_part' which is not available

**Location:** Step 1
**Process:** `surface_grinding_precision_v0`
  - File: `kb/processes/surface_grinding_precision_v0.yaml`

**Current step:**
```yaml
- process_id: surface_grinding_precision_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'seal_installation_v0') requires input 'hydraulic_seals_set' which is not available

**Location:** Step 2
**Process:** `seal_installation_v0`
  - File: `kb/processes/seal_installation_v0.yaml`

**Current step:**
```yaml
- process_id: seal_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `finished_part_deburred` (1.0 kg)
- Step 2 produces: `sealed_component` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_hydraulic_cylinder_industrial_v0.yaml`
- **BOM available:** No
