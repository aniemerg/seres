#!/usr/bin/env python3
"""
Extract and deduplicate errors/warnings from closure analysis report.
Enqueue them as gaps for fixing.
"""
import json
import re
from pathlib import Path
from collections import defaultdict

def extract_errors(report_path: Path):
    """Extract all error/warning messages from closure analysis report."""
    errors = []

    with report_path.open('r') as f:
        content = f.read()

    # Find all ERRORS/WARNINGS sections
    sections = re.split(r'ERRORS/WARNINGS:\n-+\n', content)[1:]

    for section in sections:
        # Get lines until next section separator
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('!'):
                # Remove leading '!' and whitespace
                error_msg = line[1:].strip()
                errors.append(error_msg)
            elif line.startswith('=') or not line:
                # End of error section
                break

    return errors

def categorize_error(error_msg: str):
    """Categorize error message and extract key information."""
    if 'Bootstrap import (circular)' in error_msg:
        # Extract item_id from "Bootstrap import (circular): item_id (path: ...)"
        match = re.match(r'Bootstrap import \(circular\): (\S+)', error_msg)
        if match:
            item_id = match.group(1)
            # Extract the circular path
            path_match = re.search(r'path: ([^)]+)\)', error_msg)
            path = path_match.group(1) if path_match else ""
            return {
                'type': 'circular_dependency',
                'item_id': item_id,
                'path': path,
                'message': error_msg
            }
    elif "has no inputs" in error_msg:
        # Extract recipe_id and item_id
        match = re.match(r"Recipe '([^']+)' for '([^']+)' has no inputs", error_msg)
        if match:
            recipe_id = match.group(1)
            item_id = match.group(2)
            return {
                'type': 'no_inputs_recipe',
                'item_id': item_id,
                'recipe_id': recipe_id,
                'message': error_msg
            }

    return None

def deduplicate_errors(errors):
    """Deduplicate errors by type and key item."""
    # Group by type and item_id
    grouped = defaultdict(list)

    for error in errors:
        cat = categorize_error(error)
        if cat:
            key = (cat['type'], cat['item_id'])
            grouped[key].append(cat)

    # For each unique key, keep one representative error with all paths
    deduped = []
    for (error_type, item_id), instances in grouped.items():
        if error_type == 'circular_dependency':
            # Collect all unique paths
            paths = list(set(inst['path'] for inst in instances))
            deduped.append({
                'gap_type': 'circular_dependency',
                'item_id': item_id,
                'description': f"Circular dependency detected involving {item_id}",
                'context': {
                    'error_type': 'bootstrap_import_circular',
                    'num_occurrences': len(instances),
                    'sample_paths': paths[:5],  # Keep up to 5 sample paths
                    'all_paths_count': len(paths)
                }
            })
        elif error_type == 'no_inputs_recipe':
            recipe_id = instances[0]['recipe_id']
            deduped.append({
                'gap_type': 'invalid_recipe',
                'item_id': item_id,
                'description': f"Recipe '{recipe_id}' for '{item_id}' has no inputs",
                'context': {
                    'error_type': 'no_inputs_recipe',
                    'recipe_id': recipe_id,
                    'num_occurrences': len(instances)
                }
            })

    return deduped

def main():
    report_path = Path('out/closure_analysis_full.txt')
    output_path = Path('out/closure_errors_to_fix.jsonl')

    print("Extracting errors from closure analysis report...")
    errors = extract_errors(report_path)
    print(f"Found {len(errors)} total error messages")

    print("\nDeduplicating errors...")
    deduped = deduplicate_errors(errors)
    print(f"Deduplicated to {len(deduped)} unique issues")

    # Write to JSONL
    print(f"\nWriting gaps to {output_path}...")
    with output_path.open('w') as f:
        for gap in deduped:
            f.write(json.dumps(gap) + '\n')

    # Print summary
    print("\nSummary by gap type:")
    by_type = defaultdict(int)
    for gap in deduped:
        by_type[gap['gap_type']] += 1

    for gap_type, count in sorted(by_type.items()):
        print(f"  {gap_type}: {count}")

    print(f"\nTotal gaps to enqueue: {len(deduped)}")
    print(f"Ready to enqueue with: python -m kbtool queue add --file {output_path}")

if __name__ == '__main__':
    main()
