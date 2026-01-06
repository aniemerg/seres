# Fix Intelligence: recipe_helium_mixed_isotopes_v0

## Files

- **Recipe:** `kb/recipes/recipe_helium_mixed_isotopes_v0.yaml`
- **Target item:** `helium_mixed_isotopes`
  - File: `kb/items/helium_mixed_isotopes.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'regolith_volatile_thermal_extraction_v0') requires input 'regolith_lunar_highlands' which is not available

**Location:** Step 0
**Process:** `regolith_volatile_thermal_extraction_v0`
  - File: `kb/processes/regolith_volatile_thermal_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_volatile_thermal_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'cold_trap_cryogenic_v0') requires input 'oxygen_gas' which is not available

**Location:** Step 1
**Process:** `cold_trap_cryogenic_v0`
  - File: `kb/processes/cold_trap_cryogenic_v0.yaml`

**Current step:**
```yaml
- process_id: cold_trap_cryogenic_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_helium_mixed_isotopes_v0.yaml`
- **BOM available:** No
