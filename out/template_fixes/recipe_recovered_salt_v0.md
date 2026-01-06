# Fix Intelligence: recipe_recovered_salt_v0

## Files

- **Recipe:** `kb/recipes/recipe_recovered_salt_v0.yaml`
- **Target item:** `sodium_chloride`
  - File: `kb/items/sodium_chloride.yaml`
- **BOM:** None
- **Steps:** 5 total

## Errors (5 found)

### Error 1: recipe_step_input_not_satisfied

**Message:** Step 0 (process 'chloride_recycling_to_hcl_v0') requires input 'salt_waste' which is not available

**Location:** Step 0
**Process:** `chloride_recycling_to_hcl_v0`
  - File: `kb/processes/chloride_recycling_to_hcl_v0.yaml`

**Current step:**
```yaml
- process_id: chloride_recycling_to_hcl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 2: recipe_step_input_not_satisfied

**Message:** Step 1 (process 'chloride_recycling_to_hcl_v0') requires input 'salt_waste' which is not available

**Location:** Step 1
**Process:** `chloride_recycling_to_hcl_v0`
  - File: `kb/processes/chloride_recycling_to_hcl_v0.yaml`

**Current step:**
```yaml
- process_id: chloride_recycling_to_hcl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 3: recipe_step_input_not_satisfied

**Message:** Step 2 (process 'chloride_recycling_to_hcl_v0') requires input 'salt_waste' which is not available

**Location:** Step 2
**Process:** `chloride_recycling_to_hcl_v0`
  - File: `kb/processes/chloride_recycling_to_hcl_v0.yaml`

**Current step:**
```yaml
- process_id: chloride_recycling_to_hcl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 4: recipe_step_input_not_satisfied

**Message:** Step 3 (process 'chloride_recycling_to_hcl_v0') requires input 'salt_waste' which is not available

**Location:** Step 3
**Process:** `chloride_recycling_to_hcl_v0`
  - File: `kb/processes/chloride_recycling_to_hcl_v0.yaml`

**Current step:**
```yaml
- process_id: chloride_recycling_to_hcl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

### Error 5: recipe_step_input_not_satisfied

**Message:** Step 4 (process 'chloride_recycling_to_hcl_v0') requires input 'salt_waste' which is not available

**Location:** Step 4
**Process:** `chloride_recycling_to_hcl_v0`
  - File: `kb/processes/chloride_recycling_to_hcl_v0.yaml`

**Current step:**
```yaml
- process_id: chloride_recycling_to_hcl_v0
  # NO inputs field
```

**Analysis:** Step has inputs, but one or more items don't exist or aren't available.

---

## Summary

- **Total errors:** 5
- **Recipe file:** `kb/recipes/recipe_recovered_salt_v0.yaml`
- **BOM available:** No
