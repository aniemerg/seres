# Fix Intelligence: recipe_anvil_or_die_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_anvil_or_die_set_v0.yaml`
- **Target item:** `anvil_or_die_set`
  - File: `kb/items/anvil_or_die_set.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (3 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'forging_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `forging_basic_v0`
  - File: `kb/processes/forging_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: forging_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'forging_bearing_ring_blanks_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 1
**Process:** `forging_bearing_ring_blanks_v0`
  - File: `kb/processes/forging_bearing_ring_blanks_v0.yaml`

**Current step:**
```yaml
- process_id: forging_bearing_ring_blanks_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'forging_rolls_basic_v0') requires input 'steel_stock_bar_or_billet' which is not available

**Location:** Step 2
**Process:** `forging_rolls_basic_v0`
  - File: `kb/processes/forging_rolls_basic_v0.yaml`

**Current step:**
```yaml
- process_id: forging_rolls_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_anvil_or_die_set_v0.yaml`
- **BOM available:** No
