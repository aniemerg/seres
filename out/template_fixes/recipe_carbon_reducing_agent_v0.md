# Fix Intelligence: recipe_carbon_reducing_agent_v0

## Files

- **Recipe:** `kb/recipes/recipe_carbon_reducing_agent_v0.yaml`
- **Target item:** `carbon_reducing_agent`
  - File: `kb/items/carbon_reducing_agent.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `recipe_carbon_reducing_agent_import_v0` → carbon_reducing_agent (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'carbon_reducing_agent_production_v0') requires input 'carbon_reductant' which is not available

**Location:** Step 0
**Process:** `carbon_reducing_agent_production_v0`
  - File: `kb/processes/carbon_reducing_agent_production_v0.yaml`

**Current step:**
```yaml
- process_id: carbon_reducing_agent_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_carbon_reducing_agent_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
