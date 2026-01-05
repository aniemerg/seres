# Fix Intelligence: recipe_sintering_aid_mgo_v0

## Files

- **Recipe:** `kb/recipes/recipe_sintering_aid_mgo_v0.yaml`
- **Target item:** `sintering_aid_mgo`
  - File: `kb/items/sintering_aid_mgo.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sintering_aid_mgo_production_v0') requires input 'magnesium_oxide' which is not available

**Location:** Step 0
**Process:** `sintering_aid_mgo_production_v0`
  - File: `kb/processes/sintering_aid_mgo_production_v0.yaml`

**Current step:**
```yaml
- process_id: sintering_aid_mgo_production_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sintering_aid_mgo_v0.yaml`
- **BOM available:** No
