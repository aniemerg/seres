"""
Closure Analysis Tool

Analyzes material closure for machines by recursively expanding BOMs and recipes
to determine raw material requirements, import dependencies, and ISRU percentages.
"""

import sys
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional
from collections import defaultdict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from base_builder.kb_loader import KBLoader


class ClosureAnalyzer:
    """Analyzes material closure for machines."""

    def __init__(self, kb_loader: KBLoader):
        self.kb = kb_loader
        # Track what we've already expanded to avoid infinite loops
        self.expansion_cache = {}

    def analyze_machine(self, machine_id: str) -> Dict:
        """
        Analyze closure for a single machine.

        Returns:
            dict with keys:
                - machine_id: str
                - machine_name: str
                - total_mass: float (kg)
                - raw_materials: dict {item_id: {qty, unit, mass_kg}}
                - imported_items: dict {item_id: {qty, unit, mass_kg}}
                - unresolved_items: dict {item_id: {qty, unit, mass_kg}}
                - isru_mass: float (kg)
                - imported_mass: float (kg)
                - unresolved_mass: float (kg)
                - isru_percent: float (0-100)
                - imported_percent: float (0-100)
                - unresolved_percent: float (0-100)
                - errors: list of error messages
        """
        # Clear cache for each machine analysis
        self.expansion_cache = {}

        result = {
            'machine_id': machine_id,
            'machine_name': '',
            'total_mass': 0.0,
            'raw_materials': {},
            'imported_items': {},
            'unresolved_items': {},
            'isru_mass': 0.0,
            'imported_mass': 0.0,
            'unresolved_mass': 0.0,
            'isru_percent': 0.0,
            'imported_percent': 0.0,
            'unresolved_percent': 0.0,
            'errors': []
        }

        # Get machine info
        machine = self.kb.get_item(machine_id)
        if not machine:
            result['errors'].append(f"Machine '{machine_id}' not found in KB")
            return result

        result['machine_name'] = machine.get('name', machine_id)
        result['total_mass'] = machine.get('mass', 0.0)

        # Get BOM
        bom_id = machine.get('bom')
        if not bom_id:
            result['errors'].append(f"Machine '{machine_id}' has no BOM defined")
            return result

        # BOM lookup key: strip "bom_" prefix if present
        lookup_key = bom_id[4:] if bom_id.startswith('bom_') else bom_id
        bom = self.kb.get_bom(lookup_key)
        if not bom:
            result['errors'].append(f"BOM '{bom_id}' not found in KB")
            return result

        # Expand each component
        components = bom.get('components', [])
        if not components:
            result['errors'].append(f"BOM '{bom_id}' has no components")
            return result

        for component in components:
            item_id = component.get('item_id')
            qty = component.get('qty', 0)
            unit = component.get('unit', 'count')

            if not item_id:
                result['errors'].append(f"Component missing item_id in BOM '{bom_id}'")
                continue

            # Recursively expand this component
            self._expand_item(
                item_id, qty, unit,
                result['raw_materials'],
                result['imported_items'],
                result['unresolved_items'],
                result['errors']
            )

        # Calculate totals
        result['isru_mass'] = sum(
            item['mass_kg'] for item in result['raw_materials'].values()
        )
        result['imported_mass'] = sum(
            item['mass_kg'] for item in result['imported_items'].values()
        )
        result['unresolved_mass'] = sum(
            item['mass_kg'] for item in result['unresolved_items'].values()
        )

        # Calculate percentages
        total_calculated = result['isru_mass'] + result['imported_mass'] + result['unresolved_mass']
        if total_calculated > 0:
            result['isru_percent'] = (result['isru_mass'] / total_calculated) * 100
            result['imported_percent'] = (result['imported_mass'] / total_calculated) * 100
            result['unresolved_percent'] = (result['unresolved_mass'] / total_calculated) * 100

        return result

    def _expand_item(self, item_id: str, qty: float, unit: str,
                     raw_materials: Dict, imported_items: Dict,
                     unresolved_items: Dict, errors: List,
                     expansion_path: Optional[Set[str]] = None):
        """
        Recursively expand an item to its constituent materials.

        Accumulates results in the provided dictionaries.

        Args:
            expansion_path: Set of item_ids currently being expanded (for cycle detection)
        """
        # Initialize expansion path for cycle detection
        if expansion_path is None:
            expansion_path = set()

        # Check for circular dependency
        if item_id in expansion_path:
            # Circular dependency detected - treat as unresolved
            item = self.kb.get_item(item_id)
            mass_kg = self._calculate_mass(item, qty, unit) if item else 0.0
            self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
            errors.append(f"Circular dependency detected: {item_id} (path: {' -> '.join(expansion_path)} -> {item_id})")
            return

        # Add to expansion path
        expansion_path = expansion_path | {item_id}

        # Check cache to avoid re-expanding the same item
        cache_key = f"{item_id}:{qty}:{unit}"
        if cache_key in self.expansion_cache:
            # Add cached results
            cached = self.expansion_cache[cache_key]
            for material_id, data in cached.get('raw', {}).items():
                self._accumulate(raw_materials, material_id, data['qty'],
                               data['unit'], data['mass_kg'])
            for import_id, data in cached.get('imported', {}).items():
                self._accumulate(imported_items, import_id, data['qty'],
                               data['unit'], data['mass_kg'])
            for unres_id, data in cached.get('unresolved', {}).items():
                self._accumulate(unresolved_items, unres_id, data['qty'],
                               data['unit'], data['mass_kg'])
            return

        # Initialize cache entry
        cache_entry = {
            'raw': {},
            'imported': {},
            'unresolved': {}
        }

        # Get item definition
        item = self.kb.get_item(item_id)
        if not item:
            # Item not found - this is an unresolved item
            mass_kg = self._estimate_mass(item_id, qty, unit, None)
            self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
            cache_entry['unresolved'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            self.expansion_cache[cache_key] = cache_entry
            errors.append(f"Item '{item_id}' not found in KB")
            return

        # Check if imported
        if self._is_imported(item_id, item):
            mass_kg = self._calculate_mass(item, qty, unit)
            self._accumulate(imported_items, item_id, qty, unit, mass_kg)
            cache_entry['imported'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            self.expansion_cache[cache_key] = cache_entry
            return

        # Check if has recipe
        recipe_id = item.get('recipe')
        if not recipe_id:
            # No recipe and not imported - assume it's a raw material
            mass_kg = self._calculate_mass(item, qty, unit)
            self._accumulate(raw_materials, item_id, qty, unit, mass_kg)
            cache_entry['raw'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            self.expansion_cache[cache_key] = cache_entry
            return

        # Get recipe
        recipe = self.kb.get_recipe(recipe_id)
        if not recipe:
            # Recipe referenced but not found - unresolved
            mass_kg = self._calculate_mass(item, qty, unit)
            self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
            cache_entry['unresolved'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            self.expansion_cache[cache_key] = cache_entry
            errors.append(f"Recipe '{recipe_id}' not found for item '{item_id}'")
            return

        # Expand recipe inputs
        has_inputs = False
        for step in recipe.get('steps', []):
            # Check for step-level inputs (direct inputs in the step)
            step_inputs = step.get('inputs', [])
            if step_inputs:
                for inp in step_inputs:
                    has_inputs = True
                    input_id = inp.get('item_id')
                    input_qty = inp.get('qty', 0)
                    input_unit = inp.get('unit', 'kg')

                    if input_qty is None or input_qty == 0:
                        # Quantity not specified - can't expand properly
                        continue

                    # Scale by how much output we need
                    # This assumes 1:1 ratio - in reality we'd need to look at outputs
                    scaled_qty = input_qty * qty

                    # Recursively expand (results go directly into the dicts)
                    self._expand_item(input_id, scaled_qty, input_unit,
                                    raw_materials, imported_items, unresolved_items, errors,
                                    expansion_path)

            # Check for process_id reference (inputs defined in the process)
            process_id = step.get('process_id')
            if process_id:
                process = self.kb.get_process(process_id)
                if process:
                    # Get inputs from the process
                    process_inputs = process.get('inputs', [])
                    for inp in process_inputs:
                        has_inputs = True
                        input_id = inp.get('item_id')
                        input_qty = inp.get('qty', 0)
                        input_unit = inp.get('unit', 'kg')

                        if input_qty is None or input_qty == 0:
                            # Quantity not specified - can't expand properly
                            # Still mark that we found inputs though
                            continue

                        # Scale by how much output we need
                        # This is a simplification - ideally we'd look at process outputs
                        # and calculate the scaling factor based on actual yield
                        scaled_qty = input_qty * qty

                        # Recursively expand (results go directly into the dicts)
                        self._expand_item(input_id, scaled_qty, input_unit,
                                        raw_materials, imported_items, unresolved_items, errors,
                                        expansion_path)
                else:
                    # Process referenced but not found
                    errors.append(f"Process '{process_id}' referenced in recipe '{recipe_id}' not found")

        if not has_inputs:
            # Recipe exists but has no inputs - treat as raw material
            mass_kg = self._calculate_mass(item, qty, unit)
            self._accumulate(raw_materials, item_id, qty, unit, mass_kg)
            cache_entry['raw'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}

        self.expansion_cache[cache_key] = cache_entry

    def _is_imported(self, item_id: str, item: Dict) -> bool:
        """Check if an item is imported."""
        # Check item_id naming
        if 'import' in item_id.lower():
            return True
        if 'imported' in item_id.lower():
            return True

        # Check recipe naming
        recipe_id = item.get('recipe', '')
        if 'import' in recipe_id.lower():
            return True
        if 'imported' in recipe_id.lower():
            return True

        # Check notes
        notes = item.get('notes', '')
        if isinstance(notes, str):
            if 'import' in notes.lower() and 'placeholder' in notes.lower():
                return True

        return False

    def _calculate_mass(self, item: Dict, qty: float, unit: str) -> float:
        """
        Calculate total mass in kg for a given quantity of an item.

        Args:
            item: Item definition dict
            qty: Quantity needed
            unit: Unit of quantity

        Returns:
            Total mass in kg
        """
        item_mass = item.get('mass', 0.0)
        item_unit = item.get('unit', 'kg')

        # If the item is already in kg and qty is in kg, it's straightforward
        if item_unit == 'kg' and unit == 'kg':
            return qty

        # If item unit is kg and qty is in count
        if item_unit == 'kg' and unit == 'count':
            return item_mass * qty

        # If item unit is count/each and qty is count
        if item_unit in ['count', 'each', 'unit'] and unit == 'count':
            return item_mass * qty

        # Default: assume qty is in the same unit as item
        if item_unit == unit:
            return item_mass * qty

        # Fallback: best effort
        return item_mass * qty

    def _estimate_mass(self, item_id: str, qty: float, unit: str, item: Optional[Dict]) -> float:
        """Estimate mass when item definition is missing."""
        if item and 'mass' in item:
            return self._calculate_mass(item, qty, unit)
        # Can't estimate - return 0
        return 0.0

    def _accumulate(self, target_dict: Dict, item_id: str,
                    qty: float, unit: str, mass_kg: float):
        """Accumulate quantities and masses in a target dictionary."""
        if item_id not in target_dict:
            target_dict[item_id] = {
                'qty': 0.0,
                'unit': unit,
                'mass_kg': 0.0
            }

        target_dict[item_id]['qty'] += qty
        target_dict[item_id]['mass_kg'] += mass_kg


def format_closure_report(result: Dict) -> str:
    """Format closure analysis result as a readable report."""
    lines = []

    lines.append("=" * 80)
    lines.append(f"CLOSURE ANALYSIS: {result['machine_name']} ({result['machine_id']})")
    lines.append("=" * 80)
    lines.append("")

    # Machine info
    lines.append(f"Machine Total Mass: {result['total_mass']:.2f} kg")
    lines.append("")

    # Summary
    lines.append("MATERIAL BREAKDOWN (by mass):")
    lines.append("-" * 80)
    total_calc = result['isru_mass'] + result['imported_mass'] + result['unresolved_mass']
    lines.append(f"  ISRU (Raw Materials):  {result['isru_mass']:>10.2f} kg  ({result['isru_percent']:>5.1f}%)")
    lines.append(f"  Imported:              {result['imported_mass']:>10.2f} kg  ({result['imported_percent']:>5.1f}%)")
    lines.append(f"  Unresolved:            {result['unresolved_mass']:>10.2f} kg  ({result['unresolved_percent']:>5.1f}%)")
    lines.append(f"  {'─' * 40}")
    lines.append(f"  Total Calculated:      {total_calc:>10.2f} kg")
    lines.append("")

    # Raw materials detail
    if result['raw_materials']:
        lines.append("RAW MATERIALS (ISRU):")
        lines.append("-" * 80)
        for item_id, data in sorted(result['raw_materials'].items(),
                                     key=lambda x: x[1]['mass_kg'], reverse=True):
            qty_str = f"{data['qty']:.2f} {data['unit']}"
            mass_str = f"{data['mass_kg']:.2f} kg"
            lines.append(f"  {item_id:<50} {qty_str:>15}  {mass_str:>12}")
        lines.append("")

    # Imported items detail
    if result['imported_items']:
        lines.append("IMPORTED ITEMS:")
        lines.append("-" * 80)
        for item_id, data in sorted(result['imported_items'].items(),
                                     key=lambda x: x[1]['mass_kg'], reverse=True):
            qty_str = f"{data['qty']:.2f} {data['unit']}"
            mass_str = f"{data['mass_kg']:.2f} kg"
            lines.append(f"  {item_id:<50} {qty_str:>15}  {mass_str:>12}")
        lines.append("")

    # Unresolved items detail
    if result['unresolved_items']:
        lines.append("UNRESOLVED ITEMS (Missing recipes or definitions):")
        lines.append("-" * 80)
        for item_id, data in sorted(result['unresolved_items'].items(),
                                     key=lambda x: x[1]['mass_kg'], reverse=True):
            qty_str = f"{data['qty']:.2f} {data['unit']}"
            mass_str = f"{data['mass_kg']:.2f} kg" if data['mass_kg'] > 0 else "UNKNOWN"
            lines.append(f"  {item_id:<50} {qty_str:>15}  {mass_str:>12}")
        lines.append("")

    # Errors
    if result['errors']:
        lines.append("ERRORS/WARNINGS:")
        lines.append("-" * 80)
        for error in result['errors']:
            lines.append(f"  ! {error}")
        lines.append("")

    lines.append("=" * 80)

    return "\n".join(lines)


def main():
    """CLI entry point for closure analysis."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze material closure for machines')
    parser.add_argument('--machine', type=str, help='Analyze a specific machine')
    parser.add_argument('--all', action='store_true', help='Analyze all machines')
    parser.add_argument('--output', type=str, help='Output file (default: stdout)')

    args = parser.parse_args()

    # Load KB
    print("Loading knowledge base...", file=sys.stderr)
    kb_root = Path("kb")
    kb_loader = KBLoader(kb_root)
    kb_loader.load_all()
    print(f"Loaded {len(kb_loader.items)} items, {len(kb_loader.boms)} BOMs, "
          f"{len(kb_loader.recipes)} recipes", file=sys.stderr)

    analyzer = ClosureAnalyzer(kb_loader)

    # Determine which machines to analyze
    machines_to_analyze = []

    if args.machine:
        machines_to_analyze.append(args.machine)
    elif args.all:
        # Get all machines
        machines_to_analyze = [
            item_id for item_id, item in kb_loader.items.items()
            if item.get('kind') == 'machine' and item.get('bom')
        ]
    else:
        parser.print_help()
        print("\nError: Must specify --machine <machine_id> or --all", file=sys.stderr)
        return 1

    # Analyze machines
    results = []
    for machine_id in machines_to_analyze:
        print(f"Analyzing {machine_id}...", file=sys.stderr)
        result = analyzer.analyze_machine(machine_id)
        results.append(result)

    # Format output
    output_lines = []

    if args.all:
        # Summary table for all machines
        output_lines.append("=" * 120)
        output_lines.append("CLOSURE ANALYSIS SUMMARY - ALL MACHINES")
        output_lines.append("=" * 120)
        output_lines.append("")
        output_lines.append(f"{'Machine ID':<40} {'Total Mass':>12} {'ISRU %':>10} {'Import %':>10} {'Unres %':>10}")
        output_lines.append("-" * 120)

        for result in sorted(results, key=lambda r: r['imported_percent'], reverse=True):
            output_lines.append(
                f"{result['machine_id']:<40} "
                f"{result['total_mass']:>12.1f} kg "
                f"{result['isru_percent']:>9.1f}% "
                f"{result['imported_percent']:>9.1f}% "
                f"{result['unresolved_percent']:>9.1f}%"
            )

        output_lines.append("")
        output_lines.append("=" * 120)
        output_lines.append("")
        output_lines.append("")

    # Detailed reports
    for result in results:
        output_lines.append(format_closure_report(result))
        output_lines.append("\n")

    # Output
    output_text = "\n".join(output_lines)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output_text)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(output_text)

    return 0


if __name__ == '__main__':
    sys.exit(main())
