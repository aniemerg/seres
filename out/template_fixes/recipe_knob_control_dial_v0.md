# Fix Intelligence: recipe_knob_control_dial_v0

## Files

- **Recipe:** `kb/recipes/recipe_knob_control_dial_v0.yaml`
- **Target item:** `knob_control_dial_v0`
  - File: `kb/items/knob_control_dial_v0.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_knob_control_dial_v1` → knob_control_dial (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'knob_control_dial_machining_v0') requires input 'extruded_plastic_profile' which is not available

**Location:** Step 0
**Process:** `knob_control_dial_machining_v0`
  - File: `kb/processes/knob_control_dial_machining_v0.yaml`

**Current step:**
```yaml
- process_id: knob_control_dial_machining_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_knob_control_dial_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
