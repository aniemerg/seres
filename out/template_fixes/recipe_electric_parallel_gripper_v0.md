# Fix Intelligence: recipe_electric_parallel_gripper_v0

## Files

- **Recipe:** `kb/recipes/recipe_electric_parallel_gripper_v0.yaml`
- **Target item:** `electric_parallel_gripper`
  - File: `kb/items/electric_parallel_gripper.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `casting_basic_v0`
  - File: `kb/processes/casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'machining_rough_v0') requires input 'cut_parts' which is not available

**Location:** Step 1
**Process:** `machining_rough_v0`
  - File: `kb/processes/machining_rough_v0.yaml`

**Current step:**
```yaml
- process_id: machining_rough_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'steel_refining_basic_v0') requires input 'iron_pig_or_ingot' which is not available

**Location:** Step 2
**Process:** `steel_refining_basic_v0`
  - File: `kb/processes/steel_refining_basic_v0.yaml`

**Current step:**
```yaml
- process_id: steel_refining_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'machining_rough_v0') requires input 'cut_parts' which is not available

**Location:** Step 3
**Process:** `machining_rough_v0`
  - File: `kb/processes/machining_rough_v0.yaml`

**Current step:**
```yaml
- process_id: machining_rough_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_template_missing_step_inputs

**Message:** Step 4 uses template process 'alignment_and_testing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 4
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

- Step 1 produces: `rough_part` (0.95 kg)
- Step 2 produces: `steel_billet_or_slab` (1.0 kg)
- Step 2 produces: `slag` (0.05 kg)
- Step 3 produces: `rough_part` (0.95 kg)

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_electric_parallel_gripper_v0.yaml`
- **BOM available:** No
