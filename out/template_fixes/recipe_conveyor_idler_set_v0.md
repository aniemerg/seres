# Fix Intelligence: recipe_conveyor_idler_set_v0

## Files

- **Recipe:** `kb/recipes/recipe_conveyor_idler_set_v0.yaml`
- **Target item:** `conveyor_idler_set`
  - File: `kb/items/conveyor_idler_set.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 2 recipes producing similar items:

- `recipe_conveyor_idler_set_v1` → conveyor_idler_set (4 steps)
- `recipe_conveyor_idler_set_v2` → conveyor_idler_set (4 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welded_fabrication_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welded_fabrication_basic_v0`
  - File: `kb/processes/welded_fabrication_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welded_fabrication_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

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

- Step 0 produces: `welded_fabrications` (1.0 kg)

---

### Error 3: recipe_template_missing_step_inputs

**Message:** Step 2 uses template process 'bearing_installation_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 2
**Process:** `bearing_installation_basic_v0`
  - File: `kb/processes/bearing_installation_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: bearing_installation_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `welded_fabrications` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)

---

### Error 4: recipe_template_missing_step_inputs

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

- Step 0 produces: `welded_fabrications` (1.0 kg)
- Step 1 produces: `machined_part_raw` (1.0 kg)
- Step 2 produces: `finished_part` (2.0 kg)

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_conveyor_idler_set_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 2 found
