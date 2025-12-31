"""
Unified CLI for KB Core Tools

Provides commands for:
- index: Build KB index with validation
- auto-fix: Automatically fix validation issues
- validate: Validate specific KB items

Usage:
    python -m src.cli index
    python -m src.cli auto-fix --dry-run
    python -m src.cli validate --id process:crushing_v0
"""
import sys
import argparse
from pathlib import Path


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="KB Core Tools - Indexing, Validation, and Auto-Fix",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # =========================================================================
    # SIMULATION commands
    # =========================================================================
    from src.simulation.cli import add_sim_subcommands
    add_sim_subcommands(subparsers)

    # =========================================================================
    # INDEX command
    # =========================================================================
    index_parser = subparsers.add_parser(
        'index',
        help='Build KB index with validation'
    )
    index_parser.add_argument(
        '--kb-root',
        type=Path,
        default=Path('kb'),
        help='KB root directory (default: kb)'
    )
    index_parser.add_argument(
        '--out-dir',
        type=Path,
        default=Path('out'),
        help='Output directory (default: out)'
    )

    # =========================================================================
    # AUTO-FIX command
    # =========================================================================
    autofix_parser = subparsers.add_parser(
        'auto-fix',
        help='Automatically fix validation issues'
    )
    autofix_parser.add_argument(
        '--kb-root',
        type=Path,
        default=Path('kb'),
        help='KB root directory (default: kb)'
    )
    autofix_parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview fixes without writing to disk'
    )
    autofix_parser.add_argument(
        '--max-fixes',
        type=int,
        default=None,
        help='Maximum number of fixes to apply'
    )
    autofix_parser.add_argument(
        '--rule',
        type=str,
        default=None,
        help='Fix only issues matching this rule'
    )
    autofix_parser.add_argument(
        '--level',
        type=str,
        choices=['error', 'warning'],
        default=None,
        help='Fix only issues at this level'
    )
    autofix_parser.add_argument(
        '--input',
        type=Path,
        default=Path('out/validation_issues.jsonl'),
        help='Input validation issues file (default: out/validation_issues.jsonl)'
    )

    # =========================================================================
    # VALIDATE command
    # =========================================================================
    validate_parser = subparsers.add_parser(
        'validate',
        help='Validate specific KB item'
    )
    validate_parser.add_argument(
        '--id',
        required=True,
        help='Item ID to validate (format: type:id, e.g., process:crushing_v0)'
    )
    validate_parser.add_argument(
        '--kb-root',
        type=Path,
        default=Path('kb'),
        help='KB root directory (default: kb)'
    )
    validate_parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed validation output'
    )

    # =========================================================================
    # CLOSURE command
    # =========================================================================
    closure_parser = subparsers.add_parser(
        'closure',
        help='Analyze material closure for machines'
    )
    closure_parser.add_argument(
        '--machine',
        type=str,
        help='Analyze a specific machine'
    )
    closure_parser.add_argument(
        '--all',
        action='store_true',
        help='Analyze all machines'
    )
    closure_parser.add_argument(
        '--output',
        type=str,
        help='Output file (default: stdout)'
    )
    closure_parser.add_argument(
        '--kb-root',
        type=Path,
        default=Path('kb'),
        help='KB root directory (default: kb)'
    )

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    # Dispatch to appropriate command
    try:
        if args.command == 'index':
            from src.indexer.indexer import main as index_main
            return index_main()

        elif args.command == 'auto-fix':
            from src.indexer.auto_fix import main as autofix_main
            # Set up sys.argv for the auto_fix CLI
            sys.argv = ['auto_fix']
            if args.dry_run:
                sys.argv.append('--dry-run')
            if args.max_fixes:
                sys.argv.extend(['--max-fixes', str(args.max_fixes)])
            if args.rule:
                sys.argv.extend(['--rule', args.rule])
            if args.level:
                sys.argv.extend(['--level', args.level])
            if args.input:
                sys.argv.extend(['--input', str(args.input)])
            sys.argv.extend(['--kb-root', str(args.kb_root)])
            return autofix_main()

        elif args.command == 'validate':
            return validate_item(args)

        elif args.command == 'closure':
            return analyze_closure(args)

        elif args.command == 'sim':
            from src.simulation.cli import run_sim_command
            from src.kb_core.kb_loader import KBLoader
            kb_loader = KBLoader(Path('kb'), use_validated_models=False)
            kb_loader.load_all()
            return run_sim_command(args, kb_loader)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


def validate_item(args):
    """
    Validate a specific KB item.

    Args:
        args: Parsed CLI arguments with id, kb_root, verbose

    Returns:
        Exit code (0 = success, 1 = validation errors)
    """
    from src.kb_core.kb_loader import KBLoader
    from src.kb_core.validators import validate_process, validate_recipe, ValidationLevel
    from src.kb_core.unit_converter import UnitConverter

    # Parse item ID (format: type:id)
    try:
        item_type, item_id = args.id.split(':', 1)
    except ValueError:
        print(f"Error: Invalid ID format '{args.id}'")
        print("Expected format: type:id (e.g., process:crushing_v0, recipe:recipe_steel_v0)")
        return 1

    # Load KB
    print(f"Loading KB from {args.kb_root}...")
    kb_loader = KBLoader(args.kb_root, use_validated_models=False)

    # Get the item
    if item_type == 'process':
        item_data = kb_loader.get_process(item_id)
        if not item_data:
            print(f"Error: Process '{item_id}' not found")
            return 1

        # Validate process
        converter = UnitConverter(kb_loader)
        issues = validate_process(item_data, converter)

    elif item_type == 'recipe':
        item_data = kb_loader.get_recipe(item_id)
        if not item_data:
            print(f"Error: Recipe '{item_id}' not found")
            return 1

        # Validate recipe (with converter for reference validation)
        converter = UnitConverter(kb_loader)
        issues = validate_recipe(item_data, converter)

    else:
        print(f"Error: Unsupported item type '{item_type}'")
        print("Supported types: process, recipe")
        return 1

    # Report results
    print("\n" + "="*80)
    print(f"VALIDATION RESULTS: {item_type}:{item_id}")
    print("="*80)

    if not issues:
        print("\n✅ No validation issues found")
        return 0

    # Count by level
    errors = [i for i in issues if i.level == ValidationLevel.ERROR]
    warnings = [i for i in issues if i.level == ValidationLevel.WARNING]
    info = [i for i in issues if i.level == ValidationLevel.INFO]

    print(f"\nFound {len(issues)} validation issue(s):")
    print(f"  - {len(errors)} ERROR(s)")
    print(f"  - {len(warnings)} WARNING(s)")
    print(f"  - {len(info)} INFO")

    # Show issues
    if errors:
        print("\n" + "-"*80)
        print("ERRORS:")
        print("-"*80)
        for i, issue in enumerate(errors, 1):
            print(f"\n{i}. {issue.rule}")
            print(f"   Category: {issue.category}")
            print(f"   Message: {issue.message}")
            if issue.field_path:
                print(f"   Field: {issue.field_path}")
            if issue.fix_hint and args.verbose:
                print(f"   Fix hint: {issue.fix_hint}")

    if warnings and args.verbose:
        print("\n" + "-"*80)
        print("WARNINGS:")
        print("-"*80)
        for i, issue in enumerate(warnings, 1):
            print(f"\n{i}. {issue.rule}")
            print(f"   Message: {issue.message}")
            if issue.field_path:
                print(f"   Field: {issue.field_path}")

    if info and args.verbose:
        print("\n" + "-"*80)
        print("INFO:")
        print("-"*80)
        for i, issue in enumerate(info, 1):
            print(f"\n{i}. {issue.rule}")
            print(f"   Message: {issue.message}")

    # Return error code if there are errors
    return 1 if errors else 0


def analyze_closure(args):
    """
    Analyze material closure for machines.

    Args:
        args: Parsed CLI arguments with machine, all, output, kb_root

    Returns:
        Exit code (0 = success, 1 = errors)
    """
    from src.kb_core.kb_loader import KBLoader
    from src.indexer.closure_analysis import ClosureAnalyzer, format_closure_report

    # Validate arguments
    if not args.machine and not args.all:
        print("Error: Must specify --machine <machine_id> or --all", file=sys.stderr)
        return 1

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
        # Get all machines with BOMs
        machines_to_analyze = [
            item_id for item_id, item_model in kb_loader.items.items()
            if hasattr(item_model, 'kind') and item_model.kind == 'machine'
            and hasattr(item_model, 'bom') and item_model.bom
        ]

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
