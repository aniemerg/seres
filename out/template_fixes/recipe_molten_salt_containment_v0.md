# Fix Intelligence: recipe_molten_salt_containment_v0

## Files

- **Recipe:** `kb/recipes/recipe_molten_salt_containment_v0.yaml`
- **Target item:** `molten_salt_containment_v0`
  - File: `kb/items/molten_salt_containment_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'ceramic_forming_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `ceramic_forming_basic_v0`
  - File: `kb/processes/ceramic_forming_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: ceramic_forming_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'ceramic_firing_high_temp_v0') requires input 'green_ceramic_part' which is not available

**Location:** Step 1
**Process:** `ceramic_firing_high_temp_v0`
  - File: `kb/processes/ceramic_firing_high_temp_v0.yaml`

**Current step:**
```yaml
- process_id: ceramic_firing_high_temp_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_molten_salt_containment_v0.yaml`
- **BOM available:** No
