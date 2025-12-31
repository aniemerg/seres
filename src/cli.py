"""
Unified CLI for KB Core Tools

Provides commands for:
- index: Build KB index with validation
- auto-fix: Automatically fix validation issues
- validate: Validate specific KB items
- queue: Work queue operations

Usage:
    python -m src.cli index
    python -m src.cli auto-fix --dry-run
    python -m src.cli validate --id process:crushing_v0
    python -m src.cli queue lease --agent codex
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

    # =========================================================================
    # QUEUE command
    # =========================================================================
    queue_parser = subparsers.add_parser(
        'queue',
        help='Work queue operations'
    )
    queue_sub = queue_parser.add_subparsers(dest='queue_cmd')
    queue_sub.add_parser('pop', help='Pop and print the next queue item (legacy)')
    queue_sub.add_parser('prune', help='Remove items marked resolved/superseded from queue')
    lease_parser = queue_sub.add_parser('lease', help='Lease next pending item')
    lease_parser.add_argument('--agent', required=True)
    lease_parser.add_argument('--ttl', type=int, default=900)
    lease_parser.add_argument('--priority', help='Comma-separated reasons in priority order')
    complete_parser = queue_sub.add_parser('complete', help='Mark leased item complete')
    complete_parser.add_argument('--id', required=True)
    complete_parser.add_argument('--agent', required=True)
    complete_parser.add_argument(
        '--verify',
        action='store_true',
        help='Rebuild queue and refuse completion if the gap remains',
    )
    complete_parser.add_argument(
        '--no-index',
        action='store_true',
        help='Skip indexer run when used with --verify',
    )
    verify_parser = queue_sub.add_parser('verify', help='Rebuild queue and verify gap resolution')
    verify_parser.add_argument('--id', action='append', dest='ids', required=True, help='Gap id to verify (repeatable)')
    verify_parser.add_argument('--no-index', action='store_true', help='Skip indexer run and use existing queue')
    release_parser = queue_sub.add_parser('release', help='Release a lease back to pending')
    release_parser.add_argument('--id', required=True)
    release_parser.add_argument('--agent', required=True)
    gc_parser = queue_sub.add_parser('gc', help='Revert expired leases; optionally prune old done items')
    gc_parser.add_argument('--prune-done-older-than', type=int, default=None, dest='prune_done')
    queue_sub.add_parser('ls', help='Show queue counts by status')
    add_parser = queue_sub.add_parser('add', help='Add manual gap to queue')
    add_parser.add_argument('--gap-type', required=False, help='Gap type (existing or new)')
    add_parser.add_argument('--item-id', required=False, help='Item/recipe/process ID')
    add_parser.add_argument('--description', help='Description of the issue')
    add_parser.add_argument('--context', help='JSON context string')
    add_parser.add_argument('--file', help='JSONL file with gap items to add (alternative to --gap-type)')
    queue_sub.add_parser('gap-types', help='List registered gap types')

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

        elif args.command == 'queue':
            return run_queue_command(args)

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


def _run_indexer() -> bool:
    from src.indexer.indexer import build_index
    try:
        build_index()
        return True
    except Exception as e:
        print(f"Error: Indexer failed: {e}", file=sys.stderr)
        return False


def run_queue_command(args):
    import json as json_mod
    from src.kb_core import queue_manager

    cmd = args.queue_cmd
    if cmd == 'pop':
        item = queue_manager.pop_queue()
        if item:
            print(json_mod.dumps(item))
        else:
            print("queue empty")
        return 0

    if cmd == 'prune':
        removed = queue_manager.prune_queue()
        print(f"Pruned {removed} completed items from queue")
        return 0

    if cmd == 'lease':
        priorities = args.priority.split(',') if args.priority else None
        item = queue_manager.lease_next(args.agent, ttl=args.ttl, priorities=priorities)
        if item:
            print(json_mod.dumps(item))
        else:
            print("queue empty")
        return 0

    if cmd == 'complete':
        if args.verify:
            if not args.no_index:
                ok = _run_indexer()
                if not ok:
                    raise SystemExit("Indexer failed; refusing to complete")
            remaining = queue_manager.gap_ids_present([args.id])
            if remaining:
                raise SystemExit(f"Refusing to complete; gap still present: {args.id}")
        ok = queue_manager.complete(args.id, args.agent)
        if ok:
            print(f"Marked {args.id} done")
            return 0
        if args.verify and not queue_manager.gap_id_exists(args.id):
            print(f"Gap {args.id} already resolved; no queue entry to mark done")
            return 0
        print(f"Failed to mark {args.id} done (not leased by {args.agent}?)")
        return 1

    if cmd == 'verify':
        if not args.no_index:
            ok = _run_indexer()
            if not ok:
                raise SystemExit("Indexer failed; cannot validate queue")
        remaining = queue_manager.gap_ids_present(args.ids)
        if remaining:
            print("Unresolved gaps:")
            for gap_id in sorted(remaining):
                print(f"- {gap_id}")
            return 1
        print("All specified gaps are resolved.")
        return 0

    if cmd == 'release':
        ok = queue_manager.release(args.id, args.agent)
        if ok:
            print(f"Released {args.id} to pending")
            return 0
        print(f"Failed to release {args.id} (not leased by {args.agent}?)")
        return 1

    if cmd == 'gc':
        removed = queue_manager.gc(prune_done_older_than=args.prune_done)
        print(f"GC removed {removed} items")
        return 0

    if cmd == 'ls':
        counts = queue_manager.list_queue()
        print(json_mod.dumps(counts, indent=2))
        return 0

    if cmd == 'add':
        if args.file:
            added = queue_manager.add_from_file(Path(args.file))
            print(f"Added {added} items to queue")
            return 0
        if not args.gap_type or not args.item_id:
            raise SystemExit("Error: --gap-type and --item-id required (or use --file)")
        context = json_mod.loads(args.context) if args.context else {}
        gap_id = queue_manager.add_gap(
            gap_type=args.gap_type,
            item_id=args.item_id,
            description=args.description,
            context=context,
            source="manual"
        )
        print(f"Added gap to queue: {gap_id}")
        return 0

    if cmd == 'gap-types':
        types = queue_manager.list_gap_types()
        if not types:
            print("No gap types registered")
            return 0
        indexer_types = {k: v for k, v in types.items() if v.get("source") == "indexer"}
        agent_types = {k: v for k, v in types.items() if v.get("source") != "indexer"}
        print(f"Registered Gap Types ({len(types)} total)")
        print("=" * 60)
        if indexer_types:
            print("\nIndexer-Detected Types:")
            for gap_type, meta in sorted(indexer_types.items()):
                desc = meta.get("description", "No description")
                print(f"  {gap_type:25s} - {desc}")
        if agent_types:
            print("\nAgent-Created Types:")
            for gap_type, meta in sorted(agent_types.items()):
                desc = meta.get("description", "No description")
                usage = meta.get("usage_count", 0)
                print(f"  {gap_type:25s} - {desc} (used {usage} times)")
        return 0

    raise SystemExit("Unknown queue subcommand")


if __name__ == '__main__':
    sys.exit(main())
