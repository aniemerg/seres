# Fix Intelligence: salt_contingency_nacl_import_v0

## Files

- **Recipe:** `kb/recipes/salt_contingency_nacl_import_v0.yaml`
- **Target item:** `salt_contingency_nacl`
  - File: `kb/items/salt_contingency_nacl.yaml`
- **BOM:** None
- **Steps:** 1 total

## Similar Recipes

Found 1 recipes producing similar items:

- `salt_contingency_nacl_v0` → salt_contingency_nacl (1 steps)

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'naoh_hcl_salt_synthesis_v0') requires input 'sodium_hydroxide' which is not available

**Location:** Step 0
**Process:** `naoh_hcl_salt_synthesis_v0`
  - File: `kb/processes/naoh_hcl_salt_synthesis_v0.yaml`

**Current step:**
```yaml
- process_id: naoh_hcl_salt_synthesis_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/salt_contingency_nacl_import_v0.yaml`
- **BOM available:** No
- **Similar recipes:** 1 found
