#!/usr/bin/env python3
"""
Mark generic processes as templates to fix validation errors.

These processes use generic placeholder inputs that are meant to be
overridden at the recipe level with specific materials.

Evidence:
- Used across 100+ recipes with different materials
- 282 recipes already successfully use step-level overrides
- Input names are explicitly generic (assembly_components, metal_alloy_bulk, etc.)
"""

import yaml
from pathlib import Path
from typing import Dict, Any


# Processes identified as templates based on:
# 1. Generic input names (assembly_components, machined_part_raw, etc.)
# 2. Used across many recipes (100+)
# 3. Already used with step-level overrides in existing recipes
TEMPLATE_CANDIDATES = {
    'assembly_basic_v0': {
        'generic_input': 'assembly_components',
        'error_count': 693,
        'recipes_affected': 720,
        'justification': 'Generic assembly process used with many different component types'
    },
    'machining_finish_basic_v0': {
        'generic_input': 'machined_part_raw',
        'error_count': 495,
        'recipes_affected': 495,
        'justification': 'Generic finish machining used on various metal parts'
    },
    'metal_casting_basic_v0': {
        'generic_input': 'metal_alloy_bulk',
        'error_count': 220,
        'recipes_affected': 217,
        'justification': 'Generic casting process used with aluminum, steel, copper, brass, etc.'
    },
    'inspection_basic_v0': {
        'generic_input': 'finished_part',
        'error_count': 240,
        'recipes_affected': 200,
        'justification': 'Generic inspection process used on various finished parts'
    },
    'integration_test_basic_v0': {
        'generic_input': 'assembled_electronics',
        'error_count': 122,
        'recipes_affected': 120,
        'justification': 'Generic testing process for various electronic assemblies'
    },
    'wiring_and_electronics_integration_v0': {
        'generic_input': 'electrical_wire_and_connectors',
        'error_count': 108,
        'recipes_affected': 100,
        'justification': 'Generic wiring process used with different wire/connector types'
    },
    'welding_and_fabrication_v0': {
        'generic_input': 'sheet_metal_or_structural_steel',
        'error_count': 79,
        'recipes_affected': 79,
        'justification': 'Generic welding process used with various steel types'
    },
}


def mark_process_as_template(process_path: Path, process_id: str, info: Dict[str, Any]) -> bool:
    """
    Add is_template: true to a process definition.

    Returns:
        True if modification was made, False if already a template or file doesn't exist
    """
    if not process_path.exists():
        print(f'  ✗ File not found: {process_path}')
        return False

    try:
        with open(process_path, 'r', encoding='utf-8') as f:
            content = f.read()

        data = yaml.safe_load(content)
        if not data:
            print(f'  ✗ Empty or invalid YAML: {process_path}')
            return False

        # Check if already a template
        if data.get('is_template'):
            print(f'  ⊙ Already a template: {process_id}')
            return False

        # Add is_template field after process_type (if it exists) or after name
        # To preserve order, we'll add it as the 4th field typically
        data['is_template'] = True

        # Write back
        with open(process_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return True

    except Exception as e:
        print(f'  ✗ Error processing {process_path}: {e}')
        return False


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    processes_dir = project_root / 'kb' / 'processes'

    print('='*60)
    print('MARKING GENERIC PROCESSES AS TEMPLATES')
    print('='*60)
    print()

    modified_count = 0
    already_template_count = 0
    not_found_count = 0

    for process_id, info in TEMPLATE_CANDIDATES.items():
        process_path = processes_dir / f'{process_id}.yaml'

        print(f'{process_id}:')
        print(f'  Generic input: {info["generic_input"]}')
        print(f'  Error count: {info["error_count"]}')
        print(f'  Recipes affected: {info["recipes_affected"]}')
        print(f'  Justification: {info["justification"]}')

        result = mark_process_as_template(process_path, process_id, info)

        if result:
            print(f'  ✓ Marked as template')
            modified_count += 1
        elif process_path.exists():
            already_template_count += 1
        else:
            not_found_count += 1

        print()

    print('='*60)
    print('SUMMARY:')
    print(f'  Processes marked as template: {modified_count}')
    print(f'  Already templates: {already_template_count}')
    print(f'  Not found: {not_found_count}')
    print(f'  Total processed: {len(TEMPLATE_CANDIDATES)}')
    print('='*60)
    print()
    print('Expected impact:')
    total_errors = sum(info['error_count'] for info in TEMPLATE_CANDIDATES.values())
    print(f'  Validation errors eliminated: ~{total_errors:,}')
    print(f'  Note: Recipes will now require explicit step-level input overrides')
    print('='*60)


if __name__ == '__main__':
    main()
