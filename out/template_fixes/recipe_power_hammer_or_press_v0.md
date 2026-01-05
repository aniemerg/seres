# Fix Intelligence: recipe_power_hammer_or_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_power_hammer_or_press_v0.yaml`
- **Target item:** `power_hammer_or_press`
  - File: `kb/items/power_hammer_or_press.yaml`
- **BOM:** None
- **Steps:** 6 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_machine_power_hammer_or_press_v0` → power_hammer_or_press_v0 (3 steps)

## Errors (6 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sand_casting_large_v0') requires input 'molten_material_or_preform' which is not available

**Location:** Step 0
**Process:** `sand_casting_large_v0`
  - File: `kb/processes/sand_casting_large_v0.yaml`

**Current step:**
```yaml
- process_id: sand_casting_large_v0
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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'heat_treat_basic_v0') requires input 'machined_part_raw' which is not available

**Location:** Step 2
**Process:** `heat_treat_basic_v0`
  - File: `kb/processes/heat_treat_basic_v0.yaml`

**Current step:**
```yaml
- process_id: heat_treat_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'welding_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

### Error 5: recipe_template_missing_step_inputs

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

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `welded_assemblies` (1.0 kg)

---

### Error 6: recipe_template_missing_step_inputs

**Message:** Step 5 uses template process 'integration_test_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 5
**Process:** `integration_test_basic_v0`
  - File: `kb/processes/integration_test_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: integration_test_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `sand_casting_large_v0` (45.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)
- Step 3 produces: `welded_assemblies` (1.0 kg)
- Step 4 produces: `assembled_equipment` (1.0 kg)

---

## Summary

- **Total errors:** 6
- **Recipe file:** `kb/recipes/recipe_power_hammer_or_press_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
