#!/usr/bin/env python3
"""
Auto-fix experiment: Try heuristic fixes on sample recipes and report results.

Does NOT modify KB files - only generates report showing proposed fixes
and validation results for manual review.

Usage:
    python scripts/autofix_experiment.py --sample-size 10
"""

import argparse
import json
import sys
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.kb_core.kb_loader import KBLoader
from src.kb_core.validators import validate_recipe_step_inputs


def load_validation_errors() -> List[Dict[str, Any]]:
    """Load template-related validation errors."""
    errors = []
    errors_file = Path('out/validation_issues.jsonl')

    with open(errors_file, 'r') as f:
        for line in f:
            error = json.loads(line)
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


def apply_bom_fix(recipe_dict: Dict[str, Any], step_idx: int, bom_components: List[Dict]) -> Dict[str, Any]:
    """
    Apply fix: Add all BOM components as step inputs.

    Returns: Modified recipe dict (doesn't modify original)
    """
    import copy
    fixed = copy.deepcopy(recipe_dict)

    # Ensure step has inputs field
    if 'inputs' not in fixed['steps'][step_idx]:
        fixed['steps'][step_idx]['inputs'] = []

    # Add all BOM components
    for comp in bom_components:
        fixed['steps'][step_idx]['inputs'].append({
            'item_id': comp.get('item_id'),
            'qty': comp.get('qty'),
            'unit': comp.get('unit')
        })

    return fixed


def apply_previous_output_fix(recipe_dict: Dict[str, Any], step_idx: int, kb: KBLoader) -> Optional[Dict[str, Any]]:
    """
    Apply fix: Use outputs from previous step(s) as inputs.

    Returns: Modified recipe dict or None if no previous outputs
    """
    import copy

    if step_idx == 0:
        return None  # No previous steps

    # Collect outputs from all previous steps
    outputs = []
    for i in range(step_idx):
        prev_step = recipe_dict['steps'][i]

        # Check step-level outputs first
        if prev_step.get('outputs'):
            outputs.extend(prev_step['outputs'])
        else:
            # Get from process
            prev_proc = kb.get_process(prev_step.get('process_id'))
            if prev_proc:
                prev_proc_dict = prev_proc if isinstance(prev_proc, dict) else prev_proc.model_dump()
                if prev_proc_dict.get('outputs'):
                    outputs.extend(prev_proc_dict['outputs'])

    if not outputs:
        return None

    fixed = copy.deepcopy(recipe_dict)
    fixed['steps'][step_idx]['inputs'] = outputs

    return fixed


def validate_fixed_recipe(recipe_dict: Dict[str, Any], kb: KBLoader) -> tuple:
    """
    Validate a fixed recipe.

    Returns: (issues, error_count)
    """
    issues = validate_recipe_step_inputs(recipe_dict, kb)
    error_count = len([i for i in issues if i.level.value == 'ERROR'])
    return issues, error_count


def generate_yaml_snippet(data: Any, indent: int = 0) -> str:
    """Generate YAML snippet for display."""
    yaml_str = yaml.dump(data, default_flow_style=False, sort_keys=False)
    lines = yaml_str.strip().split('\n')
    return '\n'.join('  ' * indent + line for line in lines)


def experiment_on_recipe(
    kb: KBLoader,
    recipe_id: str,
    errors: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Run auto-fix experiment on one recipe.

    Returns: Experiment results dict
    """
    recipe = kb.get_recipe(recipe_id)
    if not recipe:
        return {'recipe_id': recipe_id, 'error': 'Recipe not found'}

    recipe_dict = recipe if isinstance(recipe, dict) else recipe.model_dump()

    # Get context
    target_item_id = recipe_dict.get('target_item_id')
    bom = kb.get_bom(target_item_id) if target_item_id else None
    bom_dict = bom if isinstance(bom, dict) else (bom.model_dump() if bom else None)

    results = {
        'recipe_id': recipe_id,
        'target_item_id': target_item_id,
        'has_bom': bom_dict is not None,
        'bom_components': len(bom_dict.get('components', [])) if bom_dict else 0,
        'errors_before': len(errors),
        'error_details': [],
        'fixes_attempted': []
    }

    # Try fixing each error
    for error in errors:
        # Extract step index
        field_path = error.get('field_path', '')
        step_idx = None
        if 'steps[' in field_path:
            try:
                step_idx = int(field_path.split('[')[1].split(']')[0])
            except:
                pass

        if step_idx is None or step_idx >= len(recipe_dict['steps']):
            continue

        error_detail = {
            'step_idx': step_idx,
            'rule': error.get('rule'),
            'message': error.get('message'),
            'original_step': recipe_dict['steps'][step_idx]
        }

        # Try different fix strategies
        fix_attempts = []

        # Strategy 1: BOM components
        if bom_dict and bom_dict.get('components'):
            try:
                fixed_recipe = apply_bom_fix(recipe_dict, step_idx, bom_dict['components'])
                issues, error_count = validate_fixed_recipe(fixed_recipe, kb)

                fix_attempts.append({
                    'strategy': 'bom_all_components',
                    'description': f'Add all {len(bom_dict["components"])} BOM components as step inputs',
                    'fixed_step': fixed_recipe['steps'][step_idx],
                    'validation_passed': error_count == 0,
                    'errors_after': error_count,
                    'new_issues': [i.message for i in issues if i.level.value == 'ERROR'][:3]  # First 3
                })
            except Exception as e:
                fix_attempts.append({
                    'strategy': 'bom_all_components',
                    'error': str(e)
                })

        # Strategy 2: Previous step outputs
        try:
            fixed_recipe = apply_previous_output_fix(recipe_dict, step_idx, kb)
            if fixed_recipe:
                issues, error_count = validate_fixed_recipe(fixed_recipe, kb)

                fix_attempts.append({
                    'strategy': 'previous_outputs',
                    'description': f'Use outputs from previous steps as inputs',
                    'fixed_step': fixed_recipe['steps'][step_idx],
                    'validation_passed': error_count == 0,
                    'errors_after': error_count,
                    'new_issues': [i.message for i in issues if i.level.value == 'ERROR'][:3]
                })
        except Exception as e:
            fix_attempts.append({
                'strategy': 'previous_outputs',
                'error': str(e)
            })

        error_detail['fix_attempts'] = fix_attempts
        results['error_details'].append(error_detail)

    return results


def generate_report(experiments: List[Dict[str, Any]], output_file: Path):
    """Generate markdown report of experiment results."""

    md = []
    md.append("# Auto-Fix Experiment Results\n")
    md.append(f"**Date:** {Path('out/validation_issues.jsonl').stat().st_mtime}")
    md.append(f"**Recipes tested:** {len(experiments)}\n")

    # Summary statistics
    total_fixes_tried = 0
    successful_fixes = 0
    bom_successes = 0
    prev_output_successes = 0

    for exp in experiments:
        for err_detail in exp.get('error_details', []):
            for fix in err_detail.get('fix_attempts', []):
                total_fixes_tried += 1
                if fix.get('validation_passed'):
                    successful_fixes += 1
                    if fix['strategy'] == 'bom_all_components':
                        bom_successes += 1
                    elif fix['strategy'] == 'previous_outputs':
                        prev_output_successes += 1

    md.append("## Summary Statistics\n")
    md.append(f"- **Total fix attempts:** {total_fixes_tried}")
    md.append(f"- **Validation passed:** {successful_fixes} ({100*successful_fixes/total_fixes_tried:.1f}%)" if total_fixes_tried > 0 else "- **Validation passed:** 0")
    md.append(f"- **BOM strategy successes:** {bom_successes}")
    md.append(f"- **Previous output strategy successes:** {prev_output_successes}\n")

    # Individual recipe results
    md.append("---\n")
    md.append("## Individual Recipe Results\n")

    for i, exp in enumerate(experiments, 1):
        md.append(f"### {i}. {exp['recipe_id']}\n")

        if 'error' in exp:
            md.append(f"**Error:** {exp['error']}\n")
            md.append("---\n")
            continue

        md.append(f"- **Target:** `{exp.get('target_item_id')}`")
        md.append(f"- **BOM:** {'Yes' if exp.get('has_bom') else 'No'}" +
                  (f" ({exp.get('bom_components')} components)" if exp.get('has_bom') else ""))
        md.append(f"- **Errors before fix:** {exp.get('errors_before')}\n")

        for j, err_detail in enumerate(exp.get('error_details', []), 1):
            md.append(f"#### Error {j}: Step {err_detail['step_idx']}\n")
            md.append(f"**Rule:** `{err_detail['rule']}`")
            md.append(f"**Message:** {err_detail['message']}\n")

            md.append("**Original step:**")
            md.append("```yaml")
            md.append(generate_yaml_snippet(err_detail['original_step']))
            md.append("```\n")

            # Show fix attempts
            for fix in err_detail.get('fix_attempts', []):
                if 'error' in fix:
                    md.append(f"**Fix attempt ({fix['strategy']}):** Failed - {fix['error']}\n")
                    continue

                status_icon = "✅" if fix['validation_passed'] else "❌"
                md.append(f"**Fix attempt:** {fix['strategy']} {status_icon}\n")
                md.append(f"*{fix['description']}*\n")

                md.append("**Fixed step:**")
                md.append("```yaml")
                md.append(generate_yaml_snippet(fix['fixed_step']))
                md.append("```\n")

                md.append(f"**Validation:** {'PASSED' if fix['validation_passed'] else 'FAILED'}")
                if not fix['validation_passed']:
                    md.append(f"- Errors after fix: {fix['errors_after']}")
                    if fix.get('new_issues'):
                        md.append("- New issues:")
                        for issue in fix['new_issues']:
                            md.append(f"  - {issue}")
                md.append("")

            md.append("---\n")

        md.append("")

    # Manual review guidance
    md.append("## Manual Review Guidance\n")
    md.append("### Questions to Ask:\n")
    md.append("1. **Semantic correctness:** Does the fix make sense for what the process does?")
    md.append("2. **Quantity appropriateness:** Are the quantities reasonable?")
    md.append("3. **Input selection:** Should ALL BOM components be used, or only some?")
    md.append("4. **Process intent:** Does the fix align with the process's purpose?\n")

    md.append("### Common Issues to Watch For:\n")
    md.append("- Adding ALL BOM components when process only needs 1-2")
    md.append("- Using outputs that don't match process input requirements")
    md.append("- Quantities that are too large/small for the process")
    md.append("- Materials that don't match process type (e.g., liquids in welding)\n")

    # Write report
    with open(output_file, 'w') as f:
        f.write('\n'.join(md))


def main():
    parser = argparse.ArgumentParser(description='Auto-fix experiment on sample recipes')
    parser.add_argument('--sample-size', type=int, default=10, help='Number of recipes to test')
    parser.add_argument('--output', type=str, default='out/autofix_experiment_report.md', help='Output report file')
    args = parser.parse_args()

    print("="*70)
    print("AUTO-FIX EXPERIMENT")
    print("="*70)
    print()
    print("Testing auto-fix heuristics on sample recipes...")
    print(f"Sample size: {args.sample_size}")
    print()

    # Load KB
    print("Loading KB...")
    kb = KBLoader(Path('kb'))
    kb.load_all()
    print(f"  Loaded: {len(kb.processes)} processes, {len(kb.recipes)} recipes")
    print()

    # Load errors
    print("Loading validation errors...")
    errors = load_validation_errors()
    grouped = group_errors_by_recipe(errors)
    print(f"  Found: {len(errors)} errors in {len(grouped)} recipes")
    print()

    # Select sample - variety of cases
    print(f"Selecting {args.sample_size} sample recipes...")

    # Stratified sample: some with BOM, some without, variety of error types
    sample_recipes = []

    # Try to get variety
    with_bom = []
    without_bom = []

    for recipe_id, recipe_errors in list(grouped.items())[:100]:  # Check first 100
        recipe = kb.get_recipe(recipe_id)
        if recipe:
            recipe_dict = recipe if isinstance(recipe, dict) else recipe.model_dump()
            target = recipe_dict.get('target_item_id')
            has_bom = kb.get_bom(target) is not None if target else False

            if has_bom and len(with_bom) < args.sample_size // 2:
                with_bom.append((recipe_id, recipe_errors))
            elif not has_bom and len(without_bom) < args.sample_size // 2:
                without_bom.append((recipe_id, recipe_errors))

            if len(with_bom) + len(without_bom) >= args.sample_size:
                break

    sample_recipes = with_bom + without_bom

    print(f"  Selected: {len(with_bom)} with BOM, {len(without_bom)} without BOM")
    print()

    # Run experiments
    print("Running experiments...")
    experiments = []

    for recipe_id, recipe_errors in sample_recipes:
        print(f"  Testing: {recipe_id} ({len(recipe_errors)} errors)")
        result = experiment_on_recipe(kb, recipe_id, recipe_errors)
        experiments.append(result)

    print()

    # Generate report
    output_file = Path(args.output)
    print(f"Generating report: {output_file}")
    generate_report(experiments, output_file)

    print()
    print("="*70)
    print("EXPERIMENT COMPLETE")
    print("="*70)
    print(f"Report: {output_file}")
    print()
    print("Next steps:")
    print("  1. Review report for manual assessment")
    print("  2. Determine if auto-fix heuristics are acceptable")
    print("  3. Decide on deployment strategy")
    print()


if __name__ == '__main__':
    main()
