# Fix Intelligence: recipe_strain_gauge_bonding_station_v0

## Files

- **Recipe:** `kb/recipes/recipe_strain_gauge_bonding_station_v0.yaml`
- **Target item:** `strain_gauge_bonding_station_v0`
  - File: `kb/items/strain_gauge_bonding_station_v0.yaml`
- **BOM:** `kb/boms/bom_strain_gauge_bonding_station_v0.yaml` ✓
  - Components: 2
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'build_strain_gauge_bonding_station_v0') requires input 'assembly_components' which is not available

**Location:** Step 0
**Process:** `build_strain_gauge_bonding_station_v0`
  - File: `kb/processes/build_strain_gauge_bonding_station_v0.yaml`

**Current step:**
```yaml
- process_id: build_strain_gauge_bonding_station_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_strain_gauge_bonding_station_v0.yaml`
- **BOM available:** Yes (2 components)
