#!/usr/bin/env python3
"""
Standardize energy/power input naming to 'electrical_energy'.

Replaces:
- electricity → electrical_energy
- process_power → electrical_energy

This is semantically correct as all refer to the same concept.
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List


def standardize_energy_in_dict(data: Dict[str, Any]) -> bool:
    """
    Replace electricity/process_power with electrical_energy in a YAML dict.

    Returns:
        True if any modifications were made
    """
    modified = False

    # Process inputs
    if 'inputs' in data and isinstance(data['inputs'], list):
        for inp in data['inputs']:
            if isinstance(inp, dict) and inp.get('item_id') in ['electricity', 'process_power']:
                old_name = inp['item_id']
                inp['item_id'] = 'electrical_energy'
                modified = True

    # Process outputs
    if 'outputs' in data and isinstance(data['outputs'], list):
        for out in data['outputs']:
            if isinstance(out, dict) and out.get('item_id') in ['electricity', 'process_power']:
                old_name = out['item_id']
                out['item_id'] = 'electrical_energy'
                modified = True

    # Recipe steps (step-level inputs)
    if 'steps' in data and isinstance(data['steps'], list):
        for step in data['steps']:
            if isinstance(step, dict):
                if 'inputs' in step and isinstance(step['inputs'], list):
                    for inp in step['inputs']:
                        if isinstance(inp, dict) and inp.get('item_id') in ['electricity', 'process_power']:
                            old_name = inp['item_id']
                            inp['item_id'] = 'electrical_energy'
                            modified = True

                if 'outputs' in step and isinstance(step['outputs'], list):
                    for out in step['outputs']:
                        if isinstance(out, dict) and out.get('item_id') in ['electricity', 'process_power']:
                            old_name = out['item_id']
                            out['item_id'] = 'electrical_energy'
                            modified = True

    return modified


def standardize_file(yaml_path: Path) -> bool:
    """
    Standardize energy naming in a single YAML file.

    Returns:
        True if file was modified
    """
    try:
        with open(yaml_path, 'r', encoding='utf-8') as f:
            content = f.read()

        data = yaml.safe_load(content)
        if not data:
            return False

        modified = standardize_energy_in_dict(data)

        if modified:
            with open(yaml_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return modified

    except Exception as e:
        print(f'Error processing {yaml_path}: {e}')
        return False


def main():
    """Main entry point."""
    project_root = Path(__file__).parent.parent
    processes_dir = project_root / 'kb' / 'processes'
    recipes_dir = project_root / 'kb' / 'recipes'

    modified_processes = []
    modified_recipes = []

    print('Standardizing energy naming in processes...')
    for process_path in sorted(processes_dir.glob('*.yaml')):
        if standardize_file(process_path):
            modified_processes.append(process_path.name)
            print(f'  ✓ {process_path.name}')

    print('\nStandardizing energy naming in recipes...')
    for recipe_path in sorted(recipes_dir.glob('**/*.yaml')):
        if standardize_file(recipe_path):
            modified_recipes.append(recipe_path.relative_to(recipes_dir))
            print(f'  ✓ {recipe_path.relative_to(recipes_dir)}')

    print('\n' + '='*60)
    print(f'SUMMARY:')
    print(f'  Processes modified: {len(modified_processes)}')
    print(f'  Recipes modified: {len(modified_recipes)}')
    print(f'  Total files modified: {len(modified_processes) + len(modified_recipes)}')
    print('='*60)


if __name__ == '__main__':
    main()
