"""
Auto-Fix CLI - Command-line tool for automatically fixing validation issues in the KB.

This is a thin wrapper around src.kb_core.auto_fixer.AutoFixer that provides
a convenient CLI interface.

Usage:
    python -m src.cli auto-fix [--dry-run] [--max-fixes N] [--rule RULE]

Examples:
    # Dry-run to preview fixes
    python -m src.cli auto-fix --dry-run

    # Apply up to 10 fixes
    python -m src.cli auto-fix --max-fixes 10

    # Fix only specific rule
    python -m src.cli auto-fix --rule process_type_required
"""
import argparse
import json
from pathlib import Path
from typing import List, Optional

from src.kb_core.auto_fixer import AutoFixer, batch_fix_issues
from src.kb_core.validators import ValidationIssue, ValidationLevel

KB_ROOT = Path("kb")
OUT_DIR = Path("out")
VALIDATION_ISSUES_FILE = OUT_DIR / "validation_issues.jsonl"


def load_validation_issues(
    file_path: Path,
    rule_filter: Optional[str] = None,
    level_filter: Optional[str] = None
) -> List[ValidationIssue]:
    """
    Load validation issues from JSONL file.

    Args:
        file_path: Path to validation_issues.jsonl
        rule_filter: Optional rule name to filter by
        level_filter: Optional level (error/warning) to filter by

    Returns:
        List of ValidationIssue objects
    """
    if not file_path.exists():
        print(f"No validation issues file found at {file_path}")
        print("Run the indexer first to generate validation issues:")
        print("  python -m src.cli index")
        return []

    issues = []

    with file_path.open('r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                data = json.loads(line)

                # Apply filters
                if rule_filter and data.get('rule') != rule_filter:
                    continue

                if level_filter and data.get('level') != level_filter:
                    continue

                # Create ValidationIssue from JSON data
                issue = ValidationIssue(
                    level=ValidationLevel(data['level']),
                    category=data['category'],
                    rule=data['rule'],
                    entity_type=data['entity_type'],
                    entity_id=data['entity_id'],
                    message=data['message'],
                    field_path=data.get('field_path'),
                    fix_hint=data.get('fix_hint')
                )

                issues.append(issue)

            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Warning: Failed to parse validation issue: {e}")
                continue

    return issues


def main():
    """Main entry point for auto-fix CLI."""
    parser = argparse.ArgumentParser(
        description="Automatically fix validation issues in KB files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview fixes without writing
  python -m src.cli auto-fix --dry-run

  # Apply up to 10 fixes
  python -m src.cli auto-fix --max-fixes 10

  # Fix only process_type_required issues
  python -m src.cli auto-fix --rule process_type_required

  # Fix only ERROR level issues
  python -m src.cli auto-fix --level error
        """
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview fixes without writing to disk'
    )

    parser.add_argument(
        '--max-fixes',
        type=int,
        default=None,
        help='Maximum number of fixes to apply'
    )

    parser.add_argument(
        '--rule',
        type=str,
        default=None,
        help='Fix only issues matching this rule (e.g., process_type_required)'
    )

    parser.add_argument(
        '--level',
        type=str,
        choices=['error', 'warning'],
        default=None,
        help='Fix only issues at this level'
    )

    parser.add_argument(
        '--input',
        type=Path,
        default=VALIDATION_ISSUES_FILE,
        help=f'Input validation issues file (default: {VALIDATION_ISSUES_FILE})'
    )

    parser.add_argument(
        '--kb-root',
        type=Path,
        default=KB_ROOT,
        help=f'KB root directory (default: {KB_ROOT})'
    )

    args = parser.parse_args()

    # Load validation issues
    print(f"Loading validation issues from {args.input}...")
    issues = load_validation_issues(
        args.input,
        rule_filter=args.rule,
        level_filter=args.level
    )

    if not issues:
        print("No validation issues to fix.")
        return 0

    print(f"Found {len(issues)} validation issue(s) to process")

    if args.dry_run:
        print("\n🔍 DRY-RUN MODE: No changes will be written to disk\n")

    # Apply fixes
    successful, failed = batch_fix_issues(
        issues,
        kb_root=args.kb_root,
        dry_run=args.dry_run,
        max_fixes=args.max_fixes
    )

    # Report results
    print("\n" + "="*80)
    print("AUTO-FIX RESULTS")
    print("="*80)

    if successful:
        print(f"\n✅ Successfully fixed {len(successful)} issue(s):\n")
        for i, result in enumerate(successful, 1):
            print(f"{i}. {result.message}")
            for change in result.changes_made:
                print(f"   - {change}")

    if failed:
        print(f"\n❌ Failed to fix {len(failed)} issue(s):\n")
        for i, result in enumerate(failed, 1):
            print(f"{i}. {result.message}")

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total issues processed: {len(issues)}")
    print(f"Successfully fixed: {len(successful)}")
    print(f"Failed/Skipped: {len(failed)}")

    if args.dry_run and successful:
        print("\n💡 Run without --dry-run to apply these fixes")

    if not args.dry_run and successful:
        print("\n✨ Fixes applied! Re-run the indexer to verify:")
        print("   python -m src.cli index")

    return 0 if not failed or args.dry_run else 1


if __name__ == '__main__':
    exit(main())
