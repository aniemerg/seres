#!/usr/bin/env python3
"""
Phase 2b: Mark additional generic processes as templates.

These processes use generic placeholder inputs (rough_part, steel_stock, etc.)
that are meant to be overridden at the recipe level with specific materials.

Selection criteria:
- Generic input names with "or" (steel_plate_or_sheet) or placeholders (rough_part)
- >10 validation errors
- Used across multiple recipes with different materials
- Part of *_basic_v0 family
"""

import yaml
from pathlib import Path
from typing import Dict, Any


PHASE_2B_TEMPLATE_CANDIDATES = {
    'cutting_basic_v0': {
        'generic_input': 'steel_plate_or_sheet',
        'error_count': 73,
        'justification': 'Generic cutting process for various sheet materials (steel, aluminum, etc.)'
    },
    'precision_grinding_basic_v0': {
        'generic_input': 'rough_part',
        'error_count': 47,
        'justification': 'Generic precision grinding on any rough-machined part'
    },
    'calibration_basic_v0': {
        'generic_input': 'instrument_uncalibrated',
        'error_count': 36,
        'justification': 'Generic calibration process for various uncalibrated instruments'
    },
    'machining_precision_v0': {
        'generic_input': 'steel_stock',
        'error_count': 33,
        'justification': 'Generic precision machining from steel stock (various alloys)'
    },
    'metal_forming_basic_v0': {
        'generic_input': 'metal_sheet_or_plate',
        'error_count': 27,
        'justification': 'Generic metal forming for various sheet/plate materials'
    },
    'heat_treatment_basic_v0': {
        'generic_input': 'rough_part',
        'error_count': 24,
        'justification': 'Generic heat treatment on any rough part (various metals)'
    },
    'surface_finishing_basic_v0': {
        'generic_input': 'rough_part',
        'error_count': 15,
        'justification': 'Generic surface finishing on any rough part'
    },
    'forging_basic_v0': {
        'generic_input': 'steel_stock_bar_or_billet',
        'error_count': 14,
        'justification': 'Generic forging from steel stock (various alloys/forms)'
    },
    'machining_basic_v0': {
        'generic_input': 'raw_metal_block',
        'error_count': 13,
        'justification': 'Generic basic machining from raw metal blocks (various metals)'
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

        # Add is_template field
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
    print('PHASE 2B: MARKING ADDITIONAL TEMPLATE PROCESSES')
    print('='*60)
    print()

    modified_count = 0
    already_template_count = 0
    not_found_count = 0

    for process_id, info in PHASE_2B_TEMPLATE_CANDIDATES.items():
        process_path = processes_dir / f'{process_id}.yaml'

        print(f'{process_id}:')
        print(f'  Generic input: {info["generic_input"]}')
        print(f'  Error count: {info["error_count"]}')
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
    print('PHASE 2B SUMMARY:')
    print(f'  Processes marked as template: {modified_count}')
    print(f'  Already templates: {already_template_count}')
    print(f'  Not found: {not_found_count}')
    print(f'  Total processed: {len(PHASE_2B_TEMPLATE_CANDIDATES)}')
    print('='*60)
    print()
    print('Expected impact:')
    total_errors = sum(info['error_count'] for info in PHASE_2B_TEMPLATE_CANDIDATES.values())
    print(f'  Validation errors eliminated: ~{total_errors:,}')
    print(f'  Note: Recipes will now require explicit step-level input overrides')
    print('='*60)
    print()
    print('Combined Phase 2 + 2b:')
    phase2_errors = 1957
    combined_errors = phase2_errors + total_errors
    print(f'  Total errors eliminated: ~{combined_errors:,}')
    print(f'  Remaining errors (estimated): ~{2410 - total_errors:,}')
    print('='*60)


if __name__ == '__main__':
    main()
