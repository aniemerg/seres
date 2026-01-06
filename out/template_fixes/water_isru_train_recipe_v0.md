# Fix Intelligence: water_isru_train_recipe_v0

## Files

- **Recipe:** `kb/recipes/water_isru_train_recipe_v0.yaml`
- **Target item:** `water_isru_train_v0`
  - File: `kb/items/water_isru_train_v0.yaml`
- **BOM:** None
- **Steps:** 2 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'regolith_heating_water_extraction_v0') requires input 'regolith_carbonaceous' which is not available

**Location:** Step 0
**Process:** `regolith_heating_water_extraction_v0`
  - File: `kb/processes/regolith_heating_water_extraction_v0.yaml`

**Current step:**
```yaml
- process_id: regolith_heating_water_extraction_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'chemical_purification_v0') requires input 'concentrated_mineral' which is not available

**Location:** Step 1
**Process:** `chemical_purification_v0`
  - File: `kb/processes/chemical_purification_v0.yaml`

**Current step:**
```yaml
- process_id: chemical_purification_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/water_isru_train_recipe_v0.yaml`
- **BOM available:** No
