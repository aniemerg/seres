"""
Simulation Visualization - Generate graphs and charts from simulation logs.

Parses JSONL event logs and creates visualizations:
- Energy consumption over time
- Inventory levels over time
- Process execution timeline (Gantt chart)
- Energy breakdown by process
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors
import numpy as np


class SimulationVisualizer:
    """
    Parse simulation JSONL logs and generate visualizations.
    """

    def __init__(self, sim_dir: Path):
        self.sim_dir = sim_dir
        self.log_file = sim_dir / "simulation.jsonl"

        # Parsed data
        self.events: List[Dict[str, Any]] = []
        self.state_snapshots: List[Dict[str, Any]] = []
        self.process_events: List[Dict[str, Any]] = []
        self.energy_events: List[Dict[str, Any]] = []

        # Load and parse events
        self._load_events()

    def _load_events(self) -> None:
        """Load and categorize events from JSONL log."""
        if not self.log_file.exists():
            raise FileNotFoundError(f"Simulation log not found: {self.log_file}")

        with open(self.log_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    event = json.loads(line)
                    self.events.append(event)

                    event_type = event.get('type')

                    if event_type == 'state_snapshot':
                        self.state_snapshots.append(event)

                    elif event_type in ('process_start', 'process_complete'):
                        self.process_events.append(event)
                        # Also track as energy event if it has energy data
                        if event_type == 'process_complete' and 'energy_kwh' in event:
                            self.energy_events.append(event)

                except json.JSONDecodeError:
                    continue

    # ========================================================================
    # Visualization 1: Energy Consumption Over Time
    # ========================================================================

    def plot_energy_over_time(self, output_path: Path) -> None:
        """
        Create energy consumption over time visualization.

        Shows:
        - Cumulative energy consumption (line)
        - Individual process energy events (bars)
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

        # Extract cumulative energy from state snapshots
        times = []
        cumulative_energy = []

        for snapshot in self.state_snapshots:
            time_hours = snapshot.get('time_hours', 0.0)
            total_kwh = snapshot.get('total_energy_kwh', 0.0)
            times.append(time_hours)
            cumulative_energy.append(total_kwh)

        # Plot cumulative energy
        if times:
            ax1.plot(times, cumulative_energy, 'b-', linewidth=2, label='Cumulative Energy')
            ax1.fill_between(times, cumulative_energy, alpha=0.3)
            ax1.set_ylabel('Cumulative Energy (kWh)', fontsize=12)
            ax1.set_title('Energy Consumption Over Time', fontsize=14, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            ax1.legend()

        # Extract individual process energy events
        event_times = []
        event_energies = []
        event_labels = []

        for event in self.energy_events:
            # Find corresponding state snapshot to get time
            for snapshot in self.state_snapshots:
                if abs(snapshot.get('time_hours', 0) - event.get('time_hours', -999)) < 0.01:
                    time_hours = snapshot.get('time_hours', 0.0)
                    energy = event.get('energy_kwh', 0.0)
                    process_id = event.get('process_id', 'unknown')

                    event_times.append(time_hours)
                    event_energies.append(energy)
                    event_labels.append(process_id)
                    break

        # If we didn't find matches in snapshots, try using process_complete events directly
        if not event_times:
            # Build a time mapping from process events
            process_times = {}
            for event in self.process_events:
                if event.get('type') == 'process_start':
                    process_times[event.get('process_id')] = {
                        'start': event.get('starts_at', 0.0) if 'starts_at' in event else 0.0,
                        'end': event.get('ends_at', 0.0)
                    }

            for event in self.energy_events:
                process_id = event.get('process_id', 'unknown')
                energy = event.get('energy_kwh', 0.0)

                # Use end time from process_times or estimate
                if process_id in process_times:
                    time_hours = process_times[process_id]['end']
                else:
                    # Try to find from process_complete event
                    time_hours = 0.0
                    for proc_event in self.process_events:
                        if proc_event.get('type') == 'process_complete' and proc_event.get('process_id') == process_id:
                            # Use the time from state snapshots near this event
                            for snapshot in self.state_snapshots:
                                # Find snapshot right after this process
                                if snapshot.get('time_hours', 0) >= time_hours:
                                    time_hours = snapshot.get('time_hours', 0)
                                    break
                            break

                event_times.append(time_hours)
                event_energies.append(energy)
                event_labels.append(process_id)

        # Plot individual energy events as bars
        if event_times:
            # Group by time bucket (hourly)
            time_buckets = defaultdict(float)
            for t, e in zip(event_times, event_energies):
                bucket = int(t)  # Floor to nearest hour
                time_buckets[bucket] += e

            bucket_times = sorted(time_buckets.keys())
            bucket_energies = [time_buckets[t] for t in bucket_times]

            ax2.bar(bucket_times, bucket_energies, width=0.8, alpha=0.7, color='orange', label='Energy per Hour')
            ax2.set_ylabel('Energy per Time Period (kWh)', fontsize=12)
            ax2.set_xlabel('Simulation Time (hours)', fontsize=12)
            ax2.grid(True, alpha=0.3)
            ax2.legend()

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Energy over time: {output_path}")

    # ========================================================================
    # Visualization 2: Inventory Levels Over Time
    # ========================================================================

    def plot_inventory_over_time(self, output_path: Path, top_n: int = 10) -> None:
        """
        Create inventory levels over time visualization.

        Shows top N materials by maximum quantity over time.
        """
        fig, ax = plt.subplots(figsize=(14, 8))

        # Extract inventory data from state snapshots
        inventory_history: Dict[str, List[Tuple[float, float]]] = defaultdict(list)

        for snapshot in self.state_snapshots:
            time_hours = snapshot.get('time_hours', 0.0)
            inventory = snapshot.get('inventory', {})

            # Track each item
            for item_id, inv_data in inventory.items():
                quantity = inv_data.get('quantity', 0.0)
                unit = inv_data.get('unit', '')

                # Only track kg for now (or count for machines)
                if unit in ('kg', 'count', 'unit'):
                    inventory_history[item_id].append((time_hours, quantity))

        # Find top N materials by max quantity
        max_quantities = {
            item_id: max(qty for _, qty in history)
            for item_id, history in inventory_history.items()
        }

        top_items = sorted(max_quantities.items(), key=lambda x: x[1], reverse=True)[:top_n]

        # Plot each top item
        colors = plt.cm.tab10(np.linspace(0, 1, len(top_items)))

        for (item_id, _), color in zip(top_items, colors):
            history = inventory_history[item_id]
            times = [t for t, _ in history]
            quantities = [q for _, q in history]

            # Truncate long names
            display_name = item_id if len(item_id) < 30 else item_id[:27] + '...'

            ax.plot(times, quantities, marker='o', markersize=3,
                   linewidth=2, label=display_name, color=color)

        ax.set_xlabel('Simulation Time (hours)', fontsize=12)
        ax.set_ylabel('Quantity (kg or units)', fontsize=12)
        ax.set_title(f'Inventory Levels Over Time (Top {len(top_items)} Materials)',
                    fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Inventory over time: {output_path}")

    # ========================================================================
    # Visualization 3: Process Execution Timeline (Gantt Chart)
    # ========================================================================

    def plot_process_timeline(self, output_path: Path) -> None:
        """
        Create Gantt chart of process execution timeline.

        Shows when each process started and ended.
        """
        # Extract process start/end times
        processes: Dict[str, Dict[str, Any]] = {}

        for event in self.process_events:
            process_id = event.get('process_id', 'unknown')

            if event.get('type') == 'process_start':
                if process_id not in processes:
                    processes[process_id] = {'starts': [], 'ends': []}

                # Get start time from state snapshot time_hours (current time)
                start_time = 0.0
                ends_at = event.get('ends_at', 0.0)

                # Find the state snapshot around this event to get current time
                for snapshot in self.state_snapshots:
                    if any(proc.get('process_id') == process_id and proc.get('ends_at') == ends_at
                          for proc in snapshot.get('active_processes', [])):
                        start_time = snapshot.get('time_hours', 0.0)
                        break

                processes[process_id]['starts'].append(start_time)
                processes[process_id]['ends'].append(ends_at)

        if not processes:
            print("  ⚠ No process events found for timeline")
            return

        # Create Gantt chart
        fig, ax = plt.subplots(figsize=(14, max(6, len(processes) * 0.4)))

        # Sort processes by first start time
        sorted_processes = sorted(processes.items(),
                                 key=lambda x: min(x[1]['starts']) if x[1]['starts'] else 0)

        colors = plt.cm.tab20(np.linspace(0, 1, len(sorted_processes)))

        for idx, ((process_id, data), color) in enumerate(zip(sorted_processes, colors)):
            starts = data['starts']
            ends = data['ends']

            # Plot each execution of this process
            for start, end in zip(starts, ends):
                duration = end - start

                # Draw horizontal bar
                ax.barh(idx, duration, left=start, height=0.8,
                       color=color, alpha=0.8, edgecolor='black', linewidth=0.5)

        # Format y-axis with process names
        process_names = [pid if len(pid) < 40 else pid[:37] + '...'
                        for pid, _ in sorted_processes]
        ax.set_yticks(range(len(sorted_processes)))
        ax.set_yticklabels(process_names, fontsize=9)

        ax.set_xlabel('Simulation Time (hours)', fontsize=12)
        ax.set_title('Process Execution Timeline', fontsize=14, fontweight='bold')
        ax.grid(True, axis='x', alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Process timeline: {output_path}")

    # ========================================================================
    # Visualization 4: Energy Breakdown by Process
    # ========================================================================

    def plot_energy_by_process(self, output_path: Path, top_n: int = 15) -> None:
        """
        Create bar chart of total energy consumption by process type.

        Shows which processes consumed the most energy.
        """
        # Aggregate energy by process
        energy_by_process: Dict[str, float] = defaultdict(float)

        for event in self.energy_events:
            process_id = event.get('process_id', 'unknown')
            energy = event.get('energy_kwh', 0.0)

            # Strip "recipe:" prefix if present
            if process_id.startswith('recipe:'):
                process_id = process_id[7:]

            energy_by_process[process_id] += energy

        if not energy_by_process:
            print("  ⚠ No energy data found")
            return

        # Sort by energy and take top N
        sorted_processes = sorted(energy_by_process.items(),
                                 key=lambda x: x[1], reverse=True)[:top_n]

        # Create bar chart
        fig, ax = plt.subplots(figsize=(12, max(6, len(sorted_processes) * 0.3)))

        process_names = [pid if len(pid) < 40 else pid[:37] + '...'
                        for pid, _ in sorted_processes]
        energies = [energy for _, energy in sorted_processes]

        colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(sorted_processes)))
        bars = ax.barh(range(len(sorted_processes)), energies, color=colors,
                      edgecolor='black', linewidth=0.5)

        # Add value labels on bars
        for idx, (bar, energy) in enumerate(zip(bars, energies)):
            ax.text(energy, idx, f' {energy:.1f} kWh',
                   va='center', fontsize=9)

        ax.set_yticks(range(len(sorted_processes)))
        ax.set_yticklabels(process_names, fontsize=9)
        ax.set_xlabel('Total Energy Consumed (kWh)', fontsize=12)
        ax.set_title(f'Energy Breakdown by Process (Top {len(sorted_processes)})',
                    fontsize=14, fontweight='bold')
        ax.grid(True, axis='x', alpha=0.3)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Energy by process: {output_path}")

    # ========================================================================
    # Visualization 5: Inventory Heatmap (Gantt-style)
    # ========================================================================

    def plot_inventory_heatmap(self, output_path: Path, items_to_show: Optional[List[str]] = None) -> None:
        """
        Create a Gantt-style heatmap showing inventory levels over time.

        Uses color intensity to represent quantity at each time point.
        Shows all items (or filtered subset) as rows, time as columns.
        """
        # Extract inventory data from state snapshots
        inventory_history: Dict[str, List[Tuple[float, float]]] = defaultdict(list)
        all_times = set()

        for snapshot in self.state_snapshots:
            time_hours = snapshot.get('time_hours', 0.0)
            all_times.add(time_hours)
            inventory = snapshot.get('inventory', {})

            # Track each item
            for item_id, inv_data in inventory.items():
                quantity = inv_data.get('quantity', 0.0)
                inventory_history[item_id].append((time_hours, quantity))

        if not inventory_history:
            print("  ⚠ No inventory data found")
            return

        # Sort times
        times = sorted(all_times)
        if len(times) < 2:
            print("  ⚠ Not enough time points for heatmap")
            return

        # Determine which items to show
        if items_to_show is None:
            # Show all items, sorted by name
            items_to_show = sorted(inventory_history.keys())

        # Build matrix: rows = items, columns = time points
        matrix = []
        item_labels = []

        for item_id in items_to_show:
            if item_id not in inventory_history:
                continue

            # Build time series for this item
            history_dict = {t: q for t, q in inventory_history[item_id]}
            row = [history_dict.get(t, 0.0) for t in times]

            matrix.append(row)
            # Truncate long names
            display_name = item_id if len(item_id) < 35 else item_id[:32] + '...'
            item_labels.append(display_name)

        if not matrix:
            print("  ⚠ No items to display in heatmap")
            return

        matrix = np.array(matrix)

        # Create figure
        fig, ax = plt.subplots(figsize=(16, max(8, len(item_labels) * 0.3)))

        # Use logarithmic color scale if quantities span multiple orders of magnitude
        max_qty = np.max(matrix)
        min_nonzero = np.min(matrix[matrix > 0]) if np.any(matrix > 0) else 1.0

        if max_qty > 0 and max_qty / min_nonzero > 100:
            # Use log scale
            norm = mcolors.LogNorm(vmin=max(0.1, min_nonzero), vmax=max_qty)
            cmap = plt.cm.viridis
        else:
            # Use linear scale
            norm = None
            cmap = plt.cm.viridis

        # Create heatmap
        im = ax.imshow(matrix, aspect='auto', cmap=cmap, norm=norm,
                      interpolation='nearest', origin='upper')

        # Set ticks
        ax.set_xticks(np.arange(len(times))[::max(1, len(times)//20)])  # Show ~20 time labels
        ax.set_xticklabels([f'{times[i]:.0f}h' for i in range(len(times))][::max(1, len(times)//20)],
                          rotation=45, ha='right', fontsize=9)

        ax.set_yticks(np.arange(len(item_labels)))
        ax.set_yticklabels(item_labels, fontsize=8)

        # Labels and title
        ax.set_xlabel('Simulation Time (hours)', fontsize=12)
        ax.set_ylabel('Item ID', fontsize=12)
        ax.set_title('Inventory Levels Over Time (Heatmap)', fontsize=14, fontweight='bold')

        # Colorbar
        cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        cbar.set_label('Quantity (kg or units)', fontsize=11)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✓ Inventory heatmap: {output_path}")

    # ========================================================================
    # Generate All Visualizations
    # ========================================================================

    def generate_all(self, output_dir: Optional[Path] = None) -> None:
        """
        Generate all visualizations.

        Args:
            output_dir: Directory to save plots (default: sim_dir/plots)
        """
        if output_dir is None:
            output_dir = self.sim_dir / "plots"

        output_dir.mkdir(exist_ok=True)

        print(f"\nGenerating visualizations for {self.sim_dir.name}...")
        print(f"Output directory: {output_dir}\n")

        # Generate each visualization
        self.plot_energy_over_time(output_dir / "energy_over_time.png")
        self.plot_inventory_over_time(output_dir / "inventory_over_time.png")
        self.plot_inventory_heatmap(output_dir / "inventory_heatmap.png")
        self.plot_process_timeline(output_dir / "process_timeline.png")
        self.plot_energy_by_process(output_dir / "energy_by_process.png")

        print(f"\n✓ All visualizations generated in: {output_dir}")


def visualize_simulation(sim_dir: Path, output_dir: Optional[Path] = None) -> None:
    """
    Main entry point for visualization.

    Args:
        sim_dir: Path to simulation directory
        output_dir: Optional output directory for plots
    """
    visualizer = SimulationVisualizer(sim_dir)
    visualizer.generate_all(output_dir)
