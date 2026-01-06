# Fix Intelligence: recipe_silicon_steel_electrical_v0

## Files

- **Recipe:** `kb/recipes/recipe_silicon_steel_electrical_v0.yaml`
- **Target item:** `silicon_steel_electrical_v0`
  - File: `kb/items/silicon_steel_electrical_v0.yaml`
- **BOM:** None
- **Steps:** 3 total

## Errors (2 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'steel_ingot_cast_v0') requires input 'steel_billet_or_slab' which is not available

**Location:** Step 0
**Process:** `steel_ingot_cast_v0`
  - File: `kb/processes/steel_ingot_cast_v0.yaml`

**Current step:**
```yaml
- process_id: steel_ingot_cast_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'silicon_electrical_steel_synthesis_v0') requires input 'silicon_metal_v0' which is not available

**Location:** Step 2
**Process:** `silicon_electrical_steel_synthesis_v0`
  - File: `kb/processes/silicon_electrical_steel_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: silicon_electrical_steel_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 2
- **Recipe file:** `kb/recipes/recipe_silicon_steel_electrical_v0.yaml`
- **BOM available:** No
