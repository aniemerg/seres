# Template Fix Suggestion Tool Design

**Purpose:** Semi-automated tool to help fix 4,609 template-related validation errors with intelligent suggestions and human/agent review.

**Target Users:** Human developers OR AI agents tasked with fixing recipe errors

---

## Problem Statement

### Error Types to Fix

| Error Type | Count | Description |
|------------|-------|-------------|
| `recipe_template_missing_step_inputs` | 2,954 | Template process used without step-level input overrides |
| `recipe_step_input_not_satisfied` (generic) | ~137 | Step inputs use generic placeholders (`steel_plate_or_sheet`) |
| `recipe_step_input_not_satisfied` (other) | ~1,516 | Step inputs reference items that don't exist |

**Total:** 4,609 errors affecting ~2,400 recipes

### Why Not Auto-Fix?

**Can't blindly auto-fix because:**

1. **Multiple valid choices** - BOM might have 10 items, step needs 2-3 specific ones
2. **Semantic understanding needed** - Need to know what process actually does
3. **Generic item selection** - Choosing between `steel_plate_1mm` vs `steel_plate_2mm` requires context
4. **Recipe intent unclear** - Author may have had specific materials in mind

**Solution:** Tool provides **intelligent suggestions**, human/agent **validates and applies**.

---

## Tool Architecture

### High-Level Flow

```
1. Load validation errors from out/validation_issues.jsonl
2. Group by recipe (many errors per recipe)
3. For each recipe:
   a. Analyze context (BOM, target item, similar recipes)
   b. Generate fix suggestions for each error
   c. Present to user/agent for review
   d. Apply approved fixes
   e. Re-validate recipe
4. Generate summary report
```

### Components

```
scripts/
  fix_template_errors.py          # Main CLI tool
  lib/
    suggestion_engine.py           # Core suggestion logic
    fix_strategies.py              # Different fix strategies
    recipe_patcher.py              # Apply fixes to YAML
    validation_helper.py           # Re-run validation
```

---

## Suggestion Engine Design

### Strategy 1: BOM-Based Suggestions

**When to use:** Recipe has target_item_id with a BOM

**Logic:**
```python
def suggest_from_bom(recipe, step, template_process, bom):
    """
    Suggest step inputs from BOM components.

    Heuristics:
    1. If template input is generic plural (assembly_components), suggest ALL BOM components
    2. If template input has material type (metal_*), filter BOM by material
    3. If template input has form factor (*_sheet, *_plate), filter BOM by form
    4. Rank by quantity (larger quantities = more likely primary inputs)
    """
    suggestions = []

    # Get template's placeholder inputs for reference
    template_inputs = template_process.inputs

    # Filter BOM components
    for component in bom.components:
        confidence = calculate_match_confidence(component, template_inputs)
        suggestions.append({
            'item_id': component.item_id,
            'qty': component.qty,
            'unit': component.unit,
            'confidence': confidence,
            'reason': f'From BOM (confidence: {confidence:.0%})'
        })

    return sorted(suggestions, key=lambda x: x['confidence'], reverse=True)
```

**Example output:**
```
Suggestion: Use BOM components (3 items found)
  ✓ aluminum_alloy_6061_plate [90% confidence]
    qty: 5.0 kg (from BOM)
    reason: Matches material type for assembly
  ✓ fastener_kit_small [75% confidence]
    qty: 1.0 unit (from BOM)
    reason: Common assembly component
  ✓ sealant_silicone_tube [60% confidence]
    qty: 0.1 kg (from BOM)
    reason: Auxiliary material
```

---

### Strategy 2: Previous Step Output Suggestions

**When to use:** Previous steps produce outputs

**Logic:**
```python
def suggest_from_previous_outputs(recipe, step_idx, template_process):
    """
    Suggest inputs from outputs of previous steps.

    Heuristics:
    1. Check if previous step outputs match template's expected input type
    2. Prioritize immediate predecessor (step N-1)
    3. Consider all previous steps (0 to N-1)
    4. Match by material type and form factor
    """
    suggestions = []
    accumulated_outputs = []

    for i in range(step_idx):
        prev_step = recipe.steps[i]
        prev_process = kb.get_process(prev_step.process_id)

        # Collect outputs
        for output in prev_step.outputs or prev_process.outputs:
            confidence = calculate_output_input_match(output, template_process)
            if confidence > 0.3:  # Threshold
                suggestions.append({
                    'item_id': output.item_id,
                    'qty': output.qty,
                    'unit': output.unit,
                    'confidence': confidence,
                    'reason': f'Output from step {i} ({prev_process.name})'
                })

    return sorted(suggestions, key=lambda x: x['confidence'], reverse=True)
```

**Example output:**
```
Suggestion: Use output from previous steps (2 matches found)
  ✓ machined_aluminum_housing [95% confidence]
    qty: 1.0 unit (from step 1 output)
    reason: Output from machining_precision_v0
  ✓ cut_steel_brackets [80% confidence]
    qty: 4.0 each (from step 0 output)
    reason: Output from cutting_basic_v0
```

---

### Strategy 3: Similar Recipe Analysis

**When to use:** Other recipes produce the same target_item_id

**Logic:**
```python
def suggest_from_similar_recipes(recipe, step_idx, template_process):
    """
    Find other recipes that:
    1. Produce the same target_item_id (variants OK)
    2. Use the same template process at similar step
    3. Have step-level input overrides

    Copy their approach.
    """
    suggestions = []

    # Find similar recipes
    similar = find_recipes_by_target(recipe.target_item_id)

    for sim_recipe in similar:
        for sim_step in sim_recipe.steps:
            if sim_step.process_id == template_process.id and sim_step.inputs:
                confidence = 0.85  # High confidence - proven pattern
                suggestions.append({
                    'inputs': sim_step.inputs,
                    'confidence': confidence,
                    'reason': f'Pattern from {sim_recipe.id} (proven to work)'
                })

    return suggestions
```

**Example output:**
```
Suggestion: Use pattern from similar recipe (1 match found)
  ✓ Pattern from recipe_pump_centrifugal_v1 [85% confidence]
    inputs:
      - item_id: aluminum_alloy_6061_plate
        qty: 2.0 kg
      - item_id: stainless_fastener_set
        qty: 1.0 unit
    reason: Same target item, same process, proven to work
```

---

### Strategy 4: Generic Item Replacement

**When to use:** Step has inputs with generic "or" patterns

**Logic:**
```python
def suggest_generic_replacements(item_id_generic, recipe, bom):
    """
    Replace generic placeholders with specific items.

    Examples:
    - steel_plate_or_sheet → steel_plate_1mm, steel_plate_2mm, steel_sheet_18ga
    - powder_metal_or_ceramic → iron_powder_v0, nickel_powder_v0, alumina_powder
    - bulk_material_or_parts → (check BOM or recipe inputs)

    Heuristics:
    1. Parse "or" pattern to understand options
    2. Search item catalog for specific variants
    3. Filter by BOM (if available)
    4. Rank by commonality in other recipes
    """
    suggestions = []

    # Parse pattern
    if '_or_' in item_id_generic:
        options = item_id_generic.split('_or_')
        base_pattern = options[0]  # e.g., "steel_plate"

        # Search catalog
        candidates = search_items_by_pattern(base_pattern)

        # Filter by BOM
        if bom:
            candidates = [c for c in candidates if c.item_id in bom.component_ids]

        # Rank
        for candidate in candidates:
            confidence = calculate_replacement_confidence(candidate, item_id_generic, bom)
            suggestions.append({
                'item_id': candidate.item_id,
                'qty': 1.0,  # Default, user adjusts
                'unit': 'kg',  # Default
                'confidence': confidence,
                'reason': f'Specific variant of {base_pattern}'
            })

    return sorted(suggestions, key=lambda x: x['confidence'], reverse=True)
```

**Example output:**
```
Suggestion: Replace generic 'steel_plate_or_sheet' (4 specific variants found)
  ✓ steel_plate_6mm [90% confidence]
    In BOM: Yes (5.0 kg)
    reason: Most common variant in similar recipes
  ✓ steel_plate_3mm [75% confidence]
    In BOM: Yes (2.0 kg)
    reason: Alternative thickness variant
  ✓ steel_sheet_20ga [60% confidence]
    In BOM: No
    reason: Sheet form factor option
  ✓ stainless_steel_plate_3mm [50% confidence]
    In BOM: No
    reason: Stainless variant
```

---

### Strategy 5: Item Catalog Search

**When to use:** No BOM, no similar recipes, need to find items

**Logic:**
```python
def suggest_from_catalog(template_process, recipe):
    """
    Search item catalog for items that could satisfy template.

    Use NLP/heuristics:
    1. Extract keywords from process name (e.g., "welding" → metal items)
    2. Extract keywords from template input name (e.g., "wet_material" → liquids)
    3. Check recipe's target_item_id for context (e.g., "pump" → mechanical parts)
    4. Rank by frequency of use in similar process types
    """
    suggestions = []

    # Keyword extraction
    process_keywords = extract_keywords(template_process.name)
    input_keywords = extract_keywords(template_process.inputs[0].item_id)
    target_keywords = extract_keywords(recipe.target_item_id)

    # Search catalog
    candidates = search_items_by_keywords(
        process_keywords + input_keywords + target_keywords
    )

    # Rank by usage frequency in KB
    for candidate in candidates[:10]:  # Limit to top 10
        confidence = calculate_catalog_confidence(candidate, template_process, recipe)
        suggestions.append({
            'item_id': candidate.item_id,
            'qty': 1.0,
            'unit': candidate.default_unit,
            'confidence': confidence,
            'reason': f'Matches process keywords: {", ".join(process_keywords[:3])}'
        })

    return sorted(suggestions, key=lambda x: x['confidence'], reverse=True)
```

**Example output:**
```
Suggestion: Search catalog by keywords (5 matches found)
  ✓ aluminum_alloy_6061_ingot [70% confidence]
    reason: Matches keywords: metal, forming, machining
  ✓ steel_bar_stock_20mm [65% confidence]
    reason: Matches keywords: metal, machining
  ✓ copper_billet_rectangular [55% confidence]
    reason: Matches keywords: metal, forming
```

---

## Tool Modes

### Mode 1: Interactive CLI (Human User)

**Usage:**
```bash
python scripts/fix_template_errors.py --mode interactive

# Workflow:
# 1. Load errors
# 2. For each recipe, show:
#    - Error description
#    - Recipe context (target, BOM, steps)
#    - Suggestions with confidence scores
# 3. Prompt user:
#    - [a] Apply suggestion #1
#    - [b] Apply suggestion #2
#    - [e] Edit manually
#    - [s] Skip
#    - [q] Quit
# 4. Apply fix and re-validate
# 5. Show result
```

**Example session:**
```
=================================================================
Recipe: recipe_pump_centrifugal_v2 (Error 1 of 2,954)
=================================================================

Target: pump_centrifugal_v2
BOM: Yes (5 components)
Steps: 3 total

Error: Step 1 uses template process 'assembly_basic_v0' but doesn't
       provide step-level input overrides

Current step:
  - process_id: assembly_basic_v0
    # NO inputs specified

Template process has placeholder input: 'assembly_components'

─────────────────────────────────────────────────────────────────
SUGGESTIONS (3 strategies found):
─────────────────────────────────────────────────────────────────

[1] BOM Components (90% confidence) ⭐ RECOMMENDED
    Use 3 items from BOM:
      - aluminum_pump_housing (2.0 kg)
      - stainless_impeller_v1 (1.5 kg)
      - rubber_seal_kit (1.0 unit)

    Resulting step:
      - process_id: assembly_basic_v0
        inputs:
        - item_id: aluminum_pump_housing
          qty: 2.0
          unit: kg
        - item_id: stainless_impeller_v1
          qty: 1.5
          unit: kg
        - item_id: rubber_seal_kit
          qty: 1.0
          unit: unit

[2] Previous Step Outputs (85% confidence)
    Use 2 outputs from step 0:
      - machined_pump_housing (1.0 unit)
      - machined_impeller (1.0 unit)

[3] Similar Recipe Pattern (80% confidence)
    Copy from recipe_pump_centrifugal_v1:
      - aluminum_alloy_6061_plate (2.0 kg)
      - fastener_kit_assembly (1.0 unit)

─────────────────────────────────────────────────────────────────
ACTION:
  [1-3] Apply suggestion number
  [e]   Edit manually in $EDITOR
  [s]   Skip this error
  [i]   Show more info
  [q]   Quit

Your choice: 1

✓ Applied suggestion 1
✓ Updated recipe_pump_centrifugal_v2.yaml
✓ Re-validating...

Result: ✅ Recipe now passes validation (2 errors → 1 error)

Continue to next error? [y/n]: y
```

---

### Mode 2: Batch Review (Agent-Friendly)

**Usage:**
```bash
python scripts/fix_template_errors.py --mode batch --output suggestions.jsonl

# Generates suggestions for ALL errors
# Agent reviews suggestions.jsonl
# Agent applies fixes via fix_template_errors.py --apply suggestions.jsonl
```

**Output format (`suggestions.jsonl`):**
```json
{
  "recipe_id": "recipe_pump_centrifugal_v2",
  "error": {
    "rule": "recipe_template_missing_step_inputs",
    "step_idx": 1,
    "process_id": "assembly_basic_v0",
    "message": "Step 1 uses template process but doesn't provide step-level input overrides"
  },
  "context": {
    "target_item_id": "pump_centrifugal_v2",
    "has_bom": true,
    "bom_components": ["aluminum_pump_housing", "stainless_impeller_v1", "rubber_seal_kit"],
    "previous_outputs": [],
    "current_step": {
      "process_id": "assembly_basic_v0",
      "inputs": null
    }
  },
  "suggestions": [
    {
      "strategy": "bom_components",
      "confidence": 0.90,
      "reason": "BOM has 3 components matching assembly needs",
      "fix": {
        "action": "add_step_inputs",
        "step_idx": 1,
        "inputs": [
          {"item_id": "aluminum_pump_housing", "qty": 2.0, "unit": "kg"},
          {"item_id": "stainless_impeller_v1", "qty": 1.5, "unit": "kg"},
          {"item_id": "rubber_seal_kit", "qty": 1.0, "unit": "unit"}
        ]
      }
    },
    {
      "strategy": "similar_recipe",
      "confidence": 0.80,
      "reason": "Pattern from recipe_pump_centrifugal_v1",
      "fix": {
        "action": "add_step_inputs",
        "step_idx": 1,
        "inputs": [
          {"item_id": "aluminum_alloy_6061_plate", "qty": 2.0, "unit": "kg"},
          {"item_id": "fastener_kit_assembly", "qty": 1.0, "unit": "unit"}
        ]
      }
    }
  ],
  "recommended_suggestion": 0
}
```

**Agent workflow:**
```bash
# 1. Generate suggestions
python scripts/fix_template_errors.py --mode batch --output suggestions.jsonl

# 2. Agent reviews suggestions.jsonl and creates decisions.jsonl
# decisions.jsonl format:
{
  "recipe_id": "recipe_pump_centrifugal_v2",
  "error_idx": 0,
  "action": "apply",  # or "skip" or "custom"
  "suggestion_idx": 0,  # which suggestion to apply
  "notes": "BOM-based suggestion has high confidence"
}

# 3. Apply approved fixes
python scripts/fix_template_errors.py --apply decisions.jsonl

# 4. Generate report
python scripts/fix_template_errors.py --report
```

---

### Mode 3: Auto-Apply High Confidence (with Review)

**Usage:**
```bash
python scripts/fix_template_errors.py --mode auto --confidence-threshold 0.85

# Automatically apply suggestions with confidence >= 85%
# Generate report of what was changed
# User/agent reviews report and can revert if needed
```

**Output:**
```
Auto-applying high-confidence fixes (threshold: 85%)...

Processing 2,954 errors...

✓ recipe_pump_centrifugal_v2: Applied BOM suggestion (90% confidence)
✓ recipe_motor_electric_v1: Applied similar recipe pattern (88% confidence)
✓ recipe_valve_check_v0: Applied BOM suggestion (92% confidence)
⊘ recipe_sensor_pressure_v3: No high-confidence suggestion (best: 75%)
⊘ recipe_bearing_assembly_v2: No high-confidence suggestion (best: 70%)
✓ recipe_filter_oil_v0: Applied previous output (87% confidence)

Summary:
  Applied: 1,847 fixes (62.5%)
  Skipped: 1,107 errors (37.5% - need manual review)

Changes written to:
  - 1,247 recipe files modified
  - auto_fix_report.md (detailed changelog)
  - skipped_errors.jsonl (errors needing manual review)

Next steps:
  1. Review auto_fix_report.md
  2. Re-run indexer to verify
  3. Address skipped_errors.jsonl manually
```

---

## Implementation Plan

### Phase 1: Core Suggestion Engine (Day 1-2)

**Files to create:**
```
scripts/lib/suggestion_engine.py
  - suggest_from_bom()
  - suggest_from_previous_outputs()
  - suggest_from_similar_recipes()
  - suggest_generic_replacements()
  - suggest_from_catalog()
  - rank_suggestions()

scripts/lib/fix_strategies.py
  - calculate_match_confidence()
  - calculate_output_input_match()
  - calculate_replacement_confidence()
  - extract_keywords()
  - search_items_by_pattern()

scripts/lib/recipe_patcher.py
  - load_recipe_yaml()
  - add_step_inputs()
  - replace_step_input()
  - write_recipe_yaml()  # Preserve formatting
```

**Tests:**
```
test/unit/test_suggestion_engine.py
  - test_bom_suggestions_all_components()
  - test_bom_suggestions_filtered_by_material()
  - test_previous_output_suggestions()
  - test_similar_recipe_pattern()
  - test_generic_replacement_steel_or_aluminum()
  - test_confidence_scoring()
```

---

### Phase 2: CLI Modes (Day 3)

**Files to create:**
```
scripts/fix_template_errors.py
  - main()
  - interactive_mode()
  - batch_mode()
  - auto_mode()
  - load_errors()
  - group_errors_by_recipe()
  - display_error_context()
  - display_suggestions()
  - apply_fix()
  - revalidate_recipe()
```

**Features:**
- Color-coded output (green=high confidence, yellow=medium, red=low)
- Progress bar for batch processing
- Undo/revert functionality
- Dry-run mode (show what would change)

---

### Phase 3: Agent Instructions (Day 4)

**Documentation:**
```
docs/agent-instructions-fix-template-errors.md
  - How to run the tool
  - How to interpret suggestions
  - When to apply vs skip
  - How to handle edge cases
  - Examples of good fixes
  - Examples of bad fixes (what to avoid)
```

**Agent decision rubric:**
```markdown
## Decision Rubric for Agents

Apply suggestion IF:
✓ Confidence >= 85% AND strategy is BOM or similar_recipe
✓ All suggested items exist in KB (verify with kb.get_item())
✓ Quantities are reasonable (not 0, not > 1000 for typical items)
✓ Units make sense for item type (kg for materials, unit/each for assemblies)

Skip suggestion IF:
✗ Confidence < 70%
✗ No suggestions found
✗ Multiple suggestions with similar confidence (ambiguous)
✗ Suggested items don't exist in KB
✗ Recipe is marked with "WIP" or "DRAFT" in notes

Request human review IF:
⚠ Confidence 70-85% (medium range)
⚠ Catalog search is only strategy (no BOM/similar recipe)
⚠ Quantities seem unusual
⚠ Target item is critical infrastructure (power_supply, processor, etc.)
```

---

### Phase 4: Testing and Refinement (Day 5)

**Test cases:**
```
1. Recipe with BOM - all components used
2. Recipe with BOM - subset of components
3. Recipe with no BOM - use previous outputs
4. Recipe with no BOM, no previous outputs - similar recipe
5. Recipe with generic "or" pattern - replacement
6. Recipe with no good suggestions - low confidence
7. Recipe with multiple errors - fix all at once
8. Recipe where fix introduces new error - rollback
```

**Validation:**
- Fix 100 recipes manually (baseline)
- Run tool on same 100 recipes
- Compare tool suggestions to manual fixes
- Measure accuracy: % of suggestions that match manual fixes
- Target: >= 80% accuracy for high-confidence suggestions

---

## Success Metrics

### Tool Quality

| Metric | Target |
|--------|--------|
| Suggestion accuracy (confidence >= 85%) | >= 80% match manual fixes |
| Suggestion accuracy (confidence >= 70%) | >= 60% match manual fixes |
| Suggestions found (any confidence) | >= 90% of errors |
| Auto-fix success rate (confidence >= 85%) | >= 95% validate correctly |

### Error Reduction

| Phase | Errors | Method |
|-------|--------|--------|
| Current | 4,609 | - |
| After auto-fix (85%+ confidence) | ~2,500 | Automated |
| After agent review (70%+ confidence) | ~1,000 | Agent-assisted |
| After manual review | ~200 | Human manual |

---

## Agent Instructions Preview

**File:** `docs/agent-instructions-fix-template-errors.md`

```markdown
# Agent Instructions: Fixing Template Validation Errors

## Task
Fix 4,609 recipe validation errors related to template processes.

## Background
Template processes (marked `is_template: true`) are generic process
definitions that require step-level input overrides in recipes.
Many recipes use templates without providing these overrides or
use generic placeholder item IDs.

## Tool Usage

### Step 1: Generate Suggestions
```bash
python scripts/fix_template_errors.py --mode batch --output suggestions.jsonl
```

This creates `suggestions.jsonl` with fix suggestions for all errors.

### Step 2: Review Suggestions
For each suggestion in `suggestions.jsonl`:

1. Read the error context
2. Review all suggestion strategies
3. Check confidence scores
4. Verify suggested items exist in KB
5. Apply decision rubric (see below)
6. Record decision in `decisions.jsonl`

### Step 3: Apply Decisions
```bash
python scripts/fix_template_errors.py --apply decisions.jsonl
```

### Step 4: Validate Results
```bash
python -m src.cli index
# Check that errors decreased
```

## Decision Rubric
[... full rubric from Phase 3 ...]

## Examples
[... detailed examples with reasoning ...]
```

---

## Next Steps

1. **User approval** - Review this design, suggest changes
2. **Priority decisions** - Which modes to implement first?
3. **Implementation** - Build Phase 1 (suggestion engine core)
4. **Testing** - Validate suggestions on sample recipes
5. **Deployment** - Run tool on full KB with agent assistance

## Questions for User

1. **Confidence thresholds** - Are 85% for auto-fix, 70% for agent-review reasonable?
2. **Agent vs human** - Should we optimize for AI agent use or human interactive use first?
3. **Validation strictness** - Should we allow low-confidence fixes or require high-confidence only?
4. **BOM priority** - Should BOM-based suggestions always rank highest (currently yes)?
5. **Batch size** - Fix all 4,609 errors at once or test on subset first (e.g., 100)?
