#!/usr/bin/env python3
"""
Simulation Analysis Tool

Analyzes simulation.jsonl files to extract learnings, patterns, and insights
that can be shared with future Claude Code sessions to improve simulations.

Usage:
    python tools/analyze_simulations.py [simulation_name]

    If no simulation_name provided, analyzes all simulations.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any
from datetime import datetime


class SimulationAnalyzer:
    def __init__(self, sim_path: Path):
        self.sim_path = sim_path
        self.sim_name = sim_path.parent.name
        self.events = []
        self.load_events()

    def load_events(self):
        """Load all events from simulation.jsonl"""
        jsonl_file = self.sim_path / "simulation.jsonl"
        if not jsonl_file.exists():
            return

        with open(jsonl_file, 'r') as f:
            for line in f:
                if line.strip():
                    self.events.append(json.loads(line))

    def analyze(self) -> Dict[str, Any]:
        """Analyze simulation and return insights"""
        if not self.events:
            return {"error": "No events found", "sim_name": self.sim_name}

        analysis = {
            "sim_name": self.sim_name,
            "event_count": len(self.events),
            "start_time": self.events[0].get("timestamp", "unknown"),
            "end_time": self.events[-1].get("timestamp", "unknown"),
            "total_sim_hours": 0,
            "supply_chains": [],
            "imports": [],
            "recipes_run": [],
            "processes_run": [],
            "machines_built": [],
            "final_inventory": {},
            "errors": [],
            "insights": [],
        }

        # Track state across events
        imports = []
        recipes = []
        processes = []
        machines = set()
        errors = []
        supply_chains = defaultdict(list)  # item -> processes that created it

        for event in self.events:
            event_type = event.get("type")

            # Track simulation time
            if "time_hours" in event:
                analysis["total_sim_hours"] = max(
                    analysis["total_sim_hours"],
                    event["time_hours"]
                )

            # Track imports
            if event_type == "import":
                imports.append({
                    "item": event.get("item_id"),
                    "quantity": event.get("quantity"),
                    "unit": event.get("unit"),
                    "mass_kg": event.get("mass_kg")
                })

            # Track recipes
            elif event_type == "recipe_start":
                recipes.append({
                    "recipe_id": event.get("recipe_id"),
                    "quantity": event.get("quantity"),
                    "duration_hours": event.get("duration_hours"),
                    "started_at": event.get("timestamp")
                })

            # Track processes
            elif event_type == "process_start":
                processes.append({
                    "process_id": event.get("process_id"),
                    "scale": event.get("scale"),
                    "duration": event.get("ends_at", 0) - event.get("started_at", 0) if "ends_at" in event else None
                })

            # Track process completions (for supply chain mapping)
            elif event_type == "process_complete":
                process_id = event.get("process_id")
                outputs = event.get("outputs", {})
                for item_id in outputs.keys():
                    supply_chains[item_id].append(process_id)

            # Track recipe completions (for supply chain mapping)
            elif event_type == "recipe_complete":
                recipe_id = event.get("recipe_id")
                outputs = event.get("outputs", {})
                for item_id in outputs.keys():
                    supply_chains[item_id].append(recipe_id)

            # Track machine builds
            elif event_type == "machine_built":
                machines.add(event.get("machine_id"))

            # Track errors
            elif event_type == "error":
                errors.append({
                    "message": event.get("message"),
                    "context": event.get("context", {}),
                    "timestamp": event.get("timestamp")
                })

            # Capture final state
            elif event_type == "state_snapshot":
                analysis["final_inventory"] = event.get("inventory", {})
                if "machines_built" in event:
                    machines.update(event["machines_built"])

        # Store aggregated data
        analysis["imports"] = imports
        analysis["recipes_run"] = recipes
        analysis["processes_run"] = processes
        analysis["machines_built"] = list(machines)
        analysis["errors"] = errors

        # Convert supply chains to list format
        analysis["supply_chains"] = [
            {"item": item, "producers": producers}
            for item, producers in supply_chains.items()
        ]

        # Generate insights
        analysis["insights"] = self._generate_insights(analysis)

        return analysis

    def _generate_insights(self, analysis: Dict) -> List[str]:
        """Generate human-readable insights from analysis"""
        insights = []

        # Time efficiency
        total_hours = analysis["total_sim_hours"]
        event_count = analysis["event_count"]
        if total_hours > 0:
            insights.append(
                f"Simulation ran for {total_hours:.1f} hours with {event_count} events "
                f"({event_count/total_hours:.1f} events/hour)"
            )

        # Import dependency
        import_count = len(analysis["imports"])
        if import_count > 0:
            total_import_mass = sum(
                imp.get("mass_kg", 0) or 0
                for imp in analysis["imports"]
            )
            insights.append(
                f"Required {import_count} imports totaling {total_import_mass:.1f} kg"
            )

            # List key imports
            key_imports = [imp["item"] for imp in analysis["imports"][:5]]
            if key_imports:
                insights.append(f"Key imports: {', '.join(key_imports)}")

        # Manufacturing success
        recipe_count = len(analysis["recipes_run"])
        process_count = len(analysis["processes_run"])
        if recipe_count > 0 or process_count > 0:
            insights.append(
                f"Ran {recipe_count} recipes and {process_count} processes"
            )

        # Supply chain depth
        supply_chain_count = len(analysis["supply_chains"])
        if supply_chain_count > 0:
            insights.append(
                f"Established {supply_chain_count} supply chains"
            )

            # Find deepest supply chain
            max_depth = max(
                len(sc["producers"])
                for sc in analysis["supply_chains"]
            )
            if max_depth > 1:
                deep_items = [
                    sc["item"]
                    for sc in analysis["supply_chains"]
                    if len(sc["producers"]) >= max_depth
                ]
                insights.append(
                    f"Deepest supply chains ({max_depth} steps): {', '.join(deep_items[:3])}"
                )

        # Machine building
        machine_count = len(analysis["machines_built"])
        if machine_count > 0:
            insights.append(
                f"Built {machine_count} machines: {', '.join(analysis['machines_built'])}"
            )

        # Final inventory summary
        inv_count = len(analysis["final_inventory"])
        if inv_count > 0:
            insights.append(
                f"Final inventory: {inv_count} unique items"
            )

        # Errors and blockers
        error_count = len(analysis["errors"])
        if error_count > 0:
            insights.append(
                f"⚠️  Encountered {error_count} errors"
            )
            # Show first error
            if analysis["errors"]:
                first_error = analysis["errors"][0]["message"]
                insights.append(f"First error: {first_error}")

        return insights


def analyze_all_simulations(simulations_dir: Path) -> Dict[str, Any]:
    """Analyze all simulations and generate summary report"""

    sim_dirs = sorted(simulations_dir.glob("*/"))
    analyses = []

    for sim_dir in sim_dirs:
        jsonl_file = sim_dir / "simulation.jsonl"
        if jsonl_file.exists():
            analyzer = SimulationAnalyzer(sim_dir)
            analysis = analyzer.analyze()
            analyses.append(analysis)

    # Generate comparative insights
    summary = {
        "total_simulations": len(analyses),
        "simulations": analyses,
        "comparative_insights": _generate_comparative_insights(analyses)
    }

    return summary


def _generate_comparative_insights(analyses: List[Dict]) -> List[str]:
    """Generate insights by comparing multiple simulations"""
    insights = []

    if not analyses:
        return insights

    # Find most comprehensive simulation
    if analyses:
        most_events = max(analyses, key=lambda a: a["event_count"])
        insights.append(
            f"Most comprehensive: {most_events['sim_name']} "
            f"({most_events['event_count']} events, "
            f"{most_events['total_sim_hours']:.1f} hours)"
        )

        # Find longest running simulation
        longest = max(analyses, key=lambda a: a["total_sim_hours"])
        if longest["sim_name"] != most_events["sim_name"]:
            insights.append(
                f"Longest running: {longest['sim_name']} "
                f"({longest['total_sim_hours']:.1f} hours)"
            )

    # Common supply chains across simulations
    all_items = defaultdict(int)
    for analysis in analyses:
        for sc in analysis["supply_chains"]:
            all_items[sc["item"]] += 1

    common_items = [
        item for item, count in all_items.items()
        if count >= len(analyses) / 2
    ]
    if common_items:
        insights.append(
            f"Commonly produced items ({len(common_items)}): "
            f"{', '.join(common_items[:5])}"
        )

    # Import patterns
    all_imports = defaultdict(int)
    for analysis in analyses:
        for imp in analysis["imports"]:
            all_imports[imp["item"]] += 1

    common_imports = sorted(
        all_imports.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    if common_imports:
        insights.append(
            f"Most imported items: {', '.join(item for item, _ in common_imports)}"
        )

    return insights


def format_report(summary: Dict) -> str:
    """Format analysis summary as markdown report"""

    lines = ["# Simulation Analysis Report\n"]
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append(f"Total simulations analyzed: {summary['total_simulations']}\n")

    # Comparative insights
    if summary["comparative_insights"]:
        lines.append("\n## Cross-Simulation Insights\n")
        for insight in summary["comparative_insights"]:
            lines.append(f"- {insight}\n")

    # Individual simulation details
    lines.append("\n## Individual Simulations\n")

    for analysis in summary["simulations"]:
        lines.append(f"\n### {analysis['sim_name']}\n")

        # Basic stats
        lines.append(f"- Events: {analysis['event_count']}\n")
        lines.append(f"- Duration: {analysis['total_sim_hours']:.1f} hours\n")
        lines.append(f"- Started: {analysis['start_time']}\n")

        # Insights
        if analysis["insights"]:
            lines.append("\n**Key Insights:**\n")
            for insight in analysis["insights"]:
                lines.append(f"- {insight}\n")

        # Supply chains
        if analysis["supply_chains"]:
            lines.append(f"\n**Supply Chains ({len(analysis['supply_chains'])}):**\n")
            for sc in analysis["supply_chains"][:10]:  # Show first 10
                producers = ", ".join(sc["producers"])
                lines.append(f"- `{sc['item']}` ← {producers}\n")
            if len(analysis["supply_chains"]) > 10:
                lines.append(f"- ... and {len(analysis['supply_chains']) - 10} more\n")

        # Errors
        if analysis["errors"]:
            lines.append(f"\n**Errors ({len(analysis['errors'])}):**\n")
            for error in analysis["errors"][:5]:  # Show first 5
                lines.append(f"- {error['message']}\n")
            if len(analysis["errors"]) > 5:
                lines.append(f"- ... and {len(analysis['errors']) - 5} more\n")

        lines.append("\n---\n")

    return "".join(lines)


def main():
    simulations_dir = Path(__file__).parent.parent / "simulations"

    if not simulations_dir.exists():
        print(f"Error: Simulations directory not found: {simulations_dir}")
        sys.exit(1)

    # Check for specific simulation argument
    if len(sys.argv) > 1:
        sim_name = sys.argv[1]
        sim_path = simulations_dir / sim_name

        if not sim_path.exists():
            print(f"Error: Simulation not found: {sim_name}")
            print(f"Available simulations:")
            for d in sorted(simulations_dir.glob("*/")):
                print(f"  - {d.name}")
            sys.exit(1)

        # Analyze single simulation
        analyzer = SimulationAnalyzer(sim_path)
        analysis = analyzer.analyze()

        print(f"# Analysis: {analysis['sim_name']}\n")
        print(f"Events: {analysis['event_count']}")
        print(f"Duration: {analysis['total_sim_hours']:.1f} hours\n")

        print("## Insights\n")
        for insight in analysis["insights"]:
            print(f"- {insight}")

        if analysis["supply_chains"]:
            print(f"\n## Supply Chains ({len(analysis['supply_chains'])})\n")
            for sc in analysis["supply_chains"]:
                producers = ", ".join(sc["producers"])
                print(f"- {sc['item']} ← {producers}")

    else:
        # Analyze all simulations
        summary = analyze_all_simulations(simulations_dir)
        report = format_report(summary)

        # Save to file
        output_path = simulations_dir.parent / "docs" / "simulation_learnings.md"
        output_path.parent.mkdir(exist_ok=True)

        with open(output_path, 'w') as f:
            f.write(report)

        print(f"✓ Analysis complete!")
        print(f"  Report saved to: {output_path}")
        print(f"  Analyzed {summary['total_simulations']} simulations")

        # Also print to stdout
        print("\n" + report)


if __name__ == "__main__":
    main()
