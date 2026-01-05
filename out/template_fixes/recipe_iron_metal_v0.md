# Fix Intelligence: recipe_iron_metal_v0

## Files

- **Recipe:** `kb/recipes/recipe_iron_metal_v0.yaml`
- **Target item:** `iron_metal`
  - File: `kb/items/iron_metal.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sizing_grinding_basic_v0') requires input 'coarse_powder' which is not available

**Location:** Step 0
**Process:** `sizing_grinding_basic_v0`
  - File: `kb/processes/sizing_grinding_basic_v0.yaml`

**Current step:**
```yaml
- process_id: sizing_grinding_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'iron_smelting_reduction_v0') requires input 'iron_ore_or_ilmenite' which is not available

**Location:** Step 1
**Process:** `iron_smelting_reduction_v0`
  - File: `kb/processes/iron_smelting_reduction_v0.yaml`

**Current step:**
```yaml
- process_id: iron_smelting_reduction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'metal_casting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `metal_casting_basic_v0`
  - File: `kb/processes/metal_casting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: metal_casting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `fine_powder` (1.0 kg)
- Step 1 produces: `iron_pig_or_ingot` (1.0 kg)
- Step 1 produces: `slag` (0.8 kg)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_iron_metal_v0.yaml`
- **BOM available:** No
