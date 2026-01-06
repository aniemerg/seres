# Fix Intelligence: recipe_pitch_residue_v0

## Files

- **Recipe:** `kb/recipes/recipe_pitch_residue_v0.yaml`
- **Target item:** `pitch_residue`
  - File: `kb/items/pitch_residue.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbon_anode_forming_v0') requires input 'carbon_anode_material' which is not available

**Location:** Step 0
**Process:** `carbon_anode_forming_v0`
  - File: `kb/processes/carbon_anode_forming_v0.yaml`

**Current step:**
```yaml
- process_id: carbon_anode_forming_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_pitch_residue_v0.yaml`
- **BOM available:** No
