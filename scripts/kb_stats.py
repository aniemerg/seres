#!/usr/bin/env python3
"""Generate statistics about the knowledge base."""

import yaml
from pathlib import Path
from collections import Counter

def main():
    print("# Knowledge Base Statistics\n")
    print("Generated: 2025-12-18\n")

    # Count files by type
    kb_root = Path("kb")

    machines = list((kb_root / "items" / "machines").glob("*.yaml"))
    parts = list((kb_root / "items" / "parts").glob("*.yaml"))
    materials = list((kb_root / "items" / "materials").glob("*.yaml"))
    processes = list((kb_root / "processes").glob("*.yaml"))
    boms = list((kb_root / "boms").glob("*.yaml"))
    recipes = list((kb_root / "recipes").glob("*.yaml"))
    resources = list((kb_root / "resources").glob("*.yaml"))
    seeds = list((kb_root / "seeds").glob("*.yaml"))

    print("## File Counts by Type\n")
    print("| Type | Count |")
    print("|------|-------|")
    print(f"| Machines | {len(machines)} |")
    print(f"| Parts | {len(parts)} |")
    print(f"| Materials | {len(materials)} |")
    print(f"| Processes | {len(processes)} |")
    print(f"| BOMs | {len(boms)} |")
    print(f"| Recipes | {len(recipes)} |")
    print(f"| Resources | {len(resources)} |")
    print(f"| Seeds | {len(seeds)} |")
    total_files = len(machines) + len(parts) + len(materials) + len(processes) + len(boms) + len(recipes) + len(resources) + len(seeds)
    print(f"| **Total** | **{total_files}** |")

    # Recipe coverage
    recipe_targets = set()
    for recipe_file in recipes:
        try:
            with open(recipe_file) as f:
                recipe = yaml.safe_load(f)
                if recipe and "target_item_id" in recipe:
                    recipe_targets.add(recipe["target_item_id"])
        except Exception as e:
            print(f"# Warning: Could not parse {recipe_file}: {e}", file=__import__('sys').stderr)

    total_items = len(machines) + len(parts) + len(materials)
    print(f"\n## Recipe Coverage\n")
    print(f"- Total items (machines + parts + materials): {total_items}")
    print(f"- Items with recipes: {len(recipe_targets)}")
    if total_items > 0:
        print(f"- Coverage: {len(recipe_targets)/total_items*100:.1f}%")

    # Machine BOM coverage
    machines_with_bom = 0
    for machine_file in machines:
        try:
            with open(machine_file) as f:
                machine = yaml.safe_load(f)
                if machine and machine.get("bom"):
                    machines_with_bom += 1
        except Exception as e:
            print(f"# Warning: Could not parse {machine_file}: {e}", file=__import__('sys').stderr)

    print(f"\n## Machine BOM Coverage\n")
    print(f"- Total machines: {len(machines)}")
    print(f"- Machines with BOMs: {machines_with_bom}")
    if len(machines) > 0:
        print(f"- Coverage: {machines_with_bom/len(machines)*100:.1f}%")

    # BOM analysis
    total_components = 0
    component_refs = Counter()
    for bom_file in boms:
        try:
            with open(bom_file) as f:
                bom = yaml.safe_load(f)
                if bom and "components" in bom and bom["components"]:
                    components = bom["components"]
                    total_components += len(components)
                    for comp in components:
                        if "item_id" in comp:
                            component_refs[comp["item_id"]] += 1
        except Exception as e:
            print(f"# Warning: Could not parse {bom_file}: {e}", file=__import__('sys').stderr)

    print(f"\n## BOM Statistics\n")
    print(f"- Total BOMs: {len(boms)}")
    print(f"- Total component references: {total_components}")
    if len(boms) > 0:
        print(f"- Average components per BOM: {total_components/len(boms):.1f}")
    print(f"- Unique parts referenced: {len(component_refs)}")

    print(f"\n## Most Referenced Parts in BOMs (Top 20)\n")
    print("| Part ID | Reference Count |")
    print("|---------|-----------------|")
    for part_id, count in component_refs.most_common(20):
        print(f"| {part_id} | {count} |")

    # Process layer distribution
    layer_counts = Counter()
    for proc_file in processes:
        try:
            with open(proc_file) as f:
                proc = yaml.safe_load(f)
                if proc and "tags" in proc:
                    layer_tags = [t for t in proc["tags"] if t.startswith("layer_")]
                    for tag in layer_tags:
                        layer_counts[tag] += 1
        except Exception as e:
            print(f"# Warning: Could not parse {proc_file}: {e}", file=__import__('sys').stderr)

    print(f"\n## Process Layer Distribution\n")
    print("| Layer | Count |")
    print("|-------|-------|")
    for layer in sorted(layer_counts.keys()):
        print(f"| {layer} | {layer_counts[layer]} |")

    # Material class distribution
    material_classes = Counter()
    for part_file in parts:
        try:
            with open(part_file) as f:
                part = yaml.safe_load(f)
                if part and "material_class" in part:
                    material_classes[part["material_class"]] += 1
        except Exception as e:
            print(f"# Warning: Could not parse {part_file}: {e}", file=__import__('sys').stderr)

    print(f"\n## Part Material Class Distribution (Top 15)\n")
    print("| Material Class | Count |")
    print("|----------------|-------|")
    for mat_class, count in material_classes.most_common(15):
        print(f"| {mat_class} | {count} |")

if __name__ == "__main__":
    main()
