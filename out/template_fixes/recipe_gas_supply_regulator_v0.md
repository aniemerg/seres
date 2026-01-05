# Fix Intelligence: recipe_gas_supply_regulator_v0

## Files

- **Recipe:** `kb/recipes/recipe_gas_supply_regulator_v0.yaml`
- **Target item:** `gas_supply_regulator`
  - File: `kb/items/gas_supply_regulator.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_gas_supply_regulator_import_v0` → gas_supply_regulator (4 steps)

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'machining_finish_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 1 produces: `cast_metal_parts` (0.95 kg)

---

### Error 3: recipe_template_missing_step_inputs

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

- Step 1 produces: `cast_metal_parts` (0.95 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_gas_supply_regulator_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
