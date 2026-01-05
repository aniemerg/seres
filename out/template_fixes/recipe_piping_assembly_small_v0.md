# Fix Intelligence: recipe_piping_assembly_small_v0

## Files

- **Recipe:** `kb/recipes/recipe_piping_assembly_small_v0.yaml`
- **Target item:** `piping_assembly_small_v0`
  - File: `kb/items/piping_assembly_small_v0.yaml`
- **BOM:** None
- **Steps:** 4 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_piping_assembly_small_v3` → piping_assembly_small (3 steps)
- `recipe_piping_assembly_small_v2` → piping_assembly_small (3 steps)
- `recipe_piping_assembly_small_v1` → piping_assembly_small (3 steps)

## Errors (4 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'cutting_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `cutting_basic_v0`
  - File: `kb/processes/cutting_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: cutting_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

#### Option B: Use previous step outputs

- Step 0 produces: `cut_parts` (9.5 kg)

---

### Error 3: recipe_template_missing_step_inputs

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)

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

- Step 0 produces: `cut_parts` (9.5 kg)
- Step 1 produces: `welded_assemblies` (1.0 kg)
- Step 2 produces: `machined_part_raw` (1.0 kg)

#### Option C: Pattern from `recipe_piping_assembly_small_v3`

Similar recipe uses this process (step 2) with:

```yaml
  inputs:
  - item_id: piping_and_valves_set
    qty: 6.5
    unit: kg
```

#### Option C: Pattern from `recipe_piping_assembly_small_v2`

Similar recipe uses this process (step 2) with:

```yaml
  inputs:
  - item_id: piping_and_valves_set
    qty: 6.5
    unit: kg
```

#### Option C: Pattern from `recipe_piping_assembly_small_v1`

Similar recipe uses this process (step 2) with:

```yaml
  inputs:
  - item_id: piping_and_valves_set
    qty: 6.5
    unit: kg
```

---

## Summary

- **Total errors:** 4
- **Recipe file:** `kb/recipes/recipe_piping_assembly_small_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
