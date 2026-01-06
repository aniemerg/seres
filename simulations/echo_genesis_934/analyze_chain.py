#!/usr/bin/env python3
"""
Analyze the full manufacturing chain for labor_bot_general_v0
Track all machines, raw materials, and imports needed
"""
import os
import yaml
from collections import defaultdict

def load_yaml(filepath):
    """Load and parse a YAML file"""
    try:
        with open(filepath) as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def find_recipe(target_item_id):
    """Find recipe for a given item"""
    for root, dirs, files in os.walk('kb/recipes'):
        for file in files:
            if file.endswith('.yaml'):
                filepath = os.path.join(root, file)
                recipe = load_yaml(filepath)
                if recipe and recipe.get('target_item_id') == target_item_id:
                    return recipe, filepath
    return None, None

def get_recipe_inputs(recipe):
    """Extract input requirements from a recipe"""
    inputs = []
    if not recipe or 'steps' not in recipe:
        return inputs

    for step in recipe['steps']:
        if 'inputs' in step:
            for inp in step['inputs']:
                inputs.append(inp.get('item_id'))
    return inputs

def get_recipe_machines(recipe):
    """Extract machine requirements from recipe steps"""
    machines = []
    if not recipe or 'steps' not in recipe:
        return machines

    for step in recipe['steps']:
        if 'process_id' in step:
            machines.append(step['process_id'])
    return machines

# Load labor bot BOM
bom = load_yaml('kb/boms/bom_labor_bot_general_v0.yaml')
components = []
for comp in bom['components']:
    components.append((comp['item_id'], comp.get('qty', 1)))

# Track analysis
items_to_manufacture = []
items_to_import = []
all_machines = set()
raw_materials = set()

# Known raw materials (from sim plan output)
KNOWN_RAW = {'regolith_lunar_mare', 'regolith_lunar_highlands',
             'solar_irradiance', 'bulk_material_or_parts_import'}

print("=" * 80)
print("LABOR BOT MANUFACTURING CHAIN ANALYSIS")
print("=" * 80)
print()

# Analyze each component
for item_id, qty in components:
    recipe, recipe_path = find_recipe(item_id)

    if recipe:
        items_to_manufacture.append(item_id)
        machines = get_recipe_machines(recipe)
        all_machines.update(machines)
        print(f"✓ {item_id}")
        print(f"  Recipe: {os.path.basename(recipe_path)}")
        if machines:
            print(f"  Machines: {', '.join(machines)}")
    else:
        items_to_import.append(item_id)
        print(f"✗ {item_id} - NO RECIPE (must import)")

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"\nComponents to MANUFACTURE: {len(items_to_manufacture)}")
print(f"Components to IMPORT: {len(items_to_import)}")
print(f"\nUnique machines needed: {len(all_machines)}")
print("\nMachines required:")
for machine in sorted(all_machines):
    print(f"  - {machine}")

print(f"\nMust import ({len(items_to_import)} items):")
for item in sorted(items_to_import):
    print(f"  - {item}")
