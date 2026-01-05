# Fix Intelligence: recipe_sulfuric_acid_concentrated_v0

## Files

- **Recipe:** `kb/recipes/recipe_sulfuric_acid_concentrated_v0.yaml`
- **Target item:** `sulfuric_acid_concentrated`
  - File: `kb/items/sulfuric_acid_concentrated.yaml`
- **BOM:** None
- **Steps:** 1 total

## Errors (1 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'sulfuric_acid_contact_process_v0') requires input 'sulfur_dioxide_gas' which is not available

**Location:** Step 0
**Process:** `sulfuric_acid_contact_process_v0`
  - File: `kb/processes/sulfuric_acid_contact_process_v0.yaml`

**Current step:**
```yaml
- process_id: sulfuric_acid_contact_process_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 1
- **Recipe file:** `kb/recipes/recipe_sulfuric_acid_concentrated_v0.yaml`
- **BOM available:** No
