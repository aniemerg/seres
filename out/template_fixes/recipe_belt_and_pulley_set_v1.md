# Fix Intelligence: recipe_belt_and_pulley_set_v1

## Files

- **Recipe:** `kb/recipes/recipe_belt_and_pulley_set_v1.yaml`
- **Target item:** `belt_and_pulley_set`
  - File: `kb/items/belt_and_pulley_set.yaml`
- **BOM:** None
- **Steps:** 5 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_belt_and_pulley_set_v0` → belt_and_pulley_set (8 steps)

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'machining_precision_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `machining_precision_v0`
  - File: `kb/processes/machining_precision_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: machining_precision_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'molding_rubber_or_plastic_v0') requires input 'silicone_rubber' which is not available

**Location:** Step 1
**Process:** `molding_rubber_or_plastic_v0`
  - File: `kb/processes/molding_rubber_or_plastic_v0.yaml`

**Current step:**
```yaml
- process_id: molding_rubber_or_plastic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'balancing_dynamic_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `balancing_dynamic_basic_v0`
  - File: `kb/processes/balancing_dynamic_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: balancing_dynamic_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `molded_rubber_or_plastic_piece_v0` (1.0 unit)

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

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `molded_rubber_or_plastic_piece_v0` (1.0 unit)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

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

- Step 0 produces: `machined_steel_part_precision` (7.0 kg)
- Step 1 produces: `molded_rubber_or_plastic_piece_v0` (1.0 unit)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_belt_and_pulley_set_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
