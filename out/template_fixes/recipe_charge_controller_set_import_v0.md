# Fix Intelligence: recipe_charge_controller_set_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_charge_controller_set_import_v0.yaml`
- **Target item:** `charge_controller_set`
  - File: `kb/items/charge_controller_set.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_charge_controller_set_v0` → charge_controller_set (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'electrical_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `electrical_assembly_basic_v0`
  - File: `kb/processes/electrical_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: electrical_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'pcb_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `pcb_assembly_basic_v0`
  - File: `kb/processes/pcb_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: pcb_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'enclosure_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `enclosure_assembly_basic_v0`
  - File: `kb/processes/enclosure_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: enclosure_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 4: recipe_template_missing_step_inputs

**Message:** Step 3 uses template process 'sealing_and_assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 3
**Process:** `sealing_and_assembly_basic_v0`
  - File: `kb/processes/sealing_and_assembly_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: sealing_and_assembly_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 2 produces: `enclosure_electrical_medium` (1.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_charge_controller_set_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
