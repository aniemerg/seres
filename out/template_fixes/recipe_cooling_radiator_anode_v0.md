# Fix Intelligence: recipe_cooling_radiator_anode_v0

## Files

- **Recipe:** `kb/recipes/recipe_cooling_radiator_anode_v0.yaml`
- **Target item:** `cooling_radiator_anode`
  - File: `kb/items/cooling_radiator_anode.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'cooling_radiator_anode_production_v0') requires input 'iron_pig_or_ingot' which is not available

**Location:** Step 0
**Process:** `cooling_radiator_anode_production_v0`
  - File: `kb/processes/cooling_radiator_anode_production_v0.yaml`

**Current step:**
```yaml
- process_id: cooling_radiator_anode_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_cooling_radiator_anode_v0.yaml`
- **BOM available:** No
