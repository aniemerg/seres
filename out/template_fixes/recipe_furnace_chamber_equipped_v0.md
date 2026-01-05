# Fix Intelligence: recipe_furnace_chamber_equipped_v0

## Files

- **Recipe:** `kb/recipes/recipe_furnace_chamber_equipped_v0.yaml`
- **Target item:** `furnace_chamber_equipped`
  - File: `kb/items/furnace_chamber_equipped.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'heating_element_installation_v0') requires input 'heating_element_resistive' which is not available

**Location:** Step 0
**Process:** `heating_element_installation_v0`
  - File: `kb/processes/heating_element_installation_v0.yaml`

**Current step:**
```yaml
- process_id: heating_element_installation_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_furnace_chamber_equipped_v0.yaml`
- **BOM available:** No
