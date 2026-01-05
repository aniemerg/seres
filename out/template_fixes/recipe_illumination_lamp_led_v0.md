# Fix Intelligence: recipe_illumination_lamp_led_v0

## Files

- **Recipe:** `kb/recipes/recipe_illumination_lamp_led_v0.yaml`
- **Target item:** `illumination_lamp_led`
  - File: `kb/items/illumination_lamp_led.yaml`
- **BOM:** None
- **Steps:** 2 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_illumination_lamp_led_import_v0` → illumination_lamp_led (2 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'electronics_assembly_v0') requires input 'pcb_populated' which is not available

**Location:** Step 0
**Process:** `electronics_assembly_v0`
  - File: `kb/processes/electronics_assembly_v0.yaml`

**Current step:**
```yaml
- process_id: electronics_assembly_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_illumination_lamp_led_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
