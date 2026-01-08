#!/usr/bin/env python3
"""
Migration Script: requires_ids → resource_requirements

Migrates machine references from requires_ids to resource_requirements.
Part of ADR-003 implementation (2026-01-08).

Changes:
- Moves machines from requires_ids to resource_requirements
- Adds qty: 1, unit: count for each migrated machine
- Preserves existing resource_requirements entries
- Removes requires_ids field from processes
"""

import os
import sys
from pathlib import Path
from typing import Dict, Any, List
import yaml

# Custom YAML representer to preserve formatting
class CustomDumper(yaml.SafeDumper):
    pass

def str_representer(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

CustomDumper.add_representer(str, str_representer)


def migrate_process_file(filepath: Path) -> Dict[str, Any]:
    """
    Migrate a single process file.

    Returns:
        {"migrated": bool, "machines_moved": int, "error": str or None}
    """
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)

        if not data or data.get('kind') != 'process':
            return {"migrated": False, "machines_moved": 0, "error": "Not a process file"}

        # Check if has requires_ids
        requires_ids = data.get('requires_ids', [])
        if not requires_ids:
            return {"migrated": False, "machines_moved": 0, "error": None}

        # Get existing resource_requirements or create empty list
        resource_requirements = data.get('resource_requirements', [])
        if not isinstance(resource_requirements, list):
            resource_requirements = []

        # Get set of existing machine_ids in resource_requirements
        existing_machines = {req.get('machine_id') for req in resource_requirements if isinstance(req, dict) and req.get('machine_id')}

        # Migrate each machine from requires_ids
        machines_moved = 0
        for machine_id in requires_ids:
            # Skip if already in resource_requirements
            if machine_id in existing_machines:
                continue

            # Add to resource_requirements
            resource_requirements.append({
                'machine_id': machine_id,
                'qty': 1,
                'unit': 'count'
            })
            machines_moved += 1

        # Update data
        data['resource_requirements'] = resource_requirements
        del data['requires_ids']

        # Write back to file
        with open(filepath, 'w') as f:
            yaml.dump(data, f, Dumper=CustomDumper, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return {"migrated": True, "machines_moved": machines_moved, "error": None}

    except Exception as e:
        return {"migrated": False, "machines_moved": 0, "error": str(e)}


def main():
    """Run migration on all process files."""
    processes_dir = Path("kb/processes")

    if not processes_dir.exists():
        print(f"ERROR: Directory {processes_dir} not found")
        return 1

    # Collect all process files
    process_files = list(processes_dir.glob("*.yaml"))
    print(f"Found {len(process_files)} process files")

    # Statistics
    migrated_count = 0
    skipped_count = 0
    error_count = 0
    total_machines_moved = 0
    errors = []

    # Migrate each file
    for filepath in sorted(process_files):
        result = migrate_process_file(filepath)

        if result["migrated"]:
            migrated_count += 1
            total_machines_moved += result["machines_moved"]
            if result["machines_moved"] > 0:
                print(f"✓ {filepath.name}: moved {result['machines_moved']} machine(s)")
        elif result["error"]:
            if result["error"] == "Not a process file":
                skipped_count += 1
            else:
                error_count += 1
                errors.append(f"{filepath.name}: {result['error']}")
                print(f"✗ {filepath.name}: ERROR - {result['error']}")
        else:
            # No requires_ids, nothing to migrate
            skipped_count += 1

    # Summary
    print("\n" + "="*60)
    print("Migration Summary")
    print("="*60)
    print(f"Total files processed:  {len(process_files)}")
    print(f"  Migrated:             {migrated_count}")
    print(f"  Skipped (no changes): {skipped_count}")
    print(f"  Errors:               {error_count}")
    print(f"\nTotal machines moved:   {total_machines_moved}")

    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\n✓ Migration completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
