# Fix Intelligence: recipe_enclosure_small_additive_v0

## Files

- **Recipe:** `kb/recipes/recipe_enclosure_small_additive_v0.yaml`
- **Target item:** `enclosure_small`
  - File: `kb/items/enclosure_small.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_enclosure_small_v0` → enclosure_small (5 steps)

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'additive_manufacturing_polymer_v0') requires input 'polymer_printing_feedstock' which is not available

**Location:** Step 0
**Process:** `additive_manufacturing_polymer_v0`
  - File: `kb/processes/additive_manufacturing_polymer_v0.yaml`

**Current step:**
```yaml
- process_id: additive_manufacturing_polymer_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
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

- Step 0 produces: `polymer_printed_part` (0.9 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_enclosure_small_additive_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
