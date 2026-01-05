# Fix Intelligence: recipe_surface_treatment_station_import_v0

## Files

- **Recipe:** `kb/recipes/recipe_surface_treatment_station_import_v0.yaml`
- **Target item:** `surface_treatment_station`
  - File: `kb/items/surface_treatment_station.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 3 recipes producing similar items:

- `recipe_surface_treatment_station_unversioned_v0` → surface_treatment_station (1 steps)
- `recipe_machine_surface_treatment_station_import_v0` → surface_treatment_station_v0 (1 steps)
- `recipe_surface_treatment_station_base_v0` → surface_treatment_station (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'surface_treatment_station_assembly_v0') requires input 'chemical_bath_tank_set' which is not available

**Location:** Step 0
**Process:** `surface_treatment_station_assembly_v0`
  - File: `kb/processes/surface_treatment_station_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: surface_treatment_station_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_surface_treatment_station_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 3 found
