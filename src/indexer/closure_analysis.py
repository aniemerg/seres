"""
Closure Analysis Tool

Analyzes material closure for machines by recursively expanding BOMs and recipes
to determine raw material requirements, import dependencies, and ISRU percentages.

Ported to use src.kb_core infrastructure with Pydantic models.
"""

import sys
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional, Any

from src.kb_core.kb_loader import KBLoader


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
        machine_model = self.kb.get_item(machine_id)
        if not machine_model:
            result['errors'].append(f"Machine '{machine_id}' not found in KB")
            return result

        # Convert Pydantic model to dict for compatibility
        machine = self._to_dict(machine_model)

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
            # Circular dependency detected - treat second encounter as virtual import for bootstrap
            item_model = self.kb.get_item(item_id)
            item = self._to_dict(item_model) if item_model else None
            mass_kg = self._calculate_mass(item, qty, unit) if item else 0.0
            self._accumulate(imported_items, item_id, qty, unit, mass_kg)
            errors.append(f"Bootstrap import (circular): {item_id} (path: {' -> '.join(expansion_path)} -> {item_id})")
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
        item_model = self.kb.get_item(item_id)
        if not item_model:
            # Item not found - this is an unresolved item
            mass_kg = self._estimate_mass(item_id, qty, unit, None)
            self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
            cache_entry['unresolved'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            self.expansion_cache[cache_key] = cache_entry
            errors.append(f"Item '{item_id}' not found in KB")
            return

        # Convert to dict for easier access
        item = self._to_dict(item_model)

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
            # No recipe - check if it's a raw material
            if self._is_raw_material(item_id, item):
                # Legitimate raw material
                mass_kg = self._calculate_mass(item, qty, unit)
                self._accumulate(raw_materials, item_id, qty, unit, mass_kg)
                cache_entry['raw'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
                self.expansion_cache[cache_key] = cache_entry
            else:
                # No recipe and not raw - UNRESOLVED
                mass_kg = self._calculate_mass(item, qty, unit)
                self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
                cache_entry['unresolved'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
                self.expansion_cache[cache_key] = cache_entry
                errors.append(f"Item '{item_id}' has no recipe and is not a raw material")
            return

        # Get recipe
        recipe_model = self.kb.get_recipe(recipe_id)
        if not recipe_model:
            # Recipe referenced but not found - unresolved
            mass_kg = self._calculate_mass(item, qty, unit)
            self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
            cache_entry['unresolved'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            self.expansion_cache[cache_key] = cache_entry
            errors.append(f"Recipe '{recipe_id}' not found for item '{item_id}'")
            return

        # Convert recipe to dict
        recipe = self._to_dict(recipe_model)

        # Expand recipe inputs
        # Priority order:
        # 1. Recipe-level inputs (explicit material flow)
        # 2. Step-level inputs (legacy/rare)
        # 3. Process-level inputs (derived from processes)

        has_inputs = False
        null_qty_found = False

        # FIRST: Check for recipe-level inputs (added 2025-12-24)
        recipe_inputs = recipe.get('inputs', [])
        if recipe_inputs:
            for inp in recipe_inputs:
                has_inputs = True
                input_id = inp.get('item_id')
                input_qty = inp.get('qty', 0)
                input_unit = inp.get('unit', 'kg')

                if input_qty is None or input_qty == 0:
                    # Null quantity at recipe level - FLAG THIS
                    null_qty_found = True
                    errors.append(f"Recipe '{recipe_id}' input '{input_id}' has null/zero quantity")
                    continue

                # Scale by how much output we need
                # Use recipe outputs to determine scaling if available
                recipe_outputs = recipe.get('outputs', [])
                scale_factor = qty
                if recipe_outputs:
                    for out in recipe_outputs:
                        if out.get('item_id') == item_id:
                            output_qty = out.get('qty', 1)
                            if output_qty and output_qty > 0:
                                scale_factor = qty / output_qty
                            break

                scaled_qty = input_qty * scale_factor

                # Recursively expand (results go directly into the dicts)
                self._expand_item(input_id, scaled_qty, input_unit,
                                raw_materials, imported_items, unresolved_items, errors,
                                expansion_path)

        # SECOND: Check step-level and process-level inputs
        # (only if no recipe-level inputs were found)
        if not recipe_inputs:
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
                            # Null quantity at step level - FLAG THIS
                            null_qty_found = True
                            errors.append(f"Recipe '{recipe_id}' step input '{input_id}' has null/zero quantity")
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
                    process_model = self.kb.get_process(process_id)
                    if process_model:
                        # Convert to dict
                        process = self._to_dict(process_model)
                        # Get inputs from the process
                        process_inputs = process.get('inputs', [])
                        for inp in process_inputs:
                            has_inputs = True
                            input_id = inp.get('item_id')
                            input_qty = inp.get('qty', 0)
                            input_unit = inp.get('unit', 'kg')

                            if input_qty is None or input_qty == 0:
                                # Null quantity in process - FLAG THIS
                                null_qty_found = True
                                errors.append(f"Process '{process_id}' (in recipe '{recipe_id}') input '{input_id}' has null/zero quantity")
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
            # Recipe exists but has no inputs - check if it's a raw material extraction
            if self._is_raw_material(item_id, item):
                # Legitimate raw material extraction recipe (mining, etc.)
                mass_kg = self._calculate_mass(item, qty, unit)
                self._accumulate(raw_materials, item_id, qty, unit, mass_kg)
                cache_entry['raw'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
            else:
                # Recipe exists but broken (no inputs) - UNRESOLVED
                mass_kg = self._calculate_mass(item, qty, unit)
                self._accumulate(unresolved_items, item_id, qty, unit, mass_kg)
                cache_entry['unresolved'][item_id] = {'qty': qty, 'unit': unit, 'mass_kg': mass_kg}
                errors.append(f"Recipe '{recipe_id}' for '{item_id}' has no inputs")

        self.expansion_cache[cache_key] = cache_entry

    def _is_imported(self, item_id: str, item: Dict) -> bool:
        """
        Check if an item is imported.

        With ADR-007, imports are identified by:
        1. Explicit is_import field (most reliable)
        2. Item ID with import_ prefix (new architecture)
        3. Legacy patterns (_imported suffix)
        4. Recipe with import_placeholder variant
        """
        # 1. Check explicit is_import field (NEW - most reliable)
        if item.get('is_import', False):
            return True

        # 2. Check item_id prefix (NEW ARCHITECTURE)
        if item_id.startswith('import_'):
            return True

        # 3. Check for legacy import patterns (_imported suffix)
        if '_imported' in item_id.lower():
            return True

        # 4. Check recipe - specifically for import placeholder variants
        recipe_id = item.get('recipe')
        if recipe_id:
            if recipe_id.startswith('recipe_import_placeholder_'):
                return True
            if 'import_placeholder_v0' in recipe_id.lower():
                return True

        # 5. Check variant_id for import placeholder
        variant_id = item.get('variant_id')
        if variant_id:
            if variant_id.startswith('import_'):
                return True
            if variant_id == 'import_placeholder_v0':
                return True

        return False

    def _is_raw_material(self, item_id: str, item: Dict) -> bool:
        """
        Check if an item is a true raw material.

        Raw materials are:
        1. Defined in kb/items/raw_materials/ folder, OR
        2. Have explicit is_raw_material field, OR
        3. Have notes containing "BASE material"
        """
        # Check folder location
        defined_in = item.get('defined_in', '')
        if 'raw_materials' in defined_in:
            return True

        # Check explicit field
        if item.get('is_raw_material'):
            return True

        # Check notes for BASE marker
        notes = item.get('notes', '')
        if isinstance(notes, str) and 'BASE material' in notes:
            return True

        return False

    def _calculate_mass(self, item: Optional[Dict], qty: float, unit: str) -> float:
        """
        Calculate total mass in kg for a given quantity of an item.

        Args:
            item: Item definition dict (can be None)
            qty: Quantity needed
            unit: Unit of quantity

        Returns:
            Total mass in kg
        """
        if not item:
            return 0.0

        item_mass = item.get('mass', 0.0)
        item_unit = item.get('unit', 'kg')

        # Handle None mass
        if item_mass is None:
            item_mass = 0.0

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

    def _to_dict(self, model: Any) -> Dict:
        """
        Convert Pydantic model to dict for compatibility.

        Args:
            model: Pydantic model (RawProcess, RawRecipe, RawItem, etc.)

        Returns:
            Dict representation of the model
        """
        if model is None:
            return {}
        if isinstance(model, dict):
            return model
        if hasattr(model, 'model_dump'):
            return model.model_dump()
        if hasattr(model, 'dict'):
            return model.dict()
        return {}


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
    parser.add_argument('--kb-root', type=Path, default=Path('kb'), help='KB root directory (default: kb)')

    args = parser.parse_args()

    # Load KB
    print("Loading knowledge base...", file=sys.stderr)
    kb_loader = KBLoader(args.kb_root, use_validated_models=False)
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
            item_id for item_id, item_model in kb_loader.items.items()
            if hasattr(item_model, 'kind') and item_model.kind == 'machine'
            and hasattr(item_model, 'bom') and item_model.bom
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
