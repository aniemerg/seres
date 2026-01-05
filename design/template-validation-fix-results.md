# Template Validation Fix - Actual Scope Discovery

**Date:** 2026-01-04
**Issue:** Validation was incorrectly skipping template process inputs entirely
**Fix:** Now validates step-level inputs for template processes and errors if missing

---

## The Bug

### Original (WRONG) Implementation

```python
# Skip template processes (inputs defined in recipe)
if process_dict.get("is_template"):
    continue  # ← BUG: Skips ALL validation!
```

**What this did:**
- Template processes: NO validation at all (skipped entirely)
- Recipe could use template without step inputs → NO ERROR
- Recipe could use template with invalid step inputs → NO ERROR

**Result:** Hid 3,093 real errors

---

### Fixed (CORRECT) Implementation

```python
# Template processes MUST have step-level input overrides
if process_dict.get("is_template"):
    if not step_inputs:
        ERROR: "Template process must have step-level input overrides"
        continue
    # Validate the step-level inputs
    required_inputs = step_inputs
# ... then validate required_inputs are available ...
```

**What this does:**
- Template + no step inputs → **ERROR** (recipe incomplete)
- Template + has step inputs → **VALIDATE** those step inputs
- Non-template → Normal validation

**Result:** Catches errors at validation time, not simulation time

---

## Impact: The Real Scope

### Error Count Change

| State | Errors | Change |
|-------|--------|--------|
| **Before fix (hiding errors)** | 1,516 | - |
| **After fix (correct)** | 4,609 | +3,093 (204% increase!) |

### Error Breakdown

| Rule | Count | Description |
|------|-------|-------------|
| `recipe_template_missing_step_inputs` | 2,954 | Template used without step-level overrides |
| `recipe_step_input_not_satisfied` | 1,653 | Step inputs reference unavailable items |
| `scaling_basis_not_found` | 2 | Minor issue |

---

## Analysis of 2,954 Missing Step Input Errors

### What These Are

Recipes using template processes WITHOUT providing step-level input overrides.

**Example:**
```yaml
id: recipe_some_product_v0
steps:
- process_id: drying_basic_v0  # Template with placeholder input 'wet_material'
  # NO inputs: field - falls back to process input
```

**At simulation:** Would fail trying to find item `wet_material` (doesn't exist)

**Now at validation:** ❌ ERROR - "Step uses template process but doesn't provide step-level input overrides"

### Top Template Processes Used Without Overrides

```bash
$ cat out/validation_issues.jsonl | jq -r 'select(.rule == "recipe_template_missing_step_inputs") | .message' | \
  sed "s/.*process '\([^']*\)'.*/\1/" | sort | uniq -c | sort -rn | head -10
```

Expecting to see:
- `drying_basic_v0` (~XXX errors)
- `metal_casting_basic_v0` (~XXX errors)
- `machining_finish_basic_v0` (~XXX errors)
- `assembly_basic_v0` (~XXX errors)
- etc.

---

## Analysis of 1,653 Step Input Not Satisfied Errors

### What Changed

| Type | Before Fix | After Fix | New Errors |
|------|------------|-----------|------------|
| Non-template inputs missing | 1,516 | 1,516 | 0 |
| Template step inputs invalid | 0 (hidden) | 137 | +137 |
| **Total** | **1,516** | **1,653** | **+137** |

### New 137 Errors: Template Steps with Invalid Inputs

Recipes that DO provide step-level overrides for templates, but use **generic/placeholder** item IDs.

**Example:**
```yaml
steps:
- process_id: assembly_basic_v0  # Template
  inputs:  # ← Has step inputs (good!)
  - item_id: steel_plate_or_sheet  # ← But uses generic "or" pattern (bad!)
    qty: 0.2
```

**Problem:** `steel_plate_or_sheet` is not a real item - it's another placeholder!

**Now caught at validation:** ❌ ERROR - "requires input 'steel_plate_or_sheet' which is not available"

### Top Invalid Generic Inputs in Step Overrides

```bash
$ cat out/validation_issues.jsonl | jq -r 'select(.rule == "recipe_step_input_not_satisfied" and (.message | contains("_or_"))) | .message' | \
  sed "s/.*input '\([^']*\)'.*/\1/" | sort | uniq -c | sort -rn
```

Expected patterns:
- `steel_plate_or_sheet`
- `powder_metal_or_ceramic`
- `steel_billet_or_slab`
- `bulk_material_or_parts`

---

## What This Means

### The Good News

1. **Validation is now correct** - catches errors early instead of hiding them
2. **True scope revealed** - we know the real extent of recipe issues
3. **Work queue will help** - 4,609 errors → 4,609 work items for fixing

### The Bad News

1. **Many recipes are incomplete** - 2,954 template uses without overrides
2. **Many overrides are also generic** - 137 use placeholders instead of real items
3. **Phases 2-2c didn't "fix" errors** - just revealed them through better validation

### The Reality

**The original 4,262 errors were REAL.** Marking processes as templates was necessary to:
1. Distinguish generic processes from concrete ones
2. Enable correct validation logic

But the errors didn't go away - they were just miscategorized:
- **Before:** 4,262 errors (mostly false positives due to wrong validation logic)
- **After template marking + wrong skip logic:** 1,516 errors (hiding real issues)
- **After template marking + correct validation:** 4,609 errors (TRUE count)

---

## What Needs to Happen Now

### Option 1: Fix Recipes Manually

**Scope:** 4,609 recipes need fixes

**Types of fixes:**
1. **2,954 missing step inputs** - Add `inputs:` field to template steps
2. **137 generic step inputs** - Replace `steel_plate_or_sheet` with `steel_plate_1mm` (specific item)
3. **1,516 other missing inputs** - Add to recipe inputs, BOM, or previous steps

**Effort:** Enormous - manual review of ~2,400 recipes (some have multiple errors)

**Feasibility:** Low for one person, need tooling or multiple contributors

---

### Option 2: Auto-Infer Step Inputs from BOM (Issue #3 Extension)

**Current behavior (Issue #3 fix):**
- Recipe-level inputs can be inferred from BOM
- ADR-019: BOM components available to all steps

**Proposed extension:**
- Step-level inputs for templates ALSO inferred from BOM
- If template has no step inputs, check BOM for compatible items

**Example:**
```yaml
# BOM
id: bom_my_product_v0
components:
- item_id: steel_plate_1mm  # Specific item
  qty: 5.0

# Recipe
id: recipe_my_product_v0
target_item_id: my_product_v0
steps:
- process_id: assembly_basic_v0  # Template
  # NO inputs - infer from BOM
```

**Auto-inference logic:**
```python
if template and not step_inputs and bom_exists:
    # Try to match BOM components to template's placeholder inputs
    # If template needs "assembly_components", use ALL BOM components
    step_inputs = bom.components
```

**Pros:**
- Could auto-fix many of the 2,954 missing step input errors
- Leverages existing BOM infrastructure
- Consistent with ADR-019 philosophy

**Cons:**
- May not always pick the RIGHT items from BOM
- Hides recipe author intent
- Template inputs might need subset of BOM, not all

**Estimated impact:** Could fix 1,500-2,500 of the 2,954 missing step input errors

---

### Option 3: Provide Tooling to Suggest Fixes

**Script:** `scripts/suggest_template_step_inputs.py`

**Functionality:**
1. For each template error, find recipe's BOM
2. Suggest BOM components as step inputs
3. Generate YAML patch or interactive fix

**Example output:**
```bash
$ python scripts/suggest_template_step_inputs.py recipe_my_product_v0

Recipe: recipe_my_product_v0
Step 0: assembly_basic_v0 (template) - missing step inputs

Suggested fix (from BOM):
  inputs:
  - item_id: steel_plate_1mm
    qty: 5.0
    unit: kg
  - item_id: fastener_kit_small
    qty: 1.0
    unit: unit

Apply? [y/n/edit]:
```

**Pros:**
- Semi-automated (human validates suggestions)
- Learns from BOM (likely correct)
- Can be batched across many recipes

**Cons:**
- Still requires human review
- Might suggest wrong items
- Effort to build tooling

**Estimated impact:** Could help fix 2,000-3,000 errors with human approval

---

### Option 4: Mark More Processes as Templates (Phase 2d+)

**Rationale:** Some of the 1,653 "step input not satisfied" errors might be from processes that SHOULD be templates.

**Example:**
- `sheet_metal_fabrication_v0` uses `sheet_metal_or_structural_steel` (generic "or" pattern)
- Currently NOT a template
- 65+ errors
- **Should be template** - then recipes must override

**Process:**
1. Identify processes using generic "or" patterns that aren't templates
2. Mark them as templates
3. Errors move from "step_input_not_satisfied" to "template_missing_step_inputs"
4. Same number of errors, but clearer categorization

**Estimated impact:** Recategorize ~150 errors, no reduction

---

## Recommendation

**Immediate:** Accept the 4,609 error count as the TRUE state

**Short-term (1-2 days):**
1. **Phase 2d:** Mark remaining "or" pattern processes as templates (~5 processes)
2. **Extend ADR-019 auto-inference:** Allow BOM to satisfy template step inputs (code change)
3. **Re-run indexer:** See how many errors auto-inference fixes

**Expected after auto-inference:** 4,609 → ~2,000-2,500 errors

**Medium-term (1 week):**
1. **Build suggestion tool:** `suggest_template_step_inputs.py`
2. **Semi-automated fixing:** Human-approved batch fixes
3. **Documentation:** Recipe authoring guide

**Expected after tool-assisted fixes:** ~2,500 → ~500-1,000 errors

**Long-term:**
1. **Manual recipe fixes:** Remaining legitimate errors
2. **Recipe quality guidelines:** Prevent future errors
3. **CI validation:** Block new recipes with template errors

---

## Lessons Learned

### 1. Question Everything

User correctly questioned: "Doesn't this just require recipes to be very good?"

Answer revealed: **My implementation was hiding errors entirely** instead of validating correctly.

### 2. Validation vs. Hiding

**Wrong approach:** Skip validation for templates (hides 3,093 errors)
**Right approach:** Require and validate step inputs for templates (catches 3,093 errors)

### 3. Error Reduction Can Be Misleading

**Phases 2-2c claimed:** 64.4% error reduction (4,262 → 1,516)
**Reality:** We just hid errors by skipping validation
**Actual reduction:** 0% (errors still exist, just not detected)

### 4. Test What Matters

Test `test_template_process_skipped` was too weak - just checked "doesn't crash"
Should have checked: "template without step inputs generates error"

---

## Current Status

| Metric | Value |
|--------|-------|
| **Total validation errors** | 4,609 |
| **Template missing step inputs** | 2,954 (64%) |
| **Step inputs not satisfied** | 1,653 (36%) |
| **Templates in KB** | 92 (11% of processes) |
| **Recipes affected** | ~2,400 (est. 50% of 1,929 recipes) |

**Validation is now CORRECT but reveals scope of recipe quality issues.**

---

## Files Modified

- `src/kb_core/validators.py` - Fixed template validation logic (lines 1130-1157)
- `out/validation_issues.jsonl` - Now contains 4,609 errors (was 1,516)
- `out/work_queue.jsonl` - Now contains 4,609 work items (was 1,516)

---

## Next Steps (User Decision Required)

**Question for user:** How do you want to proceed?

**Options:**
1. **Accept current state** - 4,609 errors is the truth, work on fixes gradually
2. **Implement BOM auto-inference** - Could reduce to ~2,000-2,500 errors automatically
3. **Build suggestion tooling** - Semi-automated fixes with human approval
4. **Revert template validation fix** - Go back to hiding errors (NOT recommended)
5. **Different approach** - User has alternative idea

**My recommendation:** Option 2 (BOM auto-inference) for quick automated reduction, then Option 3 (tooling) for remaining errors.
