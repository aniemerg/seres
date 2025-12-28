#!/usr/bin/env python3
"""
build_context.py

Generates the cached context file for the autonomous queue agent.

Outputs:
- agents/cached_context.md - Static context (memos + KB structure + examples + papers)

This file is intended to be cached and reused across all agent invocations.
"""
from __future__ import annotations

import json
import yaml
from pathlib import Path
from typing import List, Dict, Any


REPO_ROOT = Path(__file__).parent.parent
KB_ROOT = REPO_ROOT / "kb"
DESIGN_ROOT = REPO_ROOT / "design"
OUT_DIR = REPO_ROOT / "out"
OUTPUT_FILE = REPO_ROOT / "queue_agents" / "cached_context.md"


def read_file(path: Path) -> str:
    """Read a file and return its contents."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"[Error reading {path}: {e}]"


def load_yaml_file(path: Path) -> dict:
    """Load a YAML file and return as dict."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def score_complexity(kind: str, data: dict) -> int:
    """Score an item's complexity for example selection."""
    score = 0

    if kind == "process":
        score += len(data.get("inputs", []) or []) * 2
        score += len(data.get("outputs", []) or []) * 2
        score += len(data.get("byproducts", []) or [])
        score += len(data.get("resource_requirements", []) or []) * 3
        if data.get("energy_model"):
            score += 5
        if data.get("time_model"):
            score += 5
        if data.get("notes"):
            score += 3

    elif kind == "recipe":
        score += len(data.get("steps", []) or []) * 5
        if data.get("notes"):
            score += 3

    elif kind == "bom":
        score += len(data.get("components", []) or []) * 2
        if data.get("notes"):
            score += 3

    elif kind == "machine":
        score += len(data.get("capabilities", []) or []) * 5
        if data.get("bom"):
            score += 10
        if data.get("mass"):
            score += 3
        if data.get("notes"):
            score += 3

    elif kind in ("part", "material"):
        if data.get("mass"):
            score += 3
        if data.get("material_class"):
            score += 3
        if data.get("notes"):
            score += 3

    return score


def collect_examples() -> Dict[str, List[tuple[str, dict]]]:
    """Collect complex examples of each KB kind."""
    examples = {
        "process": [],
        "recipe": [],
        "bom": [],
        "machine": [],
        "part": [],
        "material": [],
    }

    # Scan KB directory
    for yaml_file in KB_ROOT.rglob("*.yaml"):
        data = load_yaml_file(yaml_file)
        if not data or not isinstance(data, dict):
            continue

        kind = data.get("kind")
        if kind not in examples:
            continue

        score = score_complexity(kind, data)
        rel_path = yaml_file.relative_to(REPO_ROOT)
        examples[kind].append((score, str(rel_path), data))

    # Sort by complexity and take top N
    result = {}
    for kind, items in examples.items():
        items.sort(reverse=True, key=lambda x: x[0])
        # Take top 3 for each kind
        result[kind] = [(path, data) for score, path, data in items[:3]]

    return result


def list_papers() -> List[Dict[str, str]]:
    """List papers in design/papers/ with basic metadata."""
    papers = []
    papers_dir = DESIGN_ROOT / "papers"

    if not papers_dir.exists():
        return papers

    for pdf_file in sorted(papers_dir.glob("*.pdf")):
        txt_file = pdf_file.with_suffix(".txt")
        papers.append({
            "pdf": pdf_file.name,
            "txt": txt_file.name if txt_file.exists() else None,
            "available": txt_file.exists(),
        })

    return papers


def format_yaml_example(path: str, data: dict) -> str:
    """Format a YAML example for display."""
    yaml_str = yaml.dump(data, default_flow_style=False, sort_keys=False)
    return f"```yaml\n# {path}\n{yaml_str}```"


def build_context() -> str:
    """Build the complete cached context."""
    sections = []

    # Header
    sections.append("# Cached Context for Autonomous Queue Agent")
    sections.append("\nThis context is cached and reused across all agent invocations.\n")

    # Section 1: Agent Reference (Condensed from meta-memo, memo_a, memo_b)
    sections.append("---\n## 1. Agent Reference\n")
    agent_memo = read_file(DESIGN_ROOT / "agent-memo.md")
    sections.append(agent_memo)

    # Section 2: Gap Resolution Guidance (Conservative Mode + Closure Errors)
    sections.append("\n---\n## 2. Gap Resolution Guidance\n")
    sections.append("\nAgents MUST follow these guides when fixing queue items:\n")

    sections.append("\n### 2.1 Conservative Mode (Default Approach)\n")
    conservative_guide = read_file(REPO_ROOT / "docs" / "conservative_mode_guide.md")
    sections.append(conservative_guide)

    sections.append("\n### 2.2 Closure Error Resolution\n")
    closure_guide = read_file(REPO_ROOT / "docs" / "closure_error_guidance.md")
    sections.append(closure_guide)

    # Section 3: KB Structure Guide
    sections.append("\n---\n## 3. Knowledge Base Structure\n")
    sections.append("""
The KB is organized as:

```
kb/
├── items/
│   ├── materials/    # Raw and processed materials (regolith, metals, glass, etc.)
│   ├── parts/        # Components (bearings, gears, electrodes, etc.)
│   └── machines/     # Equipment that provides manufacturing capacity
├── processes/        # Unit operations (crush, grind, cast, sinter, etc.)
├── recipes/          # How to make items (chains of processes)
├── boms/            # Bill of materials (item composition trees)
├── resources/       # Resource types (machine capabilities)
└── seeds/           # Seed configurations for analysis

Each YAML file defines one entity with:
- Unique `id` (lowercase snake_case)
- Required fields per kind (see memo_a.md)
- Optional provenance, notes, source_tags
```
""")

    # Section 4: Complex Examples
    sections.append("\n---\n## 4. Complex Examples (Templates)\n")
    sections.append("\nUse these as templates when creating new KB entries.\n")

    examples = collect_examples()

    for kind in ["process", "recipe", "bom", "machine", "part", "material"]:
        sections.append(f"\n### {kind.title()} Examples\n")
        for path, data in examples.get(kind, []):
            sections.append(format_yaml_example(path, data))
            sections.append("")

    # Section 5: Papers Directory
    sections.append("\n---\n## 5. Available Papers\n")
    sections.append("\nPapers are located in `design/papers/`. Use `rg_search` to search extracted text.\n")

    papers = list_papers()
    if papers:
        sections.append("\nAvailable papers:\n")
        for paper in papers:
            status = "✓" if paper["available"] else "✗"
            sections.append(f"- {status} `{paper['pdf']}` → `{paper['txt']}`")
    else:
        sections.append("\n(No papers found)")

    sections.append("""

Key papers from Alex Ellery:
- Ellery's work on self-replicating lunar systems is canonical
- Focus on processes, ISRU methods, and manufacturable actuation
- Papers describe chemical reaction families and machine classes
- Use as primary source for process parameters and material flows
""")

    # Section 6: Queue Workflow
    sections.append("\n---\n## 6. Queue Workflow\n")
    sections.append("""
When working on queue items, you'll use these tools:

**Available tools (defined in queue_agents/kb_tools.py):**

- **rg_search**: Search repository using ripgrep
- **read_file**: Read file contents
- **write_file**: Write/overwrite files with diff output
- **run_indexer**: Validate changes by running the indexer
- **queue_release**: Give up on an item and release it back to pending
- **queue_add_gap**: Add discovered issues to the queue for another agent

**queue_add_gap - Reporting Discovered Issues:**

**IMPORTANT: When to fix directly vs. queue:**
- **Fix directly** if the issue is in the file you're currently editing AND you have sufficient information to make the change
- **Queue the work** if it requires special research, working in other files, or is outside your current task scope

Use this tool when you discover problems that need separate attention:

```python
queue_add_gap(
    gap_type="quality_concern",
    item_id="steel_melting_v0",
    description="Energy model shows 1.2 kWh/kg but Ellery 2023 paper indicates 3.5 kWh/kg",
    context={"paper_ref": "ellery_2023.pdf", "section": "Table 4"}
)
```

Common gap types:
- `quality_concern` - Incorrect data, unrealistic estimates, conflicts with papers
- `needs_consolidation` - Multiple similar items should be merged
- `needs_review` - Requires domain expertise or verification
- `missing_dependency` - Found reference to undefined item not caught by indexer
- `data_inconsistency` - Values don't match across related items

You can create new gap types by using descriptive names (e.g., `energy_model_mismatch`).

**Workflow:**
1. Lease next task with your agent name
2. Research the gap using rg_search and read_file
3. Fix the issue by creating/updating YAML files with write_file
4. Validate with run_indexer to ensure the gap is resolved
5. If you discover other issues, use queue_add_gap to report them
6. The system will mark your task complete automatically if validation succeeds
""")

    # Section 7: Validation and Gap Types
    sections.append("\n---\n## 7. Gap Types and Validation\n")
    sections.append("""
The indexer identifies several gap types:

1. **missing_field** - Required fields not populated
   - Examples: `material_class` for parts, `energy_model` for processes
   - Fix: Research similar items and add the missing field

2. **no_recipe** - Items without manufacturing recipes
   - These will be treated as imports unless a recipe is created
   - Fix: Create a recipe referencing appropriate processes

3. **unresolved_ref** - Free-text requirements needing definition
   - Example: `requires_text: ["ball mill or grinder"]`
   - Fix: Replace with structured `requires_ids` or create the missing item

4. **referenced_only** - IDs referenced but not defined
   - Fix: Create the missing item definition

5. **import_stub** - Recipes marked as imports needing local manufacturing
   - Fix: Replace import recipe with actual manufacturing steps

6. **no_provider_machine** - Resource types with no machine providing them
   - Fix: Add capability to an existing machine or create a new machine

The indexer outputs:
- `out/work_queue.jsonl` - All gaps (rebuilt each run)
- `out/validation_report.md` - Detailed validation results
- `out/unresolved_refs.jsonl` - Unresolved references
- `out/missing_fields.jsonl` - Missing required fields
""")

    # Section 8: Best Practices
    sections.append("\n---\n## 8. Best Practices\n")
    sections.append("""
When filling gaps:

1. **Research first**: Use `rg_search` to find similar items in the KB
2. **Follow patterns**: Use the complex examples above as templates
3. **Be specific**: Use proper IDs, units, and structure
4. **Add context**: Include notes explaining assumptions or sources
5. **One item well**: Focus on quality over quantity
6. **Let indexer guide**: Don't try to anticipate downstream gaps
7. **Conservative assumptions**: When uncertain, use reasonable defaults from similar items
8. **Provenance**: Note sources in comments (e.g., "Based on ball_mill_v0")

File naming conventions:
- Items: `{category}_{description}_v{N}.yaml` (e.g., `ball_mill_v0.yaml`)
- Processes: `{action}_{target}_{variant}.yaml` (e.g., `crushing_basic_v0.yaml`)
- Recipes: `recipe_{target}_v{N}.yaml` (e.g., `recipe_steel_ingot_v0.yaml`)
- BOMs: `bom_{owner_item}_v{N}.yaml` (e.g., `bom_ball_mill_v0.yaml`)

Required fields by kind:
- **Material**: id, name, kind: material, unit (usually kg)
- **Part**: id, name, kind: part, mass, material_class
- **Machine**: id, name, kind: machine, mass, capabilities (optional: bom)
- **Process**: id, name, inputs, outputs, resource_requirements, energy_model, time_model
- **Recipe**: id, target_item_id, steps (list of process_ids)
- **BOM**: id, owner_item_id, components (list of {item_id, qty})
""")

    return "\n".join(sections)


def main():
    """Generate the cached context file."""
    print("Building cached context...")

    context = build_context()

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(context, encoding="utf-8")

    print(f"✓ Cached context written to: {OUTPUT_FILE}")
    print(f"  Size: {len(context):,} characters ({len(context) // 1000}K)")

    # Estimate tokens (rough: ~4 chars per token)
    estimated_tokens = len(context) // 4
    print(f"  Estimated tokens: ~{estimated_tokens:,}")


if __name__ == "__main__":
    main()
