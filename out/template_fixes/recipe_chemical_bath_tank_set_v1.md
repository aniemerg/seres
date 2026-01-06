# Fix Intelligence: recipe_chemical_bath_tank_set_v1

## Files

- **Recipe:** `kb/recipes/recipe_chemical_bath_tank_set_v1.yaml`
- **Target item:** `chemical_bath_tank_set`
  - File: `kb/items/chemical_bath_tank_set.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_chemical_bath_tank_set_v0` → chemical_bath_tank_set (2 steps)

## Errors (2 found)

### Error 1: recipe_template_missing_step_inputs

**Message:** Step 0 uses template process 'welding_brazing_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 0
**Process:** `welding_brazing_basic_v0`
  - File: `kb/processes/welding_brazing_basic_v0.yaml`

**Process type:** TEMPLATE (requires step-level inputs)

**Current step:**
```yaml
- process_id: welding_brazing_basic_v0
  # NO inputs field
```

**Analysis:** Template process used without step-level input overrides.

---

### Error 2: recipe_template_missing_step_inputs

**Message:** Step 1 uses template process 'assembly_basic_v0' but doesn't provide step-level input overrides

**Location:** Step 1
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

- Step 0 produces: `welded_assemblies` (1.0 kg)

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_chemical_bath_tank_set_v1.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
