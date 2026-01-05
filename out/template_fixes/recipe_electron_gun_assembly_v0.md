# Fix Intelligence: recipe_electron_gun_assembly_v0

## Files

- **Recipe:** `kb/recipes/recipe_electron_gun_assembly_v0.yaml`
- **Target item:** `electron_gun_assembly`
  - File: `kb/items/electron_gun_assembly.yaml`
- **BOM:** None
- **Steps:** 3 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_electron_gun_assembly_v0_alt` → electron_gun_assembly_v0 (3 steps)

## Errors (3 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'vacuum_tube_assembly_v0') requires input 'tungsten_cathode_coated' which is not available

**Location:** Step 1
**Process:** `vacuum_tube_assembly_v0`
  - File: `kb/processes/vacuum_tube_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: vacuum_tube_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_template_missing_step_inputs

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

- Step 0 produces: `assembled_electronics` (1.0 unit)
- Step 1 produces: `thermionic_vacuum_tube` (1.0 unit)

---

## Summary

- **Total errors:** 3
- **Recipe file:** `kb/recipes/recipe_electron_gun_assembly_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
