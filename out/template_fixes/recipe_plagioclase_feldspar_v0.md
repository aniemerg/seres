# Fix Intelligence: recipe_plagioclase_feldspar_v0

## Files

- **Recipe:** `kb/recipes/recipe_plagioclase_feldspar_v0.yaml`
- **Target item:** `plagioclase_feldspar`
  - File: `kb/items/plagioclase_feldspar.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'beneficiation_magnetic_basic_v0') requires input 'regolith_powder' which is not available

**Location:** Step 0
**Process:** `beneficiation_magnetic_basic_v0`
  - File: `kb/processes/beneficiation_magnetic_basic_v0.yaml`

**Current step:**
```yaml
- process_id: beneficiation_magnetic_basic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'regolith_screening_sieving_v0') requires input 'regolith_lunar_mare' which is not available

**Location:** Step 1
**Process:** `regolith_screening_sieving_v0`
  - File: `kb/processes/regolith_screening_sieving_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_screening_sieving_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_plagioclase_feldspar_v0.yaml`
- **BOM available:** No
