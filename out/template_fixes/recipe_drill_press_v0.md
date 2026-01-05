# Fix Intelligence: recipe_drill_press_v0

## Files

- **Recipe:** `kb/recipes/recipe_drill_press_v0.yaml`
- **Target item:** `drill_press`
  - File: `kb/items/drill_press.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_machine_drill_press_v0` → drill_press_v0 (5 steps)
- `recipe_drill_press_v1` → drill_press (4 steps)

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

- Step 0 produces: `machined_part_raw` (1.0 kg)

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'belt_installation_and_tensioning_v0') requires input 'belt_and_pulley_set' which is not available

**Location:** Step 2
**Process:** `belt_installation_and_tensioning_v0`
  - File: `kb/processes/belt_installation_and_tensioning_v0.yaml`

**Current step:**
```yaml
- process_id: belt_installation_and_tensioning_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
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

- Step 0 produces: `machined_part_raw` (1.0 kg)
- Step 1 produces: `assembled_equipment` (1.0 kg)
- Step 2 produces: `installed_belt_drive` (1.0 unit)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_drill_press_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
