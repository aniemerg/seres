#!/usr/bin/env python3
"""
Migration script for ADR 003: Process-Machine Schema Harmonization

Changes:
1. Process resource_requirements: resource_type → machine_id, amount → qty
2. Machines: add processes_supported, remove capabilities
3. Delete kb/resources/*.yaml files
"""

import yaml
from pathlib import Path
from collections import defaultdict
import sys

def migrate_process(process_path: Path, dry_run: bool = True) -> dict:
    """Migrate a single process file."""
    with open(process_path) as f:
        content = f.read()

    changes = []

    # Replace resource_type: with machine_id:
    if 'resource_type:' in content:
        content = content.replace('resource_type:', 'machine_id:')
        changes.append('resource_type → machine_id')

    # Replace amount: with qty: in resource_requirements
    # Need to be careful not to replace amount in other contexts
    lines = content.split('\n')
    new_lines = []
    in_resource_reqs = False

    for line in lines:
        if 'resource_requirements:' in line:
            in_resource_reqs = True
            new_lines.append(line)
        elif in_resource_reqs:
            # Check if we're still in resource_requirements (indented)
            if line.strip() and not line.startswith(' '):
                in_resource_reqs = False
            elif '  amount:' in line or '    amount:' in line:
                line = line.replace('amount:', 'qty:')
                if 'amount → qty' not in changes:
                    changes.append('amount → qty in resource_requirements')
            new_lines.append(line)
        else:
            new_lines.append(line)

    content = '\n'.join(new_lines)

    if changes and not dry_run:
        with open(process_path, 'w') as f:
            f.write(content)

    return {
        'path': str(process_path),
        'changes': changes
    }

def build_machine_process_map() -> dict:
    """Build mapping of machine_id → list of processes that use it."""
    machine_to_processes = defaultdict(list)

    for process_path in Path("kb/processes").glob("*.yaml"):
        try:
            with open(process_path) as f:
                proc = yaml.safe_load(f)

            if proc and 'resource_requirements' in proc:
                for req in proc['resource_requirements']:
                    if isinstance(req, dict):
                        # Check for both old and new field names
                        machine_id = req.get('machine_id') or req.get('resource_type')
                        if machine_id:
                            machine_to_processes[machine_id].append(proc['id'])
        except Exception as e:
            print(f"Warning: Could not parse {process_path}: {e}", file=sys.stderr)

    return machine_to_processes

def migrate_machine(machine_path: Path, machine_to_processes: dict, dry_run: bool = True) -> dict:
    """Migrate a single machine file."""
    with open(machine_path) as f:
        machine = yaml.safe_load(f)

    if not machine:
        return {'path': str(machine_path), 'changes': []}

    machine_id = machine.get('id')
    changes = []

    # Add processes_supported
    if machine_id in machine_to_processes:
        processes = sorted(set(machine_to_processes[machine_id]))
        machine['processes_supported'] = processes
        changes.append(f'Added processes_supported: {len(processes)} processes')

    # Remove capabilities
    if 'capabilities' in machine and machine['capabilities']:
        old_caps = machine['capabilities']
        del machine['capabilities']
        changes.append(f'Removed capabilities: {len(old_caps)} items')

    if changes and not dry_run:
        with open(machine_path, 'w') as f:
            yaml.dump(machine, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    return {
        'path': str(machine_path),
        'changes': changes
    }

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Migrate KB files for ADR 003')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without modifying files')
    parser.add_argument('--processes', action='store_true', help='Migrate processes only')
    parser.add_argument('--machines', action='store_true', help='Migrate machines only')
    args = parser.parse_args()

    # If neither specified, do both
    if not args.processes and not args.machines:
        args.processes = True
        args.machines = True

    if args.dry_run:
        print("DRY RUN MODE - no files will be modified\n")

    # Migrate processes
    if args.processes:
        print("=" * 60)
        print("MIGRATING PROCESSES")
        print("=" * 60)

        process_paths = list(Path("kb/processes").glob("*.yaml"))
        modified_count = 0

        for process_path in process_paths:
            result = migrate_process(process_path, dry_run=args.dry_run)
            if result['changes']:
                modified_count += 1
                print(f"\n{result['path']}")
                for change in result['changes']:
                    print(f"  ✓ {change}")

        print(f"\nProcesses: {modified_count}/{len(process_paths)} modified")

    # Migrate machines
    if args.machines:
        print("\n" + "=" * 60)
        print("MIGRATING MACHINES")
        print("=" * 60)

        print("\nBuilding machine → processes map...")
        machine_to_processes = build_machine_process_map()
        print(f"Found {len(machine_to_processes)} machines referenced by processes")

        machine_paths = list(Path("kb/items/machines").glob("*.yaml"))
        modified_count = 0

        for machine_path in machine_paths:
            result = migrate_machine(machine_path, machine_to_processes, dry_run=args.dry_run)
            if result['changes']:
                modified_count += 1
                print(f"\n{result['path']}")
                for change in result['changes']:
                    print(f"  ✓ {change}")

        print(f"\nMachines: {modified_count}/{len(machine_paths)} modified")

    # Summary
    print("\n" + "=" * 60)
    print("MIGRATION SUMMARY")
    print("=" * 60)

    if args.dry_run:
        print("\nDRY RUN completed. No files were modified.")
        print("Run without --dry-run to apply changes.")
    else:
        print("\nMigration completed!")
        print("\nNext steps:")
        print("1. Re-index: .venv/bin/python -m kbtool index")
        print("2. Check validation report: cat out/validation_report.md")
        print("3. Delete kb/resources/*.yaml when ready")

if __name__ == "__main__":
    main()
