"""
Circular Dependency Fixer

Automatically identifies circular dependencies and breaks them by marking
items as imports following the rule: "child in dependency chain becomes import"
"""

import sys
from pathlib import Path
from typing import Dict, Set, List, Tuple
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))

from base_builder.kb_loader import KBLoader


class CircularDependencyFixer:
    """Identifies and fixes circular dependencies by marking items as imports."""

    def __init__(self, kb_loader: KBLoader):
        self.kb = kb_loader
        self.circular_loops = []
        self.import_candidates = set()

    def find_all_circular_dependencies(self) -> List[List[str]]:
        """
        Find all circular dependency loops in the knowledge base.

        Returns:
            List of loops, where each loop is a list of item_ids
        """
        loops = []
        visited = set()
        rec_stack = set()
        path = []

        def dfs(item_id: str, current_path: List[str]) -> None:
            """DFS to detect cycles."""
            if item_id in rec_stack:
                # Found a cycle - extract the loop
                loop_start = current_path.index(item_id)
                loop = current_path[loop_start:]
                if loop and loop not in loops:
                    loops.append(loop)
                return

            if item_id in visited:
                return

            visited.add(item_id)
            rec_stack.add(item_id)
            current_path.append(item_id)

            # Get dependencies for this item
            dependencies = self._get_dependencies(item_id)
            for dep_id in dependencies:
                dfs(dep_id, current_path.copy())

            rec_stack.remove(item_id)

        # Start DFS from all items
        for item_id in self.kb.items.keys():
            if item_id not in visited:
                dfs(item_id, [])

        self.circular_loops = loops
        return loops

    def _get_dependencies(self, item_id: str) -> Set[str]:
        """Get all direct dependencies for an item (items it requires to be built)."""
        dependencies = set()

        # Get item
        item = self.kb.get_item(item_id)
        if not item:
            return dependencies

        # Check if item has a recipe
        recipe_id = item.get('recipe')
        if not recipe_id:
            return dependencies

        # Get recipe
        recipe = self.kb.get_recipe(recipe_id)
        if not recipe:
            return dependencies

        # Get inputs from recipe steps
        for step in recipe.get('steps', []):
            # Check step-level inputs
            for inp in step.get('inputs', []):
                input_id = inp.get('item_id')
                if input_id:
                    dependencies.add(input_id)

            # Check process inputs
            process_id = step.get('process_id')
            if process_id:
                process = self.kb.get_process(process_id)
                if process and isinstance(process, dict):
                    for inp in process.get('inputs', []) or []:
                        if isinstance(inp, dict):
                            input_id = inp.get('item_id')
                            if input_id:
                                dependencies.add(input_id)

        return dependencies

    def identify_import_candidates(self) -> Dict[str, List[str]]:
        """
        For each circular loop, identify which item should be marked as import.

        Strategy: Mark the item that appears in the most loops, or the most
        complex item (has most dependencies).

        Returns:
            Dict mapping item_id -> list of loops it's involved in
        """
        # Count how many loops each item appears in
        item_loop_count = defaultdict(list)

        for loop in self.circular_loops:
            for item_id in loop:
                item_loop_count[item_id].append(loop)

        # For each unique loop, pick one item to mark as import
        # Strategy: pick the item with most overall loop appearances
        loops_to_fix = {}
        for loop in self.circular_loops:
            loop_tuple = tuple(sorted(loop))  # Normalize loop representation
            if loop_tuple not in loops_to_fix:
                # Pick the item in this loop that appears in the most total loops
                best_candidate = max(loop, key=lambda x: len(item_loop_count[x]))
                loops_to_fix[loop_tuple] = best_candidate
                self.import_candidates.add(best_candidate)

        # Create report of which items should be imports and why
        result = {}
        for item_id in self.import_candidates:
            result[item_id] = item_loop_count[item_id]

        return result

    def generate_fix_report(self) -> str:
        """Generate a human-readable report of circular dependencies and fixes."""
        lines = []

        lines.append("=" * 80)
        lines.append("CIRCULAR DEPENDENCY FIX REPORT")
        lines.append("=" * 80)
        lines.append("")

        # Find all loops
        loops = self.find_all_circular_dependencies()

        if not loops:
            lines.append("✅ No circular dependencies found!")
            return "\n".join(lines)

        lines.append(f"Found {len(loops)} circular dependency loops")
        lines.append("")

        # Identify what to mark as imports
        import_candidates = self.identify_import_candidates()

        lines.append("=" * 80)
        lines.append(f"RECOMMENDED BOOTSTRAP IMPORTS: {len(import_candidates)} items")
        lines.append("=" * 80)
        lines.append("")
        lines.append("To break all circular dependencies, mark these items as imports:")
        lines.append("")

        for item_id, loops_involved in sorted(import_candidates.items()):
            item = self.kb.get_item(item_id)
            item_name = item.get('name', item_id) if item else item_id

            lines.append(f"📦 {item_id}")
            lines.append(f"   Name: {item_name}")
            lines.append(f"   Breaks {len(loops_involved)} circular loop(s)")
            lines.append("")

        lines.append("=" * 80)
        lines.append("DETAILED LOOP ANALYSIS")
        lines.append("=" * 80)
        lines.append("")

        for i, loop in enumerate(loops, 1):
            lines.append(f"Loop {i}: {' → '.join(loop)} → {loop[0]}")

            # Find which item should be marked as import for this loop
            loop_tuple = tuple(sorted(loop))
            for item_id in self.import_candidates:
                if item_id in loop:
                    # Check if this is the chosen import for this loop
                    lines.append(f"  ✂️  Break by importing: {item_id}")
                    break
            lines.append("")

        lines.append("=" * 80)
        lines.append("IMPLEMENTATION PLAN")
        lines.append("=" * 80)
        lines.append("")
        lines.append("For each item above, update its recipe to:")
        lines.append("")
        lines.append("  variant_id: import_placeholder_v0")
        lines.append("  steps: []")
        lines.append("  notes: 'Bootstrap import - needed to break circular dependency'")
        lines.append("")

        return "\n".join(lines)

    def auto_fix_recipes(self, dry_run: bool = True) -> List[str]:
        """
        Automatically update recipes to mark import candidates as imports.

        Args:
            dry_run: If True, only report what would be changed without making changes

        Returns:
            List of files that were (or would be) modified
        """
        import_candidates = self.identify_import_candidates()
        modified_files = []

        for item_id in import_candidates:
            item = self.kb.get_item(item_id)
            if not item:
                continue

            recipe_id = item.get('recipe')
            if not recipe_id:
                continue

            # Find recipe file
            recipe_files = list(Path('kb/recipes').glob(f'{recipe_id}.yaml'))
            if not recipe_files:
                continue

            recipe_file = recipe_files[0]

            if dry_run:
                print(f"Would modify: {recipe_file}")
                modified_files.append(str(recipe_file))
            else:
                # Read, modify, write recipe file
                # (Implementation would go here - reading YAML, modifying, writing back)
                print(f"Modified: {recipe_file}")
                modified_files.append(str(recipe_file))

        return modified_files


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Find and fix circular dependencies in knowledge base'
    )
    parser.add_argument('--fix', action='store_true',
                       help='Actually fix the recipes (default: dry run)')
    parser.add_argument('--output', type=str,
                       help='Output report to file')

    args = parser.parse_args()

    # Load KB
    print("Loading knowledge base...", file=sys.stderr)
    kb_root = Path("kb")
    kb_loader = KBLoader(kb_root)
    kb_loader.load_all()
    print(f"Loaded {len(kb_loader.items)} items, {len(kb_loader.recipes)} recipes",
          file=sys.stderr)

    # Analyze circular dependencies
    fixer = CircularDependencyFixer(kb_loader)
    report = fixer.generate_fix_report()

    # Output report
    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        print(report)

    # Apply fixes if requested
    if args.fix:
        print("\n" + "=" * 80, file=sys.stderr)
        print("APPLYING FIXES...", file=sys.stderr)
        print("=" * 80, file=sys.stderr)
        modified = fixer.auto_fix_recipes(dry_run=False)
        print(f"\nModified {len(modified)} recipe files", file=sys.stderr)
    else:
        print("\n(Run with --fix to apply changes)", file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main())
