#!/usr/bin/env python3
"""
Batch analysis of template validation errors.

Generates intelligence files for each recipe with template errors,
providing context and suggestions for fixing.

Output: out/template_fixes/recipe_<id>.md (one per recipe)
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.kb_core.kb_loader import KBLoader


def load_validation_errors() -> List[Dict[str, Any]]:
    """Load validation errors from JSONL file."""
    errors = []
    errors_file = Path('out/validation_issues.jsonl')

    if not errors_file.exists():
        print(f"Error: {errors_file} not found. Run 'python -m src.cli index' first.")
        sys.exit(1)

    with open(errors_file, 'r') as f:
        for line in f:
            error = json.loads(line)
            # Only template-related errors
            if error.get('rule') in ['recipe_template_missing_step_inputs', 'recipe_step_input_not_satisfied']:
                errors.append(error)

    return errors


def group_errors_by_recipe(errors: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Group errors by recipe_id."""
    grouped = defaultdict(list)

    for error in errors:
        if error.get('entity_type') == 'recipe':
            recipe_id = error.get('entity_id')
            if recipe_id:
                grouped[recipe_id].append(error)

    return dict(grouped)


def find_similar_recipes(kb: KBLoader, recipe: Any, max_results: int = 3) -> List[Dict[str, Any]]:
    """
    Find recipes that produce the same target_item_id.

    Returns list of similar recipes with their step patterns.
    """
    similar = []

    recipe_dict = recipe if isinstance(recipe, dict) else recipe.model_dump()
    target_item_id = recipe_dict.get('target_item_id')

    if not target_item_id:
        return []

    # Search for recipes with same target (including variants)
    base_target = target_item_id.rsplit('_v', 1)[0] if '_v' in target_item_id else target_item_id

    for other_recipe_id, other_recipe in kb.recipes.items():
        if other_recipe_id == recipe_dict.get('id'):
            continue  # Skip self

        other_dict = other_recipe if isinstance(other_recipe, dict) else other_recipe.model_dump()
        other_target = other_dict.get('target_item_id', '')

        if not other_target:
            continue

        # Check if targets match (including variants)
        other_base = other_target.rsplit('_v', 1)[0] if '_v' in other_target else other_target

        if base_target == other_base or target_item_id == other_target:
            similar.append({
                'recipe_id': other_recipe_id,
                'target_item_id': other_target,
                'steps': other_dict.get('steps', []),
                'inputs': other_dict.get('inputs', [])
            })

        if len(similar) >= max_results:
            break

    return similar


def find_items_by_pattern(kb: KBLoader, pattern: str, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Find items matching a generic pattern like 'steel_plate_or_sheet'.

    For "or" patterns, searches for items containing either option.
    """
    matches = []

    # Handle "or" patterns
    if '_or_' in pattern:
        parts = pattern.split('_or_')
        search_terms = parts
    else:
        search_terms = [pattern.replace('_', ' ')]

    for item_id, item in kb.items.items():
        for term in search_terms:
            if term.replace(' ', '_') in item_id:
                item_dict = item if isinstance(item, dict) else item.model_dump()
                matches.append({
                    'item_id': item_id,
                    'name': item_dict.get('name', item_id),
                    'unit': item_dict.get('unit', 'unknown')
                })
                break

        if len(matches) >= limit:
            break

    return matches


def generate_intelligence_file(
    kb: KBLoader,
    recipe_id: str,
    errors: List[Dict[str, Any]]
) -> str:
    """
    Generate markdown intelligence file for a recipe with errors.

    Returns: markdown content
    """
    # Load recipe
    recipe = kb.get_recipe(recipe_id)
    if not recipe:
        return f"# Error: Recipe {recipe_id} not found\n"

    recipe_dict = recipe if isinstance(recipe, dict) else recipe.model_dump()

    # Get context
    target_item_id = recipe_dict.get('target_item_id')
    bom = kb.get_bom(target_item_id) if target_item_id else None
    bom_dict = bom if isinstance(bom, dict) else (bom.model_dump() if bom else None)

    steps = recipe_dict.get('steps', [])

    # Find similar recipes
    similar_recipes = find_similar_recipes(kb, recipe)

    # Build markdown
    md = []
    md.append(f"# Fix Intelligence: {recipe_id}\n")

    # Files section
    md.append("## Files\n")
    md.append(f"- **Recipe:** `kb/recipes/{recipe_id}.yaml`")

    if target_item_id:
        md.append(f"- **Target item:** `{target_item_id}`")
        md.append(f"  - File: `kb/items/{target_item_id}.yaml`")

    if bom_dict:
        bom_id = bom_dict.get('id', f'bom_{target_item_id}')
        md.append(f"- **BOM:** `kb/boms/{bom_id}.yaml` ✓")
        md.append(f"  - Components: {len(bom_dict.get('components', []))}")
    else:
        md.append(f"- **BOM:** None")

    md.append(f"- **Steps:** {len(steps)} total\n")

    # Similar recipes section
    if similar_recipes:
        md.append("## Similar Recipes\n")
        md.append(f"Found {len(similar_recipes)} recipes producing similar items:\n")
        for sim in similar_recipes:
            md.append(f"- `{sim['recipe_id']}` → {sim['target_item_id']} ({len(sim['steps'])} steps)")
        md.append("")

    # Errors section
    md.append(f"## Errors ({len(errors)} found)\n")

    for idx, error in enumerate(errors, 1):
        md.append(f"### Error {idx}: {error.get('rule')}\n")

        # Extract step index from field_path (e.g., "steps[1].inputs")
        field_path = error.get('field_path', '')
        step_idx = None
        if 'steps[' in field_path:
            try:
                step_idx = int(field_path.split('[')[1].split(']')[0])
            except:
                pass

        md.append(f"**Message:** {error.get('message')}\n")

        if step_idx is not None and step_idx < len(steps):
            step = steps[step_idx]
            process_id = step.get('process_id')

            md.append(f"**Location:** Step {step_idx}")
            md.append(f"**Process:** `{process_id}`")
            md.append(f"  - File: `kb/processes/{process_id}.yaml`\n")

            # Get process info
            process = kb.get_process(process_id)
            process_dict = process if isinstance(process, dict) else (process.model_dump() if process else {})
            is_template = process_dict.get('is_template', False)

            if is_template:
                md.append(f"**Process type:** TEMPLATE (requires step-level inputs)\n")

            # Show current step YAML
            md.append("**Current step:**")
            md.append("```yaml")
            md.append(f"- process_id: {process_id}")

            if step.get('inputs'):
                md.append("  inputs:")
                for inp in step['inputs']:
                    md.append(f"  - item_id: {inp.get('item_id')}")
                    if inp.get('qty'):
                        md.append(f"    qty: {inp.get('qty')}")
                    if inp.get('unit'):
                        md.append(f"    unit: {inp.get('unit')}")
            else:
                md.append("  # NO inputs field")

            md.append("```\n")

            # Generate suggestions based on error type
            if error.get('rule') == 'recipe_template_missing_step_inputs':
                # Missing step inputs for template
                md.append("**Analysis:** Template process used without step-level input overrides.\n")

                # Option A: BOM components
                if bom_dict and bom_dict.get('components'):
                    md.append("#### Option A: Use BOM components\n")
                    md.append(f"BOM has {len(bom_dict['components'])} components:\n")
                    for comp in bom_dict['components']:
                        md.append(f"- `{comp.get('item_id')}` (qty: {comp.get('qty')} {comp.get('unit')})")

                    md.append("\nSuggested fix:")
                    md.append("```yaml")
                    md.append(f"- process_id: {process_id}")
                    md.append("  inputs:")
                    for comp in bom_dict['components']:
                        md.append(f"  - item_id: {comp.get('item_id')}")
                        md.append(f"    qty: {comp.get('qty')}")
                        md.append(f"    unit: {comp.get('unit')}")
                    md.append("```\n")

                # Option B: Previous step outputs
                if step_idx > 0:
                    prev_outputs = []
                    for i in range(step_idx):
                        prev_step = steps[i]
                        if prev_step.get('outputs'):
                            prev_outputs.extend([(i, out) for out in prev_step['outputs']])
                        else:
                            # Get from process
                            prev_proc = kb.get_process(prev_step.get('process_id'))
                            if prev_proc:
                                prev_proc_dict = prev_proc if isinstance(prev_proc, dict) else prev_proc.model_dump()
                                if prev_proc_dict.get('outputs'):
                                    prev_outputs.extend([(i, out) for out in prev_proc_dict['outputs']])

                    if prev_outputs:
                        md.append("#### Option B: Use previous step outputs\n")
                        for step_i, output in prev_outputs:
                            md.append(f"- Step {step_i} produces: `{output.get('item_id')}` ({output.get('qty')} {output.get('unit')})")
                        md.append("")

                # Option C: Similar recipe pattern
                if similar_recipes:
                    for sim in similar_recipes:
                        # Find matching step in similar recipe
                        for sim_step_idx, sim_step in enumerate(sim['steps']):
                            if sim_step.get('process_id') == process_id and sim_step.get('inputs'):
                                md.append(f"#### Option C: Pattern from `{sim['recipe_id']}`\n")
                                md.append(f"Similar recipe uses this process (step {sim_step_idx}) with:\n")
                                md.append("```yaml")
                                md.append("  inputs:")
                                for inp in sim_step['inputs']:
                                    md.append(f"  - item_id: {inp.get('item_id')}")
                                    if inp.get('qty'):
                                        md.append(f"    qty: {inp.get('qty')}")
                                    if inp.get('unit'):
                                        md.append(f"    unit: {inp.get('unit')}")
                                md.append("```\n")
                                break

            elif error.get('rule') == 'recipe_step_input_not_satisfied':
                # Step has inputs but they reference invalid items
                md.append("**Analysis:** Step has inputs, but one or more items don't exist or aren't available.\n")

                if step.get('inputs'):
                    for inp in step['inputs']:
                        item_id = inp.get('item_id')

                        # Check if it's a generic "or" pattern
                        if '_or_' in item_id or item_id.startswith('bulk_') or item_id.startswith('assembly_'):
                            md.append(f"#### Problem: Generic placeholder `{item_id}`\n")
                            md.append("This is not a real item. Need to replace with specific item.\n")

                            # Find matching specific items
                            matches = find_items_by_pattern(kb, item_id)

                            if matches:
                                md.append("**Specific items matching pattern:**\n")

                                # Check which are in BOM
                                bom_item_ids = [c.get('item_id') for c in bom_dict.get('components', [])] if bom_dict else []

                                for match in matches:
                                    in_bom = match['item_id'] in bom_item_ids
                                    marker = " ← IN BOM" if in_bom else ""
                                    md.append(f"- `{match['item_id']}`{marker}")

                                    # Show BOM quantity if available
                                    if in_bom:
                                        for comp in bom_dict.get('components', []):
                                            if comp.get('item_id') == match['item_id']:
                                                md.append(f"  - BOM qty: {comp.get('qty')} {comp.get('unit')}")
                                                break

                                md.append("")
                            else:
                                md.append("*No matching items found in catalog.*\n")
                        else:
                            # Item doesn't exist
                            md.append(f"#### Problem: Item `{item_id}` not found\n")
                            md.append("This item doesn't exist in the KB.\n")

                            # Check if it's in BOM
                            if bom_dict:
                                bom_items = [c.get('item_id') for c in bom_dict.get('components', [])]
                                if item_id not in bom_items:
                                    md.append("**Suggestions:**")
                                    md.append("1. Check if item name is misspelled")
                                    md.append("2. Add item to BOM if it should be a component")
                                    md.append("3. Replace with an output from a previous step\n")

        md.append("---\n")

    # Summary
    md.append("## Summary\n")
    md.append(f"- **Total errors:** {len(errors)}")
    md.append(f"- **Recipe file:** `kb/recipes/{recipe_id}.yaml`")
    if bom_dict:
        md.append(f"- **BOM available:** Yes ({len(bom_dict.get('components', []))} components)")
    else:
        md.append(f"- **BOM available:** No")
    if similar_recipes:
        md.append(f"- **Similar recipes:** {len(similar_recipes)} found")
    md.append("")

    return '\n'.join(md)


def main():
    """Main entry point."""
    print("="*70)
    print("TEMPLATE ERROR BATCH ANALYSIS")
    print("="*70)
    print()

    # Load KB
    print("Loading KB...")
    kb_root = Path('kb')
    kb = KBLoader(kb_root)
    kb.load_all()
    print(f"  Loaded: {len(kb.processes)} processes, {len(kb.recipes)} recipes, {len(kb.items)} items, {len(kb.boms)} BOMs")
    print()

    # Load validation errors
    print("Loading validation errors...")
    errors = load_validation_errors()
    print(f"  Found: {len(errors)} template-related errors")
    print()

    # Group by recipe
    print("Grouping errors by recipe...")
    grouped = group_errors_by_recipe(errors)
    print(f"  Recipes affected: {len(grouped)}")
    print()

    # Generate intelligence files
    print("Generating intelligence files...")
    output_dir = Path('out/template_fixes')
    output_dir.mkdir(parents=True, exist_ok=True)

    for recipe_id, recipe_errors in grouped.items():
        output_file = output_dir / f"{recipe_id}.md"

        try:
            content = generate_intelligence_file(kb, recipe_id, recipe_errors)

            with open(output_file, 'w') as f:
                f.write(content)

            print(f"  ✓ {recipe_id} ({len(recipe_errors)} errors)")
        except Exception as e:
            print(f"  ✗ {recipe_id}: {e}")

    print()
    print("="*70)
    print("SUMMARY")
    print("="*70)
    print(f"  Intelligence files generated: {len(grouped)}")
    print(f"  Output directory: {output_dir}")
    print(f"  Total errors analyzed: {len(errors)}")
    print("="*70)
    print()
    print("Next steps:")
    print("  1. Review sample files in out/template_fixes/")
    print("  2. Test agent workflow:")
    print("     python -m src.cli queue get")
    print("     cat out/template_fixes/<recipe_id>.md")
    print("  3. Run auto-fix experiment:")
    print("     python scripts/autofix_template_errors.py --dry-run")
    print()


if __name__ == '__main__':
    main()
